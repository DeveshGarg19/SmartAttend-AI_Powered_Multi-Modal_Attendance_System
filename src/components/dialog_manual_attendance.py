import streamlit as st
from datetime import datetime
from src.database.db import get_enrolled_students, create_attendance
import time

@st.dialog("Mark Manual Attendance")
def manual_attendance_dialog(subject_id, subject_name):
    st.markdown(f"<p style='color: #94A3B8; font-size: 0.95rem; margin-bottom: 1rem;'>Marking manual attendance for <b style='color: #818CF8;'>{subject_name}</b></p>", unsafe_allow_html=True)
    
    enrolled_nodes = get_enrolled_students(subject_id)
    if not enrolled_nodes:
        st.warning("No students enrolled in this subject yet.")
        if st.button("Close", key=f"close_empty_manual_{subject_id}"):
            st.session_state.pop("active_manual_dialog", None)
            st.rerun()
        return

    students = [node['students'] for node in enrolled_nodes if node.get('students')]
    students = sorted(students, key=lambda s: s['name'].lower())

    if "attendance_time" not in st.session_state:
        st.session_state.attendance_time = datetime.now().time()
    attendance_date = st.date_input("Attendance Date", value=datetime.now().date(), max_value=datetime.today())
    attendance_time = st.time_input("Attendance Time", key="attendance_time")
    
    dt_str = datetime.combine(attendance_date, attendance_time).strftime("%Y-%m-%dT%H:%M:%S")

    st.write("")
    st.markdown("<h4 style='color: #F8FAFC; margin-bottom: 0.5rem; font-weight: 600;'>Student Attendance Status</h4>", unsafe_allow_html=True)

    for s in students:
        t_key = f"manual_toggle_{subject_id}_{s['student_id']}"
        if t_key not in st.session_state:
            st.session_state[t_key] = True

    col_all1, col_all2 = st.columns(2)

    with col_all1:
        if st.button("Select All Present", type="secondary", icon=":material/done_all:", use_container_width=True, key=f"btn_all_present_{subject_id}"):
            for s in students:
                st.session_state[f"manual_toggle_{subject_id}_{s['student_id']}"] = True

    with col_all2:
        if st.button("Select All Absent", type="secondary", icon=":material/deselect:", use_container_width=True, key=f"btn_all_absent_{subject_id}"):
            for s in students:
                st.session_state[f"manual_toggle_{subject_id}_{s['student_id']}"] = False


    st.divider()

    updated_states = {}
    for student in students:
        s_id = student['student_id']
        t_key = f"manual_toggle_{subject_id}_{s_id}"

        c_info, c_status = st.columns([2.5, 1.5], vertical_alignment="center")
        with c_info:
            face_badge = "👤 Face" if student.get('face_embedding') else ""
            voice_badge = "🎙️ Voice" if student.get('voice_embedding') else ""
            badges = " • ".join(filter(None, [face_badge, voice_badge]))
            badge_html = f"<div style='font-size: 0.75rem; color: #94A3B8; margin-top: 2px;'>{badges}</div>" if badges else ""
            st.markdown(f"<div style='padding: 2px 0;'><div style='font-weight: 600; color: #F8FAFC; font-size: 1rem;'>{student['name']} <span style='color: #CBD5E1; font-weight: normal; font-size: 0.85rem;'>(ID: {s_id})</span></div>{badge_html}</div>", unsafe_allow_html=True)
        
        with c_status:
            current_val = st.session_state.get(t_key, True)
            status_label = "✅ Present" if current_val else "❌ Absent"
            is_pres = st.toggle(
                status_label,
                key=t_key
            )
            updated_states[s_id] = is_pres


    st.divider()

    if st.button("Save Attendance Record", type="primary", icon=":material/save:", use_container_width=True, key=f"btn_save_att_{subject_id}"):
        logs = []
        present_count = 0
        for s_id, is_pres in updated_states.items():
            logs.append({
                "student_id": s_id,
                "subject_id": subject_id,
                "timestamp": dt_str,
                "is_present": bool(is_pres)
            })
            if is_pres:
                present_count += 1

        create_attendance(logs)
        st.session_state.pop("active_manual_dialog", None)
        st.toast(f"Saved attendance! {present_count}/{len(students)} students marked Present.", icon="✅")
        time.sleep(1)
        st.rerun()
