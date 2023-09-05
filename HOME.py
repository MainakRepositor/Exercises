import streamlit as st


def local_css(file_name):
     with open(file_name) as f:
         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style1.css")



st.markdown("""
<style>
/* Set the font size based on the screen size */
@media screen and (max-width: 768px) {
  body {
    font-size: 16px;
    color: white;
  }
}
@media screen and (min-width: 769px) and (max-width: 992px) {
  body {
    font-size: 18px;
    color: white;
  }
}
@media screen and (min-width: 993px) {
  body {
    font-size: 20px;
    color: white;
  }
  
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .title {
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
        margin-bottom: 50px;
        color: #FFFFF;
        text-transform: uppercase;
        letter-spacing: 2px;
        line-height: 1.2;
        font-family: 'Arial', sans-serif;
        border-bottom: 4px solid #FF0000;
        padding-bottom: 10px;
    
    }
    .stApp {
            background-image: url('https://t3.ftcdn.net/jpg/04/29/35/62/360_F_429356296_CVQ5LkC6Pl55kUNLqLisVKgTw9vjyif1.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            font-family: 'Helvetica', sans-serif;
    }
    </style>
    
    <h1 class="title">YOUR EXERCISE AND FITNESS BUDDY!</h1>
    """
    , unsafe_allow_html=True)

st.markdown("<p> * Welcome to our gym website! We are thrilled that you are considering joining our community of fitness enthusiasts. Our gym is a place where people come to work hard, sweat, and achieve their health and fitness goals. Whether you are a seasoned athlete or a beginner, we have something for everyone.</p>", unsafe_allow_html=True)

st.markdown("<p> * We believe that fitness is not just about physical strength, but also mental and emotional well-being. That's why we strive to create a welcoming and inclusive environment where everyone feels comfortable and supported.</p>", unsafe_allow_html=True)

st.markdown("<p>---Start exploring by selecting an option from the sidebar---</p>", unsafe_allow_html=True)

