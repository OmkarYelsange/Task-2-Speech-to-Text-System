pip install -r requirements.txt
python speech_to_text.py

### Task 2: Speech-to-Text System
# This script converts an audio file into text using Google Speech Recognition API.

import speech_recognition as sr

def transcribe_audio(file_path):
    """Transcribes the given audio file to text using Google Speech Recognition."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Error with the speech recognition service.")

if __name__ == "__main__":
    transcribe_audio("sample_audio.wav")  # Replace with your audio file
