# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
streamlit.title(f" My Parents New Healthy Diner ")
streamlit.write(
  """Breakfast Menu
  """
)


streamlit.write('Omega 3 & Blueberry Oatmeal')
streamlit.write('Kale, Spinach & Rocket Smoothie')
streamlit.write('Hard-Boiled Free-Range Egg')

cnx = st.connection("Snowflake")
session = cnx.session()







    
   
    
