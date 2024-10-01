import streamlit as st
import numpy as np
import pandas as pd
import joblib


st.title(" Predictive Modeling for Heart Failure")

st.sidebar.header("Page sidebar")
st.sidebar.image("py.jpg")
sidebar = st.sidebar.selectbox(
    "The app features",
    ("Main Page", "Dataset", "Analysis",
     "Our Model Prediction", "About", "Team", "Feedback")
)

# ========= MAIN PAGE TAB =========
if sidebar == "Main Page":
    st.header("The Heart Disease")

    st.write("""A heart attack, also called a myocardial infarction, happens when a part of the heart muscle doesn't get enough blood.

The more time that passes without treatment to restore blood flow, the greater the damage to the heart muscle.

Coronary artery disease (CAD) is the main cause of heart attack. A less common cause is a severe spasm, or sudden contraction, of a coronary artery that can stop blood flow to the heart muscle.""")

    st.image("ty.jpg")
    st.subheader("Symptoms")

    st.write("""
            The major symptoms of a heart attack are

- Chest pain or discomfort. Most heart attacks involve discomfort in the center or left side of the chest that lasts for more than a few minutes or that goes away and comes back. The discomfort can feel like uncomfortable pressure, squeezing, fullness, or pain.
- Feeling weak, light-headed, or faint. You may also break out into a cold sweat.
- Pain or discomfort in the jaw, neck, or back.
- Pain or discomfort in one or both arms or shoulders.
- Shortness of breath. This often comes along with chest discomfort, but shortness of breath also can happen before chest discomfort.
""")

    st.subheader("Risk factors")

    st.write("""Several health conditions, your lifestyle, and your age and family history can increase your risk for heart disease and heart attack. These are called risk factors. About half of all Americans have at least one of the three key risk factors for heart disease: high blood pressure, high blood cholesterol, and smoking.

Some risk factors cannot be controlled, such as your age or family history. But you can take steps to lower your risk by changing the factors you can control.
""")

    st.subheader("Recover after a heart attack")

    st.write("""
        If you’ve had a heart attack, your heart may be damaged. This could affect your heart’s rhythm and its ability to pump blood to the rest of the body. You may also be at risk for another heart attack or conditions such as stroke, kidney disorders, and peripheral arterial disease (PAD).

You can lower your chances of having future health problems following a heart attack with these steps:

- Physical activity—Talk with your health care team about the things you do each day in your life and work. Your doctor may want you to limit work, travel, or sexual activity for some time after a heart attack.
- Lifestyle changes—Eating a healthier diet, increasing physical activity, quitting smoking, and managing stress—in addition to taking prescribed medicines—can help improve your heart health and quality of life. Ask your health care team about attending a program called cardiac rehabilitation to help you make these lifestyle changes.
- Cardiac rehabilitation—Cardiac rehabilitation is an important program for anyone recovering from a heart attack, heart failure, or other heart problem that required surgery or medical care. Cardiac rehab is a supervised program that includes
1. Physical activity
2. Education about healthy living, including healthy eating, taking medicine as prescribed, and ways to help you quit smoking
3. Counseling to find ways to relieve stress and improve mental health

A team of people may help you through cardiac rehab, including your health care team, exercise and nutrition specialists, physical therapists, and counselors or mental health professionals.


""")

# ========= DATASET TAB =========
if sidebar == "Dataset":
    st.write("Here's the dataset")

    df = pd.read_csv("Heart_datasets/heart.csv")
    x = df.head(100)
    st.write(x)

    lst = ["Main Page", "Dataset", "Analysis", "Our Model Prediction"]

# st.sidebar()

# ========= ANALYSIS TAB =========
if sidebar == "Analysis":

    st.header("Analysis")
    st.write("Insights dataset")

    st.image("img/heart1.jpg")
    st.image("img/heart2.jpg")
    st.image("img/heart3.jpg")

# ========= OUR MODEL PREDICTION TAB =========
if sidebar == "Our Model Prediction":
    st.header("lets use AI")
    st.write("*Lets see what does it say about heart*")
    st.subheader("Your details")

    sex = st.selectbox('Gender = Male : 1,  Female : 0', (0, 1))
    cp = st.number_input(
        "Chest Pain. Are u feeling any Chest pain, if yes please enter the chest pain(cp) prescribed by the doctor", min_value=0, max_value=3)
    exng = st.selectbox(
        "Exercise induced angina. Is there any pain while working out, doing a simple exercise or while in stress", (0, 1))
    oldpeak = st.number_input(
        "Previous peak, Values may be in between 0 and 6.2 but these estimated values might differ", step=0.1, format="%.2f")
    caa = st.number_input(
        "Number of major vessels having issue", min_value=0, max_value=4)

    clicked = st.button("Predict")

    if clicked:
        try:
            model = joblib.load(open('model.pkl', 'rb'))

            if model != None:
                # Ensure the input features are in the correct format
                features = np.array([[sex, cp, exng, oldpeak, caa]])
                predicted = model.predict(features)

                st.header("Predicted Result")
                st.info(
                    '0 (No possibility of heart attack), 1 (Future heart attack detected)')
                st.success(predicted[0])

        except Exception as e:
            st.error(f"Error loading the model: {e}")

