import numpy as np
import pickle
import streamlit as st
from PIL import Image
import pandas as pd
# loading the saved model
loaded_model = pickle.load(open(r'T:/Project_file/Model_Kmeans_new','rb'))
df=pd.read_csv("T:/Project_file/Cluster_world_Development_data.csv")
def Cluster_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Developing Country'
    elif (prediction[0] == 1):
      return 'Developed Country'
    else:
      return 'Under Developed Country'  


def main():

    # giving a title
    st.title('Cluster Prediction')
    
    # getting the input data from the user
    Birth_Rate = st.text_input('Enter birth rate')
    Business_Tax_Rate = st.text_input('Enter tax Percentage')
    CO2_Emissions = st.text_input('CO2_Emissions')
    Days_to_Start_Business = st.text_input('Enter Number of days to start business')
    Ease_of_Business = st.text_input('Ease_of_Business')
    Energy_Usage = st.text_input('Total Energy Usage')
    GDP = st.text_input('Total GDP')
    Health_Exp_Per_GDP =st.text_input('Enter HEP GDP')
    Health_Exp_Capita = st.text_input('Total Health expenditure')
    Hours_to_do_Tax = st.text_input('Hours_to_do_Tax')
    Infant_Mortality_Rate = st.text_input('Infant_Mortality_Rate in Percentage')
    Internet_Usage = st.text_input('Average Internet_Usage')
    Lending_Interest = st.text_input('Lending_Interest')
    Life_Expectancy_Female = st.text_input('Life_Expectancy_Female')
    Life_Expectancy_Male = st.text_input('Life_Expectancy_Male')
    Mobile_Phone_Usage = st.text_input('Mobile_Phone_Usage')
    Population_0_14 = st.text_input('Total population between 0-14 in percentage')
    Population_15_64 = st.text_input('Total population between 15-64 in percentage')
    Population_65_and_above = st.text_input('Total population above 65 in percentage')
    Population_Total = st.text_input('Total population')
    Population_Urban = st.text_input('Urban population in percentage')
    Tourism_Inbound = st.text_input('$ earned in tourism')
    Tourism_Outbound = st.text_input('$ spent on tourism')
    
    # code for Prediction
    Predict = ''
    
    # creating a button for Prediction
    
    if st.button('Submit'):
        Predict = Cluster_prediction([Birth_Rate,Business_Tax_Rate,CO2_Emissions,Days_to_Start_Business, Ease_of_Business, Energy_Usage, GDP,Health_Exp_Per_GDP,Health_Exp_Capita, Hours_to_do_Tax,Infant_Mortality_Rate, Internet_Usage, Lending_Interest,Life_Expectancy_Female, Life_Expectancy_Male, Mobile_Phone_Usage, Population_0_14, Population_15_64,Population_65_and_above, Population_Total, Population_Urban,Tourism_Inbound, Tourism_Outbound])

    st.success(Predict)
    
if __name__ == '__main__':
    main()

