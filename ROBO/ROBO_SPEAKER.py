import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    engine.say("welcome to robospeaker write down your thoughts and i am gonna voice over the whole things...")
    engine.runAndWait()
    while True:
        x=input("enter what you want to speak: ")
        if x.lower()=='byebye':
            engine.say("ok,byebye")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()