# ========= ABOUT TAB =========
if sidebar == "About":

    st.header("About")

    st.subheader("How soon after treatment will I feel better?")
    st.write("""
After you’ve had a heart attack, you’re at a higher risk of a similar occurrence. Your healthcare provider will likely recommend follow-up monitoring, testing and care to avoid future heart attacks. Some of these include:

- Heart scans: Similar to the methods used to diagnose a heart attack, these can assess the effects of your heart attack and determine if you have permanent heart damage. They can also look for signs of heart and circulatory problems that increase the chance of future heart attacks.
- Stress test: These heart tests and scans that take place while you’re exercising can show potential problems that stand out only when your heart is working harder.
- Cardiac rehabilitation: These programs help you improve your overall health and lifestyle, which can prevent another heart attack.


Additionally, you’ll continue to take medicines — some of the ones you received for immediate treatment of your heart attack — long-term. These include:

- Beta-blockers.
- ACE inhibitors.
- Aspirin and other blood-thinning agents.""")

    st.subheader("How soon after treatment will I feel better?")
    st.write("""
In general, your heart attack symptoms should decrease as you receive treatment. You’ll likely have some lingering weakness and fatigue during your hospital stay and for several days after. Your healthcare provider will give you guidance on rest, medications to take, etc.

Recovery from the treatments also varies, depending on the method of treatment. The average hospital stay for a heart attack is between four and five days. In general, expect to stay in the hospital for the following length of time:

- Medication only: People treated with medication only have an average hospital stay of approximately six days.
- PCI: Recovering from PCI is easier than surgery because it’s a less invasive method for treating a heart attack. The average length of stay for PCI is about four days.
- CABG: Recovery from heart bypass surgery takes longer because it’s a major surgery. The average length of stay for CABG is about seven days.
    """)

    st.subheader("How common are heart attacks?")
    st.write("""
Heart attacks are quite common in India, with cardiovascular diseases being a leading cause of mortality. According to various studies, it’s estimated that around 1 in 4 people in India may suffer from some form of heart disease, with heart attacks increasingly affecting younger populations due to lifestyle factors, stress, and dietary habits.

Urbanization, smoking, sedentary lifestyles, and increasing obesity rates contribute to this trend. Awareness and early intervention are critical, as many cases can be managed or prevented with lifestyle changes and proper medical care .""")

# ========= TEAM TAB =========
if sidebar == "Team":
    st.title("About Team⚡")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("img/1.png")
        st.subheader("ABHISEK PANDA")
        st.subheader("Front End Developer")
        st.markdown('''
            * **`Github`** ⭐
                https://github.com/abhisek2004
            * **`Portfolio`** 🌐
                https://abhisekpanda.vercel.app/
        ''')

    with col2:
        st.image("img/2.png")
        st.subheader("Debabrata Mishra")
        st.subheader("Data analytics")
        st.markdown('''
            * **`Github`** ⭐
                https://github.com/debaraja-394
        ''')

    with col3:
        st.image("img/3.png")
        st.subheader("Gobinda Gagan Dey")
        st.subheader("MERN Developer")
        st.markdown('''
            * **`Github`** ⭐
                https://github.com/Developer-Alok
            * **`Portfolio`** 🌐
                https://gobindagagan.vercel.app/
            
        ''')
# ========= FEEDBACK TAB =========
if sidebar == "Feedback":
    col1, col2 = st.columns([2, 2])
    # with col2:
    #     st.image("Images\\AppSettings.png")
    st.markdown("### Bug Report 🪲")
    bug_report = st.text_area("Please describe the issue or report a bug:")
    uploaded_file = st.file_uploader(
        "Attach Screenshot (optional):", type=["png", "jpg"])
    if uploaded_file is not None:
        st.markdown(
            "**<span style = 'color:lightgreen'>Screenshot Attached Successfully 👍🏻</span>**", unsafe_allow_html=True)
        with st.expander("Preview Attached Screenshot"):
            st.image(uploaded_file)
    send_button = st.button("Send Report ✈️")
    if send_button:
        st.markdown(
            "<span style = 'color:lightgreen'>Report Sent Successfully, We'll get back to you super soon ⚡</span>", unsafe_allow_html=True)
        st.markdown(
            "## <span style = 'color:white'>Thank You 💖</span>", unsafe_allow_html=True)
