from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from pathlib import Path
import sqlite3
import re
import joblib
import numpy as np
import nltk

app = Flask(__name__, static_folder='Static')
app.secret_key = "fake_news_detection_secret_key"

DB_NAME = "users.db"

# --- MACHINE LEARNING MODEL SETUP ---
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "fake_news_model.pkl"
VECTORIZER_PATH = BASE_DIR / "tfidf_vectorizer.pkl"

# Ensure NLTK stopwords are downloaded silently
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    text = re.sub(r"\W", " ", str(text))
    text = text.lower()
    return " ".join(word for word in text.split() if word not in STOP_WORDS)

def load_artifacts():
    if not MODEL_PATH.exists() or not VECTORIZER_PATH.exists():
        raise FileNotFoundError(
            "Model files not found. Run your model training script first to create "
            "'fake_news_model.pkl' and 'tfidf_vectorizer.pkl'."
        )
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer

MODEL, VECTORIZER = None, None

def get_model():
    global MODEL, VECTORIZER
    if MODEL is None or VECTORIZER is None:
        MODEL, VECTORIZER = load_artifacts()
    return MODEL, VECTORIZER

def predict_news(text: str):
    model, vectorizer = get_model()

    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])

    # Class order: 0 -> FAKE, 1 -> REAL
    probs = model.predict_proba(vectorized)[0]
    fake_prob = float(probs[0] * 100)
    real_prob = float(probs[1] * 100)

    pred_idx = int(np.argmax(probs))
    prediction = "REAL" if pred_idx == 1 else "FAKE"
    confidence = round(max(fake_prob, real_prob), 2)

    # Explanation logic via linear model coefficients
    feature_names = vectorizer.get_feature_names_out()
    coef = model.coef_[0]

    row = vectorized.toarray().ravel()
    active_indices = np.where(row > 0)[0]

    contributions = []
    for idx in active_indices:
        contribution = row[idx] * coef[idx]
        contributions.append((feature_names[idx], contribution))

    # Identify the top 5 highest absolute impact terms
    top_terms = [w for w, _ in sorted(contributions, key=lambda x: abs(x[1]), reverse=True)[:5]]

    if len(text.split()) < 10:
        explanation = (
            "Warning: the text is very short, so the prediction may be less reliable. "
            f"The model still classified it as {prediction}."
        )
    else:
        if top_terms:
            explanation = (
                f"The article was classified as {prediction} because words such as "
                f"{', '.join(top_terms)} had the strongest influence on the model."
            )
        else:
            explanation = f"The article was classified as {prediction} by the trained model."

    return prediction, confidence, round(fake_prob, 2), round(real_prob, 2), top_terms, explanation


# --- DATABASE SETUP ---
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()


# --- AUTHENTICATION ROUTES ---
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            return render_template('login.html', error="Invalid Email Format")

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            error = "Incorrect Email or Password"

    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            return render_template('register.html', error="Invalid Email Format")

        if password != confirm_password:
            return render_template('register.html', error="Passwords do not match")

        if len(password) < 8:
            return render_template('register.html', error="Password must contain at least 8 characters")

        hashed_password = generate_password_hash(password)

        try:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, hashed_password)
            )
            conn.commit()
            conn.close()
            return render_template('login.html', error='Registration successful. Please login.')
        except sqlite3.IntegrityError:
            return render_template('register.html', error="Email already registered")

    return render_template('register.html', error=error)


# --- CORE DASHBOARD & ML PREDICTION ROUTES ---
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Security Guard Check
    if 'user_id' not in session:
        return redirect(url_for('login'))

    news = request.form.get("news", "").strip()
    if not news:
        return render_template(
            "dashboard.html",
            prediction=None,
            confidence=None,
            fake_prob=None,
            real_prob=None,
            influential_words=[],
            explanation="Please paste a news article first."
        )

    # Compute prediction tracking matrices using the loaded ML model
    prediction, confidence, fake_prob, real_prob, influential_words, explanation = predict_news(news)

    return render_template(
        'dashboard.html',
        prediction=prediction,
        confidence=confidence,
        fake_prob=fake_prob,
        real_prob=real_prob,
        influential_words=influential_words,
        explanation=explanation
    )

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)