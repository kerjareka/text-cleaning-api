👤 Author

Rekarius
AI Engineer Portfolio Project

# Day 1 – Text Cleaning Module for NLP (AI Engineer Portfolio)

This project is part of a daily AI Engineer portfolio challenge.  
Day 1 focuses on building a **reusable text preprocessing module** for Natural Language Processing (NLP) tasks.

Text preprocessing is a critical step in real-world AI systems such as:
- Spam & phishing SMS detection
- Sentiment analysis
- Text classification
- Chatbot input normalization

---

## 🚀 Project Objectives
- Understand how text preprocessing works in NLP pipelines
- Build clean, modular, and reusable Python code
- Prepare text data for machine learning and deep learning models

---

## ✨ Features
The `clean_text()` function performs:
- Lowercasing
- Removal of numbers and special characters
- Tokenization
- Stopword removal
- Cleaning noisy text (symbols & emojis)

---

## 🛠️ Tech Stack
- **Python 3.11**
- **NLTK (Natural Language Toolkit)**

---

## 📁 Project Structure
day1-text-cleaning-api/
│
├── app/
│ ├── init.py
│ └── preprocessing.py
│
├── .gitignore
└── README.md


---

## 🧪 Example Usage

```python
from app.preprocessing import clean_text

text = "SELAMAT!!! Anda MENANG 50JT 🎉"
result = clean_text(text)

print(result)

Output:
selamat menang jt

🧠 Why This Project Matters

In real-world AI applications, raw text data is noisy and inconsistent.
Without proper preprocessing:

-Models perform poorly
-Training becomes unstable
-Accuracy drops significantly

This module demonstrates a foundational skill required for AI Engineers before building any NLP model.


#🚀 API Usage

This project exposes an Indonesian NLP preprocessing service via REST API.

Start the API:
uvicorn app.main:app --reload

Then open:
http://127.0.0.1:8000/docs

Clean Text Endpoint:
POST /clean-text

Request body:
{
  "text": "SELAMAT!!! Anda MENANG 50JT 🎉"
}

Response:
{
  "cleaned_text": "selamat menang jt"
}

Use Cases

-This API can be used for:

-Spam & phishing detection

-Sentiment analysis

-Chatbot preprocessing

-Social media monitoring

-NLP pipelines