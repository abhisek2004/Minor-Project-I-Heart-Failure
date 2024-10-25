import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pymongo
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# MongoDB connection (initialize once)
if "client" not in st.session_state:
    st.session_state["client"] = pymongo.MongoClient(
        "mongodb+srv://abhisekpanda2004guddul:Y3pU0wNKOW8r1ea7@cluster0.0khgj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
st.session_state["db"] = st.session_state["client"].get_database("User_Login")
st.session_state["users_collection"] = st.session_state["db"].get_collection(
    "users")

# Load the model once
if "model" not in st.session_state:
    st.session_state["model"] = joblib.load(open('model.pkl', 'rb'))

# Function to create a PDF report


def create_pdf(name, age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope, prediction_result):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Update the image path to the correct filename
    # Ensure this path is correct
    background_image = ImageReader("img/pdf.jpg")
    p.drawImage(background_image, 0, 0, width=letter[0], height=letter[1])

    # Set font and color for the text
    p.setFont("Helvetica-Bold", 24)
    p.setFillColor(colors.black)
    p.drawString(100, 750, "🫀 Heart Failure Prediction Report 🩺")

    # Project Details
    p.setFont("Helvetica", 12)
    p.drawString(100, 720, "Project: Heart Disease Prediction")
    p.drawString(
        100, 705, "Created by: Abhisek Panda, Debabrata Mishra, Gobinda Gagan Dey")
    p.drawString(100, 690, "📅 Date: " + str(pd.Timestamp.now().date()))

    # User Details
    p.setFont("Helvetica", 14)
    p.drawString(100, 650, f"👤 Name: {name}")
    p.drawString(100, 630, f"🎂 Age: {age}")
    p.drawString(100, 610, f"⚥ Sex: {'Male' if sex == 1 else 'Female'}")
    p.drawString(100, 590, f"💔 Chest Pain Type: {chest_pain_type}")
    p.drawString(100, 570, f"🩸 Resting Blood Pressure: {resting_bp} mm Hg")
    p.drawString(100, 550, f"💊 Cholesterol: {cholesterol} mg/dL")
    p.drawString(100, 530, f"🍽️ Fasting Blood Sugar: {
                 'True' if fasting_bs == 1 else 'False'}")
    p.drawString(100, 510, f"📈 Resting ECG Results: {resting_ecg}")
    p.drawString(100, 490, f"❤️ Max Heart Rate Achieved: {max_hr}")
    p.drawString(100, 470, f"🏃 Exercise Induced Angina: {
                 'Yes' if exercise_angina == 1 else 'No'}")
    p.drawString(100, 450, f"📉 Oldpeak: {oldpeak}")
    p.drawString(100, 430, f"📊 Slope of the ST Segment: {st_slope}")

    # Prediction Result
    p.drawString(100, 400, f"🔍 Prediction Result: {prediction_result}")

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer.read()

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
        # Save user data to MongoDB
        st.session_state["users_collection"].insert_one(
            {"email": email, "full_name": full_name})
        st.session_state["authenticated"] = True
        st.success("Login successful!")

    return False

# Main application logic


def main_app():
    st.title("Predictive Modeling for Heart Failure")

    st.sidebar.header("Sidebar")
    st.sidebar.image("py.jpg")
    sidebar = st.sidebar.selectbox(
        "The app features",
        ("Main Page", "Dataset", "Analysis",
         "Our Model Prediction", "About", "Team", "Feedback")
    )

    # Main Page Tab
    if sidebar == "Main Page":
        st.image("heart.jpg")
        st.header("The Heart Disease")
        st.write("A heart attack, or myocardial infarction, occurs when a section of the heart muscle is deprived of oxygen-rich blood, leading to potential damage...")
        st.image("ty.jpg")
        st.subheader("Symptoms")
        st.write("The major symptoms of a heart attack are...")
        st.subheader("Risk factors")
        st.write("Several health conditions, your lifestyle, and your age and family history can increase your risk for heart disease...")
        st.subheader("Recover after a heart attack")
        st.write("If you’ve had a heart attack, your heart may be damaged...")

    # Dataset Tab
    if sidebar == "Dataset":
        st.write("Here's the dataset")
        df = pd.read_csv("Heart_datasets/heart.csv")
        st.write(df.head(100))

    # Analysis Tab
    if sidebar == "Analysis":
        st.header("Analysis")
        st.write("Insights dataset")
        st.image("img/heart1.jpg")
        st.image("img/heart2.jpg")
        st.image("img/heart3.jpg")

    # Our Model Prediction Tab
    if sidebar == "Our Model Prediction":
        st.image("artificial.jpg")
        st.header("Let's use our data for Heart Failure Prediction")
        st.write("Let's see what the AI says about your heart")
        st.subheader("Enter your details")

        # Input fields for the heart failure prediction attributes
        name = st.text_input("Name", value="", max_chars=30)
        age = st.number_input("Age", min_value=1, max_value=120, value=None)
        sex = st.selectbox('Sex ( Male  or Female)', options=[
                           ""] + list({"Male": 1, "Female": 0}.keys()))
        chest_pain_type = st.selectbox('Chest Pain Type', options=[
                                       ""] + list({"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}.keys()))
        resting_bp = st.number_input(
            "Resting Blood Pressure (Min 68mm Hg to Max 250mm Hg)", min_value=68, max_value=250, value=None)
        cholesterol = st.number_input(
            "Cholesterol (Min 100 mg/dL to Max 600mg/dL)", min_value=50, max_value=600, value=None)
        fasting_bs = st.selectbox('Fasting Blood Sugar (1: True, 0: False)', options=[
                                  ""] + list({"True": 1, "False": 0}.keys()))
        resting_ecg = st.selectbox('Resting ECG Results', options=[
                                   ""] + list({"Normal": 0, "Having ST-T Wave Abnormality": 1, "Showing Left Ventricular Hypertrophy": 2}.keys()))
        max_hr = st.number_input(
            "Maximum Heart Rate Achieved (Min 60bpm to Max 220bpm)", min_value=60, max_value=220, value=None)
        exercise_angina = st.selectbox('Exercise Induced Angina', options=[
                                       ""] + list({"Yes": 1, "No": 0}.keys()))
        oldpeak = st.number_input("Oldpeak (Min 0.0 to Max 6.2)", min_value=0.0,
                                  max_value=6.2, step=0.1, format="%.1f", value=None)
        st_slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[
                                ""] + list({"Upsloping": 0, "Flat": 1, "Downsloping": 2}.keys()))

        clicked = st.button("Predict")

        if clicked:
            if not name.strip():
                st.error("Please enter your name.")
            elif age is None or age <= 0 or age > 120:
                st.error("Please enter a valid age between 1 and 120.")
            elif cholesterol is None or cholesterol < 50 or cholesterol > 600:
                st.error(
                    "Please enter a valid cholesterol level between 50 and 600.")
            else:
                try:
                    # Convert user inputs to appropriate format for model prediction
                    sex_values = {"Male": 1, "Female": 0}[sex]
                    chest_pain_type_values = {"Typical Angina": 0, "Atypical Angina": 1,
                                              "Non-anginal Pain": 2, "Asymptomatic": 3}[chest_pain_type]
                    fasting_bs_values = {"True": 1, "False": 0}[fasting_bs]
                    resting_ecg_values = {"Normal": 0, "Having ST-T Wave Abnormality": 1,
                                          "Showing Left Ventricular Hypertrophy": 2}[resting_ecg]
                    exercise_angina_values = {
                        "Yes": 1, "No": 0}[exercise_angina]
                    st_slope_values = {"Upsloping": 0,
                                       "Flat": 1, "Downsloping": 2}[st_slope]
                    features = np.array([[age, sex_values, chest_pain_type_values, resting_bp, cholesterol,
                                          fasting_bs_values, resting_ecg_values, max_hr, exercise_angina_values, oldpeak, st_slope_values]])
                    predicted = st.session_state["model"].predict(features)

                    # Display header for predicted result
                    st.header("Predicted Result")
                    st.info(
                        '0 (No possibility of heart attack), 1 (Future heart attack detected)')

                    # Conditional message display based on prediction
                    prediction_message = ""
                    if predicted[0] == 0:
                        prediction_message = "✅ Good news! No possibility of heart attack"
                    elif predicted[0] == 1:
                        prediction_message = "⚠ Future heart attack detected"
                    else:
                        st.error("Unexpected prediction value")

                    st.success(prediction_message)

                    # Display the user's input values
                    st.subheader("Your Input Values")
                    st.write(f"**Name:** {name}")
                    st.write(f"**Age:** {age}")
                    st.write(
                        f"**Sex:** {'Male' if sex_values == 1 else 'Female'}")
                    st.write(f"**Chest Pain Type:** {chest_pain_type}")
                    st.write(f"**Resting Blood Pressure:** {resting_bp} mm Hg")
                    st.write(f"**Cholesterol:** {cholesterol} mg/dL")
                    st.write(
                        f"**Fasting Blood Sugar:** {'True' if fasting_bs_values == 1 else 'False'}")
                    st.write(f"**Resting ECG Results:** {resting_ecg}")
                    st.write(f"**Maximum Heart Rate Achieved:** {max_hr}")
                    st.write(
                        f"**Exercise Induced Angina:** {'Yes' if exercise_angina_values == 1 else 'No'}")
                    st.write(f"**Oldpeak:** {oldpeak}")
                    st.write(
                        f"**Slope of the Peak Exercise ST Segment:** {st_slope}")

                    # Create PDF
                    pdf = create_pdf(name, age, sex_values, chest_pain_type, resting_bp, cholesterol, fasting_bs_values,
                                     resting_ecg, max_hr, exercise_angina_values, oldpeak, st_slope_values, prediction_message)

                    # Download button for PDF
                    st.download_button(
                        "Download PDF Report", pdf, "heart_failure_prediction_report.pdf")

                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")

    # About Tab
    if sidebar == "About":
        st.header("About")
        st.subheader("How soon after treatment will You feel better?")
        st.write("After you’ve had a heart attack, you’re at a higher risk...")
        st.subheader("How soon after treatment will I feel better?")
        st.write("In general, your heart attack symptoms should decrease...")
        st.subheader("How common are heart attacks?")
        st.write("Heart attacks are quite common in India...")

    # Team Tab
    if sidebar == "Team":
        st.title("About Team⚡")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("img/1.png")
            st.subheader("ABHISEK PANDA")
            st.subheader("Front End Developer")
            st.markdown(
                '''* **`Github`** ⭐ https://github.com/abhisek2004 * **`Portfolio`** 🌐 https://abhisekpanda.vercel.app/''')
        with col2:
            st.image("img/2.png")
            st.subheader("Debabrata Mishra")
            st.subheader("Data analytics")
            st.markdown('''* **`Github`** ⭐ https://github.com/debaraja-394''')
        with col3:
            st.image("img/3.png")
            st.subheader("Gobinda Gagan Dey")
            st.subheader("MERN Developer")
            st.markdown(
                '''* **`Github`** ⭐ https://github.com/Developer-Alok * **`Portfolio`** 🌐 https://gobindagagan.vercel.app/''')

    # Feedback Tab
    if sidebar == "Feedback":
        col1, col2 = st.columns([2, 2])
        st.markdown("### Bug Report 🪲")
        bug_report = st.text_area("Please describe the issue or report a bug:")
        uploaded_file = st.file_uploader(
            "Attach Screenshot (optional):", type=["png", "jpg"])
        if uploaded_file is not None:
            st.markdown(
                "**<span style='color:lightgreen'>Screenshot Attached Successfully 👍🏻</span>**", unsafe_allow_html=True)
            with st.expander("Preview Attached Screenshot"):
                st.image(uploaded_file)
        send_button = st.button("Send Report ✈️")
        if send_button:
            st.markdown(
                "<span style='color:lightgreen'>Report Sent Successfully, We'll get back to you super soon ⚡</span>", unsafe_allow_html=True)
            st.markdown(
                "## <span style='color:white'>Thank You 💖</span>", unsafe_allow_html=True)


# Run the application
if authenticate_user():
    main_app()
else:
    st.info("Please log in to access the application.")
