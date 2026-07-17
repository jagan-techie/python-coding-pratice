### 📄 c:\Users\bjaga\JC-Badiga J-1bab\2ND SEMESTER\PROJECTS\NLP projet\Fake_news_ui_database_connected\Fake news ui - Copy\app.py
*Saved at: 5/20/2026, 8:40:08 PM*

**[REMOVED]**
```
(from line ~5)
import os

```
**[ADDED]**
```
110   
```
**[REMOVED]**
```
(from line ~121)
    fake_words = ['breaking', 'viral', 'shocking', 'secret', 'exclusive', 'scandal']
    suspicious_words = [word for word in fake_words if word in news.lower()]

```
**[ADDED]**
```
121       fake_words = [
122           'breaking',
123           'viral',
124           'shocking',
125           'secret',
126           'exclusive',
127           'scandal',
128           'miracle',
129           'exposed',
130           'urgent',
131           'unbelievable'
132       ]
```
**[REMOVED]**
```
(from line ~134)
    if len(suspicious_words) >= 2:

```
**[ADDED]**
```
134       influential_words = [
135           word for word in fake_words
136           if word in news.lower()
137       ]
138   
139       if len(influential_words) >= 2:
```
**[REMOVED]**
```
(from line ~141)
        confidence = '92%'

```
**[ADDED]**
```
141           fake_prob = 92
142           real_prob = 8
143           confidence = 92
144           explanation = "Suspicious words were found in the article. These words are commonly used in misleading or fake news content."
```
**[REMOVED]**
```
(from line ~147)
        confidence = '87%'

```
**[ADDED]**
```
147           fake_prob = 13
148           real_prob = 87
149           confidence = 87
150           explanation = "No major suspicious words found. The article appears more authentic."
```
**[REMOVED]**
```
(from line ~156)
        suspicious_words=suspicious_words

```
**[ADDED]**
```
156           fake_prob=fake_prob,
157           real_prob=real_prob,
158           influential_words=influential_words,
159           explanation=explanation
```
**[REMOVED]**
```
(from line ~170)
    app.run(debug=True)

```
**[ADDED]**
```
170       app.run(debug=True)
```

---

