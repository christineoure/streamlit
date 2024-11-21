# import streamlit as st
# import pandas as pd
# import numpy as np
# import time
# st.title("Weather Forecasting App")
#
# st.header("Weather Forecasting App")
#
# st.subheader("App status here")
#
# st.write("Hello World!")
#
# st.caption("Hello World!")
#
# st.code("age = 28")
# st.code("""
# The Swahili word "sera" means "policy" or "strategy" in English.
# It often refers to a set of ideas, plans, or a course of action
# adopted or proposed by an organization, government, or individual
# to achieve certain goals or to guide decision-making and actions.
# """)
#
# with st.echo(""):
#     st.write("This code will be printed")
#
# st.divider()
#
# df = pd.read_csv("data/football_data.csv")
# st.dataframe(df)
# st.dataframe(df.describe())
# st.dataframe(df.head())
# edited_df = st.data_editor(df, num_rows= "dynamic")
#
# st.dataframe(edited_df)
# # st.table(edited_df)
#
#
#
# st.metric("Temperature", 25, 2)
# st.metric("Rainfall", 1225, 200)
#
# if st.button("Submit"):
#     st.write("Submitted Successfully!")
#
# st.feedback()
# stars = st.feedback("stars")
# if stars:
#     st.write(stars + 1)
#
# # st.metric("Rainfall", 1000, 200)
#
# st.button()
# if st.button("Submit"):
#     st.write(f"The button has been clicked!")
#
# stars = st.feedback("stars")
# if stars:
#     stars += 1
#     if stars == 1 or stars == 2:
#         st.write("Poor reviews")
#     elif stars == 3:
#         st.write("Average product")
#     elif stars == 4 or stars == 5:
#         st.write("Awesome reviews")
#
# check = st.checkbox("I agree")
#
# if check:
#     st.write("The user has accepted")
#
# st.toggle("Activate")
#
# # categorical inputs
# st.radio("Select your gender ", ["Male", "Female"])
#
# st.selectbox("Select a soda", ["Fanta Orange", "Sprite", "Coke", "Stoney"])
#
# st.multiselect("Buy", ["Milk", "Eggs", "Bread", "Coffee"])
#
# st.select_slider("Pick a size", ["XS", "S", "M", "L", "XL", "XXL", "XXXL"])
#
# # number inputs
# st.number_input("Pick a number", -10, 10 )
#
# age = st.slider("Select your age", 18, 100)
#
# # date and time inputs
# st.date_input("Select the date of your appointment")
#
# st.time_input("Select the preferred time")
#
# # text inputs
#
# username = st.text_input("Enter your name")
# if username:
#     st.write(f"Welcome {username}!")
#
# st.text_area("Write a paragraph on why you need the scholarship", height=200)
#
# uploaded_file = st.file_uploader("Upload your dataset here")
# if uploaded_file:
#     st.write(uploaded_file)
#
# # st.camera_input("Take a photo now")
#
# st.image("data/nissanFuga.png")
#
# # columns
# col1, col2, col3 = st.columns(3)
#
# with col1:
#     st.toggle("Toggle")
#
# with col2:
#     st.image("data/nissanFuga.png")
#
#
# with col3:
#     st.metric("Temperate", 24, 1)
#
# # @st.dialog("Form")
# # def modal():
# #     st.text_input("Enter your name here")
# #     st.text_input("Enter your email here")
# #     if st.button("Submit Form"):
# #         st.write("Form has been submitted")
# #
# # modal()
#
# with st.expander("Click to view more info"):
#     st.write("More information will be displayed here")
#     st.write("More information will be displayed here")
#     st.write("More information will be displayed here")
#     st.write("More information will be displayed here")
#
# with st.popover("Settings"):
#     st.checkbox("Use Dark Mode")
#
# with st.sidebar:
#     st.write("This is in sidebar")
#     st.button("Sidebar button")
#
# # with st.spinner("Running"):
# #     time.sleep(5)
# #     st.write("Task complete")
#
# # progress bar
# # for i in range(100):
# #     st.progress(i)
# #     time.sleep(0.5)
#
# # my_bar = st.progress(0, text="Operation in progress")
# #
# # for percent_complete in range(100):
# #     time.sleep(0.1)
# #     my_bar.progress(percent_complete + 1, text="Operation in progress")
# # time.sleep(1)
# # my_bar.empty()
#
# # st.toast("Cheers!", icon=)