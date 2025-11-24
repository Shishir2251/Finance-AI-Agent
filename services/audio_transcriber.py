from faster_whisper import WhisperModel

# Load the model ONCE
model = WhisperModel("small", device="cpu")

def transcribe_audio(path: str) -> str:
    segments, info = model.transcribe(path)
    text = " ".join(segment.text for segment in segments)
    return text
