# 📰 Fake News Detector

An AI project to classify news articles as **Real** or **Fake** using Natural Language Processing (NLP) and Machine Learning.

## 🚀 Features
- Preprocess news dataset
- Transform text using TF-IDF
- Train Logistic Regression model
- Evaluate with accuracy, confusion matrix, and classification report
- Visualize frequent fake news words with WordCloud

## 📂 Dataset
Download dataset from [Kaggle Fake News Challenge](https://www.kaggle.com/c/fake-news).

## ⚙️ Tech Stack
- Python
- pandas, numpy, scikit-learn
- matplotlib, seaborn, wordcloud

## 📊 Results
- Accuracy: ~92% (Logistic Regression)
- Confusion Matrix & WordCloud available in `assets/`

## ▶️ How to Run
```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
pip install -r requirements.txt
jupyter notebook notebooks/fake_news_detection.ipynb
```

## 📸 Sample Output
![Confusion Matrix](assets/confusion_matrix.png)
![WordCloud](assets/wordcloud.png)

## 📌 Future Work
- Use advanced models (Random Forest, XGBoost, LSTM, BERT)
- Deploy with Flask/Streamlit
testing badges
