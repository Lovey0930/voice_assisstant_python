
import pyttsx3
import speech_recognition as sr
import webbrowser
import random
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import smtplib
import os
import user_config  # Make sure this contains gmail_pass securely

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Listen to user
def command():
    content = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        content = r.recognize_google(audio, language='en-in')
        print("YOU SAID: " + content)
    except Exception:
        print("Sorry, could not understand. Try again.")
        speak("Sorry, could not understand. Try again.")
    return content

# Main process
def main_process():
    speak("Hello,I am your assistant. How can I help you?")
    while True:
        request = command().lower()

        if "hello" in request:
            speak("Hi, how can I help you?")

        elif "play music" in request:
            speak("Playing music")
            songs = [
                "https://www.youtube.com/watch?v=DzYp5uqixz0&list=PLfP6i5T0-DkJPT4dkMAr0PwRq1m25UtoO&index=1&ab_channel=BreakingCopyright—RoyaltyFreeMusic",
                "https://www.youtube.com/watch?v=ETbsXdqgcTM&list=PLfP6i5T0-DkJPT4dkMAr0PwRq1m25UtoO&index=2&ab_channel=BreakingCopyright%E2%80%94RoyaltyFreeMusic",
                "https://www.youtube.com/watch?v=p5cWMxzzMdA&list=PLfP6i5T0-DkJPT4dkMAr0PwRq1m25UtoO&index=3&ab_channel=BreakingCopyright%E2%80%94RoyaltyFreeMusic",
                "https://www.youtube.com/watch?v=yIF56YN5M_Q&list=PLfP6i5T0-DkJPT4dkMAr0PwRq1m25UtoO&index=4&ab_channel=BreakingCopyright%E2%80%94RoyaltyFreeMusic",
                "https://www.youtube.com/watch?v=4HhM66X978U&list=PLfP6i5T0-DkJPT4dkMAr0PwRq1m25UtoO&index=5&ab_channel=BreakingCopyright%E2%80%94RoyaltyFreeMusic"
            ]
            webbrowser.open(random.choice(songs))

        elif "say time" in request:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time now is {time}")

        elif "say date" in request:
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            speak(f"Today's date is {date}")

        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task!="":
                speak("adding task : "+ task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")

        elif "speak task" in request:
            if os.path.exists("todo.txt"):
                with open("todo.txt", "r") as file:
                    tasks = file.read()
                speak("Here are your tasks: " + tasks)
            else:
                speak("You have no tasks saved.")

        elif "show work" in request:
            if os.path.exists("todo.txt"):
                with open("todo.txt", "r") as file:
                    task = file.read()
                notification.notify(
                    title="Today's Work",
                    message=task,
                    timeout=5
                )
                speak("I have shown your tasks as a notification.")
            else:
                speak("No tasks to show.")

        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")

        elif "open" in request:
            app = request.replace("open", "").strip()
            pyautogui.press("super")
            pyautogui.typewrite(app)
            pyautogui.sleep(1)
            pyautogui.press("enter")
            speak(f"Opening {app}")

        elif "wikipedia" in request:
            try:
                topic = request.replace("wikipedia", "").strip()
                result = wikipedia.summary(topic, sentences=2)
                print(result)
                speak(result)
            except Exception as e:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif "search google" in request:
            search_query = request.replace("search google", "").strip()
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Searching Google for {search_query}")

        elif "send whatsapp" in request:
            try:
                # Example usage — edit this to make dynamic
                pwk.sendwhatmsg("+910123456789", "Hi, how are you?", 13, 30, 15)
                speak("WhatsApp message scheduled.")
            except Exception:
                speak("Could not send WhatsApp message.")

        elif "send email" in request:
            try:
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.starttls()
                s.login("loveychoudhary.gzb@gmail.com", user_config.gmail_pass)
                message = "This is a voice assistant message.\n\nBy Lovey Choudhary"
                s.sendmail(
                    "loveychoudhary.gzb@gmail.com",
                    "lovey.9891530930@gmail.com",
                    message
                )
                s.quit()
                speak("Email sent successfully.")
            except Exception as e:
                speak("Failed to send email.")
                print(e)

        elif "exit" in request or "stop" in request:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't catch that.")

# Start the assistant
if __name__ == "__main__":
    main_process()
