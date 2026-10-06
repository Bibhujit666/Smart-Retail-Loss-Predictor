# 🛒 Smart Retail Loss Predictor

An AI/ML-powered web application that predicts **retail shrinkage/loss** and identifies the associated **risk level** based on store operating conditions such as temperature, humidity, customer footfall, staffing, employee experience, cold-chain interruptions, and weekends.

The project combines **Machine Learning, Python, FastAPI, Node.js, Express.js, and EJS** to provide an easy-to-use retail loss prediction system.

---

##  Features

-  Predicts expected retail loss in **INR (₹)**
-  Identifies retail loss risk
-  Uses environmental factors such as temperature and humidity
-  Considers customer footfall
-  Considers staff count and staff experience
-  Considers cold-chain interruption time
-  Considers weekend/weekday operations
-  Uses Random Forest Machine Learning models
-  Python ML prediction API using FastAPI
-  Node.js + Express backend
-  EJS-based web interface
-  Displays prediction results with a Chart.js visualization
-  Includes a demo-fill option for quick testing

---

##  How It Works

The application uses two Machine Learning models:

### 1. Loss Prediction — Regression

A `RandomForestRegressor` predicts the expected **shrinkage value in INR**.

### 2. Risk Prediction — Classification

A `RandomForestClassifier` predicts whether the store is at **high shrinkage risk**.

### Input Features

The models use the following features:

| Feature | Description |
|---|---|
| Temperature | Store temperature in °C |
| Humidity | Store humidity percentage |
| Footfall | Number of customers/visitors |
| Staff Count | Active staff members on shift |
| Staff Experience | Average staff experience in years |
| Cold Chain Break | Cold-chain interruption in minutes |
| Weekend | Whether the day is a weekend |

---

##  System Architecture

```text
                ┌─────────────────────┐
                │    User / Browser   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   EJS Web Interface │
                │  HTML + CSS + JS    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Node.js + Express   │
                │      Backend        │
                └──────────┬──────────┘
                           │
                           │ HTTP Request
                           ▼
                ┌─────────────────────┐
                │ Python FastAPI      │
                │    ML API           │
                └──────────┬──────────┘
                           │
                    ┌──────┴──────┐
                    ▼             ▼
             ┌────────────┐ ┌─────────────┐
             │ Regression │ │Classification│
             │   Model    │ │    Model    │
             └──────┬─────┘ └──────┬──────┘
                    │               │
                    └───────┬───────┘
                            ▼
                   Prediction + Risk
                            │
                            ▼
                  ┌───────────────────┐
                  │ Result Dashboard  │
                  │ ₹ Loss + Risk     │
                  │ Chart             │
                  └───────────────────┘
```

---

##  Project Structure

```text
Smart-Retail-Loss-Predictor/
│
├── backend/
│   ├── controllers/
│   │   └── predictionController.js
│   ├── routes/
│   │   └── predictionRoutes.js
│   └── server.js
│
├── data/
│   └── retail_data.csv
│
├── ml-model/
│   ├── train.py
│   ├── predict.py
│   ├── regressor.pkl
│   └── classifier.pkl
│
├── public/
│   └── css/
│       └── style.css
│
├── views/
│   ├── index.ejs
│   └── result.ejs
│
├── package.json
├── package-lock.json
└── README.md
```

---

##  Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- EJS
- Chart.js

### Backend
- Node.js
- Express.js
- Axios

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Random Forest Regression
- Random Forest Classification

### ML API
- FastAPI

---

##  Dataset

The project uses a retail operations dataset containing information such as:

- Store information
- Date and day information
- Temperature
- Humidity
- Customer footfall
- Staff count
- Staff experience
- Opening inventory value
- Daily sales
- Cold-chain break duration
- Shrinkage value
- Spoilage value
- High shrinkage risk
- High spoilage risk

The primary regression target is:

```text
shrinkage_value_inr
```

The classification target is:

```text
high_shrinkage_risk
```

---



#  Model Training

To retrain the Machine Learning models:

```bash
cd ml-model
python train.py
```

The training script:

1. Loads the retail dataset.
2. Removes missing values.
3. Selects relevant features.
4. Splits the dataset into training and testing sets.
5. Trains a Random Forest Regressor.
6. Trains a Random Forest Classifier.
7. Calculates model performance.
8. Displays feature importance.
9. Saves the trained models as:

```text
regressor.pkl
classifier.pkl
```

---

##  Machine Learning Models

### Random Forest Regressor

Used to predict:

```text
Shrinkage Value (₹)
```

### Random Forest Classifier

Used to predict:

```text
High Shrinkage Risk
```

Random Forest was selected because it can handle nonlinear relationships between operational factors and retail loss and generally works well with mixed numerical features.

---

##  Future Improvements

Some possible improvements for future versions:

- [ ] Add spoilage prediction
- [ ] Add store-wise prediction history
- [ ] Add database integration
- [ ] Add authentication/login
- [ ] Add interactive analytics dashboard
- [ ] Add model performance metrics to the UI
- [ ] Add SHAP-based explainable AI
- [ ] Add prediction history and reports
- [ ] Deploy the application using Docker
- [ ] Deploy ML API and Node.js backend to the cloud
- [ ] Add real-time retail monitoring
- [ ] Add alerts for high-risk conditions

---

##  Project Objective

The main objective of **Smart Retail Loss Predictor** is to demonstrate how Machine Learning can be integrated with a web application to help retailers identify potential inventory losses and operational risks.

By using environmental, staffing, customer traffic, and cold-chain information, the system provides an estimated
