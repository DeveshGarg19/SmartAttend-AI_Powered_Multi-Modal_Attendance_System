import streamlit as st

from src.components.header import header_home
from src.ui.base_layout import style_background_dashboard , style_base_layout , style_background_home

def home_screen():
    # st.header("Home Screen")

    header_home()  # Call the header function from header.py
    style_base_layout()  
    style_background_home()
    # style_background_dashboard()

    col1, col2 = st.columns(2)    # make two buttons side by side
    with col1:
        st.header("I am Teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png",width=120)
        if st.button("Go to Teacher Screen",type="primary",icon=':material/open_in_new:',icon_position="right"):
            st.session_state['login_type'] = "teacher"
            st.rerun()
    with col2:
        st.header("I am Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png",width=90)
        if st.button("Go to Student Screen",type="primary",icon=':material/open_in_new:',icon_position="right"):
            st.session_state['login_type'] = "student"
            st.rerun()
