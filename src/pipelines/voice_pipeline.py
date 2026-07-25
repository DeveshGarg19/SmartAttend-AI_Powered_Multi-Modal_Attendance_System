from speechbrain.inference.speaker import EncoderClassifier
import numpy as np
import io
import librosa
import torch
import streamlit as st
import traceback
import tempfile


@st.cache_resource
def load_voice_encoder():
    return EncoderClassifier.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
    )


def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()

        st.write(f"Audio bytes length: {len(audio_bytes)}")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            temp_path = tmp.name

        audio, sr = librosa.load(temp_path, sr=16000)
        waveform = torch.from_numpy(audio).float().unsqueeze(0)

        embedding = encoder.encode_batch(waveform)
        embedding = embedding.squeeze().detach().cpu().numpy()
        norm = np.linalg.norm(embedding)
        if norm > 0:
            embedding = embedding / norm

        return embedding.tolist()

    except Exception:
        traceback.print_exc()
        raise
    

def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None, 0.0
    
    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():
        if stored_embedding is not None:
            stored_embedding = np.asarray(stored_embedding)
            similarity = np.dot(new_embedding, stored_embedding)
            if similarity> best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid, best_score
    
    return None, best_score


def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):

    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        segments = librosa.effects.split(audio, top_db=30)

        identified_results = {}


        for start, end in segments:

            if (end-start) < sr * 0.5:
                continue
            segment_audio = audio[start:end]
            waveform = torch.from_numpy(segment_audio).float().unsqueeze(0)

            embedding = encoder.encode_batch(waveform)
            embedding = embedding.squeeze().detach().cpu().numpy()
            norm = np.linalg.norm(embedding)
            if norm > 0:
                embedding = embedding / norm

            sid, score = identify_speaker(embedding, candidates_dict, threshold)

            if sid:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results
    except Exception as e:
        st.error(f"Bulk process error: {e}")
        return {}