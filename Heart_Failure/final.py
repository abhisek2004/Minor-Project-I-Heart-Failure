import streamlit as st
import numpy as np
import pandas as pd
import joblib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Function to handle authentication


def authenticate_user():
    if st.session_state["authenticated"]:
        return True

    st.sidebar.image('py.jpg')  # Your image path
    st.markdown("<h1 style='text-align: center;'> LOGIN PAGE </h1><br>",
                unsafe_allow_html=True)
    st.header("Enter Email & Full Name: ")

    email = st.text_input(label="Email:", value="", key="email")
    full_name = st.text_input(label="Full Name:", value="", key="full_name")

    if st.button("Login"):
        st.session_state["authenticated"] = True
        st.success("Login successful!")

    return False

# Function to send email


def send_email(to_email, report_content):
    # Set up your email and password
    from_email = "nicdelhi2024@gmail.com"  # Replace with your email
    from_password = "NIC$delhi01L"  # Replace with your password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Heart Failure Prediction Report'

    msg.attach(MIMEText(report_content, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Example for Gmail
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        st.success("Report sent to your email successfully!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# Main application logic


def main_app():
    st.title("Predictive Modeling for Heart Failure")

    st.sidebar.header("Sidebar")
    st.sidebar.image("py.jpg")
    sidebar = st.sidebar.selectbox("The app features", ("Main Page", "Dataset",
                                   "Analysis", "Our Model Prediction", "About", "Team", "Feedback"))

    # ========= MAIN PAGE TAB =========
    if sidebar == "Main Page":
        st.image("heart.jpg")
        st.header("The Heart Disease")
        st.write("A heart attack, or myocardial infarction, occurs when a section of the heart muscle is deprived of oxygen-rich blood...")
        st.image("ty.jpg")
        st.subheader("Symptoms")
        st.write("The major symptoms of a heart attack are...")
        st.subheader("Risk factors")
        st.write("Several health conditions, your lifestyle, and your age and family history can increase your risk for heart disease and heart attack...")
        st.subheader("Recover after a heart attack")
        st.write("If you’ve had a heart attack, your heart may be damaged...")

    # ========= DATASET TAB =========
    if sidebar == "Dataset":
        st.write("Here's the dataset")
        df = pd.read_csv("Heart_datasets/heart.csv")
        st.write(df.head(100))

    # ========= ANALYSIS TAB =========
    if sidebar == "Analysis":
        st.header("Analysis")
        st.write("Insights dataset")
        st.image("img/heart1.jpg")
        st.image("img/heart2.jpg")
        st.image("img/heart3.jpg")

    # ========= OUR MODEL PREDICTION TAB =========
    if sidebar == "Our Model Prediction":
        st.header("Let's use AI for Heart Failure Prediction")
        st.write("Let's see what the AI says about your heart")
        st.subheader("Enter your details")

        # Input fields for the heart failure prediction attributes
        name = st.text_input("Name", value="", max_chars=50)
        email = st.text_input(
            "Email", value="", max_chars=50)  # New email input
        age = st.number_input("Age", min_value=1, max_value=120, value=None)
        sex = st.selectbox('Sex (Male: 1, Female: 0)', ("", 1, 0))
        chest_pain_type = st.selectbox(
            'Chest Pain Type (0: Typical Angina, 1: Atypical Angina, 2: Non-anginal Pain, 3: Asymptomatic)', ("", 0, 1, 2, 3))
        resting_bp = st.number_input(
            "Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, value=None)
        cholesterol = st.number_input(
            "Cholesterol (mg/dL)", min_value=50, max_value=600, value=None)
        fasting_bs = st.selectbox(
            'Fasting Blood Sugar (1: True, 0: False)', ("", 1, 0))
        resting_ecg = st.selectbox(
            'Resting ECG Results (0: Normal, 1: Having ST-T Wave Abnormality, 2: Showing Left Ventricular Hypertrophy)', ("", 0, 1, 2))
        max_hr = st.number_input(
            "Maximum Heart Rate Achieved", min_value=60, max_value=220, value=None)
        exercise_angina = st.selectbox(
            'Exercise Induced Angina (1: Yes, 0: No)', ("", 1, 0))
        oldpeak = st.number_input("Oldpeak (ST depression induced by exercise relative to rest)",
                                  min_value=0.0, max_value=6.2, step=0.1, format="%.1f", value=None)
        st_slope = st.selectbox(
            'Slope of the Peak Exercise ST Segment (0: Upsloping, 1: Flat, 2: Downsloping)', ("", 0, 1, 2))

        clicked = st.button("Predict")

        if clicked:
            if not name.strip():
                st.error("Please enter your name.")
            elif not email.strip() or "@" not in email:
                st.error("Please enter a valid email address.")
            elif age is None or age <= 0 or age > 120:
                st.error("Please enter a valid age between 1 and 120.")
            elif cholesterol is None or cholesterol < 50 or cholesterol > 600:
                st.error("Cholesterol must be between 50 and 600 mg/dL.")
            elif resting_bp is None or resting_bp < 50 or resting_bp > 250:
                st.error(
                    "Resting Blood Pressure must be between 50 and 250 mm Hg.")
            elif max_hr is None or max_hr < 60 or max_hr > 220:
                st.error("Maximum Heart Rate must be between 60 and 220.")
            elif oldpeak is None or oldpeak < 0.0 or oldpeak > 6.2:
                st.error("Oldpeak must be between 0.0 and 6.2.")
            else:
                try:
                    model = joblib.load(open('model.pkl', 'rb'))

                    if model is not None:
                        features = np.array([[age, sex, chest_pain_type, resting_bp, cholesterol,
                                              fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]])
                        predicted = model.predict(features)

                        st.header("Predicted Result")
                        st.info(
                            '0 (No possibility of heart attack), 1 (Future heart attack detected)')
                        st.success(predicted[0])

                        # Display the user's input values
                        st.subheader("Your Input Values")
                        st.write(f"**Name:** {name}")
                        st.write(f"**Email:** {email}")
                        st.write(f"**Age:** {age}")
                        st.write(
                            f"**Sex:** {'Male' if sex == 1 else 'Female'}")
                        st.write(f"**Chest Pain Type:** {chest_pain_type}")
                        st.write(
                            f"**Resting Blood Pressure:** {resting_bp} mm Hg")
                        st.write(f"**Cholesterol:** {cholesterol} mg/dL")
                        st.write(
                            f"**Fasting Blood Sugar:** {'True' if fasting_bs == 1 else 'False'}")
                        st.write(f"**Resting ECG Results:** {resting_ecg}")
                        st.write(f"**Maximum Heart Rate Achieved:** {max_hr}")
                        st.write(
                            f"**Exercise Induced Angina:** {'Yes' if exercise_angina == 1 else 'No'}")
                        st.write(f"**Oldpeak:** {oldpeak}")
                        st.write(
                            f"**Slope of the Peak Exercise ST Segment:** {st_slope}")

                        # Prepare the content for the downloadable file
                        report_content = f"""
                        Name: {name}
                        Email: {email}
                        Age: {age}
                        Sex: {'Male' if sex == 1 else 'Female'}
                        Chest Pain Type: {chest_pain_type}
                        Resting Blood Pressure: {resting_bp} mm Hg
                        Cholesterol: {cholesterol} mg/dL
                        Fasting Blood Sugar: {'True' if fasting_bs == 1 else 'False'}
                        Resting ECG Results: {resting_ecg}
                        Maximum Heart Rate Achieved: {max_hr}
                        Exercise Induced Angina: {'Yes' if exercise_angina == 1 else 'No'}
                        Oldpeak: {oldpeak}
                        Slope of the Peak Exercise ST Segment: {st_slope}
                        Prediction: {predicted[0]}
                        """

                        # Send the email
                        send_email(email, report_content)

                except Exception as e:
                    st.error(f"An error occurred: {e}")

    # ========= ABOUT TAB =========
    if sidebar == "About":
        st.write("This is an AI-based application to predict heart disease...")
        st.image("heart.jpg")

    # ========= TEAM TAB =========
    if sidebar == "Team":
        st.write("Meet our team...")
        st.image("team.jpg")

    # ========= FEEDBACK TAB =========
    if sidebar == "Feedback":
        st.header("Your Feedback")
        feedback = st.text_area("Please provide your feedback:")
        if st.button("Submit"):
            st.success("Thank you for your feedback!")


# Run the application
if authenticate_user():
    main_app()
