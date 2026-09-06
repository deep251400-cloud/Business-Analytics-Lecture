# First, install Streamlit
!pip install streamlit

import streamlit as st
import joblib
import pandas as pd

# Load the trained model
loaded_lr_model = joblib.load('lr.sav')

st.title('Sales Prediction App')
st.write('Enter the advertising budgets to predict sales.')

# Create input fields
tv = st.slider('TV Advertising Budget ($)', 0.0, 300.0, 150.0)
radio = st.slider('Radio Advertising Budget ($)', 0.0, 50.0, 25.0)
newspaper = st.slider('Newspaper Advertising Budget ($)', 0.0, 100.0, 50.0)

# Predict button
if st.button('Predict Sales'):
    # Create a DataFrame for prediction
    input_data = pd.DataFrame([{
        'TV': tv,
        'Radio': radio,
        'Newspaper': newspaper
    }])

    # Make prediction
    prediction = loaded_lr_model.predict(input_data)[0]

    st.success(f'Predicted Sales: {prediction:.2f}')
