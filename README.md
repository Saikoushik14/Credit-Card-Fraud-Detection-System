# 💳 Credit Card Fraud Detection System
**Streamlit app link** : https://credit-card-fraud-detection-system-jeyerruz3tu3fcbubyzyr7.streamlit.app/
A Machine Learning-based web application to detect fraudulent credit card transactions using **Random Forest** and deployed using **Streamlit**.

---

## 🚀 Project Overview

This project aims to identify fraudulent transactions in real-time by analyzing transaction details such as amount, location, and time.
It uses a trained machine learning model to classify transactions as **Fraudulent 🚨** or **Normal ✅**.

---

## 🎯 Features

* 📂 Upload CSV dataset
* 🤖 Automatic model training
* 📊 Model evaluation (Accuracy, Classification Report)
* 🔍 Real-time fraud prediction
* ⚡ Fast and optimized for large datasets
* 🌐 Interactive web interface using Streamlit

---

## 🧠 Machine Learning Model

* Algorithm: **Random Forest Classifier**
* Handles imbalanced data using `class_weight='balanced'`
* Feature scaling using **StandardScaler**

---

## 📁 Project Structure

```
├── app.py
├── requirements.txt
├── train_small.csv (optional)
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/Saikoushik14/Credit-Card-Fraud-Detection-System
cd fraud-detection-app
```

### 2️⃣ Create virtual environment (recommended)

```
python -m venv myenv
myenv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
```

---

## 📊 Dataset

* The dataset should contain a target column named:

```
is_fraud
```

* Non-numeric columns are automatically removed during preprocessing.

---

## ⚠️ Limitations

* Streamlit Cloud supports file uploads up to **200MB only**
* Large datasets may increase training time

---

## 💡 Future Improvements

* 📈 Add SMOTE for better fraud detection
* 📊 Visualization dashboards
* 🔐 User authentication system
* ☁️ Deployment with large-scale data handling

---

## 👨‍💻 Author

**Sai Koushik Kasula**
B.Tech Data Science | Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
