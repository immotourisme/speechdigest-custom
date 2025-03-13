import streamlit as st
import whisper
import tempfile
import os

st.title("🎙️ Speech Digest - Transcription Audio")

# Uploader un fichier audio
uploaded_file = st.file_uploader("Choisissez un fichier audio", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Sauvegarde temporaire du fichier
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    st.audio(temp_audio_path, format="audio/mp3")

    # Charger le modèle Whisper (plus rapide : "base")
    model = whisper.load_model("base")

    # Transcription
    st.write("🔄 Transcription en cours...")
    result = model.transcribe(temp_audio_path)

    # Affichage du texte transcrit
    st.subheader("📝 Transcription :")
    st.write(result["text"])

    # Suppression du fichier temporaire
    os.remove(temp_audio_path)
