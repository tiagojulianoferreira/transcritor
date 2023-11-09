import tempfile
from pprint import pprint
import streamlit as st
import whisper
from pytube import YouTube
import os


def transcribeVideoOrchestrator(youtube_url: str,  model_name: str):
    video = downloadYoutubeVideo(youtube_url)
    transcription = transcribe(video, model_name)
    return transcription


def transcribe(video: dict, model_name="medium"):
    print("Transcribing...", video['name'])
    print("Using model:", model_name)
    model = whisper.load_model(model_name)
    result = model.transcribe(video['path'], )
    pprint(result)
    return result["text"]


def downloadYoutubeVideo(youtube_url: str) -> dict:
    print("Processing : " + youtube_url)
    yt = YouTube(youtube_url)
    directory = tempfile.gettempdir()
    file_path = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(directory)
    print("VIDEO NAME " + yt._title)
    print("Download complete:" + file_path)
    return {"name": yt._title, "thumbnail": yt.thumbnail_url, "path": file_path}


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")

def transcribe_audio_orchestrator(audio_file, model_name="whisper-large"):
    # Ler o conteúdo do arquivo de áudio
    audio_content = audio_file.read()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio_path = temp_audio.name
        temp_audio.write(audio_content)

    try:
        transcription = transcribe_audio(temp_audio_path, model_name)
        return transcription
    finally:
        # Excluir automaticamente o arquivo temporário após a transcrição
        os.remove(temp_audio_path)

def save_uploaded_audio(audio_file):
    audio_path = "temp_audio.wav"
    with open(audio_path, "wb") as f:
        f.write(audio_file.read())
    return audio_path

def transcribe_audio(audio_content, model_name="whisper-large"):
    try:
        # Carregar o modelo Whisper
        model = whisper.load_model(model_name)

        # Carregar o áudio diretamente a partir do conteúdo
        audio = whisper.load_audio(audio_content)

        # Transcrição usando o modelo Whisper
        result = model.transcribe(audio)

        return result["text"]
    except Exception as e:
        pprint(f"Erro durante a transcrição: {e}")
        return None