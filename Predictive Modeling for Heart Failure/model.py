import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as ss
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from ydata_profiling import ProfileReport

# Function to display the heart disease prediction page


def prediction_page():
    st.title("Heart Disease Prediction")

    # Load dataset
    data = pd.read_csv('dataset/heart.csv')

    # Show dataset
    if st.checkbox("Show Raw Data"):
        st.subheader("Raw Data")
        st.write(data)

    # Data preprocessing
    df = data.copy()
    # Mapping categorical variables
    df['Sex'] = df['Sex'].map({"M": 0, "F": 1})
    df['RestingECG'] = df['RestingECG'].map({"Normal": 0, "ST": 1, "LVH": 2})
    df['ST_Slope'] = df['ST_Slope'].map({"Up": 2, "Flat": 1, "Down": 0})
    df['ExerciseAngina'] = df['ExerciseAngina'].map({"Y": 1, "N": 0})
    df['ChestPainType'] = df['ChestPainType'].map(
        {"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3})

    # Display boxplots
    if st.checkbox("Show Boxplots"):
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        ss.boxplot(df['RestingBP'], ax=ax[0])
        ax[0].set_title('Resting BP')
        ss.boxplot(df['Cholesterol'], ax=ax[1])
        ax[1].set_title('Cholesterol')
        st.pyplot(fig)

    # EDA Report
    if st.button("Generate EDA Report"):
        profile = ProfileReport(
            df, title="Pandas Profiling Report", explorative=True)
        profile.to_file("eda_report.html")
        st.write("EDA report generated!")

    # Model selection
    st.subheader("Choose Model")
    model_choice = st.selectbox(
        "Select Model", ["Logistic Regression", "KNN", "Decision Tree", "Random Forest"])

    # Model training and evaluation
    if st.button("Train Model"):
        X = df.drop('HeartDisease', axis=1)
        y = df['HeartDisease']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        if model_choice == "Logistic Regression":
            model = LogisticRegression(random_state=42, solver='liblinear')
        elif model_choice == "KNN":
            model = KNeighborsClassifier(n_neighbors=6)
        elif model_choice == "Decision Tree":
            model = DecisionTreeClassifier(max_depth=50, random_state=42)
        else:
            model = RandomForestClassifier(n_estimators=300, random_state=42)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        st.write(f"Accuracy: {accuracy_score(y_test, y_pred)}")
        st.write("Confusion Matrix:")
        st.write(confusion_matrix(y_test, y_pred))
        st.write("Classification Report:")
        st.text(classification_report(y_test, y_pred))

# Function to display the team page


def team_page():
    st.title("Discover Our Team")
    st.subheader("Meet the Team Members")

    team_members = {
        "Abhisek Panda": "Lead Developer - Passionate about coding and software solutions.",
        "Team Member 1": "Data Scientist - Expert in data analysis and modeling.",
        "Team Member 2": "Frontend Developer - Focused on creating user-friendly interfaces.",
        "Team Member 3": "Backend Developer - Specializes in server-side development.",
    }

    for member, description in team_members.items():
        st.write(f"**{member}**: {description}")


# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio(
    "Select a page:", ["Heart Disease Prediction", "Discover Our Team"])

# Page routing
if options == "Heart Disease Prediction":
    prediction_page()
else:
    team_page()
