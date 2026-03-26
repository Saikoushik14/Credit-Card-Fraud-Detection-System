import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report



st.set_page_config(page_title="Fraud Detection App", layout="centered")

st.title("💳 Credit Card Fraud Detection System")
st.write("Upload a dataset to train and detect fraudulent transactions.")

# 📂 Upload CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    with st.spinner("📊 Loading dataset..."):
        data = pd.read_csv(uploaded_file)

    st.success("✅ Dataset loaded successfully!")

    st.write("### 🔍 Dataset Preview")
    st.dataframe(data.head())

    # ✅ Check target column
    if "is_fraud" not in data.columns:
        st.error("❌ Dataset must contain 'is_fraud' column")
        st.stop()

    # 🎯 Features & Target
    X = data.drop("is_fraud", axis=1)
    y = data["is_fraud"]

    # ✅ Keep only numeric columns
    X = X.select_dtypes(include=['int64', 'float64'])

    st.write(f"📌 Using {X.shape[1]} numeric features for training")

    # ✂️ Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # ⚖️ Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 🤖 Train Model
    with st.spinner("🤖 Training model..."):
        model = RandomForestClassifier(
            n_estimators=30,
            max_depth=10,
            class_weight='balanced',
            n_jobs=-1,
            random_state=42
        )
        model.fit(X_train, y_train)

    st.success("✅ Model trained successfully!")

    # 📊 Evaluation
    if st.button("📊 Evaluate Model"):
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        st.write("### ✅ Accuracy:", acc)
        st.text("Classification Report:\n" + classification_report(y_test, y_pred))

    # 🔮 Prediction Section
    st.write("## 🔍 Predict New Transaction")

    input_data = []
    cols = list(X.columns)

    for col in cols:
        val = st.number_input(f"{col}", value=0.0)
        input_data.append(val)

    if st.button("🚀 Predict Fraud"):
        input_array = np.array([input_data])
        input_scaled = scaler.transform(input_array)

        pred = model.predict(input_scaled)
        prob = model.predict_proba(input_scaled)[0][1]

        if pred[0] == 1:
            st.error(f"🚨 Fraud Detected! Probability: {prob:.2f}")
        else:
            st.success(f"✅ Normal Transaction. Probability: {prob:.2f}")

else:
    st.info("👆 Please upload a CSV file to begin")