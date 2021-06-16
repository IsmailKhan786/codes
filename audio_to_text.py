import speech_recognition as srk
r =srk.Recognizer()
with srk.AudioFile("wav.wav") as source:
    audio_text = r.listen(source)
    text = r.recognize_google(audio_text)
    print(text)
print("Done")

