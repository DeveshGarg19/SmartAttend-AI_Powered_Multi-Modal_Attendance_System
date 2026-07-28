import streamlit as st
import pandas as pd
from src.database.db import get_enrolled_students, unenroll_student_to_subject
import time

def _confirm_remove_cb(confirm_key, value):
    st.session_state[confirm_key] = value

def _do_unenroll_cb(student_id, subject_id, confirm_key, student_name):
    unenroll_student_to_subject(student_id, subject_id)
    st.session_state[confirm_key] = False
    st.toast(f"Removed {student_name} from course!", icon="🗑️")

@st.dialog("Enrolled Students", width="large")
def enrolled_students_dialog(subject_id, subject_name, subject_code):
    st.markdown(f"<h3 style='margin:0; color: #F8FAFC;'>{subject_name} <span style='font-size:1rem; color:#818CF8;'>({subject_code})</span></h3>", unsafe_allow_html=True)
    
    enrolled_nodes = get_enrolled_students(subject_id)
    
    if not enrolled_nodes:
        st.info("No students enrolled in this subject yet.")
        return
    
    students = [node['students'] for node in enrolled_nodes if node.get('students')]
    students = sorted(students, key=lambda s: s['name'].lower())
    
    st.markdown(f"<p style='color: #94A3B8; margin-bottom: 0.75rem;'>Total Enrolled Students: <b style='color: #F8FAFC;'>{len(students)}</b></p>", unsafe_allow_html=True)
    
    search_query = st.text_input("Filter student", placeholder="Search by name or ID...", key=f"dialog_search_{subject_id}")

    filtered_students = students
    if search_query:
        query = search_query.lower()
        filtered_students = [
            s for s in students 
            if query in s['name'].lower() or query in str(s['student_id'])
        ]

    st.divider()

    if not filtered_students:
        st.warning("No students match your filter.")
        return

    for s in filtered_students:
        s_id = s['student_id']
        confirm_key = f"confirm_remove_{subject_id}_{s_id}"

        c_info, c_face, c_voice, c_action = st.columns([2.5, 1.2, 1.2, 1], vertical_alignment="center")
        
        with c_info:
            st.markdown(f"<div style='font-weight: 600; color: #F8FAFC;'>{s['name']} <span style='color: #CBD5E1; font-weight: normal;'>(ID: {s_id})</span></div>", unsafe_allow_html=True)
        
        with c_face:
            face_status = "✅ Registered" if s.get('face_embedding') else "❌ Missing"
            st.markdown(f"<div style='font-size: 0.85rem; color: #CBD5E1;'>Face: <b>{face_status}</b></div>", unsafe_allow_html=True)
        
        with c_voice:
            voice_status = "✅ Registered" if s.get('voice_embedding') else "❌ Missing"
            st.markdown(f"<div style='font-size: 0.85rem; color: #CBD5E1;'>Voice: <b>{voice_status}</b></div>", unsafe_allow_html=True)
        
        with c_action:
            if not st.session_state.get(confirm_key):
                st.button(
                    "Remove",
                    key=f"dialog_remove_{subject_id}_{s_id}",
                    icon=":material/person_remove:",
                    type="tertiary",
                    use_container_width=True,
                    on_click=_confirm_remove_cb,
                    args=(confirm_key, True)
                )

        if st.session_state.get(confirm_key):
            st.markdown(f"<div style='background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.4); padding: 0.5rem 0.75rem; border-radius: 8px; margin: 4px 0 8px 0;'><span style='color: #F8FAFC; font-size: 0.9rem;'>Confirm removal of <b>{s['name']}</b> from this course?</span></div>", unsafe_allow_html=True)
            c_yes, c_no, _ = st.columns([1.2, 1.2, 2.6])
            with c_yes:
                st.button(
                    "Yes, Remove",
                    key=f"btn_confirm_yes_{subject_id}_{s_id}",
                    type="primary",
                    use_container_width=True,
                    on_click=_do_unenroll_cb,
                    args=(s_id, subject_id, confirm_key, s['name'])
                )
            with c_no:
                st.button(
                    "Cancel",
                    key=f"btn_confirm_no_{subject_id}_{s_id}",
                    type="secondary",
                    use_container_width=True,
                    on_click=_confirm_remove_cb,
                    args=(confirm_key, False)
                )
