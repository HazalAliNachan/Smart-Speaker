import pyttsx3

engine = pyttsx3.init()

if __name__ == "__main__":    
    print("Welcome to Smart_Speaker 2.0. Created by HazalAli Nachan")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "Exit":
            engine.say("Goodbye Friend")
            engine.runAndWait()
            break
        else:
            engine.say(x)
            engine.runAndWait()
