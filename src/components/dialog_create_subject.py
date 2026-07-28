import streamlit as st
from src.database.db import create_subject
from src.database.config import supabase



@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")
    sub_id = st.text_input("Subject Code", placeholder="CS101")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="A")


    if st.button("Create Subject Now", type='primary', icon=':material/add_task:', use_container_width=True):

        if sub_id and sub_name and sub_section:
            existing = (
                supabase.table("subjects")
                .select("subject_code")
                .eq("subject_code", sub_id)
                .execute()
            )

            if existing.data:
                st.error("⚠️ Subject code already exists. Please enter a correct subject code.")
            else:
                try:
                    create_subject(sub_id, sub_name, sub_section, teacher_id)
                    st.toast("✅ Subject created successfully!", icon="🎉")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields")