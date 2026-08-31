# ❤️ Cardiovascular Disease Risk Prediction System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cardiovascularpredictsystem-bqbhivrzuapp9v99cfr3fso.streamlit.app/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://cardiovascular-predict-system.onrender.com/docs)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Render-Hosted-46E3B7?style=flat&logo=render&logoColor=white)](https://cardiovascular-predict-system.onrender.com)

An end-to-end Machine Learning web application designed to assess and predict patient cardiovascular disease risk based on clinical health indicators and lifestyle parameters. Built with a decoupled microservice architecture featuring a **FastAPI** inference backend and an interactive **Streamlit** user interface.

---

## 🔗 Live Deployments

* 🌐 **Live Web Application (Frontend)**: [cardiovascularpredictsystem.streamlit.app](https://cardiovascularpredictsystem-bqbhivrzuapp9v99cfr3fso.streamlit.app/)
* ⚡ **Live REST API (Swagger Docs)**: [cardiovascular-predict-system.onrender.com/docs](https://cardiovascular-predict-system.onrender.com/docs)
* 🐙 **GitHub Repository**: [Naren1122/cardiovascular_predict_system](https://github.com/Naren1122/cardiovascular_predict_system)

---

## 📌 Features

* **Dual Machine Learning Engine**: Compare predictions using both **Logistic Regression** and **Support Vector Machine (SVM)** classifiers.
* **Interactive Health Assessment Dashboard**: User-friendly input controls (sliders, selectors) for entering biometric data (blood pressure, cholesterol, glucose, BMI factors, etc.).
* **Real-time RESTful Inference API**: High-performance FastAPI server delivering sub-second predictions with strict Pydantic data validation.
* **Model Insights & Visualizations**: In-app performance metrics, confusion matrices, and classification reports.
* **Production Cloud Architecture**: Fully deployed on Streamlit Community Cloud (Frontend) and Render (Backend API).

---

## 🛠️ Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend UI** | Streamlit, Matplotlib, Seaborn, Requests |
| **Backend API** | FastAPI, Uvicorn, Pydantic |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy, Joblib |
| **Deployment & CI/CD** | Render (Web Service), Streamlit Community Cloud, Git/GitHub |

---

## 🏗️ System Architecture & Project Structure

```text
cardiovascular_predict_system/
├── Ui/                               # Streamlit Frontend Application
│   ├── home.py                       # App landing page & navigation
│   ├── logistic.py                   # Logistic regression prediction UI
│   ├── svm.py                        # SVM prediction UI
│   ├── models.py                     # Data loading & evaluation utilities
│   ├── Cardiovascular_Disease.csv    # Dataset for analytics
│   └── requirements.txt              # Frontend dependencies
│
├── server/                           # FastAPI REST Backend Service
│   ├── app/
│   │   ├── main.py                   # API routes & startup handler
│   │   ├── schema.py                 # Pydantic input/output schemas
│   │   ├── l_model.py                # Logistic Regression loader
│   │   └── svm_models.py             # SVM model loader
│   ├── models/                       # Serialized trained models & scalers (.pkl)
│   │   ├── logistic/
│   │   └── svm/
│   ├── train_model.py                # Model training script
│   └── requirements.txt              # Backend API dependencies
│
└── README.md                         # Project documentation
```

---

## 📊 Dataset & Features

The models analyze 11 clinical features:
* **Demographics**: Age, Gender
* **Body Metrics**: Height (cm), Weight (kg)
* **Cardiovascular Metrics**: Systolic Blood Pressure (`ap_hi`), Diastolic Blood Pressure (`ap_lo`)
* **Laboratory Metrics**: Cholesterol levels (Normal, Above Normal, Well Above Normal), Glucose levels
* **Lifestyle Indicators**: Smoking status, Alcohol intake, Physical activity level

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Root health check & welcome message |
| `POST` | `/request-logistic-cardio` | Inference using Logistic Regression model |
| `POST` | `/request-svm-cardio` | Inference using Support Vector Machine (SVM) model |
| `GET` | `/docs` | Interactive Swagger API Documentation |

### Sample Request Body (`POST /request-logistic-cardio`):
```json
{
  "age": 45,
  "gender": 2,
  "height": 172,
  "weight": 75,
  "ap_hi": 130,
  "ap_lo": 85,
  "cholesterol": 2,
  "gluc": 1,
  "smoke": 0,
  "alco": 0,
  "active": 1
}
```

### Sample Response:
```json
{
  "Prediction Stats": 1,
  "Status": "Likely to have cardiovascular Disease"
}
```

---

## 💻 Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Naren1122/cardiovascular_predict_system.git
cd cardiovascular_predict_system
```

### 2. Run the Backend API (FastAPI)
```bash
cd server
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
*API will run at `http://127.0.0.1:8000` (Docs at `http://127.0.0.1:8000/docs`).*

### 3. Run the Frontend App (Streamlit)
Open a new terminal window:
```bash
cd Ui
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run home.py
```
*UI will open in your browser at `http://localhost:8501`.*

---

## 👨‍💻 Author

* **GitHub**: [@Naren1122](https://github.com/Naren1122)
* **Project**: [Cardiovascular Predict System](https://github.com/Naren1122/cardiovascular_predict_system)
