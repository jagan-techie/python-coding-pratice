### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:21:48 PM*

**[ADDED]**
```
99        # Visualize SHAP values
100       shap.plots.bar(shap_values, show=False)
101       plt.title(f'SHAP Values for Prediction: {label}')
102       plt.show()
103       
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:21:29 PM*

**[ADDED]**
```
51    # Visualization: Confusion Matrix
52    cm = confusion_matrix(y_test, y_pred)
53    plt.figure(figsize=(6,4))
54    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['FAKE', 'REAL'], yticklabels=['FAKE', 'REAL'])
55    plt.title('Confusion Matrix')
56    plt.xlabel('Predicted')
57    plt.ylabel('Actual')
58    plt.show()
59    
60    # Visualization: ROC Curve
61    y_prob = model.predict_proba(X_test)[:, 1]
62    fpr, tpr, _ = roc_curve(y_test, y_prob)
63    roc_auc = auc(fpr, tpr)
64    plt.figure()
65    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
66    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
67    plt.xlim([0.0, 1.0])
68    plt.ylim([0.0, 1.05])
69    plt.xlabel('False Positive Rate')
70    plt.ylabel('True Positive Rate')
71    plt.title('Receiver Operating Characteristic')
72    plt.legend(loc="lower right")
73    plt.show()
74    
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:21:18 PM*

**[ADDED]**
```
10    import seaborn as sns
```
**[REMOVED]**
```
(from line ~14)
from sklearn.metrics import classification_report, accuracy_score

```
**[ADDED]**
```
14    from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, roc_curve, auc
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:09:34 PM*

**[REMOVED]**
```
(from line ~22)
df = pd.read_csv("C:/Users/Mohamed Tawfeeq/Downloads/fake_or_real_news.csv/fake_or_real_news.csv")  

```
**[ADDED]**
```
22    df = pd.read_csv("fake_or_real_news.csv")  
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:09:09 PM*

**[REMOVED]**
```
(from line ~47)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))

```
**[ADDED]**
```
47    print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:09:01 PM*

**[REMOVED]**
```
(from line ~86)
user_text = input("\n✍️Enter a news article text: ")

```
**[ADDED]**
```
86    user_text = input("\nEnter a news article text: ")
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:08:59 PM*

**[REMOVED]**
```
(from line ~86)
user_text = input("\n✍️ Enter a news article text: ")

```
**[ADDED]**
```
86    user_text = input("\n✍️Enter a news article text: ")
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:05:22 PM*

**[REMOVED]**
```
(from line ~64)
        return "UNRELIABLE", "⚠️ Warning: Very short text, prediction may be unreliable."

```
**[ADDED]**
```
64            return "UNRELIABLE", "Warning: Very short text, prediction may be unreliable."
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:05:16 PM*

**[REMOVED]**
```
(from line ~89)
print("\n Prediction:", label)

```
**[ADDED]**
```
89    print("\nPrediction:", label)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:05:14 PM*

**[REMOVED]**
```
(from line ~90)
print(" Explanation:", explanation)
```
**[ADDED]**
```
90    print("Explanation:", explanation)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:05:08 PM*

**[REMOVED]**
```
(from line ~90)
print("📝 Explanation:", explanation)
```
**[ADDED]**
```
90    print(" Explanation:", explanation)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:05:06 PM*

**[REMOVED]**
```
(from line ~89)
print("\n🔮 Prediction:", label)

```
**[ADDED]**
```
89    print("\n Prediction:", label)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:04:58 PM*

**[REMOVED]**
```
(from line ~1)
# Fake News Detection with Automatic Sentence Explanations

```
**[ADDED]**
```
1     # Fake News Detection with User Input + SHAP Explainability + Short Text Warning
```
**[REMOVED]**
```
(from line ~21)
# 1. Load Dataset
df = pd.read_csv("fake_or_real_news.csv")

```
**[ADDED]**
```
21    # 1. Load Dataset (for training only)
22    df = pd.read_csv("C:/Users/Mohamed Tawfeeq/Downloads/fake_or_real_news.csv/fake_or_real_news.csv")  
```
**[REMOVED]**
```
(from line ~47)
print("Accuracy:", accuracy_score(y_test, y_pred))

```
**[ADDED]**
```
47    print("✅ Accuracy:", accuracy_score(y_test, y_pred))
```
**[REMOVED]**
```
(from line ~54)
# 8. SHAP Explainer
masker = shap.maskers.Independent(X_train)
explainer = shap.Explainer(model, masker)

```
**[ADDED]**
```
54    # 8. SHAP Explainer (LinearExplainer for Logistic Regression)
55    explainer = shap.LinearExplainer(model, X_train, feature_names=tfidf.get_feature_names_out())
```
**[ADDED]**
```
62        # Short text safeguard
63        if len(text.split()) < 10:
64            return "UNRELIABLE", "⚠️ Warning: Very short text, prediction may be unreliable."
65        
```
**[REMOVED]**
```
(from line ~68)
    
    # Confidence score

```
**[REMOVED]**
```
(from line ~70)
    # SHAP local explanation

```
**[ADDED]**
```
70        # SHAP values for this input
```
**[REMOVED]**
```
(from line ~72)
    top_words_idx = np.argsort(np.abs(shap_values.values[0]))[-5:]
    influential = [tfidf.get_feature_names_out()[i] for i in top_words_idx]

```
**[ADDED]**
```
72        values = shap_values.values[0]
```
**[REMOVED]**
```
(from line ~74)
    # Auto-generated sentence

```
**[ADDED]**
```
74        # Get top words actually present in this input
75        indices = np.argsort(np.abs(values))[-5:]
76        influential = [tfidf.get_feature_names_out()[i] for i in indices if vectorized[0, i] > 0]
77        
```
**[REMOVED]**
```
(from line ~85)
# Example usage: pick any article from dataset
index = 0
news_text = df['text'].iloc[index]
label, explanation = predict_with_explanation(news_text)

```
**[ADDED]**
```
85    # 🔹 NEW: User Input
86    user_text = input("\n✍️ Enter a news article text: ")
87    label, explanation = predict_with_explanation(user_text)
```
**[REMOVED]**
```
(from line ~89)
print("\n📰 News Text:", news_text[:500], "...")
print(" Prediction:", label)
print(" Explanation:", explanation)
```
**[ADDED]**
```
89    print("\n🔮 Prediction:", label)
90    print("📝 Explanation:", explanation)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\index.html
*Saved at: 5/13/2026, 2:45:56 PM*

**[REMOVED]**
```
(from line ~33)
            min-height:100vh;

```
**[REMOVED]**
```
(from line ~34)
            padding:20px 40px;

```
**[ADDED]**
```
34                padding:20px 35px;
```
**[REMOVED]**
```
(from line ~45)
            font-size:58px;

