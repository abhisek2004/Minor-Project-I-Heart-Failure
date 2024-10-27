import time
import os
import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pymongo
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader  # Corrected import
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# MongoDB connection (initialize once)
if "client" not in st.session_state:
    st.session_state["client"] = pymongo.MongoClient(
        "mongodb+srv://abhisekpanda2004guddul:Y3pU0wNKOW8r1ea7@cluster0.0khgj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
st.session_state["db"] = st.session_state["client"].get_database("User_Login")
st.session_state["users_collection"] = st.session_state["db"].get_collection(
    "users")
st.session_state["feedback_collection"] = st.session_state["db"].get_collection(
    "Feedback")
st.session_state["rating_collection"] = st.session_state["db"].get_collection(
    "Rating")

# Load the model once
if "model" not in st.session_state:
    st.session_state["model"] = joblib.load(open('model.pkl', 'rb'))

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

# Function to create the PDF

def create_pdf(name, age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope, prediction_result):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Set background image
    background_image = ImageReader("img/pdf.jpg")
    p.drawImage(background_image, 0, 0, width=letter[0], height=letter[1])

    # Add title
    p.setFont("Helvetica-Bold", 24)
    p.setFillColor(colors.darkred)
    p.drawString(100, 750, "🫀 Heart Failure Prediction Report 🩺")

    # Add project details
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.black)
    text_lines = [
        "Project: Heart Disease Prediction",
        "Created by: Abhisek Panda (Lead 👨‍💻),",
        "Debabrata Mishra (Data Analyst 📊),",
        "Gobinda Gagan Dey (MERN Developer 💻),",
        f"Download Date: {datetime.datetime.now().date()}"
    ]

    y_position = 700
    for line in text_lines:
        p.drawString(100, y_position, line)
        y_position -= 30  # Move down for the next line

    # Add user input details
    p.setFont("Helvetica", 14)
    p.drawString(100, y_position, "User Input Details:")
    y_position -= 20

    details = [
        f"Name: {name}",
        f"Age: {age}",
        f"Sex: {sex}",
        f"Chest Pain Type: {chest_pain_type}",
        f"Resting Blood Pressure: {resting_bp} mm Hg",
        f"Cholesterol: {cholesterol} mg/dL",
        f"Fasting Blood Sugar: {'Yes' if fasting_bs == 1 else 'No'}",
        f"Resting ECG Results: {resting_ecg}",
        f"Maximum Heart Rate Achieved: {max_hr}",
        f"Exercise Induced Angina: {'Yes' if exercise_angina == 1 else 'No'}",
        f"Oldpeak: {oldpeak}",
        f"Slope of the Peak Exercise ST Segment: {st_slope}",
        f"Prediction Result: {
            'No possibility of heart attack' if prediction_result == 0 else 'Future heart attack detected'}"
    ]

    for detail in details:
        p.drawString(100, y_position, detail)
        y_position -= 20

    # Save the PDF
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

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
        st.write("A heart attack, or myocardial infarction, occurs when a section of the heart muscle is deprived of oxygen-rich blood...")
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

        # Making dictionaries
        sex_options = {"Male": 1, "Female": 0}
        chest_pain_type_options = {
            "Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3
        }
        fasting_bs_options = {"True": 1, "False": 0}
        resting_ecg_options = {
            "Normal": 0, "Having ST-T Wave Abnormality": 1, "Showing Left Ventricular Hypertrophy": 2
        }
        exercise_angina_options = {"Yes": 1, "No": 0}
        st_slope_option = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}

        # Input fields for the heart failure prediction attributes
        name = st.text_input("Name", value="", max_chars=30)
        age = st.number_input("Age", min_value=1, max_value=120, value=None)
        sex = st.selectbox('Sex (Male or Female)', options=[
                           ""] + list(sex_options.keys()))
        chest_pain_type = st.selectbox('Chest Pain Type', options=[
                                       ""] + list(chest_pain_type_options.keys()))
        resting_bp = st.number_input(
            "Resting Blood Pressure (Min 68mm Hg to Max 250mm Hg)", min_value=68, max_value=250, value=None)
        cholesterol = st.number_input(
            "Cholesterol (Min 100 mg/dL to Max 600mg/dL)", min_value=50, max_value=600, value=None)
        fasting_bs = st.selectbox('Fasting Blood Sugar (1: True, 0: False)', options=[
                                  ""] + list(fasting_bs_options.keys()))
        resting_ecg = st.selectbox('Resting ECG Results', options=[
                                   ""] + list(resting_ecg_options.keys()))
        max_hr = st.number_input(
            "Maximum Heart Rate Achieved (Min 60bpm to Max 220bpm)", min_value=60, max_value=220, value=None)
        exercise_angina = st.selectbox('Exercise Induced Angina', options=[
                                       ""] + list(exercise_angina_options.keys()))
        oldpeak = st.number_input("Oldpeak (Min 0.0 to Max 6.2)", min_value=0.0,
                                  max_value=6.2, step=0.1, format="%.1f", value=None)
        st_slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[
                                ""] + list(st_slope_option.keys()))

        clicked = st.button("Predict")

        if clicked:
            if not name.strip():
                st.error("Please enter your name.")
            elif age is None or age <= 0 or age > 120:
                st.error("Please enter a valid age between 1 and 120.")
            elif cholesterol is None or cholesterol < 50 or cholesterol > 600:
                st.error("Cholesterol must be between 50 and 600 mg/dL.")
            elif resting_bp is None or resting_bp < 68 or resting_bp > 250:
                st.error(
                    "Resting Blood Pressure must be between 68 and 250 mm Hg.")
            elif max_hr is None or max_hr < 60 or max_hr > 220:
                st.error("Maximum Heart Rate must be between 60 and 220.")
            elif oldpeak is None or oldpeak < 0.0 or oldpeak > 6.2:
                st.error("Oldpeak must be between 0.0 and 6.2.")
            else:
                try:
                    # Use the pre-loaded model
                    model = st.session_state["model"]

                    if model is not None:
                        sex_values = sex_options[sex]
                        chest_pain_type_values = chest_pain_type_options[chest_pain_type]
                        fasting_bs_values = fasting_bs_options[fasting_bs]
                        resting_ecg_values = resting_ecg_options[resting_ecg]
                        exercise_angina_values = exercise_angina_options[exercise_angina]
                        st_slope_values = st_slope_option[st_slope]
                        features = np.array([[age, sex_values, chest_pain_type_values, resting_bp, cholesterol,
                                              fasting_bs_values, resting_ecg_values, max_hr, exercise_angina_values, oldpeak, st_slope_values]])
                        predicted = model.predict(features)

                        # Display header for predicted result
                        st.header("Predicted Result")
                        st.info(
                            '0 (No possibility of heart attack), 1 (Future heart attack detected)')

                        # Conditional message display based on prediction
                        if predicted[0] == 0:
                            st.success(
                                "✅ Good news! No possibility of heart attack")
                        elif predicted[0] == 1:
                            st.warning("⚠ Future heart attack detected")
                        else:
                            st.error("Unexpected prediction value")

                        # Display the user's input values
                        st.subheader("Your Input Values")
                        st.write(f"**Name:** {name}")
                        st.write(f"**Age:** {age}")
                        st.write(
                            f"**Sex:** {'Male' if sex_values == 1 else 'Female'}")
                        st.write(f"**Chest Pain Type:** {chest_pain_type}")
                        st.write(
                            f"**Resting Blood Pressure:** {resting_bp} mm Hg")
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

                        # Create PDF report
                        pdf = create_pdf(name, age, 'Male' if sex_values == 1 else 'Female', chest_pain_type, resting_bp, cholesterol,
                                         fasting_bs_values, resting_ecg, max_hr, exercise_angina_values, oldpeak, st_slope_values, predicted[0])
                        st.download_button(
                            "Download PDF Report", pdf, "heart_failure_report.pdf", "application/pdf")

                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")

    # About Tab
    if sidebar == "About":
        st.header("About")
        st.subheader("How soon after treatment will you feel better?")
        st.write("After you’ve had a heart attack, you’re at a higher risk...")
        st.subheader("How soon after treatment will I feel better?")
        st.write("In general, your heart attack symptoms should decrease...")
        st.subheader("How common are heart attacks?")
        st.write("Heart attacks are quite common in India...")

    # Team Tab
    if sidebar == "Team":
        st.title("Discover Our Team⚡")
        st.write("""
    🌟 **As a team of passionate individuals**, we embarked on a journey to create a user-friendly and efficient application to predict diseases, such as **Predictive Modeling for Heart Failure**. 💓💻
        """)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("img/1.png")
            st.subheader("ABHISEK PANDA (Lead)")
            st.subheader("Front End Developer")
            st.markdown(
                '''* **`Github`** ⭐ https://github.com/abhisek2004 * **`Portfolio`** 🌐 https://abhisekpanda.vercel.app/''')
        with col2:
            st.image("img/2.png")
            st.subheader("Debabrata Mishra (Member 1)")
            st.subheader("Data analytics")
            st.markdown('''* **`Github`** ⭐ https://github.com/debaraja-394''')
        with col3:
            st.image("img/3.png")
            st.subheader("Gobinda Gagan Dey (Member 2)")
            st.subheader("MERN Developer")
            st.markdown(
                '''* **`Github`** ⭐ https://github.com/Developer-Alok * **`Portfolio`** 🌐 https://gobindagagan.vercel.app/''')

    # Feedback Tab
    # Email configuration (use environment variables for security)
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    def send_email_with_attachment(uploaded_file, feedback_data):
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = "nicdelhi2024@gmail.com"
        msg['Subject'] = "Bug Report from Feedback Form"

        # Body of the email
        body = f"Bug Report: {feedback_data['bug_report']}\n\n"
        body += f"Reported by: {feedback_data['full_name']
                                } ({feedback_data['email']})"
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(uploaded_file.getvalue())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        f'attachment; filename={uploaded_file.name}')
        msg.attach(part)

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            st.error(f"Failed to send email: {str(e)}")

    if sidebar == "Feedback":
        col1, col2 = st.columns([2, 2])

        tab1, tab2, tab3 = st.tabs(["❓Help", "💬 Feedback", "⭐ Rating"])

        with tab1:
            st.header("Welcome to the Help Page!")
            st.write("""
                Millions of individuals worldwide suffer from heart failure, a chronic illness that significantly increases morbidity, mortality, and healthcare expenses. Improving patient outcomes and lessening the strain on healthcare systems depend heavily on early identification and efficient management of heart failure.

                Predictive modeling, which employs cutting-edge statistical and machine learning approaches, offers a potential method for identifying those at high risk for heart failure and facilitating prompt therapies. 

                This application is designed for predictive modeling for heart failure using machine learning techniques to identify high-risk patients and facilitate early intervention. The model utilizes anonymized patient data, including demographics, medical histories, and clinical assessments. Among the various algorithms tested, the Random Forest method performed the best, achieving an AUC-ROC score of 0.89.

                The application of this model can help medical professionals identify individuals at risk early, provide individualized treatment strategies, and lower the incidence of severe heart failure episodes. Future efforts will focus on expanding the dataset and incorporating real-time data from multiple hospitals to enhance the model's accuracy and practicality in clinical settings.

                Implemented through a Streamlit application, the model enables healthcare professionals to input patient data and receive real-time risk assessments. This allows for personalized treatment strategies and potentially reduces severe heart failure episodes.

                ### Objectives
                - **Data Gathering and Preprocessing:** Compile and purify a large dataset that includes clinical features, medical histories, test results, and patient demographics.
                - **Feature Selection:** Determine which features are most pertinent and have a substantial impact on predicting heart failure.
                - **Model Development:** Utilize machine learning methods to train various predictive models and evaluate their performance.
                - **Model Validation:** Assess the models' predictive power, accuracy, precision, and recall using appropriate metrics and validation procedures.
                - **Clinical Integration:** Develop techniques for incorporating the best prediction models into clinical practice to improve early diagnosis and treatment of heart failure.

                ### Expected Outcomes
                - **Accurate Predictive Models:** Creation of effective models that can estimate the likelihood of heart failure to facilitate early intervention.
                - **Improved Clinical Decision-Making:** Tools that assist medical practitioners in managing patients, resulting in better outcomes.
                - **Personalized Care:** Treatment regimens tailored to each patient's risk profile, lowering the prevalence of heart failure and its consequences.
                - **Healthcare Efficiency:** Early identification and treatment of heart failure lead to better resource allocation and reduced healthcare costs.

                ### Conclusion
                The development of predictive modeling for heart failure is a significant step forward in enhancing patient outcomes and optimizing healthcare resources. By utilizing patient data and advanced machine learning techniques, this project aims to provide tools that enable early diagnosis and individualized therapy, ultimately improving the quality of life for those at risk of heart failure.
            """)

            # Highlighted Note Box
            st.markdown("""
            <style>
                @keyframes blink {
                    0% { opacity: 1; }
                    50% { opacity: 0; }
                    100% { opacity: 1; }
                }
                .blink {
                    animation: blink 1s infinite;
                }
            </style>
            <div style="background-color: #f0f8ff; padding: 10px; border-radius: 5px; border: 2px solid #007acc;">
                <strong class="blink" style="color: #007acc; font-size: 1.2em;">💡 Important Note! 📧</strong>
                <br>
                <strong style="color: #000000;">This webpage requests your name and email to send you details about your test results.</strong> 
                <br>
                <strong style="color: #ff4500;">Rest assured, your information is safe and will be kept confidential.</strong> 🔒✨
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown("### Bug Report 🪲")
            bug_report = st.text_area(
                "Please describe the issue or report a bug:")
            uploaded_file = st.file_uploader(
                "Attach Screenshot (optional):", type=["png", "jpg", "pdf"])

            if uploaded_file is not None:
                st.markdown(
                    "**<span style='color:lightgreen'>Screenshot Attached Successfully 👍🏻</span>**", unsafe_allow_html=True)
                with st.expander("Preview Attached Screenshot"):
                    st.image(uploaded_file)

            if st.button("Send Report ✈️"):
                # Prepare data for MongoDB Feedback collection
                feedback_data = {
                    "bug_report": bug_report,
                    "screenshot": uploaded_file.name if uploaded_file else None,
                    "email": st.session_state.get("email"),
                    "full_name": st.session_state.get("full_name"),
                }
                st.session_state["feedback_collection"].insert_one(
                    feedback_data)  # Save to Feedback collection

                # Send email
                if uploaded_file is not None:
                    send_email_with_attachment(uploaded_file, feedback_data)

                st.markdown(
                    "<span style='color:lightgreen'>Report Sent Successfully, We'll get back to you super soon ⚡</span>", unsafe_allow_html=True)
                st.markdown(
                    "## <span style='color:white'>Thank You 💖</span>", unsafe_allow_html=True)

        with tab3:
            st.markdown(
                "### Please rate your overall experience in using our Web App")
            st.markdown("Your Feedback is Valuable! 🌟")

            # Create star buttons
            stars = [1, 2, 3, 4, 5]

            # Initialize selected_star to None
            selected_star = st.radio(
                "Select a star rating:", stars, format_func=lambda x: '⭐' * x, key="rating", index=None
            )

            # Automatically display feedback message and send data when a star is clicked
            if selected_star:
                feedback_rating_data = {
                    "rating": selected_star,
                    "email": st.session_state.get("email"),
                    "full_name": st.session_state.get("full_name"),
                }
                st.session_state["rating_collection"].insert_one(
                    feedback_rating_data)  # Save to Rating collection
                st.markdown(f"Thank you for your feedback! You rated us {
                            selected_star} star{'s' if selected_star > 1 else ''} 🌟")


# Run the application
if authenticate_user():
    main_app()
else:
    st.info("Please log in to access the application.")


# # List of image URLs or paths
# image_paths = [
#     "img/heart_failure_1.jpg",
#     "img/heart_failure_2.jpg",
#     "img/heart_failure_3.jpg",
#     "img/heart_failure_4.jpg",
#     "img/heart_failure_5.jpg",
#     "img/heart_failure_6.jpg",
#     "img/heart_failure_7.jpg",
#     "img/heart_failure_8.jpg",
#     "img/heart_failure_9.jpg",
#     "img/heart_failure_10.jpg",
# ]

# # Set up a placeholder for the background
# st.markdown("""
#     <style>
#     .bg {
#         background-image: url('');
#         background-size: cover;
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         z-index: -1;
#         opacity: 0.5;
#         transition: background-image 1s ease-in-out;
#     }
#     </style>
#     <div class="bg"></div>
# """, unsafe_allow_html=True)

# # Main application logic


# def main_app():
#     st.title("Predictive Modeling for Heart Failure")

#     # Your existing app code...

# # Change background images every 10 seconds


# def change_background_images():
#     while True:
#         for image_path in image_paths:
#             st.markdown(f"""
#                 <script>
#                 document.querySelector(
#                     '.bg').style.backgroundImage = "url('{image_path}')";
#                 </script>
#             """, unsafe_allow_html=True)
#             time.sleep(10)  # Change image every 10 seconds


# # Run the application
# if authenticate_user():
#     # Start the background image change in a separate thread
#     import threading
#     threading.Thread(target=change_background_images, daemon=True).start()
#     main_app()
# else:
#     st.info("Please log in to access the application.")