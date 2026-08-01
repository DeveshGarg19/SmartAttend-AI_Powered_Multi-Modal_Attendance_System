import streamlit as st
from src.screen.home_screen import home_screen
from src.screen.student_screen import student_screen
from src.screen.teacher_screen import teacher_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():
    st.markdown("""
        <style>
        [data-testid="stAlert"] {
            color: #111827 !important;
            font-weight: 600;
        }

        [data-testid="stAlert"] p {
            color: #111827 !important;
        }

        [data-testid="stAlert"] div {
            color: #111827 !important;
        }

        [data-testid="stSpinner"] p {
            color: #111827 !important;   /* Dark text */
            font-weight: 600;
            font-size: 16px;
        }

        [data-testid="stSpinner"] svg {
            stroke: #4F46E5 !important;  /* Blue spinner */
        }

        [data-testid="stAudioInput"] label {
            color: #111827 !important;
            font-weight: 600 !important;
            opacity: 1 !important;
        }

        [data-testid="stAudioInput"] p {
            color: #111827 !important;
        }
        
        </style>
        """, unsafe_allow_html=True)
    
    st.set_page_config(
        page_title='SmartAttend - Making Attendance faster using AI',
        page_icon= "https://smart-attend-beta.vercel.app/favicon.jpg"
    )

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()


    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
            
main()
