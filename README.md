# CalXpert – Calories Burnt Predictor

CalXpert predicts calories burnt during exercise from personal and exercise-related information such as gender, age, height, weight, exercise duration, heart rate, and body temperature using an XGBoost regression model.

## Folder Structure

```text
CalXpert/
├── notebook/
│   └── Calories_Burnt_Prediction.ipynb   # Data preparation, training & evaluation
├── streamlit_app/
│   ├── app.py                            # Streamlit web application
│   └── requirements.txt
└── README.md
```

## Features

1. Data loading and merging (`calories.csv` + `exercise.csv`)
2. Exploratory data analysis with visualizations
3. Data preprocessing and train/test split
4. XGBoost model training and evaluation
5. Linear Regression baseline comparison
6. Hyperparameter tuning with GridSearchCV
7. Feature importance analysis and overfitting check
8. Model saving and `predict_calories()` predictive system
9. Streamlit web app for live calorie predictions

## Dataset

The project uses the Calories Burnt Prediction Dataset containing:

- `calories.csv`
- `exercise.csv`

Dataset source:

https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos

## How to Run

### 1. Download the Dataset

Download the [Calories Burnt Prediction Dataset](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos).

### 2. Run the Notebook

Open:

```text
notebook/Calories_Burnt_Prediction.ipynb
```

Run all cells in Google Colab or Jupyter Notebook and upload the required CSV files when prompted.

The notebook trains the model and creates:

```text
calories_prediction_model.pkl
```

### 3. Install Dependencies

Open the terminal in the `streamlit_app` folder:

```bash
cd streamlit_app
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

### 5. Open the Application

Open the following address in your browser:

```text
http://localhost:8501
```

## Model Performance

| Model | MAE | R² |
|---|---:|---:|
| Linear Regression | 8.39 | 0.9669 |
| XGBoost (default) | 1.48 | 0.9988 |
| **XGBoost (tuned)** | **1.38** | **0.9991** |

**Best Model: XGBoost (tuned)**

The tuned XGBoost model achieved the lowest MAE and the highest R² among the compared models.

The model was tuned using GridSearchCV with:

- `max_depth = 3`
- `n_estimators = 300`

## Feature Importance

Feature importance was analyzed using the XGBoost model.

The top feature identified was:

**Duration**

## Predictive System

The project includes a `predict_calories()` function that takes the following inputs:

- Gender
- Age
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature

The system returns the estimated calories burnt in **kcal**.

## Streamlit Application

The Streamlit application provides a simple interface where users can enter their exercise details and receive an estimated calorie expenditure.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Joblib
- Streamlit

## License

This project is licensed under the MIT License.
