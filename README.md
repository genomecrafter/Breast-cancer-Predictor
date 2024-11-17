# Breast Cancer Predictor

This project is a basic breast cancer prediction tool built using a decision tree classifier. The predictor utilizes key features derived from breast cancer datasets to assist in assessing potential risks.

---

## Features
- **User Inputs:**  
  Adjust the following parameters through sliders to simulate data:
  - Radius
  - Texture
  - Perimeter
  - Area
  - Smoothness
  - Compactness
  - Concavity
  - Symmetry
  - Fractal Dimension

- **Prediction Model:**  
  - A decision tree classifier is used to predict whether the person has breast cancer or not based on the input features.

---

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/genomecrafter/Breast-cancer-Predictor
   cd Breast-cancer-Predictor
   streamlit run main.py
