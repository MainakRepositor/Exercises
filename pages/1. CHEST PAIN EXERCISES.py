import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown(
    """
    <style>
    
    .stApp {
            background-image: url('https://png.pngtree.com/background/20230610/original/pngtree-the-gym-scene-where-people-are-sitting-in-a-gym-picture-image_3108802.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            font-family: 'Helvetica', sans-serif;
    }
    </style>
    """
    , unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.header("CHEST WORKOUTS:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/05/Barbell-Bench-Press-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("1.HOW TO BENCH PRESS FOR GROWTH")
        st.write(
            """
            The bench press is typically performed lying on a bench with a barbell or dumbbells held at chest level. The lifter then lowers the weight down to their chest, pause briefly, and then presses the weight back up to the starting position.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/4Y2ZdHCOXok)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2021/03/V1F-Dumbbell-incline-press-on-stability-ball.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("2.HOW TO DO INCLINE DUMBBELL PRESS")
        st.write(
            """
            The Incline Dumbbell Press is an exercise that primarily targets the chest muscles, specifically the upper portion of the pectoralis major muscle. It also works the front deltoids (shoulders) and triceps.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/QsYre__-aro)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/10/Decline-Barbell-Bench-Press-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("3.HOW TO DO DECLINE BARBELL PRESS")
        st.write(
            """
            TThe decline barbell press is a popular chest exercise that is often performed as part of a strength training or bodybuilding workout. This exercise specifically targets the lower portion of the chest muscles, as well as the triceps and shoulders to a lesser extent.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/LfyQBUKR8SE)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/10/cable-standing-fly-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("4.HOW TO DO CABLE CROSSOVER")
        st.write(
            """
            Cable crossover is a popular exercise in strength training that targets the chest, shoulders, and triceps. This exercise involves using a cable machine with two adjustable pulleys and cables that are attached to handles or D-handles.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/taI4XduLpTk)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/12/Machine-Fly-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("5.HOW TO DO CHEST FLY ON MACHINE")
        st.write(
            """
           The chest fly machine is a common exercise machine found in many gyms that is used to target the chest muscles. This machine is designed to help isolate and work the pectoral muscles, which are the muscles that are responsible for controlling the movement of the arms and shoulders.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/Z57CtFmRMxA)")
        
