# Minor-Project-I

# Predictive Modeling for Heart Failure

## Project Summary

This project develops a predictive model for heart failure using machine learning techniques, designed to identify high-risk patients and facilitate early intervention. By analyzing anonymized patient data—such as demographics, medical histories, and clinical assessments—the model aims to empower healthcare professionals with the insights they need to make informed decisions.

### Key Features

- **Data Utilization:** The model leverages a comprehensive dataset that includes various patient attributes, allowing for precise risk assessment.
- **Algorithm Performance:** We evaluated several algorithms, finding that the Random Forest method performed best, achieving an AUC-ROC score of **0.89** and an accuracy of **0.93**. The Neural Network model followed closely, with an accuracy of **0.86**.
- **Real-Time Assessments:** The model is implemented through an intuitive Streamlit application, enabling healthcare professionals to input patient data and receive real-time risk assessments. This functionality facilitates personalized treatment strategies tailored to individual patient needs.

### Benefits

- **Early Identification:** The predictive model plays a crucial role in the early identification of individuals at risk for heart failure, which is essential for timely intervention and management.
- **Personalized Care:** By supporting individualized treatment plans, the model has the potential to reduce the frequency of severe heart failure episodes, leading to better patient outcomes.
- **Clinical Applicability:** Future enhancements will focus on expanding the dataset and integrating real-time data from multiple hospitals. This will further improve the model’s accuracy and its practical application in clinical settings.



Here’s the revised section with the context and project summary combined, providing detailed information about cardiovascular diseases and the dataset used in the project:

---

## Project Summary

Cardiovascular diseases (CVDs) are the leading cause of death worldwide, claiming an estimated 17.9 million lives each year, which accounts for 31% of all deaths globally. Four out of five CVD deaths are attributed to heart attacks and strokes, with one-third of these fatalities occurring prematurely in individuals under 70 years of age. Heart failure is a common outcome of CVDs, making early detection and management crucial. This project develops a predictive model for heart failure using machine learning techniques to identify high-risk patients and facilitate timely intervention.

The dataset utilized for this model contains 11 key features that are critical in predicting heart disease. These features include:

- **Age:** Age of the patient (in years)
- **Sex:** Gender of the patient (M: Male, F: Female)
- **ChestPainType:** Type of chest pain (TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic)
- **RestingBP:** Resting blood pressure (in mm Hg)
- **Cholesterol:** Serum cholesterol (in mg/dl)
- **FastingBS:** Fasting blood sugar (1: if FastingBS > 120 mg/dl, 0: otherwise)
- **RestingECG:** Resting electrocardiogram results (Normal, ST: ST-T wave abnormality, LVH: left ventricular hypertrophy)
- **MaxHR:** Maximum heart rate achieved (numeric value between 60 and 202)
- **ExerciseAngina:** Exercise-induced angina (Y: Yes, N: No)
- **Oldpeak:** ST depression (numeric value)
- **ST_Slope:** Slope of the peak exercise ST segment (Up, Flat, Down)
- **HeartDisease:** Output class (1: heart disease, 0: Normal)

### Dataset Overview

This dataset is a comprehensive compilation created by merging five existing heart disease datasets, making it the largest heart disease dataset available for research purposes. The datasets used in this curation are:

- **Cleveland:** 303 observations
- **Hungarian:** 294 observations
- **Switzerland:** 123 observations
- **Long Beach VA:** 200 observations
- **Stalog (Heart) Data Set:** 270 observations

In total, the combined dataset contains **1,190 observations**, with **272 duplicates** removed, resulting in a final dataset of **918 observations**.

### Key Features

- **Data Utilization:** The model leverages this comprehensive dataset, which includes various patient attributes, allowing for precise risk assessment.
- **Algorithm Performance:** We evaluated several algorithms, determining that the Random Forest method performed best, achieving an AUC-ROC score of **0.89** and an accuracy of **0.93**. The Neural Network model followed closely, with an accuracy of **0.86**.
- **Real-Time Assessments:** Implemented through an intuitive Streamlit application, the model enables healthcare professionals to input patient data and receive real-time risk assessments, facilitating personalized treatment strategies tailored to individual patient needs.

### Benefits

- **Early Identification:** The predictive model plays a crucial role in the early identification of individuals at risk for heart failure, which is essential for timely intervention and management.
- **Personalized Care:** By supporting individualized treatment plans, the model has the potential to reduce the frequency of severe heart failure episodes, leading to better patient outcomes.
- **Clinical Applicability:** Future enhancements will focus on expanding the dataset and integrating real-time data from multiple hospitals, further improving the model’s accuracy and practical application in clinical settings.

---

## 🚀 Getting Started

### Prerequisites

- **Hardware:** Laptop with at least 8GB of RAM and 500GB of storage.
- **Operating System:** Windows.
- **Software:**
  - Python (preferably with Anaconda)
  - Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit

### Installation

**Follow these steps to get a local copy of the project:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/heart-failure-predictive-model.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd heart-failure-predictive-model
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and go to `http://localhost:8501` to view the application.

### Usage

- Input anonymized patient data into the Streamlit application.
- Receive real-time risk assessments and tailored recommendations for heart failure management.

**Note:** This project uses Python for backend processing and Streamlit for the front end, along with libraries like Pandas and Scikit-learn for machine learning.

<div align="center">

### 💻 Tech Stacks

