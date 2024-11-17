"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Breast Cancer Predictor")

    # Add image to the home page
    st.image("./home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Detecting breast cancer early can make a significant difference in treatment outcomes. This tool provides a simple yet effective prediction model using key features like radius, texture, perimeter, area, smoothness, compactness, concavity, symmetry, and fractal dimension. By adjusting these parameters, users can receive insights based on a decision tree classifier to aid in assessing potential risks. While not a substitute for medical advice, this predictor aims to offer preliminary guidance for further evaluation.
        </p>
    """, unsafe_allow_html=True)

    