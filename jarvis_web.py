import streamlit as st
import comtypes
comtypes.CoInitialize()
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import psutil

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Feature functions
def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p")
    return f"The current time is {Time}"

def get_date():
    now = datetime.datetime.now()
    return f"The current date is {now.day}/{now.month}/{now.year}"

def get_greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        return "Good morning!"
    elif hour >= 12 and hour < 18:
        return "Good afternoon!"
    elif hour >= 18 and hour < 24:
        return "Good evening!"
    else:
        return "Good night!"

def get_cpu_info():
    usage = psutil.cpu_percent()
    battery = psutil.sensors_battery()
    return f"CPU is at {usage}% and Battery is at {battery.percent}%"

def get_joke():
    return pyjokes.get_joke()

def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return "Couldn't find information on that."

# Streamlit UI
st.set_page_config(page_title="Jarvis Web Assistant", layout="centered")
st.title("🧠 Jarvis - Your Web Assistant")
st.write("Welcome! Type a command or select an option.")

query = st.text_input("Enter your command:")

if st.button("Process Command"):
    response = ""
    query = query.lower()

    if "time" in query:
        response = get_time()
    elif "date" in query:
        response = get_date()
    elif "wikipedia" in query:
        st.info("Searching Wikipedia...")
        query = query.replace("wikipedia", "").strip()
        response = search_wikipedia(query)
    elif "chrome" in query or "search" in query:
        search_term = query.replace("search in chrome", "").strip()
        webbrowser.open_new_tab(f"https://www.google.com/search?q={search_term}")
        response = f"Searching for {search_term} in browser..."
    elif "cpu" in query:
        response = get_cpu_info()
    elif "joke" in query:
        response = get_joke()
    elif "greet" in query or "wish" in query:
        response = get_greeting()
    elif "shutdown" in query:
        response = "Shutdown command is disabled in web version."
    elif "logout" in query:
        response = "Logout command is disabled in web version."
    elif "restart" in query:
        response = "Restart command is disabled in web version."
    elif "offline" in query:
        st.success("Jarvis is now offline. Refresh to start again.")
        st.stop()
    else:
        response = "Sorry, I didn't understand that command."

    st.success(response)
    if st.checkbox("🔊 Speak it out"):
        speak(response)
