import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")



st.markdown(
    """
    <style>
    .stApp {
            background-image: url('https://www.alessioferlito.it/wp-content/uploads/2022/10/leg-press-machine.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            font-family: 'Helvetica', sans-serif;
    }
    </style>
    """
    , unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

with st.container():
    st.write("---")
    st.header("LEGS WORKOUTS:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2022/07/Barbell-front-squat-to-overhead-press.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("1.HOW TO PERFORM SQUATS")
        st.write(
            """
           Squat exercise is a compound movement that targets multiple muscle groups in the lower body, including the quadriceps, hamstrings, glutes, and calves
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/YaXPRqUwItQ)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/05/Sled-45-degree-Leg-Press-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("2.HOW TO DO LEG PRESS MACHINE")
        st.write(
            """
            The leg press is a popular strength training exercise that primarily targets the muscles in the legs, including the quadriceps, hamstrings, and glutes.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/VFk3RzndUEc)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/05/lever-leg-extension-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("3.HOW TO DO LEG EXTENSIONS")
        st.write(
            """
           Leg extensions are a strength training exercise that focus primarily on the quadriceps muscles, which are located in the front of the thighs.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/swZQC689o9U)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/11/Lever-Reverse-Hyperextension-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("4.HOW TO TRAIN HAMSTRINGS")
        st.write(
            """
            Hamstring extensions, also known as hamstring curls, are a common strength-training exercise that target the hamstring muscles at the back of the thighs. 
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/vl5nUdE9mWM)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/10/Lever-Seated-Calf-Raise-plate-loaded-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("5.HOW TO PERFORM CALF RAISES")
        st.write(
            """
         Calf raises are a type of exercise that primarily target the muscles in your calves. They are commonly used to improve calf strength, muscle tone, and endurance.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/HmgXnST4Mdw)")
        
