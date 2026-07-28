import streamlit as st
from PIL import Image

@st.dialog("Capture or Upload Photos")
def add_photos_dialog():
    st.write('Add classroom photos to scan for attendance')

    if 'added_file_ids' not in st.session_state:
        st.session_state.added_file_ids = set()

    tab_cam, tab_upload = st.tabs(["📷 Camera", "📁 Upload Photos"])

    with tab_cam:
        cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')
        if cam_photo:
            photo_bytes = cam_photo.getvalue()
            file_key = getattr(cam_photo, 'file_id', hash(photo_bytes))
            if file_key not in st.session_state.added_file_ids:
                st.session_state.added_file_ids.add(file_key)
                st.session_state.attendance_images.append(Image.open(cam_photo))
                st.toast('Photo Captured!')

    with tab_upload:
        uploaded_files = st.file_uploader('Choose image files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='dialog_upload')
        if uploaded_files:
            new_count = 0
            for f in uploaded_files:
                file_key = getattr(f, 'file_id', f"{f.name}_{f.size}")
                if file_key not in st.session_state.added_file_ids:
                    st.session_state.added_file_ids.add(file_key)
                    st.session_state.attendance_images.append(Image.open(f))
                    new_count += 1
            if new_count > 0:
                st.toast(f'{new_count} Photo(s) Uploaded Successfully!')

    st.divider()
    if st.button('Done', type='primary', icon=':material/check:', use_container_width=True):
        st.session_state.show_add_photos_dialog = False
        st.rerun()

