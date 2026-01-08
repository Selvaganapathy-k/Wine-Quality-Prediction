
# 🍷 Wine Quality Prediction

## 📌 Project Description

This project implements a **Wine Quality Prediction system** using Machine Learning.
The model predicts the **quality rating (0–10)** of wine based on its physicochemical properties.

The project includes:

* Data preprocessing and analysis
* Model training and evaluation
* A **Streamlit web application** for real-time quality prediction

This project is developed as a **mini project** to gain practical experience with regression modeling and ML deployment.

---

## 📁 Dataset Information

* **Dataset Name:** Wine Quality Dataset
* **File:** `winequality-red.csv` *(or the dataset file used)*

The dataset includes physicochemical properties such as:

* Fixed acidity
* Volatile acidity
* Citric acid
* Residual sugar
* Chlorides
* Free sulfur dioxide
* Total sulfur dioxide
* Density
* pH
* Sulphates
* Alcohol
* **Quality** (target label)

---

## 🛠️ Technologies & Libraries Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

---

## 📂 Project Structure

```
Wine-Quality-Prediction
│
├── winequality-red.csv
├── wine_quality.ipynb
├── best_model.pkl
├── scaler.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Selvaganapathy-k/Wine-Quality-Prediction
cd Wine-Quality-Prediction
```

---

### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 🌐 Live Application

🔗 **Streamlit App URL:**
https://selvaganapathy-k-wine-quality-prediction-app-86yntu.streamlit.app/


---

## 🔍 Model Details

* Problem Type: **Regression**
* Target Variable: Wine **Quality**
* Model stored in `best_model.pkl`
* Feature scaling using `scaler.pkl`

---

## 📈 Features

* Clean and user-friendly Streamlit interface
* Real-time wine quality prediction
* Uses saved model and scaler for consistent results
* Easy to deploy and use

---

## 🎓 Learning Outcomes

* Understanding regression problems
* Feature scaling and preprocessing
* Model training and evaluation
* Saving and loading models using Pickle
* Deploying ML applications using Streamlit
* Structuring end-to-end ML projects on GitHub

---

## 📌 Notes

* Virtual environment folders (`venv`, `myvenv`) are not included in this repository.
* All required dependencies are listed in `requirements.txt`.

---

## ✍️ Author

**Selvaganapathy K**
Computer Science Student

---

## 🏁 Conclusion

This project demonstrates how machine learning can be applied to predict wine quality using physicochemical properties, and how to deploy an interactive prediction app with Streamlit.