```
**[ADDED]**
```
45                font-size:55px;
```
**[REMOVED]**
```
(from line ~49)
        .header h1 span{

```
**[ADDED]**
```
49            .header span{
```
**[ADDED]**
```
54                color:#c9c9c9;
```
**[REMOVED]**
```
(from line ~56)
            color:#bdbdbd;
            font-size:18px;

```
**[REMOVED]**
```
(from line ~58)
        /* GRID */

```
**[ADDED]**
```
58            /* TOP GRID */
```
**[REMOVED]**
```
(from line ~60)
        .main-container{

```
**[ADDED]**
```
60            .top-grid{
```
**[REMOVED]**
```
(from line ~70)
            border-radius:25px;
            padding:28px;

```
**[ADDED]**
```
70                border-radius:22px;
71                padding:25px;
```
**[REMOVED]**
```
(from line ~73)
            box-shadow:0 0 20px rgba(0,0,0,0.35);

```
**[REMOVED]**
```
(from line ~78)
            margin-bottom:22px;

```
**[ADDED]**
```
78                margin-bottom:20px;
```
**[REMOVED]**
```
(from line ~89)
            height:240px;
            background:#050E33;

```
**[ADDED]**
```
89                height:230px;
90                background:#07103A;
```
**[ADDED]**
```
95                font-size:15px;
```
**[REMOVED]**
```
(from line ~98)
            font-size:15px;

```
**[REMOVED]**
```
(from line ~101)
            color:#888;

```
**[ADDED]**
```
101               color:#8a8a8a;
```
**[REMOVED]**
```
(from line ~106)
        .button-group{

```
**[ADDED]**
```
106           .buttons{
```
**[REMOVED]**
```
(from line ~109)
            margin-top:22px;

```
**[ADDED]**
```
109               margin-top:20px;
```
**[REMOVED]**
```
(from line ~112)
        .analyze-btn{
            background:linear-gradient(90deg,#7B2FF7,#F107A3);

```
**[ADDED]**
```
112           button{
```
**[REMOVED]**
```
(from line ~114)
            padding:14px 28px;

```
**[ADDED]**
```
114               padding:14px 26px;
```
**[REMOVED]**
```
(from line ~116)
            color:white;

```
**[REMOVED]**
```
(from line ~119)
            transition:0.3s;

```
**[REMOVED]**
```
(from line ~121)
        .analyze-btn:hover{
            transform:translateY(-2px);
            box-shadow:0 0 20px rgba(176,38,255,0.5);

```
**[ADDED]**
```
121           .analyze-btn{
122               background:linear-gradient(90deg,#7B2FF7,#F107A3);
123               color:white;
```
**[REMOVED]**
```
(from line ~128)
            border:none;
            padding:14px 28px;
            border-radius:14px;

```
**[REMOVED]**
```
(from line ~129)
            font-size:16px;
            font-weight:600;
            cursor:pointer;

```
**[REMOVED]**
```
(from line ~133)
        .analyzer-card{

```
**[ADDED]**
```
133           .analyzer{
```
**[REMOVED]**
```
(from line ~142)
            width:95px;
            height:95px;

```
**[ADDED]**
```
142               width:90px;
143               height:90px;
```
**[REMOVED]**
```
(from line ~156)
        .analyzer-card h2{
            font-size:36px;
            margin-bottom:12px;

```
**[ADDED]**
```
156           .analyzer h2{
157               font-size:34px;
158               margin-bottom:10px;
```
**[REMOVED]**
```
(from line ~161)
        .analyzer-card p{

```
**[ADDED]**
```
161           .analyzer p{
```
**[REMOVED]**
```
(from line ~166)
        /* RESULTS SECTION */

```
**[ADDED]**
```
166           /* RESULTS */
```
**[REMOVED]**
```
(from line ~168)
        .results-container{

```
**[ADDED]**
```
168           .results-grid{
```
**[REMOVED]**
```
(from line ~175)
        /* RESULT CARD */

```
**[ADDED]**
```
175           /* RESULT */
```
**[REMOVED]**
```
(from line ~177)
        .result-flex{

```
**[ADDED]**
```
177           .result-box{
```
**[REMOVED]**
```
(from line ~190)
        .result-icon{

```
**[ADDED]**
```
190           .status-icon{
```
**[REMOVED]**
```
(from line ~199)
        .result-icon.real{

```
**[ADDED]**
```
199           .real{
```
**[REMOVED]**
```
(from line ~203)
        .result-icon.fake{

```
**[ADDED]**
```
203           .fake{
```
**[REMOVED]**
```
(from line ~207)
        .result-icon i{
            font-size:32px;

```
**[ADDED]**
```
207           .status-icon i{
208               font-size:30px;
```
**[REMOVED]**
```
(from line ~218)
            color:#c7c7c7;

```
**[ADDED]**
```
218               color:#d0d0d0;
```
**[REMOVED]**
```
(from line ~223)
        .score-box{

```
**[ADDED]**
```
223           .score{
```
**[REMOVED]**
```
(from line ~227)
        .score-box h3{

```
**[ADDED]**
```
227           .score h3{
```
**[REMOVED]**
```
(from line ~231)
        .score{

```
**[ADDED]**
```
231           .score-value{
```
**[REMOVED]**
```
(from line ~242)
            color:#d2d2d2;

```
**[ADDED]**
```
242               color:#d5d5d5;
```
**[REMOVED]**
```
(from line ~250)
            margin-top:20px;

```
**[ADDED]**
```
253               margin-top:20px;
```
**[REMOVED]**
```
(from line ~263)
        /* VISUALIZATION */

        .visualization-grid{
            margin-top:30px;
            display:grid;
            grid-template-columns:1fr 1fr;
            gap:25px;
        }

        canvas{
            width:100% !important;
            max-height:350px;
        }


```
**[REMOVED]**
```
(from line ~265)
        .stats-grid{

```
**[ADDED]**
```
265           .stats{
```
**[REMOVED]**
```
(from line ~268)
            gap:18px;
            margin-top:20px;

```
**[ADDED]**
```
268               gap:15px;
269               margin-top:25px;
```
**[REMOVED]**
```
(from line ~272)
        .stat-box{
            background:#111A3C;

```
**[ADDED]**
```
272           .stat-card{
273               background:#121C45;
```
**[REMOVED]**
```
(from line ~279)
        .stat-box h2{
            font-size:32px;

```
**[ADDED]**
```
279           .stat-card h2{
280               font-size:35px;
```
**[REMOVED]**
```
(from line ~285)
        .stat-box p{
            color:#bdbdbd;

```
**[ADDED]**
```
285           .stat-card p{
286               color:#c5c5c5;
```
**[ADDED]**
```
290           /* CHARTS */
291   
292           .charts{
293               margin-top:30px;
294               display:grid;
295               grid-template-columns:1fr 1fr;
296               gap:25px;
297           }
298   
299           canvas{
300               width:100% !important;
301               max-height:350px;
302           }
303   
```
**[REMOVED]**
```
(from line ~308)
            .main-container,
            .results-container,
            .visualization-grid{

```
**[ADDED]**
```
308               .top-grid,
309               .results-grid,
310               .charts{
```
**[REMOVED]**
```
(from line ~316)
                font-size:40px;

```
**[ADDED]**
```
316                   font-size:38px;
```
**[REMOVED]**
```
(from line ~319)
            .result-flex{

```
**[ADDED]**
```
319               .result-box{
```
**[REMOVED]**
```
(from line ~349)
    <div class="main-container">

```
**[ADDED]**
```
349       <div class="top-grid">
```
**[REMOVED]**
```
(from line ~367)
                <div class="button-group">

```
**[ADDED]**
```
367                   <div class="buttons">
```
**[REMOVED]**
```
(from line ~369)
                    <button class="analyze-btn">

```
**[ADDED]**
```
369                       <button class="analyze-btn" type="submit">
```
**[REMOVED]**
```
(from line ~374)
                    <button type="reset" class="clear-btn">

```
**[ADDED]**
```
374                       <button class="clear-btn" type="reset">
```
**[REMOVED]**
```
(from line ~387)
        <div class="card analyzer-card">

```
**[ADDED]**
```
387           <div class="card analyzer">
```
**[REMOVED]**
```
(from line ~408)
    <!-- RESULTS -->

```
**[ADDED]**
```
408       <div class="results-grid">
```
**[REMOVED]**
```
(from line ~410)
    <div class="results-container">

```
**[ADDED]**
```
410           <!-- RESULT CARD -->
```
**[REMOVED]**
```
(from line ~412)
        <!-- PREDICTION RESULT -->


```
**[REMOVED]**
```
(from line ~419)
            <div class="result-flex">

```
**[ADDED]**
```
419               <div class="result-box">
```
**[REMOVED]**
```
(from line ~423)
                    <div class="result-icon {% if prediction == 'REAL' %}real{% else %}fake{% endif %}">

```
**[ADDED]**
```
423                       {% if prediction == "REAL" %}
```
**[REMOVED]**
```
(from line ~425)
                        {% if prediction == "REAL" %}

                            <i class="fa-solid fa-check"></i>

                        {% else %}

                            <i class="fa-solid fa-triangle-exclamation"></i>

                        {% endif %}


```
**[ADDED]**
```
425                       <div class="status-icon real">
426                           <i class="fa-solid fa-check"></i>
```
**[REMOVED]**
```
(from line ~431)
                        {% if prediction == "REAL" %}

```
**[ADDED]**
```
431                           <h2 style="color:#00E676;">
432                               REAL NEWS
433                           </h2>
```
**[REMOVED]**
```
(from line ~435)
                            <h2 style="color:#00E676;">
                                REAL NEWS
                            </h2>

```
**[ADDED]**
```
435                           <p>
436                               This article appears authentic
437                           </p>
```
**[REMOVED]**
```
(from line ~439)
                            <p>
                                This article appears authentic
                            </p>

```
**[ADDED]**
```
439                       </div>
```
**[REMOVED]**
```
(from line ~441)
                        {% else %}

```
**[ADDED]**
```
441                       {% else %}
```
**[REMOVED]**
```
(from line ~443)
                            <h2 style="color:#FF4D6D;">
                                FAKE NEWS
                            </h2>

```
**[ADDED]**
```
443                       <div class="status-icon fake">
444                           <i class="fa-solid fa-triangle-exclamation"></i>
445                       </div>
```
**[REMOVED]**
```
(from line ~447)
                            <p>
                                This article appears misleading
                            </p>

```
**[ADDED]**
```
447                       <div class="result-text">
```
**[REMOVED]**
```
(from line ~449)
                        {% endif %}

```
**[ADDED]**
```
449                           <h2 style="color:#FF4D6D;">
450                               FAKE NEWS
451                           </h2>
```
**[ADDED]**
```
453                           <p>
454                               This article appears misleading
455                           </p>
456   
```
**[ADDED]**
```
459                       {% endif %}
460   
```
**[REMOVED]**
```
(from line ~463)
                <div class="score-box">

```
**[ADDED]**
```
463                   <div class="score">
```
**[REMOVED]**
```
(from line ~467)
                    <div class="score">

```
**[ADDED]**
```
467                       <div class="score-value">
```
**[REMOVED]**
```
(from line ~475)
            <!-- EXTRA STATS -->

```
**[ADDED]**
```
475               <!-- STATS -->
```
**[REMOVED]**
```
(from line ~477)
            <div class="stats-grid">

```
**[ADDED]**
```
477               <div class="stats">
```
**[REMOVED]**
```
(from line ~479)
                <div class="stat-box">

```
**[ADDED]**
```
479                   <div class="stat-card">
```
**[REMOVED]**
```
(from line ~489)
                <div class="stat-box">

```
**[ADDED]**
```
489                   <div class="stat-card">
```
**[REMOVED]**
```
(from line ~513)


```
**[REMOVED]**
```
(from line ~514)


```
**[REMOVED]**
```
(from line ~532)
    <!-- VISUALIZATION -->

```
**[ADDED]**
```
532       <!-- CHARTS -->
```
**[REMOVED]**
```
(from line ~534)
    <div class="visualization-grid">

```
**[ADDED]**
```
534       <div class="charts">
```
**[REMOVED]**
```
(from line ~598)
                responsive: true,


```
**[REMOVED]**
```
(from line ~604)
                            color: 'white',
                            font: {
                                size: 14
                            }

```
**[ADDED]**
```
604                               color: 'white'
```
**[REMOVED]**
```
(from line ~642)
                responsive: true,


```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\index.html
*Saved at: 5/13/2026, 2:33:50 PM*

**[ADDED]**
```
19        <!-- Chart JS -->
20        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
21    
```
**[REMOVED]**
```
(from line ~60)
        /* MAIN GRID */

```
**[ADDED]**
```
60            /* GRID */
```
**[REMOVED]**
```
(from line ~64)
            grid-template-columns: 2fr 1fr;

```
**[ADDED]**
```
64                grid-template-columns:2fr 1fr;
```
**[REMOVED]**
```
(from line ~75)
            box-shadow:0 0 20px rgba(0,0,0,0.3);

```
**[ADDED]**
```
75                box-shadow:0 0 20px rgba(0,0,0,0.35);
```
**[REMOVED]**
```
(from line ~79)
            font-size:20px;

```
**[ADDED]**
```
79                font-size:22px;
```
**[REMOVED]**
```
(from line ~81)
            margin-bottom:20px;

```
**[ADDED]**
```
81                margin-bottom:22px;
```
**[REMOVED]**
```
(from line ~92)
            height:220px;

```
**[ADDED]**
```
92                height:240px;
```
**[REMOVED]**
```
(from line ~104)
            color:#8d8d8d;

```
**[ADDED]**
```
104               color:#888;
```
**[REMOVED]**
```
(from line ~110)
            margin-top:20px;

```
**[ADDED]**
```
112               margin-top:22px;
```
**[REMOVED]**
```
(from line ~116)


```
**[REMOVED]**
```
(from line ~133)

            background:#1A2246;

```
**[ADDED]**
```
133               background:#1B2449;
```
**[REMOVED]**
```
(from line ~143)
        /* ANALYZER CARD */

```
**[ADDED]**
```
143           /* ANALYZER */
```
**[REMOVED]**
```
(from line ~154)
            width:90px;
            height:90px;

```
**[ADDED]**
```
154               width:95px;
155               height:95px;
```
**[REMOVED]**
```
(from line ~165)
            font-size:38px;

```
**[ADDED]**
```
165               font-size:40px;
```
**[REMOVED]**
```
(from line ~169)
            font-size:42px;

```
**[ADDED]**
```
169               font-size:36px;
```
**[REMOVED]**
```
(from line ~174)
            color:#c5c5c5;
            line-height:1.7;

```
**[ADDED]**
```
174               color:#d2d2d2;
175               line-height:1.8;
```
**[REMOVED]**
```
(from line ~178)
        /* RESULT SECTION */

```
**[ADDED]**
```
178           /* RESULTS SECTION */
```
**[REMOVED]**
```
(from line ~180)
        .bottom-container{

```
**[ADDED]**
```
180           .results-container{
181               margin-top:30px;
```
**[REMOVED]**
```
(from line ~183)
            grid-template-columns: 1fr 1fr;

```
**[ADDED]**
```
183               grid-template-columns:1fr 1fr;
```
**[REMOVED]**
```
(from line ~185)
            margin-top:25px;

```
**[REMOVED]**
```
(from line ~193)
            margin-top:20px;

```
**[ADDED]**
```
193               margin-top:25px;
```
**[REMOVED]**
```
(from line ~203)
            width:70px;
            height:70px;

```
**[ADDED]**
```
203               width:75px;
204               height:75px;
```
**[REMOVED]**
```
(from line ~206)
            background:#00D26A;

```
**[ADDED]**
```
211           .result-icon.real{
212               background:#00D26A;
213           }
214   
215           .result-icon.fake{
216               background:#FF4D6D;
217           }
218   
```
**[REMOVED]**
```
(from line ~225)
            color:#00E676;

```
**[REMOVED]**
```
(from line ~229)
            color:#bcbcbc;
            margin-top:6px;

```
**[ADDED]**
```
229               margin-top:5px;
230               color:#c7c7c7;
```
**[REMOVED]**
```
(from line ~240)
            font-size:20px;

```
**[REMOVED]**
```
(from line ~244)
            font-size:72px;

```
**[ADDED]**
```
244               font-size:70px;
```
**[REMOVED]**
```
(from line ~253)
        .explanation-card p{
            color:#d1d1d1;

```
**[ADDED]**
```
253           .explanation{
254               color:#d2d2d2;
```
**[REMOVED]**
```
(from line ~256)
            margin-top:18px;

```
**[ADDED]**
```
256               margin-top:15px;
```
**[ADDED]**
```
259           /* WORDS */
260   
```
**[REMOVED]**
```
(from line ~262)
            margin-top:18px;

```
**[ADDED]**
```
262               margin-top:20px;
```
**[REMOVED]**
```
(from line ~277)
        .chart-section{
            margin-top:25px;

```
**[ADDED]**
```
277           .visualization-grid{
278               margin-top:30px;
279               display:grid;
280               grid-template-columns:1fr 1fr;
281               gap:25px;
```
**[REMOVED]**
```
(from line ~284)
        .chart-section img{
            width:100%;
            border-radius:20px;

```
**[ADDED]**
```
284           canvas{
285               width:100% !important;
286               max-height:350px;
```
**[ADDED]**
```
289           /* STATS */
290   
291           .stats-grid{
292               display:grid;
293               grid-template-columns:1fr 1fr;
294               gap:18px;
295               margin-top:20px;
296           }
297   
298           .stat-box{
299               background:#111A3C;
300               padding:20px;
301               border-radius:18px;
302               text-align:center;
303           }
304   
305           .stat-box h2{
306               font-size:32px;
307               margin-top:10px;
308               color:#B026FF;
309           }
310   
311           .stat-box p{
312               color:#bdbdbd;
313               margin-top:5px;
314           }
315   
```
**[REMOVED]**
```
(from line ~320)
            .main-container{
                grid-template-columns:1fr;
            }

```
**[ADDED]**
```
320               .main-container,
321               .results-container,
322               .visualization-grid{
```
**[REMOVED]**
```
(from line ~324)
            .bottom-container{

```
**[REMOVED]**
```
(from line ~333)
                gap:30px;

```
**[ADDED]**
```
334                   gap:30px;
```
**[REMOVED]**
```
(from line ~363)
        <!-- INPUT CARD -->

```
**[ADDED]**
```
363           <!-- INPUT -->
```
**[REMOVED]**
```
(from line ~397)
        <!-- AI ANALYZER CARD -->

```
**[ADDED]**
```
397           <!-- AI CARD -->
```
**[REMOVED]**
```
(from line ~408)
                Detect fake news with advanced NLP algorithms and explainable AI.

```
**[ADDED]**
```
408                   Detect fake news using NLP, machine learning,
409                   confidence analysis and explainable AI visualizations.
```
**[REMOVED]**
```
(from line ~416)
    <!-- BOTTOM SECTION -->

```
**[ADDED]**
```
416       <!-- OUTPUT SECTION -->
```
**[REMOVED]**
```
(from line ~420)
    <div class="bottom-container">

```
**[ADDED]**
```
420       <!-- RESULTS -->
```
**[REMOVED]**
```
(from line ~422)
        <!-- RESULT CARD -->

```
**[ADDED]**
```
422       <div class="results-container">
```
**[ADDED]**
```
424           <!-- PREDICTION RESULT -->
425   
```
**[REMOVED]**
```
(from line ~437)
                    <div class="result-icon">

```
**[ADDED]**
```
437                       <div class="result-icon {% if prediction == 'REAL' %}real{% else %}fake{% endif %}">
```
**[REMOVED]**
```
(from line ~460)
                                This news appears authentic

```
**[ADDED]**
```
460                                   This article appears authentic
```
**[REMOVED]**
```
(from line ~470)
                                This news appears misleading

```
**[ADDED]**
```
470                                   This article appears misleading
```
**[ADDED]**
```
491               <!-- EXTRA STATS -->
492   
493               <div class="stats-grid">
494   
495                   <div class="stat-box">
496   
497                       <i class="fa-solid fa-circle-xmark"></i>
498   
499                       <h2>{{ fake_prob }}%</h2>
500   
501                       <p>Fake Probability</p>
502   
503                   </div>
504   
505                   <div class="stat-box">
506   
507                       <i class="fa-solid fa-circle-check"></i>
508   
509                       <h2>{{ real_prob }}%</h2>
510   
511                       <p>Real Probability</p>
512   
513                   </div>
514   
515               </div>
516   
```
**[REMOVED]**
```
(from line ~521)
        <div class="card explanation-card">

```
**[ADDED]**
```
521           <div class="card">
```
**[REMOVED]**
```
(from line ~525)
                Why this prediction?

```
**[ADDED]**
```
525                   Explainable AI Analysis
```
**[REMOVED]**
```
(from line ~528)
            <p>

```
**[ADDED]**
```
528               <div class="explanation">
529   
```
**[REMOVED]**
```
(from line ~531)
            </p>

```
**[ADDED]**
```
532               </div>
533   
```
**[REMOVED]**
```
(from line ~552)
    <div class="card chart-section">

```
**[ADDED]**
```
552       <div class="visualization-grid">
```
**[REMOVED]**
```
(from line ~554)
        <div class="card-title">
            <i class="fa-solid fa-chart-simple"></i>
            Prediction Visualization

```
**[ADDED]**
```
554           <!-- PIE CHART -->
555   
556           <div class="card">
557   
558               <div class="card-title">
559                   <i class="fa-solid fa-chart-pie"></i>
560                   Prediction Distribution
561               </div>
562   
563               <canvas id="pieChart"></canvas>
564   
```
**[REMOVED]**
```
(from line ~567)
        <img
            src="{{ url_for('static', filename='chart.png') }}"
            alt="Chart">

```
**[ADDED]**
```
567           <!-- BAR CHART -->
```
**[ADDED]**
```
569           <div class="card">
570   
571               <div class="card-title">
572                   <i class="fa-solid fa-chart-simple"></i>
573                   Confidence Comparison
574               </div>
575   
576               <canvas id="barChart"></canvas>
577   
578           </div>
579   
```
**[ADDED]**
```
582       <!-- CHART SCRIPT -->
583   
584       <script>
585   
586           // PIE CHART
587   
588           const pieCtx = document.getElementById('pieChart');
589   
590           new Chart(pieCtx, {
591   
592               type: 'pie',
593   
594               data: {
595   
596                   labels: ['Fake News', 'Real News'],
597   
598                   datasets: [{
599   
600                       data: [{{ fake_prob }}, {{ real_prob }}],
601   
602                       backgroundColor: [
603   
604                           '#FF4D6D',
605                           '#00E676'
606   
607                       ],
608   
609                       borderWidth: 0
610   
611                   }]
612               },
613   
614               options: {
615   
616                   responsive: true,
617   
618                   plugins: {
619   
620                       legend: {
621   
622                           labels: {
623   
624                               color: 'white',
625                               font: {
626                                   size: 14
627                               }
628                           }
629                       }
630                   }
631               }
632           });
633   
634           // BAR CHART
635   
636           const barCtx = document.getElementById('barChart');
637   
638           new Chart(barCtx, {
639   
640               type: 'bar',
641   
642               data: {
643   
644                   labels: ['Fake', 'Real'],
645   
646                   datasets: [{
647   
648                       label: 'Confidence %',
649   
650                       data: [{{ fake_prob }}, {{ real_prob }}],
651   
652                       backgroundColor: [
653   
654                           '#FF4D6D',
655                           '#00E676'
656   
657                       ],
658   
659                       borderRadius: 10
660                   }]
661               },
662   
663               options: {
664   
665                   responsive: true,
666   
667                   scales: {
668   
669                       y: {
670   
671                           beginAtZero: true,
672   
673                           max: 100,
674   
675                           ticks: {
676   
677                               color: 'white'
678                           },
679   
680                           grid: {
681   
682                               color: 'rgba(255,255,255,0.1)'
683                           }
684                       },
685   
686                       x: {
687   
688                           ticks: {
689   
690                               color: 'white'
691                           },
692   
693                           grid: {
694   
695                               color: 'rgba(255,255,255,0.1)'
696                           }
697                       }
698                   },
699   
700                   plugins: {
701   
702                       legend: {
703   
704                           labels: {
705   
706                               color: 'white'
707                           }
708                       }
709                   }
710               }
711           });
712   
713       </script>
714   
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\index.html
*Saved at: 5/13/2026, 2:28:15 PM*

**[REMOVED]**
```
(from line ~2)
<html>

```
**[ADDED]**
```
2     <html lang="en">
```
**[ADDED]**
```
6         <meta charset="UTF-8">
7         <meta name="viewport" content="width=device-width, initial-scale=1.0">
8     
```
**[ADDED]**
```
11        <!-- Google Font -->
12        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap"
13            rel="stylesheet">
14    
15        <!-- Font Awesome -->
16        <link rel="stylesheet"
17            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
18    
19        <style>
20    
21            *{
22                margin:0;
23                padding:0;
24                box-sizing:border-box;
25                font-family:'Poppins', sans-serif;
26            }
27    
28            body{
29                background:#020B2D;
30                min-height:100vh;
31                color:white;
32                padding:20px 40px;
33            }
34    
35            /* HEADER */
36    
37            .header{
38                text-align:center;
39                margin-bottom:35px;
40            }
41    
42            .header h1{
43                font-size:58px;
44                font-weight:800;
45            }
46    
47            .header h1 span{
48                color:#B026FF;
49            }
50    
51            .header p{
52                margin-top:10px;
53                color:#bdbdbd;
54                font-size:18px;
55            }
56    
57            /* MAIN GRID */
58    
59            .main-container{
60                display:grid;
61                grid-template-columns: 2fr 1fr;
62                gap:25px;
63            }
64    
65            /* CARD */
66    
67            .card{
68                background:#0D132E;
69                border-radius:25px;
70                padding:28px;
71                border:1px solid rgba(255,255,255,0.05);
72                box-shadow:0 0 20px rgba(0,0,0,0.3);
73            }
74    
75            .card-title{
76                font-size:20px;
77                font-weight:700;
78                margin-bottom:20px;
79            }
80    
81            .card-title i{
82                margin-right:10px;
83            }
84    
85            /* TEXTAREA */
86    
87            textarea{
88                width:100%;
89                height:220px;
90                background:#050E33;
91                border:2px solid #7B2FF7;
92                border-radius:18px;
93                padding:18px;
94                color:white;
95                resize:none;
96                outline:none;
97                font-size:15px;
98            }
99    
100           textarea::placeholder{
101               color:#8d8d8d;
102           }
103   
104           /* BUTTONS */
105   
106           .button-group{
107               margin-top:20px;
108               display:flex;
109               gap:15px;
110           }
111   
112           .analyze-btn{
113   
114               background:linear-gradient(90deg,#7B2FF7,#F107A3);
115               border:none;
116               padding:14px 28px;
117               border-radius:14px;
118               color:white;
119               font-size:16px;
120               font-weight:600;
121               cursor:pointer;
122               transition:0.3s;
123           }
124   
125           .analyze-btn:hover{
126               transform:translateY(-2px);
127               box-shadow:0 0 20px rgba(176,38,255,0.5);
128           }
129   
130           .clear-btn{
131   
132               background:#1A2246;
133               border:none;
134               padding:14px 28px;
135               border-radius:14px;
136               color:white;
137               font-size:16px;
138               font-weight:600;
139               cursor:pointer;
140           }
141   
142           /* ANALYZER CARD */
143   
144           .analyzer-card{
145               display:flex;
146               flex-direction:column;
147               justify-content:center;
148               align-items:center;
149               text-align:center;
150           }
151   
152           .analyzer-icon{
153               width:90px;
154               height:90px;
155               border-radius:50%;
156               background:linear-gradient(135deg,#7B2FF7,#F107A3);
157               display:flex;
158               justify-content:center;
159               align-items:center;
160               margin-bottom:25px;
161           }
162   
163           .analyzer-icon i{
164               font-size:38px;
165           }
166   
167           .analyzer-card h2{
168               font-size:42px;
169               margin-bottom:12px;
170           }
171   
172           .analyzer-card p{
173               color:#c5c5c5;
174               line-height:1.7;
175           }
176   
177           /* RESULT SECTION */
178   
179           .bottom-container{
180               display:grid;
181               grid-template-columns: 1fr 1fr;
182               gap:25px;
183               margin-top:25px;
184           }
185   
186           /* RESULT CARD */
187   
188           .result-flex{
189               display:flex;
190               justify-content:space-between;
191               align-items:center;
192               margin-top:20px;
193           }
194   
195           .result-left{
196               display:flex;
197               align-items:center;
198               gap:18px;
199           }
200   
201           .result-icon{
202               width:70px;
203               height:70px;
204               border-radius:50%;
205               background:#00D26A;
206               display:flex;
207               justify-content:center;
208               align-items:center;
209           }
210   
211           .result-icon i{
212               font-size:32px;
213               color:black;
214           }
215   
216           .result-text h2{
217               color:#00E676;
218               font-size:40px;
219           }
220   
221           .result-text p{
222               color:#bcbcbc;
223               margin-top:6px;
224           }
225   
226           /* SCORE */
227   
228           .score-box{
229               text-align:center;
230           }
231   
232           .score-box h3{
233               font-size:20px;
234               margin-bottom:12px;
235           }
236   
237           .score{
238               font-size:72px;
239               font-weight:700;
240               background:linear-gradient(90deg,#7B2FF7,#F107A3);
241               -webkit-background-clip:text;
242               -webkit-text-fill-color:transparent;
243           }
244   
245           /* EXPLANATION */
246   
247           .explanation-card p{
248               color:#d1d1d1;
249               line-height:1.9;
250               margin-top:18px;
251           }
252   
253           .words{
254               margin-top:18px;
255               display:flex;
256               flex-wrap:wrap;
257               gap:10px;
258           }
259   
260           .word{
261               background:#7B2FF7;
262               padding:8px 14px;
263               border-radius:12px;
264               font-size:14px;
265           }
266   
267           /* VISUALIZATION */
268   
269           .chart-section{
270               margin-top:25px;
271           }
272   
273           .chart-section img{
274               width:100%;
275               border-radius:20px;
276           }
277   
278           /* RESPONSIVE */
279   
280           @media(max-width:1100px){
281   
282               .main-container{
283                   grid-template-columns:1fr;
284               }
285   
286               .bottom-container{
287                   grid-template-columns:1fr;
288               }
289   
290               .header h1{
291                   font-size:40px;
292               }
293   
294               .result-flex{
295                   flex-direction:column;
296                   gap:30px;
297                   align-items:flex-start;
298               }
299           }
300   
301       </style>
302   
```
**[REMOVED]**
```
(from line ~307)
    <h1>Fake News Detection System</h1>

```
**[ADDED]**
```
307       <!-- HEADER -->
```
**[REMOVED]**
```
(from line ~309)
    <form action="/predict" method="POST">

```
**[ADDED]**
```
309       <div class="header">
```
**[REMOVED]**
```
(from line ~311)
        <textarea
            name="news"
            rows="12"
            cols="100"
            placeholder="Enter news article here..."
            required>
        </textarea>

```
**[ADDED]**
```
311           <h1>
312               <i class="fa-regular fa-newspaper"></i>
313               Fake News <span>Detection System</span>
314           </h1>
```
**[REMOVED]**
```
(from line ~316)
        <br><br>

```
**[ADDED]**
```
316           <p>
317               AI-Powered News Verification with Explainability
318           </p>
```
**[REMOVED]**
```
(from line ~320)
        <button type="submit">
            Analyze
        </button>

```
**[ADDED]**
```
320       </div>
```
**[REMOVED]**
```
(from line ~322)
    </form>

```
**[ADDED]**
```
322       <!-- TOP SECTION -->
```
**[ADDED]**
```
324       <div class="main-container">
325   
326           <!-- INPUT CARD -->
327   
328           <div class="card">
329   
330               <div class="card-title">
331                   <i class="fa-solid fa-pen"></i>
332                   Enter News Article
333               </div>
334   
335               <form action="/predict" method="POST">
336   
337                   <textarea
338                       name="news"
339                       placeholder="Paste news article here..."
340                       required></textarea>
341   
342                   <div class="button-group">
343   
344                       <button class="analyze-btn">
345                           <i class="fa-solid fa-magnifying-glass"></i>
346                           Analyze News
347                       </button>
348   
349                       <button type="reset" class="clear-btn">
350                           <i class="fa-solid fa-trash"></i>
351                           Clear
352                       </button>
353   
354                   </div>
355   
356               </form>
357   
358           </div>
359   
360           <!-- AI ANALYZER CARD -->
361   
362           <div class="card analyzer-card">
363   
364               <div class="analyzer-icon">
365                   <i class="fa-solid fa-magnifying-glass-chart"></i>
366               </div>
367   
368               <h2>AI News Analyzer</h2>
369   
370               <p>
371                   Detect fake news with advanced NLP algorithms and explainable AI.
372               </p>
373   
374           </div>
375   
376       </div>
377   
378       <!-- BOTTOM SECTION -->
379   
```
**[REMOVED]**
```
(from line ~382)
        <hr>

```
**[ADDED]**
```
382       <div class="bottom-container">
```
**[REMOVED]**
```
(from line ~384)
        <h2>Prediction: {{ prediction }}</h2>

```
**[ADDED]**
```
384           <!-- RESULT CARD -->
```
**[REMOVED]**
```
(from line ~386)
        <h3>Confidence: {{ confidence }}%</h3>

```
**[ADDED]**
```
386           <div class="card">
```
**[REMOVED]**
```
(from line ~388)
        <h3>Explanation:</h3>

```
**[ADDED]**
```
388               <div class="card-title">
389                   <i class="fa-solid fa-chart-column"></i>
390                   Prediction Result
391               </div>
```
**[REMOVED]**
```
(from line ~393)
        <p>{{ explanation }}</p>

```
**[ADDED]**
```
393               <div class="result-flex">
```
**[REMOVED]**
```
(from line ~395)
        <h3>Influential Words:</h3>

```
**[ADDED]**
```
395                   <div class="result-left">
```
**[REMOVED]**
```
(from line ~397)
        <ul>

```
**[ADDED]**
```
397                       <div class="result-icon">
```
**[REMOVED]**
```
(from line ~399)
            {% for word in influential_words %}

```
**[ADDED]**
```
399                           {% if prediction == "REAL" %}
```
**[REMOVED]**
```
(from line ~401)
                <li>{{ word }}</li>

```
**[ADDED]**
```
401                               <i class="fa-solid fa-check"></i>
```
**[REMOVED]**
```
(from line ~403)
            {% endfor %}

```
**[ADDED]**
```
403                           {% else %}
```
**[REMOVED]**
```
(from line ~405)
        </ul>

```
**[ADDED]**
```
405                               <i class="fa-solid fa-triangle-exclamation"></i>
```
**[REMOVED]**
```
(from line ~407)
        <h3>Visualization:</h3>

```
**[ADDED]**
```
407                           {% endif %}
```
**[ADDED]**
```
409                       </div>
410   
411                       <div class="result-text">
412   
413                           {% if prediction == "REAL" %}
414   
415                               <h2 style="color:#00E676;">
416                                   REAL NEWS
417                               </h2>
418   
419                               <p>
420                                   This news appears authentic
421                               </p>
422   
423                           {% else %}
424   
425                               <h2 style="color:#FF4D6D;">
426                                   FAKE NEWS
427                               </h2>
428   
429                               <p>
430                                   This news appears misleading
431                               </p>
432   
433                           {% endif %}
434   
435                       </div>
436   
437                   </div>
438   
439                   <div class="score-box">
440   
441                       <h3>Confidence Score</h3>
442   
443                       <div class="score">
444                           {{ confidence }}%
445                       </div>
446   
447                   </div>
448   
449               </div>
450   
451           </div>
452   
453           <!-- EXPLANATION -->
454   
455           <div class="card explanation-card">
456   
457               <div class="card-title">
458                   <i class="fa-solid fa-brain"></i>
459                   Why this prediction?
460               </div>
461   
462               <p>
463                   {{ explanation }}
464               </p>
465   
466               <div class="words">
467   
468                   {% for word in influential_words %}
469   
470                       <div class="word">
471                           {{ word }}
472                       </div>
473   
474                   {% endfor %}
475   
476               </div>
477   
478           </div>
479   
480       </div>
481   
482       <!-- VISUALIZATION -->
483   
484       <div class="card chart-section">
485   
486           <div class="card-title">
487               <i class="fa-solid fa-chart-simple"></i>
488               Prediction Visualization
489           </div>
490   
```
**[REMOVED]**
```
(from line ~493)
            width="500"
        >

```
**[ADDED]**
```
493               alt="Chart">
```
**[ADDED]**
```
495       </div>
496   
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\login.html
*Saved at: 5/13/2026, 2:07:27 PM*

**[REMOVED]**
```
(from line ~109)
                    <a href="register.html">Register</a>

```
**[ADDED]**
```
109                       <a href="{{ url_for('register') }}">Register</a>
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\register.html
*Saved at: 5/13/2026, 2:04:18 PM*

**[REMOVED]**
```
(from line ~1)
*{

```
**[ADDED]**
```
1     <!DOCTYPE html>
2     <html lang="en">
3     <head>
4         <meta charset="UTF-8">
5         <meta name="viewport" content="width=device-width, initial-scale=1.0">
6         <title>Register - Fake News Detection</title>
```
**[REMOVED]**
```
(from line ~8)
    transition:0.3s;
}

```
**[ADDED]**
```
8         <!-- Google Font -->
9         <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```
**[REMOVED]**
```
(from line ~11)
.login-btn:hover{

```
**[ADDED]**
```
11        <!-- Font Awesome -->
12        <link rel="stylesheet"
13              href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
```
**[REMOVED]**
```
(from line ~15)
    transform:translateY(-2px);

```
**[ADDED]**
```
15        <style>
```
**[REMOVED]**
```
(from line ~17)
    box-shadow:0 0 20px rgba(192,38,255,0.5);
}

```
**[ADDED]**
```
17            *{
18                margin:0;
19                padding:0;
20                box-sizing:border-box;
21                font-family:'Poppins', sans-serif;
22            }
```
**[ADDED]**
```
24            body{
25                width:100%;
26                height:100vh;
27                background:#020B2D;
28                overflow:hidden;
29            }
```
**[REMOVED]**
```
(from line ~31)
/* BOTTOM TEXT */

```
**[ADDED]**
```
31            .container{
32                display:flex;
33                width:100%;
34                height:100vh;
35            }
```
**[REMOVED]**
```
(from line ~37)
.bottom-text{

```
**[ADDED]**
```
37            /* LEFT SECTION */
```
**[REMOVED]**
```
(from line ~39)
    margin-top:25px;

```
**[ADDED]**
```
39            .left-section{
40                width:50%;
41                height:100%;
42                background:#020B2D;
43                display:flex;
44                justify-content:center;
45                align-items:center;
46                flex-direction:column;
47                border-right:1px solid rgba(255,255,255,0.05);
48            }
```
**[REMOVED]**
```
(from line ~50)
    text-align:center;

```
**[ADDED]**
```
50            .logo-box{
51                width:100px;
52                height:100px;
53                background:linear-gradient(135deg,#7B2FF7,#F107A3);
54                border-radius:25px;
55                display:flex;
56                justify-content:center;
57                align-items:center;
58                box-shadow:0 0 30px rgba(161, 66, 255, 0.6);
59                margin-bottom:35px;
60            }
```
**[REMOVED]**
```
(from line ~62)
    color:#9ca3af;
}

```
**[ADDED]**
```
62            .logo-box i{
63                font-size:45px;
64                color:white;
65            }
```
**[REMOVED]**
```
(from line ~67)
.bottom-text a{

```
**[ADDED]**
```
67            .main-title{
68                font-size:64px;
69                color:white;
70                font-weight:700;
71            }
```
**[REMOVED]**
```
(from line ~73)
    color:#c026ff;

```
**[ADDED]**
```
73            .main-title span{
74                color:#B026FF;
75            }
```
**[REMOVED]**
```
(from line ~77)
    text-decoration:none;

```
**[ADDED]**
```
77            .subtitle{
78                margin-top:20px;
79                color:#d7d7d7;
80                font-size:20px;
81                font-weight:300;
82            }
```
**[REMOVED]**
```
(from line ~84)
    font-weight:600;
}

```
**[ADDED]**
```
84            /* RIGHT SECTION */
```
**[ADDED]**
```
86            .right-section{
87                width:50%;
88                height:100%;
89                display:flex;
90                justify-content:center;
91                align-items:center;
92                background:#00092A;
93            }
```
**[REMOVED]**
```
(from line ~95)
/* ERROR */

```
**[ADDED]**
```
95            .register-card{
96                width:430px;
97                background:#0E1430;
98                border-radius:25px;
99                padding:45px;
100               border:1px solid rgba(255,255,255,0.08);
101               box-shadow:0 0 20px rgba(0,0,0,0.4);
102           }
```
**[REMOVED]**
```
(from line ~104)
.error-message{

```
**[ADDED]**
```
104           .register-card h1{
105               color:white;
106               font-size:42px;
107               margin-bottom:10px;
108           }
```
**[REMOVED]**
```
(from line ~110)
    background:#ff4d4d;

```
**[ADDED]**
```
110           .register-card p{
111               color:#b6b6b6;
112               margin-bottom:35px;
113           }
```
**[REMOVED]**
```
(from line ~115)
    padding:12px;

```
**[ADDED]**
```
115           .input-box{
116               width:100%;
117               height:55px;
118               background:#0B1436;
119               border-radius:15px;
120               margin-bottom:22px;
121               display:flex;
122               align-items:center;
123               padding:0 18px;
124               border:2px solid transparent;
125               transition:0.3s;
126           }
```
**[REMOVED]**
```
(from line ~128)
    border-radius:10px;

```
**[ADDED]**
```
128           .input-box:focus-within{
129               border:2px solid #B026FF;
130               box-shadow:0 0 15px rgba(176,38,255,0.5);
131           }
```
**[REMOVED]**
```
(from line ~133)
    margin-bottom:20px;

```
**[ADDED]**
```
133           .input-box i{
134               color:#B026FF;
135               margin-right:12px;
136               font-size:15px;
137           }
```
**[REMOVED]**
```
(from line ~139)
    text-align:center;

```
**[ADDED]**
```
139           .input-box input{
140               width:100%;
141               background:none;
142               border:none;
143               outline:none;
144               color:white;
145               font-size:15px;
146           }
```
**[REMOVED]**
```
(from line ~148)
    color:white;
}

```
**[ADDED]**
```
148           .input-box input::placeholder{
149               color:#8d8d8d;
150           }
```
**[ADDED]**
```
152           .register-btn{
153               width:100%;
154               height:55px;
155               border:none;
156               border-radius:15px;
157               background:linear-gradient(90deg,#7B2FF7,#F107A3);
158               color:white;
159               font-size:18px;
160               font-weight:600;
161               cursor:pointer;
162               margin-top:10px;
163               transition:0.3s;
164           }
```
**[REMOVED]**
```
(from line ~166)
/* RESPONSIVE */

```
**[ADDED]**
```
166           .register-btn:hover{
167               transform:translateY(-2px);
168               box-shadow:0 0 20px rgba(176,38,255,0.5);
169           }
```
**[REMOVED]**
```
(from line ~171)
@media(max-width:992px){

```
**[ADDED]**
```
171           .bottom-text{
172               margin-top:25px;
173               text-align:center;
174               color:#bfbfbf;
175               font-size:14px;
176           }
```
**[REMOVED]**
```
(from line ~178)
    .main-container{
        flex-direction:column;
    }

```
**[ADDED]**
```
178           .bottom-text a{
179               color:#B026FF;
180               text-decoration:none;
181               font-weight:600;
182           }
```
**[REMOVED]**
```
(from line ~184)
    .left-section,
    .right-section{
        width:100%;
        height:50vh;
    }

```
**[ADDED]**
```
184           /* RESPONSIVE */
```
**[REMOVED]**
```
(from line ~186)
    .left-section h1{
        font-size:45px;
    }

```
**[ADDED]**
```
186           @media(max-width:1000px){
```
**[REMOVED]**
```
(from line ~188)
    .left-section p{
        font-size:18px;
    }

```
**[ADDED]**
```
188               .left-section{
189                   display:none;
190               }
```
**[REMOVED]**
```
(from line ~192)
    .login-card{
        width:90%;
    }
}
```
**[ADDED]**
```
192               .right-section{
193                   width:100%;
194               }
195           }
196   
197       </style>
198   
199   </head>
200   <body>
201   
202       <div class="container">
203   
204           <!-- LEFT -->
205   
206           <div class="left-section">
207   
208               <div class="logo-box">
209                   <i class="fa-solid fa-shield-halved"></i>
210               </div>
211   
212               <h1 class="main-title">
213                   Fake News <span>Detection</span>
214               </h1>
215   
216               <p class="subtitle">
217                   AI-Powered News Verification System with Explainability
218               </p>
219   
220           </div>
221   
222           <!-- RIGHT -->
223   
224           <div class="right-section">
225   
226               <div class="register-card">
227   
228                   <h1>Create Account 🚀</h1>
229   
230                   <p>Register to continue</p>
231   
232                   <form action="/register" method="POST">
233   
234                       <div class="input-box">
235                           <i class="fa-solid fa-user"></i>
236                           <input type="text"
237                                  name="username"
238                                  placeholder="Enter username"
239                                  required>
240                       </div>
241   
242                       <div class="input-box">
243                           <i class="fa-solid fa-envelope"></i>
244                           <input type="email"
245                                  name="email"
246                                  placeholder="Enter your email"
247                                  required>
248                       </div>
249   
250                       <div class="input-box">
251                           <i class="fa-solid fa-lock"></i>
252                           <input type="password"
253                                  name="password"
254                                  placeholder="Enter password"
255                                  required>
256                       </div>
257   
258                       <div class="input-box">
259                           <i class="fa-solid fa-lock"></i>
260                           <input type="password"
261                                  name="confirm_password"
262                                  placeholder="Confirm password"
263                                  required>
264                       </div>
265   
266                       <button class="register-btn">
267                           <i class="fa-solid fa-user-plus"></i>
268                           Register
269                       </button>
270   
271                   </form>
272   
273                   <div class="bottom-text">
274                       Already have an account?
275                       <a href="/login">Login</a>
276                   </div>
277   
278               </div>
279   
280           </div>
281   
282       </div>
283   
284   </body>
285   </html>
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\login.html
*Saved at: 5/13/2026, 1:45:40 PM*

**[REMOVED]**
```
(from line ~109)
                    <a href="">Register</a>

```
**[ADDED]**
```
109                       <a href="register.html">Register</a>
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\login.html
*Saved at: 5/13/2026, 1:45:32 PM*

**[REMOVED]**
```
(from line ~109)
                    <a href="#">Register</a>

```
**[ADDED]**
```
109                       <a href="">Register</a>
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\Static\login.css
*Saved at: 5/13/2026, 10:28:09 AM*

**[REMOVED]**
```
(from line ~9)
    background:#020617;

```
**[ADDED]**
```
9         background:#020726;
```
**[REMOVED]**
```
(from line ~11)
    height:100vh;

```
**[REMOVED]**
```
(from line ~14)
/* Main Container */

.login-container{
    display:flex;

```
**[ADDED]**
```
14    .main-container{
15        width:100%;
```
**[ADDED]**
```
17        display:flex;
```
**[ADDED]**
```
23    
```
**[REMOVED]**
```
(from line ~25)
    background:linear-gradient(
        135deg,
        #050816,
        #0b1120
    );

```
**[REMOVED]**
```
(from line ~31)
    padding:50px;

```
**[ADDED]**
```
31        background:#020726;
32    
33        border-right:1px solid rgba(255,255,255,0.05);
```
**[REMOVED]**
```
(from line ~37)
    width:120px;
    height:120px;

```
**[ADDED]**
```
38        width:110px;
39        height:110px;
40    
```
**[REMOVED]**
```
(from line ~44)
        #ec4899

```
**[ADDED]**
```
44            #ff1493
```
**[REMOVED]**
```
(from line ~53)
    font-size:50px;

```
**[ADDED]**
```
53        font-size:45px;
```
**[REMOVED]**
```
(from line ~55)
    margin-bottom:30px;

```
**[ADDED]**
```
55        margin-bottom:40px;
```
**[REMOVED]**
```
(from line ~57)
    box-shadow:0 0 40px rgba(168,85,247,0.5);

```
**[ADDED]**
```
57        box-shadow:0 0 30px rgba(192,38,255,0.6);
```
**[REMOVED]**
```
(from line ~61)
    font-size:60px;

```
**[ADDED]**
```
61    
62        font-size:70px;
```
**[REMOVED]**
```
(from line ~71)
    margin-top:20px;
    color:#bdbdbd;
    font-size:18px;

```
**[ADDED]**
```
71    
72        margin-top:25px;
73    
74        font-size:22px;
75    
76        color:#d1d5db;
77    
```
**[REMOVED]**
```
(from line ~79)
    max-width:500px;

```
**[ADDED]**
```
81    
```
**[ADDED]**
```
85    
```
**[REMOVED]**
```
(from line ~92)
    background:#050816;

```
**[ADDED]**
```
92        background:#020726;
```
**[ADDED]**
```
95    
```
**[REMOVED]**
```
(from line ~102)
    background:rgba(255,255,255,0.05);

```
**[ADDED]**
```
102       background:#0a1033;
```
**[REMOVED]**
```
(from line ~104)
    border:1px solid rgba(255,255,255,0.1);

```
**[ADDED]**
```
104       padding:50px;
```
**[REMOVED]**
```
(from line ~106)
    backdrop-filter:blur(15px);

```
**[ADDED]**
```
106       border-radius:30px;
```
**[REMOVED]**
```
(from line ~108)
    border-radius:25px;

```
**[ADDED]**
```
108       border:1px solid rgba(255,255,255,0.08);
```
**[REMOVED]**
```
(from line ~110)
    padding:45px;

    box-shadow:0 0 30px rgba(0,0,0,0.4);

```
**[ADDED]**
```
110       box-shadow:0 0 40px rgba(0,0,0,0.5);
```
**[REMOVED]**
```
(from line ~114)
    font-size:35px;

```
**[ADDED]**
```
114   
115       font-size:50px;
116   
117       line-height:1.2;
118   
```
**[ADDED]**
```
122   .login-card span{
123       color:#ff1493;
124   }
125   
```
**[REMOVED]**
```
(from line ~127)
    color:#a1a1aa;

```
**[ADDED]**
```
127   
128       color:#9ca3af;
129   
```
**[REMOVED]**
```
(from line ~133)
/* INPUT BOX */

```
**[ADDED]**
```
134   /* INPUT */
135   
```
**[REMOVED]**
```
(from line ~147)
    left:18px;

```
**[ADDED]**
```
148       left:18px;
```
**[REMOVED]**
```
(from line ~157)
    background:#0f172a;

```
**[ADDED]**
```
157       background:#11183d;
```
**[REMOVED]**
```
(from line ~159)
    border:2px solid transparent;

```
**[ADDED]**
```
159       border:none;
```
**[REMOVED]**
```
(from line ~163)
    padding:15px 15px 15px 50px;

```
**[ADDED]**
```
163       padding:16px 16px 16px 50px;
```
**[REMOVED]**
```
(from line ~165)
    border-radius:15px;

```
**[ADDED]**
```
165       border-radius:14px;
```
**[REMOVED]**
```
(from line ~169)
    font-size:16px;

```
**[ADDED]**
```
169       font-size:15px;
```
**[REMOVED]**
```
(from line ~176)
    border-color:#c026ff;

```
**[ADDED]**
```
176       box-shadow:0 0 12px rgba(192,38,255,0.5);
```
**[REMOVED]**
```
(from line ~178)
    box-shadow:0 0 15px rgba(192,38,255,0.5);

```
**[ADDED]**
```
178       border:1px solid #c026ff;
```
**[ADDED]**
```
181   
```
**[REMOVED]**
```
(from line ~188)
    border:none;


```
**[ADDED]**
```
190       border:none;
191   
```
**[REMOVED]**
```
(from line ~197)
        #ec4899

```
**[ADDED]**
```
197           #ff1493
```
**[REMOVED]**
```
(from line ~218)
/* Bottom Text */

```
**[ADDED]**
```
219   /* BOTTOM TEXT */
220   
```
**[REMOVED]**
```
(from line ~227)
    color:#a1a1aa;

```
**[ADDED]**
```
227       color:#9ca3af;
```
**[REMOVED]**
```
(from line ~239)
/* Responsive */

```
**[ADDED]**
```
240   /* ERROR */
241   
242   .error-message{
243   
244       background:#ff4d4d;
245   
246       padding:12px;
247   
248       border-radius:10px;
249   
250       margin-bottom:20px;
251   
252       text-align:center;
253   
254       color:white;
255   }
256   
257   
258   /* RESPONSIVE */
259   
```
**[REMOVED]**
```
(from line ~262)
    .login-container{

```
**[ADDED]**
```
262       .main-container{
```
**[REMOVED]**
```
(from line ~273)
        font-size:40px;

```
**[ADDED]**
```
273           font-size:45px;
```
**[ADDED]**
```
276       .left-section p{
277           font-size:18px;
278       }
279   
280       .login-card{
281           width:90%;
282       }
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\login.html
*Saved at: 5/13/2026, 10:27:39 AM*

**[REMOVED]**
```
(from line ~3)


```
**[ADDED]**
```
4     
```
**[REMOVED]**
```
(from line ~8)
    <title>Login - Fake News Detection</title>

```
**[ADDED]**
```
8         <title>Fake News Login</title>
```
**[REMOVED]**
```
(from line ~15)
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

```
**[ADDED]**
```
15        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
```
**[REMOVED]**
```
(from line ~19)
        href="{{ url_for('static', filename='login.css') }}">

```
**[ADDED]**
```
19        href="{{ url_for('static', filename='login.css') }}">
```
**[REMOVED]**
```
(from line ~22)


```
**[REMOVED]**
```
(from line ~24)
    <div class="login-container">

```
**[ADDED]**
```
24        <div class="main-container">
```
**[REMOVED]**
```
(from line ~26)
        <!-- Left Side -->

```
**[ADDED]**
```
26            <!-- LEFT SECTION -->
```
**[REMOVED]**
```
(from line ~34)
                Fake News
                <span>Detection</span>

```
**[ADDED]**
```
34                    Fake News <span>Detection</span>
```
**[REMOVED]**
```
(from line ~43)
        <!-- Right Side -->

```
**[ADDED]**
```
43    
44            <!-- RIGHT SECTION -->
```
**[REMOVED]**
```
(from line ~49)
                <h2>Welcome Back 👋</h2>

```
**[ADDED]**
```
49                    <h2>
50                        Login <span>Account</span>
51                    </h2>
```
**[ADDED]**
```
57                    {% if error %}
58                    <div class="error-message">
59                        {{ error }}
60                    </div>
61                    {% endif %}
62    
```
**[REMOVED]**
```
(from line ~65)
                    <!-- Email -->

```
**[ADDED]**
```
65                        <!-- EMAIL -->
```
**[REMOVED]**
```
(from line ~71)
                            type="email"
                            name="email"
                            placeholder="Enter your email"
                            required>

```
**[ADDED]**
```
71                            type="email"
72                            name="email"
73                            placeholder="Enter your email"
74                            required>
```
**[REMOVED]**
```
(from line ~78)
                    <!-- Password -->

```
**[ADDED]**
```
78    
79                        <!-- PASSWORD -->
```
**[REMOVED]**
```
(from line ~85)
                            type="password"
                            name="password"
                            placeholder="Enter password"
                            required>

```
**[ADDED]**
```
85                            type="password"
86                            name="password"
87                            placeholder="Enter password"
88                            required>
```
**[REMOVED]**
```
(from line ~92)
                    <!-- Button -->

```
**[ADDED]**
```
92    
93                        <!-- BUTTON -->
```
**[ADDED]**
```
104   
```
**[REMOVED]**
```
(from line ~120)


```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\register.html
*Saved at: 5/13/2026, 10:25:54 AM*

**[REMOVED]**
```
(from line ~1)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Fake News Detection</title>

```
**[ADDED]**
```
1     *{
```
**[REMOVED]**
```
(from line ~3)
    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

```
**[ADDED]**
```
3         transition:0.3s;
4     }
```
**[REMOVED]**
```
(from line ~6)
    <!-- Font Awesome -->
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

```
**[ADDED]**
```
6     .login-btn:hover{
```
**[REMOVED]**
```
(from line ~8)
    <style>

```
**[ADDED]**
```
8         transform:translateY(-2px);
```
**[REMOVED]**
```
(from line ~10)
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:'Poppins', sans-serif;
        }

```
**[ADDED]**
```
10        box-shadow:0 0 20px rgba(192,38,255,0.5);
11    }
```
**[REMOVED]**
```
(from line ~13)
        body{
            width:100%;
            height:100vh;
            background:#020B2D;
            overflow:hidden;
        }

```
**[REMOVED]**
```
(from line ~14)
        .container{
            display:flex;
            width:100%;
            height:100vh;
        }

```
**[ADDED]**
```
14    /* BOTTOM TEXT */
```
**[REMOVED]**
```
(from line ~16)
        /* LEFT SECTION */

```
**[ADDED]**
```
16    .bottom-text{
```
**[REMOVED]**
```
(from line ~18)
        .left-section{
            width:50%;
            height:100%;
            background:#020B2D;
            display:flex;
            justify-content:center;
            align-items:center;
            flex-direction:column;
            border-right:1px solid rgba(255,255,255,0.05);
        }

```
**[ADDED]**
```
18        margin-top:25px;
```
**[REMOVED]**
```
(from line ~20)
        .logo-box{
            width:100px;
            height:100px;
            background:linear-gradient(135deg,#7B2FF7,#F107A3);
            border-radius:25px;
            display:flex;
            justify-content:center;
            align-items:center;
            box-shadow:0 0 30px rgba(161, 66, 255, 0.6);
            margin-bottom:35px;
        }

```
**[ADDED]**
```
20        text-align:center;
```
**[REMOVED]**
```
(from line ~22)
        .logo-box i{
            font-size:45px;
            color:white;
        }

```
**[ADDED]**
```
22        color:#9ca3af;
23    }
```
**[REMOVED]**
```
(from line ~25)
        .main-title{
            font-size:64px;
            color:white;
            font-weight:700;
        }

```
**[ADDED]**
```
25    .bottom-text a{
```
**[REMOVED]**
```
(from line ~27)
        .main-title span{
            color:#B026FF;
        }

```
**[ADDED]**
```
27        color:#c026ff;
```
**[REMOVED]**
```
(from line ~29)
        .subtitle{
            margin-top:20px;
            color:#d7d7d7;
            font-size:20px;
            font-weight:300;
        }

```
**[ADDED]**
```
29        text-decoration:none;
```
**[REMOVED]**
```
(from line ~31)
        /* RIGHT SECTION */

```
**[ADDED]**
```
31        font-weight:600;
32    }
```
**[REMOVED]**
```
(from line ~34)
        .right-section{
            width:50%;
            height:100%;
            display:flex;
            justify-content:center;
            align-items:center;
            background:#00092A;
        }

```
**[REMOVED]**
```
(from line ~35)
        .register-card{
            width:430px;
            background:#0E1430;
            border-radius:25px;
            padding:45px;
            border:1px solid rgba(255,255,255,0.08);
            box-shadow:0 0 20px rgba(0,0,0,0.4);
        }

```
**[ADDED]**
```
35    /* ERROR */
```
**[REMOVED]**
```
(from line ~37)
        .register-card h1{
            color:white;
            font-size:42px;
            margin-bottom:10px;
        }

```
**[ADDED]**
```
37    .error-message{
```
**[REMOVED]**
```
(from line ~39)
        .register-card p{
            color:#b6b6b6;
            margin-bottom:35px;
        }

```
**[ADDED]**
```
39        background:#ff4d4d;
```
**[REMOVED]**
```
(from line ~41)
        .input-box{
            width:100%;
            height:55px;
            background:#0B1436;
            border-radius:15px;
            margin-bottom:22px;
            display:flex;
            align-items:center;
            padding:0 18px;
            border:2px solid transparent;
            transition:0.3s;
        }

```
**[ADDED]**
```
41        padding:12px;
```
**[REMOVED]**
```
(from line ~43)
        .input-box:focus-within{
            border:2px solid #B026FF;
            box-shadow:0 0 15px rgba(176,38,255,0.5);
        }

```
**[ADDED]**
```
43        border-radius:10px;
```
**[REMOVED]**
```
(from line ~45)
        .input-box i{
            color:#B026FF;
            margin-right:12px;
            font-size:15px;
        }

```
**[ADDED]**
```
45        margin-bottom:20px;
```
**[REMOVED]**
```
(from line ~47)
        .input-box input{
            width:100%;
            background:none;
            border:none;
            outline:none;
            color:white;
            font-size:15px;
        }

```
**[ADDED]**
```
47        text-align:center;
```
**[REMOVED]**
```
(from line ~49)
        .input-box input::placeholder{
            color:#8d8d8d;
        }

```
**[ADDED]**
```
49        color:white;
50    }
```
**[REMOVED]**
```
(from line ~52)
        .register-btn{
            width:100%;
            height:55px;
            border:none;
            border-radius:15px;
            background:linear-gradient(90deg,#7B2FF7,#F107A3);
            color:white;
            font-size:18px;
            font-weight:600;
            cursor:pointer;
            margin-top:10px;
            transition:0.3s;
        }

```
**[REMOVED]**
```
(from line ~53)
        .register-btn:hover{
            transform:translateY(-2px);
            box-shadow:0 0 20px rgba(176,38,255,0.5);
        }

```
**[ADDED]**
```
53    /* RESPONSIVE */
```
**[REMOVED]**
```
(from line ~55)
        .bottom-text{
            margin-top:25px;
            text-align:center;
            color:#bfbfbf;
            font-size:14px;
        }

```
**[ADDED]**
```
55    @media(max-width:992px){
```
**[REMOVED]**
```
(from line ~57)
        .bottom-text a{
            color:#B026FF;
            text-decoration:none;
            font-weight:600;
        }

```
**[ADDED]**
```
57        .main-container{
58            flex-direction:column;
59        }
```
**[REMOVED]**
```
(from line ~61)
        /* RESPONSIVE */

```
**[ADDED]**
```
61        .left-section,
62        .right-section{
63            width:100%;
64            height:50vh;
65        }
```
**[REMOVED]**
```
(from line ~67)
        @media(max-width:1000px){

```
**[ADDED]**
```
67        .left-section h1{
68            font-size:45px;
69        }
```
**[REMOVED]**
```
(from line ~71)
            .left-section{
                display:none;
            }

```
**[ADDED]**
```
71        .left-section p{
72            font-size:18px;
73        }
```
**[REMOVED]**
```
(from line ~75)
            .right-section{
                width:100%;
            }
        }

    </style>

</head>
<body>

    <div class="container">

        <!-- LEFT -->

        <div class="left-section">

            <div class="logo-box">
                <i class="fa-solid fa-shield-halved"></i>
            </div>

            <h1 class="main-title">
                Fake News <span>Detection</span>
            </h1>

            <p class="subtitle">
                AI-Powered News Verification System with Explainability
            </p>

        </div>

        <!-- RIGHT -->

        <div class="right-section">

            <div class="register-card">

                <h1>Create Account 🚀</h1>

                <p>Register to continue</p>

                <form action="/register" method="POST">

                    <div class="input-box">
                        <i class="fa-solid fa-user"></i>
                        <input type="text"
                               name="username"
                               placeholder="Enter username"
                               required>
                    </div>

                    <div class="input-box">
                        <i class="fa-solid fa-envelope"></i>
                        <input type="email"
                               name="email"
                               placeholder="Enter your email"
                               required>
                    </div>

                    <div class="input-box">
                        <i class="fa-solid fa-lock"></i>
                        <input type="password"
                               name="password"
                               placeholder="Enter password"
                               required>
                    </div>

                    <div class="input-box">
                        <i class="fa-solid fa-lock"></i>
                        <input type="password"
                               name="confirm_password"
                               placeholder="Confirm password"
                               required>
                    </div>

                    <button class="register-btn">
                        <i class="fa-solid fa-user-plus"></i>
                        Register
                    </button>

                </form>

                <div class="bottom-text">
                    Already have an account?
                    <a href="/login">Login</a>
                </div>

            </div>

        </div>

    </div>

</body>
</html>
```
**[ADDED]**
```
75        .login-card{
76            width:90%;
77        }
78    }
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\Static\login.css
*Saved at: 5/13/2026, 10:19:17 AM*

**[REMOVED]**
```
(from line ~121)
/* ERROR MESSAGE */

.error-message{

    background:#ff4d4d;

    color:white;

    padding:12px;

    border-radius:10px;

    margin-bottom:20px;

    text-align:center;

    font-weight:500;

    animation:fadeIn 0.4s ease;
}


```
**[REMOVED]**
```
(from line ~224)
/* Animation */

@keyframes fadeIn{

    from{
        opacity:0;
        transform:translateY(-10px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}


```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\login.html
*Saved at: 5/13/2026, 10:18:33 AM*

**[REMOVED]**
```
(from line ~56)
                <!-- ERROR MESSAGE -->
                {% if error %}
                    <div class="error-message">
                        {{ error }}
                    </div>
                {% endif %}


```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\index.html
*Saved at: 5/13/2026, 10:10:17 AM*

**[REMOVED]**
```
(from line ~2)
<html lang="en">

```
**[ADDED]**
```
2     <html>
3     
```
**[REMOVED]**
```
(from line ~5)
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fake News Detection System</title>

```
**[REMOVED]**
```
(from line ~6)
    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

```
**[ADDED]**
```
6         <title>Fake News Detection</title>
```
**[REMOVED]**
```
(from line ~8)
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

```
**[ADDED]**
```
9     
```
**[REMOVED]**
```
(from line ~12)
<div class="main-container">

```
**[ADDED]**
```
12        <h1>Fake News Detection System</h1>
```
**[REMOVED]**
```
(from line ~14)
    <!-- Header -->
    <div class="header-section">
        <h1>
            <i class="fa-solid fa-newspaper"></i>
            Fake News <span>Detection System</span>
        </h1>

```
**[ADDED]**
```
14        <form action="/predict" method="POST">
```
**[REMOVED]**
```
(from line ~16)
        <p>
            AI-Powered News Verification with Explainability
        </p>
    </div>

```
**[ADDED]**
```
16            <textarea
17                name="news"
18                rows="12"
19                cols="100"
20                placeholder="Enter news article here..."
21                required>
22            </textarea>
```
**[REMOVED]**
```
(from line ~24)
    <!-- Main Grid -->
    <div class="content-grid">

```
**[ADDED]**
```
24            <br><br>
```
**[REMOVED]**
```
(from line ~26)
        <!-- Left Section -->
        <div class="left-panel glass-card">

```
**[ADDED]**
```
26            <button type="submit">
27                Analyze
28            </button>
```
**[REMOVED]**
```
(from line ~30)
            <h3>
                <i class="fa-solid fa-pen"></i>
                Enter News Article
            </h3>

```
**[ADDED]**
```
30        </form>
```
**[REMOVED]**
```
(from line ~32)
            <form action="/predict" method="POST">

                <textarea
                    name="news"
                    rows="10"
                    placeholder="Paste news article here..."
                    required></textarea>

                <div class="button-group">

                    <button type="submit" class="analyze-btn">
                        <i class="fa-solid fa-magnifying-glass"></i>
                        Analyze News
                    </button>

                    <button type="reset" class="clear-btn">
                        <i class="fa-solid fa-trash"></i>
                        Clear
                    </button>

                </div>

            </form>

        </div>

        <!-- Right Section -->
        <div class="right-panel glass-card">

            <div class="news-icon">
                <i class="fa-solid fa-magnifying-glass-chart"></i>
            </div>

            <h2>AI News Analyzer</h2>

            <p>
                Detect fake news with advanced NLP algorithms and explainable AI.
            </p>

        </div>

    </div>

    <!-- Result Section -->

```
**[REMOVED]**
```
(from line ~34)
    <div class="result-grid">

```
**[ADDED]**
```
34            <hr>
```
**[REMOVED]**
```
(from line ~36)
        <!-- Prediction Card -->
        <div class="glass-card result-card">

```
**[ADDED]**
```
36            <h2>Prediction: {{ prediction }}</h2>
```
**[REMOVED]**
```
(from line ~38)
            <h3>
                <i class="fa-solid fa-chart-column"></i>
                Prediction Result
            </h3>

```
**[ADDED]**
```
38            <h3>Confidence: {{ confidence }}%</h3>
```
**[REMOVED]**
```
(from line ~40)
            <div class="prediction-box">

```
**[ADDED]**
```
40            <h3>Explanation:</h3>
```
**[REMOVED]**
```
(from line ~42)
                {% if prediction == 'FAKE' %}
                    <div class="fake-result">
                        <i class="fa-solid fa-circle-xmark"></i>
                        <div>
                            <h2>FAKE NEWS</h2>
                            <p>This news is likely to be fake</p>
                        </div>
                    </div>
                {% else %}
                    <div class="real-result">
                        <i class="fa-solid fa-circle-check"></i>
                        <div>
                            <h2>REAL NEWS</h2>
                            <p>This news appears authentic</p>
                        </div>
                    </div>
                {% endif %}

```
**[ADDED]**
```
42            <p>{{ explanation }}</p>
```
**[REMOVED]**
```
(from line ~44)
                <div class="confidence-box">
                    <h4>Confidence Score</h4>
                    <h1>{{ confidence }}</h1>
                </div>

```
**[ADDED]**
```
44            <h3>Influential Words:</h3>
```
**[REMOVED]**
```
(from line ~46)
            </div>

```
**[ADDED]**
```
46            <ul>
```
**[REMOVED]**
```
(from line ~48)
        </div>

```
**[ADDED]**
```
48                {% for word in influential_words %}
```
**[REMOVED]**
```
(from line ~50)
        <!-- Explainability -->
        <div class="glass-card explain-card">

```
**[ADDED]**
```
50                    <li>{{ word }}</li>
```
**[REMOVED]**
```
(from line ~52)
            <h3>
                <i class="fa-solid fa-brain"></i>
                Why this prediction?
            </h3>

```
**[ADDED]**
```
52                {% endfor %}
```
**[REMOVED]**
```
(from line ~54)
            <div class="keywords-section">

```
**[ADDED]**
```
54            </ul>
```
**[REMOVED]**
```
(from line ~56)
                {% for word in suspicious_words %}
                    <span class="keyword-badge">
                        {{ word }}
                    </span>
                {% endfor %}

```
**[ADDED]**
```
56            <h3>Visualization:</h3>
```
**[REMOVED]**
```
(from line ~58)
            </div>

```
**[ADDED]**
```
58            <img
59                src="{{ url_for('static', filename='chart.png') }}"
60                width="500"
61            >
```
**[REMOVED]**
```
(from line ~63)
            <div class="explanation-text">
                The model identified suspicious words commonly associated with misleading or sensational fake news articles.
            </div>

        </div>

    </div>


```
**[REMOVED]**
```
(from line ~65)
</div>


```
**[REMOVED]**
```
(from line ~66)
</html>

```
**[ADDED]**
```
66    
67    </html>
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\APP1.PY
*Saved at: 5/13/2026, 10:09:25 AM*

**[ADDED]**
```
2     import joblib
3     import re
4     import nltk
5     import numpy as np
6     import matplotlib.pyplot as plt
```
**[ADDED]**
```
8     from nltk.corpus import stopwords
9     
10    # Flask app
```
**[ADDED]**
```
13    # Load saved model
14    model = joblib.load('fake_news_model.pkl')
15    
16    # Load vectorizer
17    tfidf = joblib.load('tfidf_vectorizer.pkl')
18    
19    # Download stopwords
20    nltk.download('stopwords')
21    
22    stop_words = set(stopwords.words('english'))
23    
24    # Clean text
25    def clean_text(text):
26    
27        text = re.sub(r'\W', ' ', str(text))
28    
29        text = text.lower()
30    
31        return ' '.join([
32            word for word in text.split()
33            if word not in stop_words
34        ])
35    
36    # Home page
```
**[REMOVED]**
```
(from line ~39)
    return render_template('index.html')

```
**[ADDED]**
```
40        return render_template('dashboard.html')
41    
42    # Prediction route
```
**[ADDED]**
```
46        # User input
```
**[REMOVED]**
```
(from line ~49)
    fake_words = [
        'breaking',
        'viral',
        'shocking',
        'secret',
        'exclusive',
        'scandal'

```
**[ADDED]**
```
49        # Clean text
50        cleaned = clean_text(news)
51    
52        # TF-IDF transform
53        vectorized = tfidf.transform([cleaned])
54    
55        # Prediction
56        prediction = model.predict(vectorized)[0]
57    
58        # Probabilities
59        probabilities = model.predict_proba(vectorized)[0]
60    
61        fake_prob = round(probabilities[0] * 100, 2)
62    
63        real_prob = round(probabilities[1] * 100, 2)
64    
65        # Prediction label
66        label = "REAL" if prediction == 1 else "FAKE"
67    
68        # Confidence
69        confidence = max(fake_prob, real_prob)
70    
71        # Important words
72        feature_names = tfidf.get_feature_names_out()
73    
74        vector = vectorized.toarray()[0]
75    
76        top_indices = vector.argsort()[-5:]
77    
78        influential_words = [
79    
80            feature_names[i]
81    
82            for i in top_indices
83    
84            if vector[i] > 0
```
**[REMOVED]**
```
(from line ~87)
    suspicious_words = []

```
**[ADDED]**
```
87        # Explanation
88        explanation = (
```
**[REMOVED]**
```
(from line ~90)
    for word in fake_words:
        if word in news.lower():
            suspicious_words.append(word)

```
**[ADDED]**
```
90            f"This news is classified as {label} "
```
**[REMOVED]**
```
(from line ~92)
    if len(suspicious_words) >= 2:
        prediction = 'FAKE'
        confidence = '92%'
    else:
        prediction = 'REAL'
        confidence = '87%'

```
**[ADDED]**
```
92            f"with {confidence}% confidence because "
```
**[ADDED]**
```
94            f"words like "
95    
96            f"{', '.join(influential_words)} "
97    
98            f"strongly influenced the AI model."
99    
100       )
101   
102       # GRAPH VISUALIZATION
103       labels = ['FAKE', 'REAL']
104   
105       values = [fake_prob, real_prob]
106   
107       plt.figure(figsize=(5,4))
108   
109       bars = plt.bar(labels, values)
110   
111       plt.ylabel("Confidence %")
112   
113       plt.title("Prediction Analysis")
114   
115       plt.ylim(0,100)
116   
117       # Save chart
118       plt.savefig('static/chart.png')
119   
120       plt.close()
121   
122       # Return result
```
**[REMOVED]**
```
(from line ~124)
        'index.html',
        prediction=prediction,

```
**[ADDED]**
```
124   
125           'dashboard.html',
126   
127           prediction=label,
128   
```
**[REMOVED]**
```
(from line ~130)
        suspicious_words=suspicious_words

```
**[ADDED]**
```
130   
131           explanation=explanation,
132   
133           fake_prob=fake_prob,
134   
135           real_prob=real_prob,
136   
137           influential_words=influential_words
```
**[ADDED]**
```
140   # Run app
```
**[ADDED]**
```
142   
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:05:00 AM*

**[REMOVED]**
```
(from line ~22)
df = pd.read_csv(fake_or_real_news.csv")

```
**[ADDED]**
```
22    df = pd.read_csv("fake_or_real_news.csv")
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:04:56 AM*

**[REMOVED]**
```
(from line ~22)
df = pd.read_csv(fake_or_real_news.csv)

```
**[ADDED]**
```
22    df = pd.read_csv(fake_or_real_news.csv")
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:04:55 AM*

**[REMOVED]**
```
(from line ~22)
df = pd.read_csv(fake_or_real_news)

```
**[ADDED]**
```
22    df = pd.read_csv(fake_or_real_news.csv)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 10:04:53 AM*

**[REMOVED]**
```
(from line ~22)
df = pd.read_csv()

```
**[ADDED]**
```
22    df = pd.read_csv(fake_or_real_news)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:39:44 AM*

**[REMOVED]**
```
(from line ~22)
df = pd.read_csv("articles.csv")  

```
**[ADDED]**
```
22    df = pd.read_csv("articles.csv", encoding='latin1')
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:38:18 AM*

**[REMOVED]**
```
(from line ~22)
df = pd.read_csv("artiv.csv")  

```
**[ADDED]**
```
22    df = pd.read_csv("articles.csv")  
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:38:16 AM*

**[REMOVED]**
```
(from line ~22)
df = pd.read_csv("C:/Users/Mohamed Tawfeeq/Downloads/fake_or_real_news.csv/fake_or_real_news.csv")  

```
**[ADDED]**
```
22    df = pd.read_csv("artiv.csv")  
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:54 AM*

**[REMOVED]**
```
(from line ~47)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))

```
**[ADDED]**
```
47    print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:43 AM*

**[REMOVED]**
```
(from line ~88)
print("Prediction:", label)

```
**[ADDED]**
```
88    print(" Prediction:", label)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:41 AM*

**[REMOVED]**
```
(from line ~89)
print("Explanation:", explanation)
```
**[ADDED]**
```
89    print(" Explanation:", explanation)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:39 AM*

**[REMOVED]**
```
(from line ~89)
print("📝 Explanation:", explanation)
```
**[ADDED]**
```
89    print("Explanation:", explanation)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:37 AM*

**[REMOVED]**
```
(from line ~88)
print( "Prediction:", label)

```
**[ADDED]**
```
88    print("Prediction:", label)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:34 AM*

**[REMOVED]**
```
(from line ~88)
print( Prediction:", label)

```
**[ADDED]**
```
88    print( "Prediction:", label)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:30 AM*

**[REMOVED]**
```
(from line ~88)
print("" Prediction:", label)

```
**[ADDED]**
```
88    print( Prediction:", label)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:28 AM*

**[REMOVED]**
```
(from line ~88)
print( Prediction:", label)

```
**[ADDED]**
```
88    print("" Prediction:", label)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:25 AM*

**[REMOVED]**
```
(from line ~88)
print("🔮 Prediction:", label)

```
**[ADDED]**
```
88    print( Prediction:", label)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\model_training.py
*Saved at: 5/13/2026, 9:32:21 AM*

**[ADDED]**
```
1     # Fake News Detection with Automatic Sentence Explanations
2     
3     import pandas as pd
4     import numpy as np
5     import re
6     import nltk
7     import shap
8     import joblib
9     import matplotlib.pyplot as plt
10    from sklearn.model_selection import train_test_split
11    from sklearn.feature_extraction.text import TfidfVectorizer
12    from sklearn.linear_model import LogisticRegression
13    from sklearn.metrics import classification_report, accuracy_score
14    
15    # Download stopwords if not already
16    nltk.download('stopwords')
17    from nltk.corpus import stopwords
18    
19    stop_words = set(stopwords.words('english'))
20    
21    # 1. Load Dataset
22    df = pd.read_csv("C:/Users/Mohamed Tawfeeq/Downloads/fake_or_real_news.csv/fake_or_real_news.csv")  
23    X = df['text']
24    y = df['label'].map({'FAKE':0, 'REAL':1})
25    
26    # 2. Preprocessing
27    def clean_text(text):
28        text = re.sub(r'\W', ' ', str(text))
29        text = text.lower()
30        return ' '.join([word for word in text.split() if word not in stop_words])
31    
32    X = X.apply(clean_text)
33    
34    # 3. Feature Extraction
35    tfidf = TfidfVectorizer(max_features=5000)
36    X_tfidf = tfidf.fit_transform(X)
37    
38    # 4. Train/Test Split
39    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)
40    
41    # 5. Model Training
42    model = LogisticRegression(max_iter=1000, n_jobs=-1)
43    model.fit(X_train, y_train)
44    
45    # 6. Evaluation
46    y_pred = model.predict(X_test)
47    print("✅ Accuracy:", accuracy_score(y_test, y_pred))
48    print("\nClassification Report:\n", classification_report(y_test, y_pred))
49    
50    # 7. Save Model + Vectorizer
51    joblib.dump(model, "fake_news_model.pkl")
52    joblib.dump(tfidf, "tfidf_vectorizer.pkl")
53    
54    # 8. SHAP Explainer
55    masker = shap.maskers.Independent(X_train)
56    explainer = shap.Explainer(model, masker)
57    
58    # Function: Predict + Auto Explanation
59    def predict_with_explanation(text):
60        cleaned = clean_text(text)
61        vectorized = tfidf.transform([cleaned])
62        
63        prediction = model.predict(vectorized)[0]
64        label = "REAL" if prediction == 1 else "FAKE"
65        
66        # Confidence score
67        prob = model.predict_proba(vectorized)[0][prediction]
68        
69        # SHAP local explanation
70        shap_values = explainer(vectorized)
71        top_words_idx = np.argsort(np.abs(shap_values.values[0]))[-5:]
72        influential = [tfidf.get_feature_names_out()[i] for i in top_words_idx]
73        
74        # Auto-generated sentence
75        explanation = (
76            f"This article was classified as {label} with {prob:.2%} confidence "
77            f"because words such as {', '.join(influential)} strongly influenced the model toward {label}."
78        )
79        
80        return label, explanation
81    
82    # Example usage: pick any article from dataset
83    index = 0
84    news_text = df['text'].iloc[index]
85    label, explanation = predict_with_explanation(news_text)
86    
87    print("\n📰 News Text:", news_text[:500], "...")
88    print("🔮 Prediction:", label)
89    print("📝 Explanation:", explanation)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\register.html
*Saved at: 5/13/2026, 6:59:21 AM*

**[ADDED]**
```
1     <!DOCTYPE html>
2     <html lang="en">
3     <head>
4         <meta charset="UTF-8">
5         <meta name="viewport" content="width=device-width, initial-scale=1.0">
6         <title>Register - Fake News Detection</title>
7     
8         <!-- Google Font -->
9         <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
10    
11        <!-- Font Awesome -->
12        <link rel="stylesheet"
13              href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
14    
15        <style>
16    
17            *{
18                margin:0;
19                padding:0;
20                box-sizing:border-box;
21                font-family:'Poppins', sans-serif;
22            }
23    
24            body{
25                width:100%;
26                height:100vh;
27                background:#020B2D;
28                overflow:hidden;
29            }
30    
31            .container{
32                display:flex;
33                width:100%;
34                height:100vh;
35            }
36    
37            /* LEFT SECTION */
38    
39            .left-section{
40                width:50%;
41                height:100%;
42                background:#020B2D;
43                display:flex;
44                justify-content:center;
45                align-items:center;
46                flex-direction:column;
47                border-right:1px solid rgba(255,255,255,0.05);
48            }
49    
50            .logo-box{
51                width:100px;
52                height:100px;
53                background:linear-gradient(135deg,#7B2FF7,#F107A3);
54                border-radius:25px;
55                display:flex;
56                justify-content:center;
57                align-items:center;
58                box-shadow:0 0 30px rgba(161, 66, 255, 0.6);
59                margin-bottom:35px;
60            }
61    
62            .logo-box i{
63                font-size:45px;
64                color:white;
65            }
66    
67            .main-title{
68                font-size:64px;
69                color:white;
70                font-weight:700;
71            }
72    
73            .main-title span{
74                color:#B026FF;
75            }
76    
77            .subtitle{
78                margin-top:20px;
79                color:#d7d7d7;
80                font-size:20px;
81                font-weight:300;
82            }
83    
84            /* RIGHT SECTION */
85    
86            .right-section{
87                width:50%;
88                height:100%;
89                display:flex;
90                justify-content:center;
91                align-items:center;
92                background:#00092A;
93            }
94    
95            .register-card{
96                width:430px;
97                background:#0E1430;
98                border-radius:25px;
99                padding:45px;
100               border:1px solid rgba(255,255,255,0.08);
101               box-shadow:0 0 20px rgba(0,0,0,0.4);
102           }
103   
104           .register-card h1{
105               color:white;
106               font-size:42px;
107               margin-bottom:10px;
108           }
109   
110           .register-card p{
111               color:#b6b6b6;
112               margin-bottom:35px;
113           }
114   
115           .input-box{
116               width:100%;
117               height:55px;
118               background:#0B1436;
119               border-radius:15px;
120               margin-bottom:22px;
121               display:flex;
122               align-items:center;
123               padding:0 18px;
124               border:2px solid transparent;
125               transition:0.3s;
126           }
127   
128           .input-box:focus-within{
129               border:2px solid #B026FF;
130               box-shadow:0 0 15px rgba(176,38,255,0.5);
131           }
132   
133           .input-box i{
134               color:#B026FF;
135               margin-right:12px;
136               font-size:15px;
137           }
138   
139           .input-box input{
140               width:100%;
141               background:none;
142               border:none;
143               outline:none;
144               color:white;
145               font-size:15px;
146           }
147   
148           .input-box input::placeholder{
149               color:#8d8d8d;
150           }
151   
152           .register-btn{
153               width:100%;
154               height:55px;
155               border:none;
156               border-radius:15px;
157               background:linear-gradient(90deg,#7B2FF7,#F107A3);
158               color:white;
159               font-size:18px;
160               font-weight:600;
161               cursor:pointer;
162               margin-top:10px;
163               transition:0.3s;
164           }
165   
166           .register-btn:hover{
167               transform:translateY(-2px);
168               box-shadow:0 0 20px rgba(176,38,255,0.5);
169           }
170   
171           .bottom-text{
172               margin-top:25px;
173               text-align:center;
174               color:#bfbfbf;
175               font-size:14px;
176           }
177   
178           .bottom-text a{
179               color:#B026FF;
180               text-decoration:none;
181               font-weight:600;
182           }
183   
184           /* RESPONSIVE */
185   
186           @media(max-width:1000px){
187   
188               .left-section{
189                   display:none;
190               }
191   
192               .right-section{
193                   width:100%;
194               }
195           }
196   
197       </style>
198   
199   </head>
200   <body>
201   
202       <div class="container">
203   
204           <!-- LEFT -->
205   
206           <div class="left-section">
207   
208               <div class="logo-box">
209                   <i class="fa-solid fa-shield-halved"></i>
210               </div>
211   
212               <h1 class="main-title">
213                   Fake News <span>Detection</span>
214               </h1>
215   
216               <p class="subtitle">
217                   AI-Powered News Verification System with Explainability
218               </p>
219   
220           </div>
221   
222           <!-- RIGHT -->
223   
224           <div class="right-section">
225   
226               <div class="register-card">
227   
228                   <h1>Create Account 🚀</h1>
229   
230                   <p>Register to continue</p>
231   
232                   <form action="/register" method="POST">
233   
234                       <div class="input-box">
235                           <i class="fa-solid fa-user"></i>
236                           <input type="text"
237                                  name="username"
238                                  placeholder="Enter username"
239                                  required>
240                       </div>
241   
242                       <div class="input-box">
243                           <i class="fa-solid fa-envelope"></i>
244                           <input type="email"
245                                  name="email"
246                                  placeholder="Enter your email"
247                                  required>
248                       </div>
249   
250                       <div class="input-box">
251                           <i class="fa-solid fa-lock"></i>
252                           <input type="password"
253                                  name="password"
254                                  placeholder="Enter password"
255                                  required>
256                       </div>
257   
258                       <div class="input-box">
259                           <i class="fa-solid fa-lock"></i>
260                           <input type="password"
261                                  name="confirm_password"
262                                  placeholder="Confirm password"
263                                  required>
264                       </div>
265   
266                       <button class="register-btn">
267                           <i class="fa-solid fa-user-plus"></i>
268                           Register
269                       </button>
270   
271                   </form>
272   
273                   <div class="bottom-text">
274                       Already have an account?
275                       <a href="/login">Login</a>
276                   </div>
277   
278               </div>
279   
280           </div>
281   
282       </div>
283   
284   </body>
285   </html>
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\register.html
*Saved at: 5/13/2026, 6:53:01 AM*

**[REMOVED]**
```
(from line ~1)
 
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\register.html
*Saved at: 5/13/2026, 6:52:57 AM*

**[ADDED]**
```
1      
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\APP1.PY
*Saved at: 5/12/2026, 1:57:42 PM*

**[ADDED]**
```
1     from flask import Flask, render_template, request
2     
3     app = Flask(__name__)
4     
5     @app.route('/')
6     def home():
7         return render_template('index.html')
8     
9     @app.route('/predict', methods=['POST'])
10    def predict():
11    
12        news = request.form['news']
13    
14        fake_words = [
15            'breaking',
16            'viral',
17            'shocking',
18            'secret',
19            'exclusive',
20            'scandal'
21        ]
22    
23        suspicious_words = []
24    
25        for word in fake_words:
26            if word in news.lower():
27                suspicious_words.append(word)
28    
29        if len(suspicious_words) >= 2:
30            prediction = 'FAKE'
31            confidence = '92%'
32        else:
33            prediction = 'REAL'
34            confidence = '87%'
35    
36        return render_template(
37            'index.html',
38            prediction=prediction,
39            confidence=confidence,
40            suspicious_words=suspicious_words
41        )
42    
43    if __name__ == '__main__':
44        app.run(debug=True)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:35:02 PM*

**[REMOVED]**
```
(from line ~33)
        email_pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$''

```
**[ADDED]**
```
33            email_pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:34:59 PM*

**[REMOVED]**
```
(from line ~33)
        email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$''

```
**[ADDED]**
```
33            email_pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$''
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:34:55 PM*

**[REMOVED]**
```
(from line ~33)
        email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$""

```
**[ADDED]**
```
33            email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$''
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:34:53 PM*

**[REMOVED]**
```
(from line ~33)
        email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

```
**[ADDED]**
```
33            email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$""
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:34:51 PM*

**[REMOVED]**
```
(from line ~33)
        email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$''

```
**[ADDED]**
```
33            email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:34:49 PM*

**[REMOVED]**
```
(from line ~33)
        email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

```
**[ADDED]**
```
33            email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$''
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:34:42 PM*

**[REMOVED]**
```
(from line ~33)
        email_pattern = r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$'

```
**[ADDED]**
```
33            email_pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\Static\login.css
*Saved at: 5/12/2026, 12:30:04 PM*

**[ADDED]**
```
121   /* ERROR MESSAGE */
122   
123   .error-message{
124   
125       background:#ff4d4d;
126   
127       color:white;
128   
129       padding:12px;
130   
131       border-radius:10px;
132   
133       margin-bottom:20px;
134   
135       text-align:center;
136   
137       font-weight:500;
138   
139       animation:fadeIn 0.4s ease;
140   }
141   
```
**[ADDED]**
```
245   /* Animation */
246   
247   @keyframes fadeIn{
248   
249       from{
250           opacity:0;
251           transform:translateY(-10px);
252       }
253   
254       to{
255           opacity:1;
256           transform:translateY(0);
257       }
258   }
259   
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\login.html
*Saved at: 5/12/2026, 12:28:53 PM*

**[ADDED]**
```
56                    <!-- ERROR MESSAGE -->
57                    {% if error %}
58                        <div class="error-message">
59                            {{ error }}
60                        </div>
61                    {% endif %}
62    
```
**[REMOVED]**
```
(from line ~115)
    {% if error %}
    <div class="error-message">
        {{ error }}
    </div>
{% endif %}

```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\login.html
*Saved at: 5/12/2026, 12:27:56 PM*

**[ADDED]**
```
108       {% if error %}
109       <div class="error-message">
110           {{ error }}
111       </div>
112   {% endif %}
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:26:09 PM*

**[ADDED]**
```
1     from flask import Flask, render_template, request
2     from werkzeug.security import generate_password_hash, check_password_hash
3     import re
4     
5     app = Flask(__name__)
6     
7     # Secure Credentials
8     stored_email = "admin@fakenewsai.com"
9     
10    stored_password_hash = generate_password_hash(
11        "FakeNews@2026Secure"
12    )
13    
14    
15    # HOME PAGE
16    @app.route('/')
17    def home():
18        return render_template('login.html')
19    
20    
21    # LOGIN PAGE
```
**[REMOVED]**
```
(from line ~72)
    )
```
**[ADDED]**
```
72        )
73    
74    
75    # PREDICTION PAGE
76    @app.route('/predict', methods=['POST'])
77    def predict():
78    
79        news = request.form['news']
80    
81        fake_words = [
82            'breaking',
83            'viral',
84            'shocking',
85            'secret',
86            'exclusive',
87            'scandal'
88        ]
89    
90        suspicious_words = []
91    
92        for word in fake_words:
93            if word in news.lower():
94                suspicious_words.append(word)
95    
96        if len(suspicious_words) >= 2:
97            prediction = 'FAKE'
98            confidence = '92%'
99        else:
100           prediction = 'REAL'
101           confidence = '87%'
102   
103       return render_template(
104           'index.html',
105           prediction=prediction,
106           confidence=confidence,
107           suspicious_words=suspicious_words
108       )
109   
110   
111   if __name__ == '__main__':
112       app.run(debug=True)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:25:04 PM*

**[REMOVED]**
```
(from line ~1)
from flask import Flask, render_template, request

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('login.html')


# LOGIN PAGE

```
**[ADDED]**
```
4         error = None
5     
```
**[REMOVED]**
```
(from line ~11)
        # Dummy Login Check
        if email and password:

```
**[ADDED]**
```
11            # Email Validation
12            email_pattern = r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$'
```
**[REMOVED]**
```
(from line ~14)
            # Open Main Fake News Detection Page
            return render_template('index.html')

```
**[ADDED]**
```
14            if not re.match(email_pattern, email):
```
**[REMOVED]**
```
(from line ~16)
    return render_template('login.html')

```
**[ADDED]**
```
16                error = "Invalid Email Format"
```
**[ADDED]**
```
18                return render_template(
19                    'login.html',
20                    error=error
21                )
```
**[REMOVED]**
```
(from line ~23)
# PREDICTION PAGE
@app.route('/predict', methods=['POST'])
def predict():

```
**[ADDED]**
```
23            # Password Validation
24            if len(password) < 8:
```
**[REMOVED]**
```
(from line ~26)
    news = request.form['news']

```
**[ADDED]**
```
26                error = (
27                    "Password must contain "
28                    "at least 8 characters"
29                )
```
**[REMOVED]**
```
(from line ~31)
    fake_words = [
        'breaking',
        'viral',
        'shocking',
        'secret',
        'exclusive',
        'scandal'
    ]

```
**[ADDED]**
```
31                return render_template(
32                    'login.html',
33                    error=error
34                )
```
**[REMOVED]**
```
(from line ~36)
    suspicious_words = []

```
**[ADDED]**
```
36            # Secure Login Check
37            if email == stored_email and check_password_hash(
38                stored_password_hash,
39                password
40            ):
```
**[REMOVED]**
```
(from line ~42)
    for word in fake_words:
        if word in news.lower():
            suspicious_words.append(word)

```
**[ADDED]**
```
42                return render_template('index.html')
```
**[REMOVED]**
```
(from line ~44)
    if len(suspicious_words) >= 2:
        prediction = 'FAKE'
        confidence = '92%'
    else:
        prediction = 'REAL'
        confidence = '87%'

```
**[ADDED]**
```
44            else:
```
**[REMOVED]**
```
(from line ~46)
    return render_template(
        'index.html',
        prediction=prediction,
        confidence=confidence,
        suspicious_words=suspicious_words
    )

```
**[ADDED]**
```
46                error = "Incorrect Email or Password"
```
**[REMOVED]**
```
(from line ~48)

if __name__ == '__main__':
    app.run(debug=True)
```
**[ADDED]**
```
48        return render_template(
49            'login.html',
50            error=error
51        )
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:13:18 PM*

**[REMOVED]**
```
(from line ~8)
    return render_template('index.html')

```
**[ADDED]**
```
8         return render_template('login.html')
```
**[REMOVED]**
```
(from line ~12)
@app.route('/login')

```
**[ADDED]**
```
12    @app.route('/login', methods=['GET', 'POST'])
```
**[ADDED]**
```
14    
15        if request.method == 'POST':
16    
17            email = request.form['email']
18            password = request.form['password']
19    
20            # Dummy Login Check
21            if email and password:
22    
23                # Open Main Fake News Detection Page
24                return render_template('index.html')
25    
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:09:58 PM*

**[ADDED]**
```
5     # HOME PAGE
```
**[ADDED]**
```
10    
11    # LOGIN PAGE
12    @app.route('/login')
13    def login():
14        return render_template('login.html')
15    
16    
17    # PREDICTION PAGE
```
**[ADDED]**
```
52    
```
**[REMOVED]**
```
(from line ~54)
    app.run(debug=True)
    
```
**[ADDED]**
```
54        app.run(debug=True)
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:07:46 PM*

**[REMOVED]**
```
(from line ~1)


```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\app.py
*Saved at: 5/12/2026, 12:07:44 PM*

**[REMOVED]**
```
(from line ~1)
# from flask import Flask, render_template, request

```
**[REMOVED]**
```
(from line ~2)
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():

#     news = request.form['news']

#     fake_words = ["breaking", "viral", "shocking", "secret"]

#     suspicious = []

#     for word in fake_words:
#         if word in news.lower():
#             suspicious.append(word)

#     if len(suspicious) >= 2:
#         prediction = "FAKE"
#         confidence = "92%"
#     else:
#         prediction = "REAL"
#         confidence = "85%"

#     return render_template(
#         'index.html',
#         prediction=prediction,
#         confidence=confidence,
#         suspicious_words=suspicious
#     )

# if __name__ == '__main__':
#     app.run(debug=True)


```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\Static\login.css
*Saved at: 5/12/2026, 12:07:33 PM*

**[ADDED]**
```
1     *{
2         margin:0;
3         padding:0;
4         box-sizing:border-box;
5     }
6     
7     body{
8         font-family:'Poppins',sans-serif;
9         background:#020617;
10        color:white;
11        height:100vh;
12        overflow:hidden;
13    }
14    
15    /* Main Container */
16    
17    .login-container{
18        display:flex;
19        height:100vh;
20    }
21    
22    /* LEFT SECTION */
23    
24    .left-section{
25        width:50%;
26        background:linear-gradient(
27            135deg,
28            #050816,
29            #0b1120
30        );
31    
32        display:flex;
33        flex-direction:column;
34        justify-content:center;
35        align-items:center;
36    
37        padding:50px;
38    }
39    
40    .logo-box{
41        width:120px;
42        height:120px;
43    
44        background:linear-gradient(
45            135deg,
46            #7c3aed,
47            #ec4899
48        );
49    
50        border-radius:30px;
51    
52        display:flex;
53        justify-content:center;
54        align-items:center;
55    
56        font-size:50px;
57    
58        margin-bottom:30px;
59    
60        box-shadow:0 0 40px rgba(168,85,247,0.5);
61    }
62    
63    .left-section h1{
64        font-size:60px;
65        font-weight:700;
66    }
67    
68    .left-section span{
69        color:#c026ff;
70    }
71    
72    .left-section p{
73        margin-top:20px;
74        color:#bdbdbd;
75        font-size:18px;
76        text-align:center;
77        max-width:500px;
78    }
79    
80    /* RIGHT SECTION */
81    
82    .right-section{
83        width:50%;
84    
85        display:flex;
86        justify-content:center;
87        align-items:center;
88    
89        background:#050816;
90    }
91    
92    /* LOGIN CARD */
93    
94    .login-card{
95    
96        width:420px;
97    
98        background:rgba(255,255,255,0.05);
99    
100       border:1px solid rgba(255,255,255,0.1);
101   
102       backdrop-filter:blur(15px);
103   
104       border-radius:25px;
105   
106       padding:45px;
107   
108       box-shadow:0 0 30px rgba(0,0,0,0.4);
109   }
110   
111   .login-card h2{
112       font-size:35px;
113       margin-bottom:10px;
114   }
115   
116   .subtitle{
117       color:#a1a1aa;
118       margin-bottom:35px;
119   }
120   
121   /* INPUT BOX */
122   
123   .input-box{
124   
125       position:relative;
126   
127       margin-bottom:25px;
128   }
129   
130   .input-box i{
131   
132       position:absolute;
133   
134       left:18px;
135       top:18px;
136   
137       color:#c026ff;
138   }
139   
140   .input-box input{
141   
142       width:100%;
143   
144       background:#0f172a;
145   
146       border:2px solid transparent;
147   
148       outline:none;
149   
150       padding:15px 15px 15px 50px;
151   
152       border-radius:15px;
153   
154       color:white;
155   
156       font-size:16px;
157   
158       transition:0.3s;
159   }
160   
161   .input-box input:focus{
162   
163       border-color:#c026ff;
164   
165       box-shadow:0 0 15px rgba(192,38,255,0.5);
166   }
167   
168   /* BUTTON */
169   
170   .login-btn{
171   
172       width:100%;
173   
174       border:none;
175   
176       padding:15px;
177   
178       border-radius:15px;
179   
180       background:linear-gradient(
181           90deg,
182           #7c3aed,
183           #ec4899
184       );
185   
186       color:white;
187   
188       font-size:18px;
189   
190       font-weight:600;
191   
192       cursor:pointer;
193   
194       transition:0.3s;
195   }
196   
197   .login-btn:hover{
198   
199       transform:translateY(-2px);
200   
201       box-shadow:0 0 20px rgba(192,38,255,0.5);
202   }
203   
204   /* Bottom Text */
205   
206   .bottom-text{
207   
208       margin-top:25px;
209   
210       text-align:center;
211   
212       color:#a1a1aa;
213   }
214   
215   .bottom-text a{
216   
217       color:#c026ff;
218   
219       text-decoration:none;
220   
221       font-weight:600;
222   }
223   
224   /* Responsive */
225   
226   @media(max-width:992px){
227   
228       .login-container{
229           flex-direction:column;
230       }
231   
232       .left-section,
233       .right-section{
234           width:100%;
235           height:50vh;
236       }
237   
238       .left-section h1{
239           font-size:40px;
240       }
241   
242   }
```

---

### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake news ui\templates\login.heml
*Saved at: 5/12/2026, 12:07:11 PM*

**[ADDED]**
```
1     <!DOCTYPE html>
2     <html lang="en">
3     
4     <head>
5         <meta charset="UTF-8">
6         <meta name="viewport" content="width=device-width, initial-scale=1.0">
7     
8         <title>Login - Fake News Detection</title>
9     
10        <!-- Google Font -->
11        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
12    
13        <!-- Font Awesome -->
14        <link rel="stylesheet"
15            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
16    
17        <!-- CSS -->
18        <link rel="stylesheet"
19            href="{{ url_for('static', filename='login.css') }}">
20    
21    </head>
22    
23    <body>
24    
25        <div class="login-container">
26    
27            <!-- Left Side -->
28            <div class="left-section">
29    
30                <div class="logo-box">
31                    <i class="fa-solid fa-shield-halved"></i>
32                </div>
33    
34                <h1>
35                    Fake News
36                    <span>Detection</span>
37                </h1>
38    
39                <p>
40                    AI-Powered News Verification System with Explainability
41                </p>
42    
43            </div>
44    
45            <!-- Right Side -->
46            <div class="right-section">
47    
48                <div class="login-card">
49    
50                    <h2>Welcome Back 👋</h2>
51    
52                    <p class="subtitle">
53                        Login to continue
54                    </p>
55    
56                    <form action="/login" method="POST">
57    
58                        <!-- Email -->
59                        <div class="input-box">
60    
61                            <i class="fa-solid fa-envelope"></i>
62    
63                            <input
64                                type="email"
65                                name="email"
66                                placeholder="Enter your email"
67                                required>
68    
69                        </div>
70    
71                        <!-- Password -->
72                        <div class="input-box">
73    
74                            <i class="fa-solid fa-lock"></i>
75    
76                            <input
77                                type="password"
78                                name="password"
79                                placeholder="Enter password"
80                                required>
81    
82                        </div>
83    
84                        <!-- Button -->
85                        <button type="submit" class="login-btn">
86    
87                            <i class="fa-solid fa-right-to-bracket"></i>
88    
89                            Login
90    
91                        </button>
92    
93                    </form>
94    
95                    <div class="bottom-text">
96    
97                        Don't have an account?
98    
99                        <a href="#">Register</a>
100   
101                   </div>
102   
103               </div>
104   
105           </div>
106   
107       </div>
108   
109   </body>
110   
111   </html>
```

---

