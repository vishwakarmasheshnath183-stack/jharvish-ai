import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import time
import random
import threading

# -----------------------------------------------------
#  OPTION X – ULTRA STABLE ENGINE
# -----------------------------------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 155)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# -----------------------------------------------------
#  SMART LISTEN FUNCTION (OPTION X)
# -----------------------------------------------------
def listen():
    """Smart mode text+voice input with fallback."""
    user = input("Press ENTER for voice, or type command: ").strip()

    # If user typed something
    if user != "":
        return user.lower()

    # Voice input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 200  # Reduce background noise
        speak("Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=6)

    try:
        command = r.recognize_google(audio, language='en-in')
        print("You:", command)
        return command.lower()
    except:
        return "null"   # Very important: never return empty


# -----------------------------------------------------
#  DATA COLLECTION
# -----------------------------------------------------
indian_states = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa",
    "Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala",
    "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland",
    "Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
    "Uttar Pradesh","Uttarakhand","West Bengal","Andaman & Nicobar","Chandigarh",
    "Delhi","Jammu & Kashmir","Ladakh","Lakshadweep","Puducherry"
]

countries = [
    "India","USA","China","Russia","Japan","Germany","France","UK",
    "Italy","Canada","Australia","Brazil","South Africa","Nepal","Bhutan",
    "Sri Lanka","Pakistan","Bangladesh","Saudi Arabia","Turkey","Spain",
    "Portugal","Norway","Sweden","Finland","Denmark","UAE"
]

top_engineering = [
    "IIT Madras","IIT Delhi","IIT Bombay","IIT Kanpur","IIT Kharagpur"
]

top_medical = [
    "AIIMS Delhi","PGIMER Chandigarh","CMC Vellore","AFMC Pune","JIPMER Puducherry"
]

universities_in_india = 1150

actors = {
    "shahrukh khan": "Born 1965, known as King Khan, 80+ films.",
    "salman khan": "Born 1965, famous for Dabangg, Sultan.",
    "akshay kumar": "Born 1967, action + comedy superstar.",
    "amitabh bachchan": "Born 1942, megastar with 200+ movies.",
    "hrithik roshan": "Born 1974, known for Krrish and War.",
    "robert downey junior": "Hollywood actor, Iron Man.",
    "tom cruise": "Hollywood actor, Mission Impossible."
}


# -----------------------------------------------------
#  BASIC INFO FUNCTIONS
# -----------------------------------------------------
def tell_time():
    speak("The time is " + datetime.datetime.now().strftime("%I:%M %p"))

def tell_date():
    speak("Today's date is " + datetime.date.today().strftime("%d %B %Y"))

def tell_day():
    speak("Today is " + datetime.datetime.now().strftime("%A"))

def tell_states():
    speak("India has 28 states and 8 union territories.")
    speak(", ".join(indian_states))

def tell_countries():
    speak("Listing some major countries.")
    speak(", ".join(countries))

def tell_universities():
    speak(f"There are approx {universities_in_india} universities in India.")

def tell_engineering():
    speak("Top engineering colleges in India:")
    for i in top_engineering:
        speak(i)

def tell_medical():
    speak("Top medical colleges in India:")
    for i in top_medical:
        speak(i)

def india_politics():
    speak("India is a democratic republic.")
    speak("Prime Minister: Narendra Modi.")
    speak("President: Droupadi Murmu.")
    speak("543 Lok Sabha seats and 245 Rajya Sabha seats.")

def geography():
    speak("India covers 3.28 million square kilometers.")
    speak("Himalayas in the north, Indian Ocean in the south.")

def history():
    speak("Indian history includes Indus Valley civilization from 3300 BCE.")
    speak("Maurya Empire in 322 BCE, Mughal Empire from 1526 to 1857.")
    speak("India got independence on 15 August 1947.")

def actor_info(name):
    key = name.lower()
    if key in actors:
        speak(actors[key])
    else:
        speak("Actor information not available.")


# -----------------------------------------------------
#  SYSTEM & INTERNET FEATURES
# -----------------------------------------------------
def search_wiki(cmd):
    try:
        topic = cmd.replace("wikipedia", "").strip()
        speak("Searching Wikipedia...")
        result = wikipedia.summary(topic, sentences=3)
        speak(result)
    except:
        speak("Sorry, I could not fetch Wikipedia information.")

