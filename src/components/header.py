import streamlit as st

def header_home():
    logo_url = "https://smart-attend-beta.vercel.app/favicon.jpg"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom: 2rem; margin-top: 1rem;">
            <img src='{logo_url}' style='height:110px; border-radius:22px; box-shadow: 0 12px 25px rgba(0,0,0,0.35); transition: transform 0.3s ease;' />
            <h1 style='text-align:center; color:#FFFFFF; margin-top:0.85rem; text-shadow: 0 4px 14px rgba(0,0,0,0.3); letter-spacing: -0.02em;'>SMART<br/>ATTEND</h1>
        </div>   
        """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://smart-attend-beta.vercel.app/favicon.jpg"
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:flex-start; gap:14px; margin-bottom: 0.5rem;">
            <img src='{logo_url}' style='height:70px; border-radius:16px; box-shadow: 0 6px 16px rgba(79,70,229,0.25);' />
            <h2 style='text-align:left; color:#4F46E5; margin:0; line-height:1.0;'>SMART<br/>ATTEND</h2>
        </div>   
        """, unsafe_allow_html=True)


