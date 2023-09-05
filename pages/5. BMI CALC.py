import streamlit as st
from PIL import Image

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown(
    """
    <style>
    .stApp {
            background-image: url('https://images.pexels.com/photos/3253500/pexels-photo-3253500.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');
            background-size: cover;
            background-repeat: no-repeat;
            font-family: 'Helvetica', sans-serif;
    }
    </style>
    """
    , unsafe_allow_html=True)



# Define CSS style
CSS = """
h1 {
    color: #FFFFF;
    font-size: 40px;
    margin-bottom: 50px;
}
label {
    font-size: 20px;
}
"""

# Render HTML with CSS style
st.markdown(f'<style>{CSS}</style>', unsafe_allow_html=True)
st.markdown("<h1>BMI CALCULATOR:</h1>", unsafe_allow_html=True)

# Collect user input
weight = st.number_input("Enter your weight (in kilograms):", min_value=1)
height_feet = st.number_input("Enter your height (in feet):", min_value=1)
height_inches = st.number_input("Enter your height (in inches):", min_value=0, max_value=11)

# Convert height to meters
height_total_inches = (height_feet * 12) + height_inches
height_meters = height_total_inches * 0.0254

# Calculate BMI
if weight and height_meters:
    bmi = round(weight / (height_meters ** 2), 1)
    st.write("Your BMI is:", bmi)
    if bmi < 18.5:
        st.write("You are underweight.")
    elif bmi >= 18.5 and bmi <= 24.9:
        st.write("You are at a healthy weight.")
    elif bmi >= 25 and bmi <= 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
else:
    st.warning("Please enter your weight and height.")