![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23F4A261.svg?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

---

## ✨ Features
- 🩺 **Risk Assessment:** Provides real-time risk assessments for heart failure based on patient data.
- 🔍 **Model Evaluation:** Allows users to explore model performance metrics and validation results.
- 🎛️ **User-Friendly Interface:** Simple and intuitive interface for healthcare professionals.
- 📈 **Data Visualization:** Displays key insights and trends through interactive graphs and charts.
- 📊 **Personalized Recommendations:** Generates individualized treatment strategies based on risk profiles.

---

## 🌈 Project Overview

The **Predictive Modeling for Heart Failure** project aims to leverage machine learning to identify high-risk patients and facilitate early interventions. By analyzing anonymized patient data, the model provides healthcare professionals with valuable insights to improve patient outcomes.

---

## 📊 Current Status

The project is currently in the development phase, with core features implemented and undergoing testing. 🛠️

---

## 🚀 Future Work

To enhance the model's performance and its utility in clinical environments, we plan to:

- 📊 **Expand the dataset** by including a diverse range of anonymized patient records from different healthcare institutions. 📈
- 🌐 **Integrate real-time patient data** to allow dynamic risk assessments and improve the model's predictive capabilities. ⏱️
- 🔄 **Continuously refine algorithms** and evaluate additional machine learning techniques to optimize accuracy and reliability. 🔍

---

### Future Needs

Future enhancements could also include:

- 🎨 **Improved user interface** for a better user experience. 🖥️
- 🔒 **Enhanced security features** for data protection. 🔑
- 📈 **Advanced machine learning models** to further enhance predictive accuracy. 🤖
- 🌍 **Wider accessibility** to ensure healthcare professionals can easily utilize the model. 📲
- 📚 **Comprehensive documentation** to assist users in understanding and implementing the model effectively. 📖

---

## <img src="https://github.com/Meetjain1/wanderlust/assets/133582566/90f3930e-5a12-4a4e-8ac9-0dc7d5396adb" width="35" height="35"> Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

- If you have suggestions for the project, such as reporting a bug, improving the model, or enhancing the README.md file, feel free to **open an issue** or create a pull request with the necessary changes.
- Please ensure that your code is well-commented and follows Python best practices.
- Create individual pull requests for each suggestion to keep changes focused and manageable.

Your involvement helps to improve the project and make it better for everyone. Thank you for your contributions!

Kindly go through [CONTRIBUTING.md](CONTRIBUTING.md) to understand everything from setup to contributing guidelines.


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

We would like to thank all the researchers and institutions that contributed to the availability of anonymized patient datasets, as well as the open-source community for their invaluable libraries and tools. 

---

![Predictive Model for Heart failure-1](https://github.com/user-attachments/assets/47e158bf-09bc-4696-bc62-d38a30c8ebe2)
![Predictive Model for Heart failure-2](https://github.com/user-attachments/assets/e41ecbc0-e2b9-4d3c-a24f-a2b46d043e21)
![Predictive Model for Heart failure-3](https://github.com/user-attachments/assets/ad4a92bf-ac55-491b-ad18-48a2d5914582)
![Predictive Model for Heart failure-4](https://github.com/user-attachments/assets/da5a008a-add7-43c5-b259-baacb10fde09)
![Predictive Model for Heart failure-5](https://github.com/user-attachments/assets/7528ed7e-39ff-43b5-a214-662160517f89)
![Predictive Model for Heart failure-6](https://github.com/user-attachments/assets/270a8a96-fee6-438f-9234-a26a25c8de84)
![Predictive Model for Heart failure-7](https://github.com/user-attachments/assets/0c93694e-8c6a-43c6-a544-a64388f86558)
![Predictive Model for Heart failure-8](https://github.com/user-attachments/assets/22614fd3-4b87-49bc-8a22-74a3f74104a8)
![Predictive Model for Heart failure-9](https://github.com/user-attachments/assets/a8f5555e-b40d-4a4f-9754-a235824ac28d)
![Predictive Model for Heart failure-10](https://github.com/user-attachments/assets/8884b1ff-d017-4046-b3cf-2d8bf13db940)
![Predictive Model for Heart failure-11](https://github.com/user-attachments/assets/acfb4f7f-5d03-4292-8331-4332446786bd)
![Predictive Model for Heart failure-12](https://github.com/user-attachments/assets/1c2fccc7-a918-43a4-90e7-d58042bb857c)
![Predictive Model for Heart failure-13](https://github.com/user-attachments/assets/7e3e141e-56fb-46c8-a3e3-b8099135cc1a)
![Predictive Model for Heart failure-14](https://github.com/user-attachments/assets/f952d3a9-93dc-4e2f-9e87-e60a37fb98f9)
![Predictive Model for Heart failure-15](https://github.com/user-attachments/assets/de4d679e-700c-4322-a6e2-cae66e949f4f)



































## <h2 align="center"><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Red%20Heart.png" width="35" height="35">Our Contributors</h2>
<h3>Thank you for contributing to our repository</h3>

![Contributors](https://contrib.rocks/image?repo=abhisek2004/Minor-Project-I-Heart-Failure)

---

## Stargazers

<div align='center'>

[![Stargazers repo roster for @abhisek2004/Minor-Project-I-Heart-Failure](https://reporoster.com/stars/abhisek2004/Minor-Project-I-Heart-Failure)](https://github.com/abhisek2004/Minor-Project-I-Heart-Failure/stargazers)

</div>

## Forkers

<div align='center'>

[![Forkers repo roster for @abhisek2004/Minor-Project-I-Heart-Failure](https://reporoster.com/forks/abhisek2004/Minor-Project-I-Heart-Failure)](https://github.com/abhisek2004/Minor-Project-I-Heart-Failure/network/members)

</div>
