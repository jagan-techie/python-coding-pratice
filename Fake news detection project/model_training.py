# Fake News Detection with User Input + SHAP Explainability + Short Text Warning

import pandas as pd
import numpy as np
import re
import nltk
import shap
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, roc_curve, auc

# Download stopwords if not already
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# 1. Load Dataset (for training only)
df = pd.read_csv("fake_or_real_news.csv")  
X = df['text']
y = df['label'].map({'FAKE':0, 'REAL':1})

# 2. Preprocessing
def clean_text(text):
    text = re.sub(r'\W', ' ', str(text))
    text = text.lower()
    return ' '.join([word for word in text.split() if word not in stop_words])

X = X.apply(clean_text)

# 3. Feature Extraction
tfidf = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf.fit_transform(X)

# 4. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# 5. Model Training
model = LogisticRegression(max_iter=1000, n_jobs=-1)
model.fit(X_train, y_train)

# 6. Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Visualization: Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['FAKE', 'REAL'], yticklabels=['FAKE', 'REAL'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Visualization: ROC Curve
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

# 7. Save Model + Vectorizer
joblib.dump(model, "fake_news_model.pkl")
joblib.dump(tfidf, "tfidf_vectorizer.pkl")

# 8. SHAP Explainer (LinearExplainer for Logistic Regression)
explainer = shap.LinearExplainer(model, X_train, feature_names=tfidf.get_feature_names_out())

# Function: Predict + Auto Explanation
def predict_with_explanation(text):
    cleaned = clean_text(text)
    vectorized = tfidf.transform([cleaned])
    
    # Short text safeguard
    if len(text.split()) < 10:
        return "UNRELIABLE", "Warning: Very short text, prediction may be unreliable."
    
    prediction = model.predict(vectorized)[0]
    label = "REAL" if prediction == 1 else "FAKE"
    prob = model.predict_proba(vectorized)[0][prediction]
    
    # SHAP values for this input
    shap_values = explainer(vectorized)
    values = shap_values.values[0]
    
    # Visualize SHAP values
    shap.plots.bar(shap_values, show=False)
    plt.title(f'SHAP Values for Prediction: {label}')
    plt.show()
    
    # Get top words actually present in this input
    indices = np.argsort(np.abs(values))[-5:]
    influential = [tfidf.get_feature_names_out()[i] for i in indices if vectorized[0, i] > 0]
    
    explanation = (
        f"This article was classified as {label} with {prob:.2%} confidence "
        f"because words such as {', '.join(influential)} strongly influenced the model toward {label}."
    )
    
    return label, explanation

# 🔹 NEW: User Input
user_text = input("\nEnter a news article text: ")
label, explanation = predict_with_explanation(user_text)

print("\nPrediction:", label)
print("Explanation:", explanation)