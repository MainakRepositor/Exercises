import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")



st.markdown(
    """
    <style>
    .stApp {
            background-image: url('https://wallpaperaccess.com/full/2651448.jpg');
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
    st.header("BACK WORKOUTS:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/10/Bent-over-barbell-row.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("1.HOW TO DO BENT OVER ROW")
        st.write(
            """
            The bent-over row is a popular weightlifting exercise that targets the back muscles, primarily the lats, rhomboids, and traps. 
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FWJR5Ve8bnQ)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2017/01/Lat-pull-down-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("2.HOW TO DO LAT PULLDOWN")
        st.write(
            """
            Lat pulldown is an exercise that primarily targets the latissimus dorsi muscles, commonly known as the lats. 
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/43hWj8mfYGY)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2017/02/straight-back-seated-cable-row-resized-1.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("3.HOW TO DO SEATED ROW")
        st.write(
            """
            The seated cable row is an exercise commonly used in weight training to target the muscles in the back, shoulders, and arms.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/sP_4vybjVJs)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/05/Barbell-Deadlift-1.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("4.HOW TO PERFORM DEADLIFT")
        st.write(
            """
            The deadlift is a compound weightlifting exercise that targets multiple muscle groups, including the lower back, glutes, hamstrings, and legs.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/r4MzxtBKyNE)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://cdn-0.weighttraining.guide/wp-content/uploads/2016/10/pull-up-2-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4")
    with text_column:
        st.subheader("5.HOW TO DO PULL UPS")
        st.write(
            """
         Pull-ups are a bodyweight exercise that primarily target the muscles in the upper back and arms.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/eGo4IYlbE5g)")
        