def open_website(site):
    common = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "instagram": "https://instagram.com",
        "github": "https://github.com",
        "facebook": "https://facebook.com"
    }
    for k, v in common.items():
        if k in site:
            speak(f"Opening {k}")
            webbrowser.open(v)
            return
    webbrowser.open("https://" + site)

def play_song(song):
    speak(f"Playing {song}")
    pywhatkit.playonyt(song)

def weather(city):
    speak(f"Showing weather for {city}")
    webbrowser.open(f"https://www.google.com/search?q=weather+{city}")


# -----------------------------------------------------
#  FUN + HELPER FEATURES
# -----------------------------------------------------
def joke():
    jokes = [
        "Why did the computer get tired? Because it had too many tabs open.",
        "I told my laptop I needed a break — it froze!",
        "Why do programmers prefer dark mode? Because the light attracts bugs."
    ]
    speak(random.choice(jokes))

def calculator(raw):
    try:
        exp = raw.replace("calculate", "")
        speak("The answer is " + str(eval(exp)))
    except:
        speak("Invalid calculation.")

def set_alarm(t):
    def alarm_thread():
        speak(f"Alarm set for {t}")
        while True:
            if datetime.datetime.now().strftime("%H:%M") == t:
                speak("Alarm ringing!")
                break
    threading.Thread(target=alarm_thread).start()

def reminder(msg, time_set):
    def rem():
        while True:
            if datetime.datetime.now().strftime("%H:%M") == time_set:
                speak("Reminder: " + msg)
                break
    threading.Thread(target=rem).start()


# -----------------------------------------------------
#  MAIN LOOP (SMART AI MATCHING)
# -----------------------------------------------------
speak("Jarvis Option-X Activated. How can I help you?")

while True:
    cmd = listen()

    if cmd == "null":
        speak("I didn't catch that.")
        continue

    # EXIT
    if "exit" in cmd or "stop" in cmd or "quit" in cmd:
        speak("Goodbye boss.")
        break

    # Time/Date/Day
    if "time" in cmd:
        tell_time()
    elif "date" in cmd:
        tell_date()
    elif "day" in cmd:
        tell_day()

    # Wikipedia
    elif "wikipedia" in cmd:
        search_wiki(cmd)

    # Open Website
    elif "open" in cmd:
        site = cmd.replace("open", "").strip()
        open_website(site)

    # Play Song
    elif "play" in cmd:
        song = cmd.replace("play", "").strip()
        play_song(song)

    # States / Countries / Colleges
    elif "state" in cmd:
        tell_states()
    elif "countries" in cmd or "country" in cmd:
        tell_countries()
    elif "university" in cmd:
        tell_universities()
    elif "engineering" in cmd:
        tell_engineering()
    elif "medical" in cmd:
        tell_medical()

    # Info
    elif "politics" in cmd:
        india_politics()
    elif "geography" in cmd:
        geography()
    elif "history" in cmd:
        history()

    # Actor
    elif "actor" in cmd:
        name = cmd.replace("actor", "").strip()
        actor_info(name)

    # Weather
    elif "weather" in cmd:
        city = cmd.replace("weather", "").strip()
        weather(city)

    # Calculator
    elif "calculate" in cmd:
        calculator(cmd)

    # Jokes
    elif "joke" in cmd:
        joke()

    # Alarm
    elif "alarm" in cmd:
        t = cmd.replace("alarm", "").strip()
        set_alarm(t)

    # Reminder
    elif "remind" in cmd:
        try:
            parts = cmd.split("at")
            msg = parts[0].replace("remind me", "").strip()
            t = parts[1].strip()
            reminder(msg, t)
        except:
            speak("Correct format: remind me *message* at *time*")

    # Fallback
    else:
        speak("Sorry, I don't understand. Please repeat.")

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import time
import random
import threading

# -------------------- ONLINE AI SETUP --------------------
try:
    import openai
    OPENAI_AVAILABLE = True
    openai.api_key = "YOUR_OPENAI_KEY_HERE"  # Replace with your key
except:
    OPENAI_AVAILABLE = False

