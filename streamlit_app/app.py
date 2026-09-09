import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="CalXpert", page_icon="🏃", layout="wide")

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 4rem;
            padding-bottom: 4rem;
        }

        [data-testid="stSelectbox"] * {
            cursor: pointer !important;
        }
        
        [data-testid="InputInstructions"] {
            display: none !important;
        }

        .result-card {
            # background-color: #f0f7ff;
            # border: 1px solid #b6d4fe;
            border-radius: 12px;
            
            padding: 1.5rem 2rem;
            margin-top: 1rem;
        }

        .result-card .label {
            font-size: 2rem;
            color: #555;
            margin-bottom: 0.3rem;
            text-align: center;
        }

        .result-card .value {
            font-size: 1.8rem;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            color: #1a4fa0;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Calories Burnt Predictor")
st.write("Enter your exercise details below to estimate how many calories you burnt.")
st.write("")

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "notebook",
    "calories_prediction_model.pkl"
)

@st.cache_resource
def load_model(path):
    return joblib.load(path) if os.path.exists(path) else None

model = load_model(MODEL_PATH)

if model is None:
    st.error(f"Couldn't find `{MODEL_PATH}`. Run the notebook through 'Saving the Trained Model' first.")
    st.stop()

def predict_calories(gender, age, height, weight, duration, heart_rate, body_temp):
    input_df = pd.DataFrame([{
        "Gender": 0 if gender == "male" else 1,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }])
    return round(float(model.predict(input_df)[0]), 2)

with st.form("prediction_form", border=False):
    col1, col2, col3, col4 = st.columns(4, gap="large")

    with col1:
        gender = st.selectbox("Gender", ["male", "female"], index=None, placeholder="Select gender")
        age = st.number_input("Age (years)", min_value=10, max_value=100, value=None, placeholder="e.g. 28")

    with col2:
        height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=None, placeholder="e.g. 175")
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=None, placeholder="e.g. 72")

    with col3:
        duration = st.number_input("Exercise Duration (minutes)", min_value=1.0, max_value=180.0, value=None, placeholder="e.g. 25")
        heart_rate = st.number_input("Average Heart Rate (bpm)", min_value=60.0, max_value=200.0, value=None, placeholder="e.g. 110")

    with col4:
        body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=None, placeholder="e.g. 40.5")

    st.write("")
    submitted = st.form_submit_button("Predict Calories Burnt", use_container_width=True)

st.write("")

if submitted:
    inputs = [gender, age, height, weight, duration, heart_rate, body_temp]
    if any(v is None for v in inputs):
        st.warning("Please fill in all fields before predicting.")
    else:
        result = predict_calories(gender, age, height, weight, duration, heart_rate, body_temp)
        st.markdown(
            f"""
            <div class="result-card">
                <div class="label">Estimated calories burnt</div>
                <div class="value">{result} kcal</div>
            </div>
            """,
            unsafe_allow_html=True
        )