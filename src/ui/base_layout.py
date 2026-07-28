import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 45%, #311B92 100%) !important;
                background-attachment: fixed !important;
            }
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
                background: rgba(255, 255, 255, 0.96) !important;
                backdrop-filter: blur(20px) !important;
                padding: 2.25rem !important;
                border-radius: 2.5rem !important;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(255, 255, 255, 0.6) inset !important;
                transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease !important;
            }
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:hover {
                transform: translateY(-4px) !important;
                box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(255, 255, 255, 0.9) inset !important;
            }
        </style>  
        """, unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(180deg, #F8FAFC 0%, #EEF2FF 50%, #E0E7FF 100%) !important;
                background-attachment: fixed !important;
            }
        </style>  
        """, unsafe_allow_html=True)
    
def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300..800;1,300..800&family=Outfit:wght@300;400;500;600;700;800&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top: 1.75rem !important;
                padding-bottom: 3rem !important;
                max-width: 1100px !important;
            }

            h1 {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 800 !important;
                font-size: 3.2rem !important;
                line-height: 1.15 !important;
                margin-bottom: 0.25rem !important;
                letter-spacing: -0.03em !important;
            }
                
            h2 {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 700 !important;
                font-size: 2.1rem !important;
                line-height: 1.2 !important;
                margin-bottom: 0.5rem !important;
                letter-spacing: -0.02em !important;
            }
                
            h3, h4, h5, h6 {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 600 !important;
            }

            p, label, div {
                font-family: 'Outfit', sans-serif !important;    
            }

            span:not([data-testid="stIconMaterial"]):not(.material-symbols-outlined):not(.material-icons) {
                font-family: 'Outfit', sans-serif !important;
            }

            [data-testid="stIconMaterial"], .material-symbols-outlined, .material-icons {
                font-family: 'Material Symbols Outlined', 'Google Symbols', sans-serif !important;
                font-style: normal !important;
                display: inline-block !important;
                line-height: 1 !important;
                text-transform: none !important;
                letter-spacing: normal !important;
                word-wrap: normal !important;
                white-space: nowrap !important;
                direction: ltr !important;
            }

            hr {
                margin: 1.75rem 0 !important;
                border-color: rgba(79, 70, 229, 0.15) !important;
            }

            /* --- Unified Button System --- */
            kbd, [data-testid="stShortcut"], .stShortcut {
                font-family: monospace, sans-serif !important;
                font-size: 0.7rem !important;
                padding: 1px 5px !important;
                border-radius: 5px !important;
                background: rgba(255, 255, 255, 0.25) !important;
                color: currentColor !important;
                border: 1px solid rgba(255, 255, 255, 0.3) !important;
                margin-left: 0.3rem !important;
                white-space: nowrap !important;
                display: inline-block !important;
                vertical-align: middle !important;
            }

            div[data-testid="stButton"] > button,
            button[data-testid*="stBaseButton"],
            .stButton > button {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.9rem !important;
                letter-spacing: 0.01em !important;
                border-radius: 1.25rem !important;
                padding: 0.55rem 1rem !important;
                border: none !important;
                outline: none !important;
                cursor: pointer !important;
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 0.4rem !important;
                white-space: nowrap !important;
                text-overflow: ellipsis !important;
                overflow: hidden !important;
                max-width: 100% !important;
                transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
                background: linear-gradient(135deg, #4F46E5 0%, #3B82F6 100%) !important;
                color: #FFFFFF !important;
                box-shadow: 0 4px 14px 0 rgba(79, 70, 229, 0.38) !important;
            }

            /* Primary Button Override */
            div[data-testid="stButton"] > button[kind="primary"],
            button[data-testid="stBaseButton-primary"] {
                background: linear-gradient(135deg, #4F46E5 0%, #3B82F6 100%) !important;
                color: #FFFFFF !important;
                box-shadow: 0 4px 14px 0 rgba(79, 70, 229, 0.38) !important;
            }

            /* Secondary Button Override */
            div[data-testid="stButton"] > button[kind="secondary"],
            button[data-testid="stBaseButton-secondary"] {
                background: linear-gradient(135deg, #F43F5E 0%, #E11D48 100%) !important;
                color: #FFFFFF !important;
                box-shadow: 0 4px 14px 0 rgba(244, 63, 94, 0.38) !important;
            }

            /* Tertiary / Slate Button Override */
            div[data-testid="stButton"] > button[kind="tertiary"],
            button[data-testid="stBaseButton-tertiary"] {
                background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important;
                color: #F8FAFC !important;
                box-shadow: 0 4px 14px 0 rgba(15, 23, 42, 0.25) !important;
            }

            /* Hover & Active Interactions */
            div[data-testid="stButton"] > button:hover,
            button[data-testid*="stBaseButton"]:hover {
                transform: translateY(-2px) scale(1.02) !important;
                box-shadow: 0 8px 22px 0 rgba(79, 70, 229, 0.48) !important;
            }

            div[data-testid="stButton"] > button[kind="secondary"]:hover,
            button[data-testid="stBaseButton-secondary"]:hover {
                box-shadow: 0 8px 22px 0 rgba(244, 63, 94, 0.48) !important;
            }

            div[data-testid="stButton"] > button[kind="tertiary"]:hover,
            button[data-testid="stBaseButton-tertiary"]:hover {
                box-shadow: 0 8px 20px 0 rgba(15, 23, 42, 0.35) !important;
                background: #020617 !important;
            }

            div[data-testid="stButton"] > button:active,
            button[data-testid*="stBaseButton"]:active {
                transform: translateY(0px) scale(0.98) !important;
                box-shadow: 0 2px 8px 0 rgba(79, 70, 229, 0.3) !important;
            }

            /* Disabled Button Styling */
            div[data-testid="stButton"] > button:disabled,
            button[data-testid*="stBaseButton"]:disabled {
                opacity: 0.55 !important;
                transform: none !important;
                box-shadow: none !important;
                cursor: not-allowed !important;
                background: #CBD5E1 !important;
                color: #64748B !important;
            }

            /* Custom Input and Select Box Styling */
            div[data-baseweb="input"], div[data-baseweb="select"] {
                border-radius: 0.85rem !important;
                border: 1px solid #CBD5E1 !important;
                transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
            }

            div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
                border-color: #4F46E5 !important;
                box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2) !important;
            }
        </style>  
        """, unsafe_allow_html=True)

