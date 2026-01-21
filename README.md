# AISA Labwork - Semester 5

This repository contains lab assignments and projects for the **Artificial Intelligence and Systems Applications (AISA)** course, Semester 5.

## 📁 Folder Contents

### 📓 Jupyter Notebooks (Labs)

| File | Description |
| :--- | :--- |
| `Lab1.ipynb` | **Simple Rule-Based AI Agent**: A menu-driven program that explains AI concepts (AI, ML, DL, NLP) and includes a simple quiz. |
| `Lab2.ipynb` | **Data Cleaning & Preprocessing**: Demonstrates data cleaning techniques on the `Air_Quality.csv` dataset, including handling missing values, encoding, and scaling. |
| `Lab3.ipynb` | **Spam Detection**: Implementation of a Spam detection system using the Multinomial Naive Bayes classifier and Bag of Words (CountVectorizer). |
| `Lab4.ipynb` | **Face Recognition**: A system identifying faces in static images using Haar Cascades. |
| `Lab4.1.ipynb` | **Real-time Face Recognition**: Extends face recognition to live webcam feeds using the `face_recognition` library. |
| `Lab5.ipynb` | **Sentiment Analysis**: Sentiment classification using Logistic Regression, Multinomial Naive Bayes, TextBlob, and VADER Lexicon-based analysis. |

### 🐍 Python Scripts
- `assignmet_8.py`: A standalone script for **Face Detection** using OpenCV and Haar Cascades.

### 📊 Datasets (CSV)
- `Air_Quality.csv`: Data used for preprocessing exercises in Lab 2.
- `spam.csv`: Dataset containing SMS messages labeled as 'spam' or 'ham'.
- `Sentiment.csv`: Collection of tweets/text used for sentiment analysis in Lab 5.
- `Sentiment_VADER_Result.csv`: Sentiment analysis results generated using the VADER tool in Lab 5.

### 🖼️ Images
- Used for image processing and face detection tasks:
    - `MESSI.jpg`, `neymar.jpg`, `ronaldo.jpg`: Individual football player images.
    - `trio.jpg`: Group image of players.
    - `img.png`: Sample image for face detection testing.

### 🛠️ Dependencies & Resources
- `haarcascade_frontalface_default.xml`: Pre-trained XML model from OpenCV used for detecting frontal faces.

---

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Install required libraries:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn opencv-python textblob nltk face-recognition
   ```
3. Open the `.ipynb` files in **Jupyter Notebook** or **Google Colab** to executive the cells.
4. Run the python script directly using:
   ```bash
   python assignmet_8.py
   ```

---
*Created as part of the AISA Labwork curriculum.*