# -------------------- SPEECH ENGINE --------------------
engine = pyttsx3.init()
engine.setProperty("rate", 155)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# -------------------- SMART LISTEN --------------------
def listen():
    """Returns voice command or text input."""
    user = input("Press ENTER for voice or type command: ").strip()
    if user != "":
        return user.lower()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 200
        speak("Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=6)
    try:
        cmd = r.recognize_google(audio, language='en-in')
        print("You:", cmd)
        return cmd.lower()
    except:
        return "null"

# -------------------- DATA --------------------
indian_states = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa",
"Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
"Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan",
"Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
"Andaman & Nicobar","Chandigarh","Delhi","Jammu & Kashmir","Ladakh","Lakshadweep","Puducherry"]

countries = ["India","USA","China","Russia","Japan","Germany","France","UK","Italy",
"Canada","Australia","Brazil","South Africa","Nepal","Bhutan","Sri Lanka","Pakistan","Bangladesh",
"Saudi Arabia","Turkey","Spain","Portugal","Norway","Sweden","Finland","Denmark","UAE"]

top_engineering = ["IIT Madras","IIT Delhi","IIT Bombay","IIT Kanpur","IIT Kharagpur"]
top_medical = ["AIIMS Delhi","PGIMER Chandigarh","CMC Vellore","AFMC Pune","JIPMER Puducherry"]
universities_in_india = 1150

actors = {
    "shahrukh khan":"Born 1965, King Khan, 80+ films",
    "salman khan":"Born 1965, famous for Dabangg, Sultan",
    "akshay kumar":"Born 1967, action + comedy superstar",
    "amitabh bachchan":"Born 1942, megastar with 200+ movies",
    "hrithik roshan":"Born 1974, known for Krrish and War",
    "robert downey junior":"Hollywood actor, Iron Man",
    "tom cruise":"Hollywood actor, Mission Impossible"
}

# -------------------- HELPER FUNCTIONS --------------------
def tell_time(): speak(datetime.datetime.now().strftime("The time is %I:%M %p"))
def tell_date(): speak(datetime.date.today().strftime("Today's date is %d %B %Y"))
def tell_day(): speak(datetime.datetime.now().strftime("Today is %A"))

def tell_states(): speak("India has 28 states and 8 union territories: "+", ".join(indian_states))
def tell_countries(): speak("Some countries: "+", ".join(countries))
def tell_universities(): speak(f"Universities in India: approx {universities_in_india}")
def tell_engineering(): speak("Top engineering colleges: "+", ".join(top_engineering))
def tell_medical(): speak("Top medical colleges: "+", ".join(top_medical))

def india_politics():
    speak("India is a parliamentary democratic republic.")
    speak("Prime Minister: Narendra Modi. President: Droupadi Murmu. 543 Lok Sabha seats, 245 Rajya Sabha seats.")

def geography():
    speak("India covers 3.28 million sq km. Himalayas in north, Thar desert in west, Indian Ocean in south.")

def history():
    speak("Indus Valley 3300 BCE. Maurya Empire 322 BCE. Mughal Empire 1526-1857. Independence 15 August 1947.")

def actor_info(name):
    name = name.lower()
    if name in actors: speak(actors[name])
    else: speak("Actor info not available.")

def search_wiki(query):
    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=3)
        speak(result)
    except:
        speak("Could not fetch Wikipedia info.")

def open_website(site):
    common = {"google":"https://google.com","youtube":"https://youtube.com",
              "github":"https://github.com","instagram":"https://instagram.com"}
    for k,v in common.items():
        if k in site: webbrowser.open(v); speak(f"Opening {k}"); return
    webbrowser.open("https://"+site); speak(f"Opening {site}")

def play_song(song):
    speak(f"Playing {song}")
    pywhatkit.playonyt(song)

def weather(city):
    speak(f"Weather for {city}")
    webbrowser.open(f"https://www.google.com/search?q=weather+{city}")

def joke():
    jokes=["Why did the computer get tired? Too many tabs open.",
           "I told my laptop I needed a break — it froze!",
           "Why programmers prefer dark mode? Light attracts bugs."]
    speak(random.choice(jokes))

def calculator(cmd):
    try: speak("The answer is "+str(eval(cmd.replace("calculate",""))))
    except: speak("Invalid calculation.")

