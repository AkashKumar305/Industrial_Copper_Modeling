# Industrial_Copper_Modeling

## Overview

This project addresses challenges in the copper industry related to sales and lead classification. The dataset undergoes preprocessing, including handling skewness, outliers, and cleaning. Two machine learning models are implemented: a regression model predicting 'Selling_Price' and a classification model predicting 'Status' (WON or LOST). A Streamlit GUI is created for user interaction, allowing input of values for prediction.

## Problem Statement

The copper industry faces issues with manual predictions due to skewed and noisy data. A regression model is implemented to predict 'Selling_Price', and a classification model predicts 'Status' (WON/LOST). The project involves data exploration, preprocessing, EDA, feature engineering, model building, and evaluation.

## Project Workflow Execution

1. **Data Understanding:**
   - Identify variable types and distributions.
   - Treat 'Material_Reference' values starting with '00000' as null.
   - Treat reference columns as categorical variables.
   - Remove the 'ID' column as it may not be useful.

2. **Data Preprocessing:**
   - Treat outliers using IQR.
   - Identify and treat skewness using log transformation or other techniques.
   - Encode categorical variables using suitable techniques.

3. **EDA (Exploratory Data Analysis):**
   - Visualize outliers and skewness using Seaborn's plots.
   - Use boxplot, distplot, and violinplot for visualization.

4. **Feature Engineering:**
   - Create new features if applicable.
   - Drop highly correlated columns using a heatmap.

5. **Model Building and Evaluation:**
   - Split the dataset into training and testing sets.
   - Train and evaluate regression and classification models.
   - Use metrics like accuracy, precision, recall, F1 score, and AUC curve.
   - Optimize model hyperparameters using cross-validation and grid search.

6. **Model GUI (Streamlit):**
   - Create an interactive page with task input (Regression or Classification).
   - Enter values for each column except 'Selling_Price' for regression and 'Status' for classification.
   - Predict new data from Streamlit and display the output.
  
LinkedIn Profile
Link: www.linkedin.com/in/akashkumarl Visit the link to see the project video

## Project Structure

- `main.py`: Main Python script containing the Streamlit application.
- `Copper_Cleaned.csv`: Cleaned dataset used for modeling.
- `regression_model.joblib`: Joblib file containing the trained regression model.
- `classification_model.joblib`: Joblib file containing the trained classification model.
- `Copper_Set.xlsx`: Original dataset used for preprocessing.
- `Data Preprocessing.ipynb`: Data Preprocessing steps performed in a notebook.
- `Model Building - Regression or Classification`: Model Building steps performed for finding best model.

## Usage

1. Install required libraries: `pip install streamlit pandas scikit-learn joblib`.
2. Run the Streamlit application: `streamlit run main.py`.
3. Choose between 'Home' and 'ML Prediction' in the sidebar.
4. For 'ML Prediction,' select the model type (Regression or Classification).
5. Input values in the Streamlit GUI and click 'Submit' for predictions.

## Technologies Used

- Streamlit
- Pandas
- Scikit-Learn
- Seaborn
- Data Wrangling

Feel free to contribute, report issues, or suggest improvements!
