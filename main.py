# Importing necessary libraries
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import joblib

# Function to display project information
def display_project_info():

    st.title('Industrial Copper Modeling')
    st.subheader('Technologies used:')
    streamlit_list = "1. Streamlit\n2. Pandas\n3. Data Wrangling\n4. Machine Learning"
    st.write(streamlit_list)
    st.subheader('Domain:')
    st.write('Manufacturing')
    st.subheader('About:')
    st.write('''This project aims to analyze a dataset from the copper industry. 
             The dataset has been cleaned of null values, outliers have been removed, 
             skewed distributions have been transformed, feature engineering has been performed, 
             and both regression and classification models have been used to predict various target variables.''')
    
# Function to create input columns
def create_input_columns(column, input_labels):

    with column:
        st.subheader('Enter the Values:')
        inputs = [st.text_input(label, 0) for label in input_labels]
    return inputs

# Function to predict results using the loaded model
def predict_results(loaded_model, input_data):

    try:
        results = loaded_model.predict([input_data])
        st.success(f'Predicted Result: {results[0]}')
    except Exception as e:
        st.error(f'Error predicting: {e}')

# Function to run regression model  
def run_regression(df, loaded_model):

    st.dataframe(df)
    col1,col2,col3,col4 = st.columns(4)

    input_labels = [
        'Quantity_Tons', 'Country', 'Status',
        'Application', 'Thickness', 'Width', 'Material_Ref',
        'Purchased_Month', 'Purchased_Year',
        'Delivered_Month', 'Delivered_Year',
        'Item_Type_PL', 'Item_Type_S', 'Item_Type_W'
    ]

    inputs = create_input_columns(col1, input_labels)

    if st.button('Submit'):
        input_data = [value for value in inputs]
        predict_results(loaded_model, input_data)

# Function to run classification model
def run_classification(df, loaded_model):

    st.dataframe(df)
    col1,col2,col3,col4 = st.columns(4)

    input_labels = [
        'Quantity_Tons', 'Country',
        'Application', 'Thickness', 'Width', 'Material_Ref',
        'Selling_price','Purchased_Month', 'Purchased_Year',
        'Delivered_Month', 'Delivered_Year',
        'Item_Type_PL', 'Item_Type_S', 'Item_Type_W'
    ]
    
    inputs = create_input_columns(col1, input_labels)

    if st.button('Submit'):
        input_data = [value for value in inputs]
        predict_results(loaded_model, input_data)

# Main function
def main():
    # Load the data from CSV file
    df = pd.read_csv(r'Copper_Cleaned.csv')

    # Load the Models
    loaded_regression_model = joblib.load('regression_model.joblib')
    loaded_classification_model = joblib.load('classification_model.joblib')

    # Sidebar menu options
    with st.sidebar:
        options = option_menu('Menu',['Home','ML Prediction'])

    if options == 'Home':
        display_project_info()

    if options == 'ML Prediction':
        st.subheader('Model Type:')
        selected_type = st.selectbox('Select a Model Type:',('Regression','Classification'))

        if selected_type == 'Regression':
            run_regression(df, loaded_regression_model)
        elif selected_type == 'Classification':
            run_classification(df, loaded_classification_model)


# Call the main function
if __name__ == '__main__':
    main()