def set_alarm(t):
    def alarm_thread():
        speak(f"Alarm set for {t}")
        while True:
            if datetime.datetime.now().strftime("%H:%M")==t: speak("Alarm ringing!"); break
    threading.Thread(target=alarm_thread).start()

def reminder(msg,t):
    def rem():
        while True:
            if datetime.datetime.now().strftime("%H:%M")==t: speak("Reminder: "+msg); break
    threading.Thread(target=rem).start()

# -------------------- ONLINE + OFFLINE AI --------------------
def ai_brain(query):
    """Option-Z AI Brain Mode"""
    if OPENAI_AVAILABLE:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"Answer clearly: {query}",
                max_tokens=300
            )
            speak(response.choices[0].text.strip())
            return
        except:
            pass
    # OFFLINE fallback
    fallback_answers(query)

def fallback_answers(query):
    """Offline reasoning fallback"""
    q=query.lower()
    if "time" in q: tell_time()
    elif "date" in q: tell_date()
    elif "day" in q: tell_day()
    elif "state" in q: tell_states()
    elif "country" in q: tell_countries()
    elif "university" in q: tell_universities()
    elif "engineering" in q: tell_engineering()
    elif "medical" in q: tell_medical()
    elif "history" in q: history()
    elif "geography" in q: geography()
    elif "politics" in q: india_politics()
    elif "actor" in q: actor_info(q.replace("actor","").strip())
    elif "joke" in q: joke()
    elif "weather" in q: weather(q.replace("weather","").strip())
    elif "wikipedia" in q: search_wiki(q.replace("wikipedia","").strip())
    else: speak("I am offline and cannot answer that perfectly. Try rephrasing or use online mode.")

# -------------------- MAIN LOOP --------------------
speak("Jarvis Option-Z Activated. Hybrid Online + Offline AI")

while True:
    cmd = listen()
    if cmd in ["exit","stop","quit"]: speak("Goodbye"); break
    # Send query to AI brain
    ai_brain(cmd)

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import random
import threading

# ---------------------- ONLINE AI ----------------------
try:
    import openai
    OPENAI_AVAILABLE = True
    openai.api_key = "YOUR_OPENAI_KEY_HERE"  # Replace with your OpenAI key
except:
    OPENAI_AVAILABLE = False

# ---------------------- SPEECH ENGINE ----------------------
engine = pyttsx3.init()
engine.setProperty("rate", 155)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------------- MEMORY SYSTEM ----------------------
MEMORY_FILE = "memory.txt"

def remember(query, answer):
    try:
        with open(MEMORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"Q: {query}\nA: {answer}\n\n")
    except:
        pass

def recall(query):
    try:
        if not os.path.exists(MEMORY_FILE):
            return None
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            lines = f.read()
            if query.lower() in lines.lower():
                return lines  # return all memory for now
    except:
        return None
    return None

# ---------------------- LISTEN FUNCTION ----------------------
def listen():
    choice = input("Press ENTER for voice or type command: ").strip()
    if choice != "":
        return choice.lower()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 200
        speak("Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=6)
    try:
        cmd = r.recognize_google(audio, language='en-in')
        print("You:", cmd)
        return cmd.lower()
    except:
        return "null"

# ---------------------- DATA ----------------------
indian_states = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa",
"Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
"Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan",
"Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
"Andaman & Nicobar","Chandigarh","Delhi","Jammu & Kashmir","Ladakh","Lakshadweep","Puducherry"]

countries = ["India","USA","China","Russia","Japan","Germany","France","UK","Italy",
"Canada","Australia","Brazil","South Africa","Nepal","Bhutan","Sri Lanka","Pakistan","Bangladesh",
"Saudi Arabia","Turkey","Spain","Portugal","Norway","Sweden","Finland","Denmark","UAE"]

top_engineering = ["IIT Madras","IIT Delhi","IIT Bombay","IIT Kanpur","IIT Kharagpur"]
top_medical = ["AIIMS Delhi","PGIMER Chandigarh","CMC Vellore","AFMC Pune","JIPMER Puducherry"]
universities_in_india = 1150

