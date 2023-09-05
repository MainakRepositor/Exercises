import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown(
    """
    <style>
    .stApp {
            background-image: url('https://images.pexels.com/photos/17093368/pexels-photo-17093368/free-photo-of-barbell-dumbbells-triceps-rope-and-clamps-on-the-floor-at-the-gym-top-down-view-flat-lay-with-bodybuilding-equipment-on-a-black-background-and-empty-space-for-text-fitness-weight-trai.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');
            background-size: cover;
            background-repeat: no-repeat;
            font-family: 'Helvetica', sans-serif;
    }
    </style>
    """
    , unsafe_allow_html=True)


# Set page background color and font
st.markdown(
    """
    <style>
    body {
        background-color: #f2f2f2;
        font-family: Arial, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define the fat percentage calculation function
def calculate_fat_percentage(sex: str, waist: float, neck: float, height: float) -> float:
    if sex == "Male":
        fat_percentage = 495 / (1.0324 - 0.19077 * (float((waist))) + 0.15456 * (float((height))) - 450)
    else:
        fat_percentage = 495 / (1.29579 - 0.35004 * (float((waist) + (float((hip))) - float((neck)))) + 0.22100 * (float((height))) - 450)
    return round(fat_percentage, 2)

# Create the app interface
st.title("FAT PERCENTAGE CALCULATOR:")

sex = st.selectbox("Select your sex", options=["Male", "Female"])
waist = st.number_input("Enter your waist circumference (in cm)", min_value=1.0, max_value=200.0, step=0.1)
if sex == "Female":
    hip = st.number_input("Enter your hip circumference (in cm)", min_value=1.0, max_value=200.0, step=0.1)
neck = st.number_input("Enter your neck circumference (in cm)", min_value=1.0, max_value=200.0, step=0.1)
height = st.number_input("Enter your height (in cm)", min_value=1.0, max_value=300.0, step=0.1)

if st.button("Calculate Fat Percentage"):
    fat_percentage = calculate_fat_percentage(sex, waist, neck, height)
    st.success(f"Your fat percentage is {fat_percentage}%")

    if fat_percentage < 20:
        st.warning("You have a healthy level of body fat")
    elif fat_percentage >= 20 and fat_percentage < 30:
        st.success("You have an acceptable level of body fat")
    elif fat_percentage >= 30 and fat_percentage < 40:
        st.warning("You have an elevated level of body fat")
    else:
        st.error("You have a high level of body fat")
