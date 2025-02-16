# import library
import streamlit as st
import numpy as np
import pandas as pd
import pickle

#Judul Utama
st.title('Deposit Rate Predictor')
st.text('This web can be used to predict your survival rate')



# Menambahkan sidebar
st.sidebar.header("Please input your features")

def create_user_input():
    
    # Numerical Features
    age = st.sidebar.slider('age', min_value=18, max_value=95, value=25)
    balance = st.sidebar.number_input('balance', min_value=-6847, max_value=37127, value=1000)
    campaign = st.sidebar.slider('campaign', min_value=1, max_value=33, value=2)
    pdays = st.sidebar.slider('pdays', min_value=-1, max_value=828, value=100)

    # Categorical Features
    job = st.sidebar.selectbox('job', ['blue-collar', 'technician', 'student', 'retired', 'admin', 'housemaid', 'services', 'unemployed', 'management', 'entrepreneur', 'self-employed'])
    housing = st.sidebar.radio('housing', ['yes', 'no'])
    loan = st.sidebar.radio('loan', ['yes', 'no'])
    contact = st.sidebar.radio('contact', ['cellular', 'telephone'])
    month = st.sidebar.selectbox('month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
    poutcome = st.sidebar.selectbox('poutcome', ['unknown', 'success', 'other', 'failure'])

    # Creating a dictionary with user input
    user_data = {
        'age': age,
        'balance': balance,
        'campaign': campaign,
        'pdays': pdays,
        'job': job,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'month': month,
        'poutcome': poutcome
    }
    
    # Convert the dictionary into a pandas DataFrame (for a single row)
    user_data_df = pd.DataFrame([user_data])
    
    return user_data_df
# Get customer data
data_customer = create_user_input()

# Membuat 2 kontainer
col1, col2 = st.columns(2)

# Kiri
with col1:
    st.subheader("Customer's Features")
    st.write(data_customer.transpose())

# Load model
with open(r'Bank_marketing.sav', 'rb') as f:
    model_loaded = pickle.load(f)
    
# Predict to data
kelas = model_loaded.predict(data_customer)
probability = model_loaded.predict_proba(data_customer)[0]  # Get the probabilities

# Menampilkan hasil prediksi

# Bagian kanan (col2)
with col2:
    st.subheader('Prediction Result')
    if probability[1] > .39:
        st.write('This Customer will deposit')
    else:
        st.write('This Customer will not deposit')
    
    # Displaying the probability of the customer buying
    st.write(f"Probability of Deposit: {probability[1]:.2f}")  # Probability of class 1 (BUY)
