import speech_recognition as sr 
a =sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source:
            print("say somthing")
            audio = a.listen(source)
             
            text = a.recognize_google(audio)
            text = text.lower()
            print(f"Recognize speech: {text}")
    except:
        print("Could not understand")
        a = sr.Recognizer()
        continue
    