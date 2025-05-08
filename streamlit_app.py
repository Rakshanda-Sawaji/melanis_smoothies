# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
streamlit.title(f" My Parents New Healthy Diner ")
streamlit.write(
  """Breakfast Menu
  """
)

#name_on_order =st.text_input('Name on Smoothie:')
streamlit.write('Omega 3 & Blueberry Oatmeal')
streamlit.write('Kale, Spinach & Rocket Smoothie')
streamlit.write('Hard-Boiled Free-Range Egg')

cnx = st.connection("Snowflake")
session = cnx.session()

#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))




    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""
    time_to_insert = st.button('Submit Order')

#st.write(my_insert_stmt)
    
   
    
