import pyttsx3
engine = pyttsx3.init()
engine.say("Welcome to the email validation program.")
engine.runAndWait()
email = input("Enter your email address: ").lower()
engine.say("Validating email...")
engine.runAndWait()
if len(email) > 6:
    if email[0].isalpha():
        if "@" in email:
            if "gmail.com" in email or "yahoo.com" in email or "outlook.com" in email:
                engine.say("Email is valid.")
                engine.runAndWait()
            else:
                engine.say("Email must be from gmail.com, yahoo.com, or outlook.com.")
                engine.runAndWait()
        else:
            engine.say("Email must contain '@' symbol.")
            engine.runAndWait()
    else:
        engine.say("Email must contain only alphabetic characters.")
        engine.runAndWait()
else:
    engine.say("Email must be longer than 6 characters.")
    engine.runAndWait()
exit(0)

