from gtts import gTTS
import os
text = 'Hello parvez lala tune khana kaya kyaaaa'
language = 'es'
obj = gTTS(text =text,lang = language,slow = False)
obj.save("text_to_audio.mp3")
os.system("text_to_audio.mp3")
print("COMPLETED")


