# 🎯 Regression-Based Salary Predictor API

A lightweight, Django-based REST API that predicts a person's salary using different regression machine learning models based on years of experience.

📁 Models are pre-trained using scikit-learn and stored in the `media/Models/` folder.

---

## 🚀 Features

- 🔍 Predict salary using multiple regression algorithms:
  - Linear Regression
  - Lasso Regression
  - Ridge Regression
  - SVR (Support Vector Regression)
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - AdaBoost Regressor
- 🧠 Uses pre-trained `.pkl` model files
- 🛠️ Built with Django & Django REST Framework
- 📦 Easily extendable for more models and features

---

## 🏗️ Project Structure

```

SalaryPredictor/
├── RegressionBasedSalaryAPI/
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── ...
├── media/
│   └── Models/
│       ├── linear\_regression.pkl
│       ├── ridge\_regression.pkl
│       └── ...
├── SalaryPredictor/
│   └── settings.py
└── manage.py

```

---

## 📥 API Usage

### 🔗 Endpoint

```

POST /api/predict/

````

### 📨 Request Payload

```json
{
  "model_name": "linear_regression",
  "experience_year": 5.3
}
````

### ✅ Supported `model_name` values:

* `linear_regression`
* `lasso_regression`
* `ridge_regression`
* `svr_regression`
* `decision_tree`
* `random_forest`
* `gradient_boost`
* `adaboost`

### 📤 Response Example

```json
{
  "model": "linear_regression",
  "experience_year": 5.3,
  "predicted_salary": 68217.09
}
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dhruvsh1997/SalaryPredictor.git
cd SalaryPredictor
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

<sub>*(Or manually: `pip install django djangorestframework scikit-learn numpy pandas`)*</sub>

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Start the Server

```bash
python manage.py runserver
```

---

## 🧪 Testing the API

Use Postman, Curl, or any API client:

```bash
curl -X POST http://127.0.0.1:8000/api/predict/ \
     -H "Content-Type: application/json" \
     -d '{"model_name": "linear_regression", "experience_year": 3.2}'
```

---

## 📁 Pre-trained Models

Place your trained `.pkl` models in the `media/Models/` folder.
Each model file should match the naming convention used in the payload (`<model_name>.pkl`).

---

## 👨‍💻 Author

**Your Name**
📧 [dhruvsh1997@gmail.com](mailto:your.email@example.com)
🐙 [GitHub](https://github.com/dhruvsh1997)

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

