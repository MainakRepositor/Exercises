import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")



st.markdown(
    """
    <style>
    .stApp {
            background-image: url('https://steelsupplements.com/cdn/shop/articles/shutterstock_533450440_1000x.jpg?v=1636306006');
            background-size: cover;
            background-repeat: no-repeat;
            font-family: 'Helvetica', sans-serif;
            
    }
    
    [data-theme="dark"] {
  color: #000000; /* Set text color to black */
  background-color: #000000; /* Set background color to black */
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
    st.header("SHOULDER WORKOUTS:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/05/Dumbbell-Shoulder-Press-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("1.HOW TO DO DUMBBELL SHOULDER PRESS")
        st.write(
            """
            The shoulder dumbbell press is an exercise that targets the shoulders (deltoids) and is often used in strength training and bodybuilding routines.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/qEwKCR5JCog)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/05/dumbbell-lateral-raise-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("2.HOW TO PERFORM LATERAL RAISES")
        st.write(
            """
           Lateral raises, also known as side raises, are a strength training exercise that primarily targets the lateral head of the shoulder (deltoid) muscle
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/WJm9zA2NY8E)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/12/seated-bent-over-lateral-raise-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("3.HOW TO USE REAR DELT M/C")
        st.write(
            """
          The rear delt fly machine is a piece of strength training equipment that targets the rear deltoid muscles, which are located at the back of the shoulders. 
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/6yMdhi2DVao)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/10/Face-pull-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("4.HOW TO DO CABLE FACE PULL")
        st.write(
            """
            The face pull is an exercise that targets the upper back, shoulders, and rotator cuff muscles. 
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/rep-qVOkqgk)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/10/dumbbell-shrug-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("5.HOW TO DO DUMBBELL SHRUGS")
        st.write(
            """
           hrugs are a type of exercise that primarily targets the trapezius muscles, which are located in the upper back and neck area.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/cJRVVxmytaM)")
        
