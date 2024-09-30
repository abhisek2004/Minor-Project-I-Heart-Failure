import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Title and description
st.title("Heart Failure Clinical Records Analysis")
st.write("""
This app performs a Decision Tree Regression on the heart failure clinical records dataset to predict the likelihood of death.
""")

# Load the dataset


def load_data():
    dataset = pd.read_csv('dataset\heart_failure_clinical_records_dataset.csv')
    dataset = dataset.drop(columns=['age'])
    return dataset


dataset = load_data()
st.write("### Dataset Overview")
st.write(dataset.head())

# Define features and target
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Standardize the features
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Train the Decision Tree Regressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)

# Predict on the test data
y_pred = regressor.predict(X_test)

# Concatenate predicted and actual values for comparison
comparison = np.concatenate(
    (y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1)

# Display comparison
st.write("### Comparison of Predicted and Actual Values")
comparison_df = pd.DataFrame(comparison, columns=["Predicted", "Actual"])
st.write(comparison_df)

# Evaluate the model using R² score
r2 = r2_score(y_test, y_pred)
st.write(f'### R² score: {r2}')

# Plotting the comparison
st.write("### Comparison Plot")
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, edgecolors=(0, 0, 0))
ax.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=4)
ax.set_xlabel('Actual')
ax.set_ylabel('Predicted')
ax.set_title('Actual vs Predicted')
st.pyplot(fig)

# User input for prediction
st.write("### Make a Prediction")
with st.form(key='prediction_form'):
    # Create input fields for each feature except the target
    feature_inputs = {}
    for feature in dataset.columns[:-1]:
        feature_inputs[feature] = st.number_input(
            f"Enter value for {feature}", value=0.0)

    # Submit button
    submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        # Collect input values into a DataFrame
        input_values = np.array([list(feature_inputs.values())])

        # Scale the input values
        input_values_scaled = sc_X.transform(input_values)

        # Make prediction
        prediction = regressor.predict(input_values_scaled)

        # Display the prediction result
        st.write(f" Predicted Outcome: {
                 'Death' if prediction[0] == 1 else 'Survival'}")


# import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.metrics import r2_score

# # Title and description
# st.title("Heart Failure Clinical Records Analysis")
# st.write("""
# This app performs a Decision Tree Regression on the heart failure clinical records dataset to predict the likelihood of death.
# """)

# # Load the dataset


# def load_data():
#     dataset = pd.read_csv('heart_failure_clinical_records.csv')
#     dataset = dataset.drop(columns=['age'])
#     return dataset


# dataset = load_data()
# st.write("### Dataset Overview")
# st.write(dataset.head())

# # Define features and target
# X = dataset.iloc[:, :-1].values
# y = dataset.iloc[:, -1].values

# # Split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=0)

# # Standardize the features
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)

# # Train the Decision Tree Regressor
# regressor = DecisionTreeRegressor(random_state=0)
# regressor.fit(X_train, y_train)

# # Predict on the test data
# y_pred = regressor.predict(X_test)

# # Concatenate predicted and actual values for comparison
# comparison = np.concatenate(
#     (y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1)

# # Display comparison
# st.write("### Comparison of Predicted and Actual Values")
# comparison_df = pd.DataFrame(comparison, columns=["Predicted", "Actual"])
# st.write(comparison_df)

# # Evaluate the model using R² score
# r2 = r2_score(y_test, y_pred)
# st.write(f'### R² score: {r2}')

# # Plotting the comparison
# st.write("### Comparison Plot")
# fig, ax = plt.subplots()
# ax.scatter(y_test, y_pred, edgecolors=(0, 0, 0))
# ax.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=4)
# ax.set_xlabel('Actual')
# ax.set_ylabel('Predicted')
# ax.set_title('Actual vs Predicted')
# st.pyplot(fig)

# # User input for prediction
# st.write("### Make a Prediction")
# with st.form(key='prediction_form'):
#     # Create input fields for each feature except the target
#     feature_inputs = {}
#     for feature in dataset.columns[:-1]:
#         feature_inputs[feature] = st.number_input(
#             f"Enter value for {feature}", value=0.0)

#     # Submit button
#     submit_button = st.form_submit_button(label='Predict')

#     if submit_button:
#         # Collect input values into a DataFrame
#         input_values = np.array([list(feature_inputs.values())])

#         # Scale the input values
#         input_values_scaled = sc_X.transform(input_values)

#         # Make prediction
#         prediction = regressor.predict(input_values_scaled)

#         # Display the prediction result
#         outcome = 'Death' if prediction[0] == 1 else 'Survival'
#         st.write(f"Predicted Outcome: {outcome}")
