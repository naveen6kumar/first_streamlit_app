import streamlit
import pandas 
"""
streamlit.title('My Parents New Healthy Diner')
streamlit.title('Breakfast menu')

streamlit.write('Naveen is here')
streamlit.text('This is a text line Boss 🥗')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 
"""

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

