import streamlit as st
import numpy as np
from PIL import Image

from src.pipelines.face_pipeline import (
    get_face_embeddings,
    train_classifier,
)

from src.database.db import update_student_face


@st.dialog("📷 Update Face")
def update_face_dialog():
    student = st.session_state.student_data
    photo = st.camera_input(
        "Capture your new face",
        key="update_face_camera"
    )
    if photo:
        if st.button("Save Face", type="primary"):
            img = np.array(Image.open(photo))
            encodings = get_face_embeddings(img)
            if len(encodings) != 1:
                st.error("Exactly one face must be visible.")
                return

            face_embedding = encodings[0].tolist()

            update_student_face(
                student["student_id"],
                face_embedding
            )

            train_classifier()

            st.success("Face updated successfully!")

            st.rerun()