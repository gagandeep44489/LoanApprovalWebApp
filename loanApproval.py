# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import joblib 
import os

def main():
    html_temp = """<div style="background-color: #f6f6f6; padding: 20px;">
    <h2 style="color: green; text-align: center;">Loan Approval Prediction</h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Ensure the correct path and model file name
    model_path = r'E:\GreekforGreeksProject\GreekforGreeksProject\model_joblib_rfc'
    try:
        model = joblib.load(model_path)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    # Collect user input
    s1 = st.selectbox("Gender", ("Male", "Female"))
    p1 = 1 if s1 == "Male" else 0
    
    s2 = st.selectbox("Married", ("No", "Yes"))
    p2 = 1 if s2 == "Yes" else 0
    
    p3 = st.number_input("Enter Your Dependents", min_value=0, max_value=10, step=1)
    
    s3 = st.selectbox("Education", ("Graduate", "Not Graduate"))
    p4 = 1 if s3 == "Graduate" else 0
    
    s4 = st.selectbox("Self Employed", ("No", "Yes"))
    p5 = 1 if s4 == "Yes" else 0
    
    p6 = st.number_input("Enter Your Applicant Income", min_value=0)
    p7 = st.number_input("Enter Your Coapplicant Income", min_value=0)
    p8 = st.number_input("Enter Your Loan Amount", min_value=0)
    p9 = st.number_input("Enter Your Loan Amount Term", min_value=0)
    p10 = st.number_input("Enter Your Credit History (0 or 1)", min_value=0, max_value=1)
    
    s5 = st.selectbox("Property Area", ("Urban", "Rural", "Semiurban"))
    if s5 == "Urban":
        p11 = 1
    elif s5 == "Rural":
        p11 = 0
    else:
        p11 = 2  # Assuming 2 for Semiurban
    
    # Predict button
    if st.button('Predict'):
        try:
            prediction = model.predict([[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]])
            st.balloons()
            if prediction[0] == 1:
                st.success('Loan Approved')
            else:
                st.warning('Loan Not Approved')
        except Exception as e:
            st.error(f"Error during prediction: {e}")
    
if __name__ == '__main__':
    main()