actors = {
    "shahrukh khan":"Born 1965, King Khan, 80+ films",
    "salman khan":"Born 1965, famous for Dabangg, Sultan",
    "akshay kumar":"Born 1967, action + comedy superstar",
    "amitabh bachchan":"Born 1942, megastar with 200+ movies",
    "hrithik roshan":"Born 1974, known for Krrish and War",
    "robert downey junior":"Hollywood actor, Iron Man",
    "tom cruise":"Hollywood actor, Mission Impossible"
}

# ---------------------- BASIC FUNCTIONS ----------------------
def tell_time(): speak(datetime.datetime.now().strftime("The time is %I:%M %p"))
def tell_date(): speak(datetime.date.today().strftime("Today's date is %d %B %Y"))
def tell_day(): speak(datetime.datetime.now().strftime("Today is %A"))
def tell_states(): speak("India has 28 states and 8 union territories: "+", ".join(indian_states))
def tell_countries(): speak("Some countries: "+", ".join(countries))
def tell_universities(): speak(f"Universities in India: approx {universities_in_india}")
def tell_engineering(): speak("Top engineering colleges: "+", ".join(top_engineering))
def tell_medical(): speak("Top medical colleges: "+", ".join(top_medical))
def india_politics(): speak("India is a parliamentary democratic republic. PM: Narendra Modi, President: Droupadi Murmu. 543 Lok Sabha, 245 Rajya Sabha.")
def geography(): speak("India covers 3.28 million sq km. Himalayas north, Thar desert west, Indian Ocean south.")
def history(): speak("Indus Valley 3300 BCE, Maurya Empire 322 BCE, Mughal Empire 1526-1857, Independence 15 August 1947.")
def actor_info(name): speak(actors.get(name.lower(), "Actor info not available."))
def search_wiki(query):
    try: speak(wikipedia.summary(query, sentences=3))
    except: speak("Could not fetch Wikipedia info.")
def open_website(site):
    common = {"google":"https://google.com","youtube":"https://youtube.com","github":"https://github.com","instagram":"https://instagram.com"}
    for k,v in common.items():
        if k in site: webbrowser.open(v); speak(f"Opening {k}"); return
    webbrowser.open("https://"+site); speak(f"Opening {site}")
def play_song(song): pywhatkit.playonyt(song); speak(f"Playing {song}")
def weather(city): webbrowser.open(f"https://www.google.com/search?q=weather+{city}"); speak(f"Weather for {city}")
def joke(): speak(random.choice(["Why did the computer get tired? Too many tabs open.","I told my laptop I needed a break — it froze!","Why programmers prefer dark mode? Light attracts bugs."]))
def calculator(cmd):
    try: speak(str(eval(cmd.replace("calculate",""))))
    except: speak("Invalid calculation.")

# ---------------------- HYBRID AI ----------------------
def ai_brain(query):
    memory = recall(query)
    if memory:
        speak("I remember this from before:")
        speak(memory)
        return
    if OPENAI_AVAILABLE:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"Answer clearly: {query}",
                max_tokens=300
            )
            answer = response.choices[0].text.strip()
            speak(answer)
            remember(query, answer)
            return
        except:
            fallback_answers(query)
    else:
        fallback_answers(query)

def fallback_answers(query):
    q=query.lower()
    if "time" in q: tell_time()
    elif "date" in q: tell_date()
    elif "day" in q: tell_day()
    elif "state" in q: tell_states()
    elif "country" in q: tell_countries()
    elif "university" in q: tell_universities()
    elif "engineering" in q: tell_engineering()
    elif "medical" in q: tell_medical()
    elif "history" in q: history()
    elif "geography" in q: geography()
    elif "politics" in q: india_politics()
    elif "actor" in q: actor_info(q.replace("actor","").strip())
    elif "joke" in q: joke()
    elif "weather" in q: weather(q.replace("weather","").strip())
    elif "wikipedia" in q: search_wiki(q.replace("wikipedia","").strip())
    else: speak("I am offline and cannot answer perfectly. Try rephrasing or use online mode.")

# ---------------------- MAIN LOOP ----------------------
speak("Jarvis Option-Z Pro Activated. Hybrid AI with memory and voice conversation.")

while True:
    command = listen()
    if command in ["exit","stop","quit"]: speak("Goodbye!"); break
    ai_brain(command)


