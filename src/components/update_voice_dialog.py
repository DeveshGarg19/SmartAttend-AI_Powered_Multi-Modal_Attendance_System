import streamlit as st
from src.database.db import update_student_voice
from src.pipelines.voice_pipeline import get_voice_embedding
import time


@st.dialog("🎤 Update Voice")
def update_voice_dialog():

    student = st.session_state.student_data

    audio = st.audio_input("Speak your attendance phrase",key="update_voice_audio")
    if audio:
        if st.button("Save Voice", type="primary"):
            with st.spinner('Updating Audio data'):
                embedding = get_voice_embedding(audio.read())
                update_student_voice(
                    student["student_id"],
                    embedding
                )
                st.success("Voice updated successfully!")
                time.sleep(2)
                st.rerun()