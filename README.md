# Mediscan

**Mediscan** is an advanced machine learning-based detection system designed for disease analysis. This project integrates Support Vector Machines (SVM) and Logistic Regression to identify various diseases from medical datasets. The system aims to improve diagnostic accuracy and facilitate early disease detection.

## Features

- **Disease Detection:** 
  - Diabetes
  - Heart Disease
  - Parkinson’s Disease
- **Machine Learning Models:**
  - Support Vector Machines (SVM)
  - Logistic Regression
- **Performance:**
  - Training Accuracy: 78%
- **User Interface:**
  - Designed using Streamlit for a user-friendly experience and accurate data input.

## Technologies Used

- **Programming Language:** Python
- **Machine Learning Libraries:** Scikit-Learn
- **User Interface:** Streamlit
- **Data Processing:** Pandas, NumPy

## Installation

To set up and run Mediscan on your local machine, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/mediscan.git
   cd mediscan
2.Create a Virtual Environment:

```bash

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
3. Install Dependencies:

```bash

pip install -r requirements.txt
Run the Application:
```
```bash
streamlit run app.py
```

# Mediscan

Mediscan is a machine learning-based detection system designed for predicting the likelihood of diseases such as diabetes, heart disease, and Parkinson's disease. This application uses advanced predictive models to analyze medical data and provide insights into the health conditions of users.

## Usage

### Data Input
1. Access the Streamlit interface through your web browser.
2. Input the required medical data for the diseases you want to predict.

### Results
The system will process the input data and display the prediction results along with relevant insights.

### Example
To predict the likelihood of diabetes, heart disease, or Parkinson’s disease:
1. Enter the relevant medical data in the provided fields on the Streamlit interface.
2. Submit the data.
3. The application will output the predictions and any relevant details.

