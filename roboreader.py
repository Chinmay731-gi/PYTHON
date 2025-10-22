import pyttsx3

if __name__ == "__main__":
    print("Welcome")
    while True:
        engine = pyttsx3.init()
        x = input("Enter what you wanna listen: ")
        if x == "exit":
            engine.say(f"Thank you,have a nice day")
            engine.runAndWait()
            break
        engine.say(f" {x}")
        engine.runAndWait()

