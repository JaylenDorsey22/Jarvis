import openai
from apikey import api_data
import speech_recognition as sr
import webbrowser
import pyttsx3
import objc


openai.api_key = api_data

# Function to capture voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Jaylen said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

# Function to generate AI response
def Reply(question):
    prompt = f'Jaylen: {question}\n Jarvis: '
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    return answer

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main execution loop
if __name__ == '__main__':
    speak("Hello, I am your Jarvis. How can I help you today?")
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue
        if 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        elif 'bye' in query or 'exit' in query:
            speak("Goodbye!")
            break
        else:
            response = Reply(query)
            print(response)
            speak(response)
