import streamlit

streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🥞Kale, Spinach & Rocket Smoothie')
streamlit.text('🥘Hard-Boiled Free-Range Egg')
streamlit.text('🥪🥑Avocado Toast')

streamlit.header('🍑🍒Build Your Own Fruit Smoothie🍉🍊')

import pandas as pd

My_Fruit_List = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#let's put a picklist here so that customers can select the fruit they want to include in their smoothie
streamlit.multiselect("Pick your choice of Fruit:", list(My_Fruit_List.index))

streamlit.dataframe(My_Fruit_List)
