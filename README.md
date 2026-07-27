# 📸 SmartAttend - AI-Powered Multi-Modal Attendance System


> **SmartAttend** makes classroom attendance effortless, faster, and reliable using state-of-the-art **Face Recognition** and **Voice Speaker Identification** deep learning models.

---

## 📌 Overview

Traditional manual attendance systems are time-consuming and prone to proxy errors. **SmartAttend** automates attendance taking using multi-modal AI pipelines:
1. **Face Recognition**: Detects and identifies multiple students simultaneously from classroom photographs.
2. **Voice Speaker Identification**: Identifies speakers from recorded audio or bulk roll-call sound clips using speaker embedding similarity.

Built with **Streamlit** for a responsive user interface and backed by **Supabase** for secure real-time data persistence.

---

## ✨ Key Features

### 👨‍🏫 Teacher Portal
- **Subject & Section Management**: Create and manage multiple classes with unique join codes and shareable QR codes.
- **AI Face Attendance**: Upload a classroom photo to detect, recognize, and mark attendance for multiple enrolled students in seconds.
- **AI Voice Attendance**: Upload class audio clips or bulk speech files to identify active speakers and mark attendance.
- **Attendance Insights**: View detailed attendance logs, session counts, and student participation stats.

### 🎓 Student Portal
- **Instant Class Enrollment**: Join courses seamlessly via subject join codes, shareable links, or scanned QR codes.
- **Biometric Profile Setup**: Upload photo samples and voice recordings to generate personalized facial (128D) and voice embeddings.
- **Personal Dashboard**: Track subject-wise attendance history and percentage metrics in real time.

---

## 🛠️ Tech Stack

- **Frontend & Web Framework**: [Streamlit](https://streamlit.io/)
- **Backend Database**: [Supabase](https://supabase.com/) (PostgreSQL cloud database)
- **Face Processing Pipeline**:
  - `dlib`: Frontal face detector & 68-point shape predictor
  - `face_recognition_models`: Deep face recognition feature extraction (128D descriptors)
  - `scikit-learn`: Linear Support Vector Classifier (SVC) for student face prediction
- **Voice Processing Pipeline**:
  - `SpeechBrain`: `spkrec-ecapa-voxceleb` model for speaker embedding extraction
  - `librosa`: Audio loading, sampling, and voice activity splitting
  - `torch`: PyTorch execution backend for voice encoder inference
- **Utilities**:
  - `bcrypt`: Password hashing and authentication security
  - `segno`: Dynamic QR code generation for course sharing

---

## 📂 Project Structure

```
Attendance_Project/
├── app.py                         # Application entry point & screen routing
├── requirements.txt               # Dependencies list
├── .env                           # Environment variables configuration
├── .streamlit/
│   └── secrets.toml               # Streamlit secrets (Supabase credentials)
├── pretrained_models/             # Cached ML model weights (SpeechBrain, etc.)
└── src/
    ├── components/                # Modular Streamlit dialogs & cards
    │   ├── dialog_add_photo.py    # Face enrollment dialog
    │   ├── dialog_auto_enroll.py  # Link-based course auto-enrollment
    │   ├── dialog_create_subject.py
    │   ├── dialog_enroll.py
    │   ├── dialog_share_subject.py# QR code sharing dialog
    │   ├── dialog_voice_attendance.py
    │   ├── header.py
    │   └── subject_card.py
    ├── database/                  # Supabase database client and queries
    │   ├── config.py              # Database client initialization
    │   └── db.py                  # CRUD operations (users, subjects, attendance)
    ├── pipelines/                 # AI & Machine Learning pipelines
    │   ├── face_pipeline.py       # Face detection, 128D embedding & SVM classifier
    │   └── voice_pipeline.py      # Audio split, ECAPA-TDNN speaker identification
    ├── screen/                    # Screen layouts
    │   ├── home_screen.py         # Login / Register landing page
    │   ├── student_screen.py      # Student dashboard & profile management
    │   └── teacher_screen.py      # Teacher dashboard & attendance control panel
    └── ui/
        └── base_layout.py         # Common layout wrapper & navigation styling
```

---

## 🗄️ Database Schema (Supabase)

SmartAttend relies on 5 main tables in Supabase:
- **`teachers`**: `id`, `username`, `password` (hashed), `name`
- **`students`**: `student_id`, `name`, `face_embedding` (float vector), `voice_embedding` (float vector)
- **`subjects`**: `subject_id`, `subject_code`, `name`, `section`, `teacher_id`
- **`subject_students`**: `id`, `subject_id`, `student_id`
- **`attendance_logs`**: `id`, `subject_id`, `student_id`, `timestamp`, `status`

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.10+ (Recommended: Python 3.10 – 3.12)
- C++ Build Tools (Required for `dlib` compilation on Windows if pre-built wheel is not used)

### 2. Clone the Repository
```bash
git clone https://github.com/DeveshGarg19/SmartAttend-AI_Powered_Multi-Modal_Attendance_System.git
cd SmartAttend-AI_Powered_Multi-Modal_Attendance_System
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note on `dlib` installation**:
> If installation of `dlib` fails, you can install a pre-compiled wheel appropriate for your Python version:
> ```bash
> pip install dlib-20.0.99-cp313-cp313-win_amd64.whl
> ```

### 5. Configure Supabase Secrets
Create or update `.streamlit/secrets.toml` with your Supabase credentials:

```toml
SUPABASE_URL = "https://your-supabase-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key"
```

---

## 🚀 Running the Application

Launch the Streamlit web app:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`.

---

## 💡 How to Use

1. **Register / Log In**: Choose whether you are a **Teacher** or a **Student**.
2. **Student Onboarding**:
   - Students register and navigate to their profile to capture/upload a face photo and record a voice sample.
   - Join subjects using a shared join code or direct URL link (`http://localhost:8501/?join-code=<CODE>`).
3. **Teacher Workflow**:
   - Create a subject to generate a join code & QR code for class distribution.
   - Click **Take Attendance** -> Select **Face Attendance** (upload group photo) or **Voice Attendance** (upload audio).
   - Review detected students and confirm attendance submission.

---

