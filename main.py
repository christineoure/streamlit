import streamlit as st
import pandas as pd
import numpy as np
import time

from streamlit import progress

st.title("Weather Forecasting App")

st.header("Header")

st.subheader("This is a subheader")

st.write("Hello world")

st.caption("This is an example of a caption")

st.code("""
import streamlit as st
st.title("Weather Forecasting App")
st.header("Header")
st.subheader("This is a subheader")
st.write("Hello world")
st.caption("This is an example of a caption")
""")

with st.echo():
    st.write("This code will be printed")

st.divider()

df = pd.read_csv("data/football_data.csv")
st.dataframe(df.head())

edited_df = st.data_editor(df, num_rows="dynamic")

st.dataframe(edited_df)

# st.table(df)

st.metric("Rainfall", 1000, 200)

if st.button("Submit"):
    st.write(f"The button has been clicked!")

stars = st.feedback("stars")
if stars:
    stars += 1
    if stars == 1 or stars == 2:
        st.write("Poor reviews")
    elif stars == 3:
        st.write("Average product")
    elif stars == 4 or stars == 5:
        st.write("Awesome reviews")

check = st.checkbox("I agree")

if check:
    st.write("The user has accepted")

st.toggle("Activate")

# categorical inputs
st.radio("Select your gender ", ["Male", "Female"])

st.selectbox("Select a soda", ["Fanta Orange", "Sprite", "Coke", "Stoney"])

st.multiselect("Buy", ["Milk", "Eggs", "Bread", "Coffee"])

st.select_slider("Pick a size", ["XS", "S", "M", "L", "XL", "XXL", "XXXL"])

# number inputs
st.number_input("Pick a number", -10, 10 )

age = st.slider("Select your age", 18, 100)

# date and time inputs
st.date_input("Select the date of your appointment")

st.time_input("Select the preferred time")

# text inputs

username = st.text_input("Enter your name")
if username:
    st.write(f"Welcome {username}!")

st.text_area("Write a paragraph on why you need the scholarship", height=200)

uploaded_file = st.file_uploader("Upload your dataset here")
if uploaded_file:
    st.write(uploaded_file)

st.camera_input("Take a photo now")

st.image("data/11 Burger Chains with the Highest Quality Meat in America.jpeg")

# columns
col1, col2, col3 = st.columns(3)

with col1:
    st.toggle("Toggle")

with col2:
    st.image("data/11 Burger Chains with the Highest Quality Meat in America.jpeg")


with col3:
    st.metric("Temperate", 24, 1)

@st.dialog("Form")
def modal():
    st.text_input("Enter your name here")
    st.text_input("Enter your email here")
    if st.button("Submit Form"):
        st.write("Form has been submitted")

my_modal = st.selectbox("Do you want a modal? ", ["No", "Yes"])
if my_modal == "Yes":
    modal()

with st.expander("Click to view more info"):
    st.write("More information will be displayed here")
    st.write("More information will be displayed here")
    st.write("More information will be displayed here")
    st.write("More information will be displayed here")

with st.popover("Settings"):
    st.checkbox("Use Dark Mode")

with st.sidebar:
    st.write("This is in sidebar")
    st.button("Sidebar button")

# with st.spinner("Running"):
#     time.sleep(5)
#     st.write("Task complete")

# progress bar
# for i in range(100):
#     st.progress(i)
#     time.sleep(0.5)
my_bar_trigger = st.selectbox("Do you want a progress bar?", ["No", "Yes"])
if my_bar_trigger == "Yes":
    my_bar = st.progress(0, text="Operation in progress")

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text="Operation in progress")
    time.sleep(1)
    my_bar.empty()

# st.toast("Cheers!", icon= "flag-ke")

# st.balloons()

# callout messages

st.success("Thank you!")
st.info("Stay Safe!")
st.warning("Stay Safe!")
# st.error("Failed to authenticate!")
# st.exception("This is an exception")

st.write("I am a Kenyan :flag-ke:")



