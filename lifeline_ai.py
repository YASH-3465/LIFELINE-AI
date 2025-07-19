import streamlit as st   #UI
import speech_recognition as sr #voice intake
from transformers import pipeline # pretrained model
from PIL import Image #module for image display
import smtplib #connects to server
import os # path finding
import pyttsx3  # Text-to-Speech

# Load Emotion Model
@st.cache_resource #used to avoid restart of model implement everytime
def load_emotion_model():
    return pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

emotion_model = load_emotion_model()

# Voice Output with Female Voice
def speak_female(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    else:
        engine.setProperty('voice', voices[1].id)  # fallback
    engine.setProperty('rate', 175)  # slightly faster for natural tone
    engine.say(text)
    engine.runAndWait()

# Emotion Alert Email
def send_alert_email():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587) # connects to the portal
        server.starttls() #encrypts connection
        server.login("login mail[from mail]", "app password")
        message = "Subject: LIFELINE AI Alert\n\nThe person is disturbed and may need emotional support."
        server.sendmail("from mail", "To mail", message)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Email failed: {e}")
        return False

# Memory Display
def show_memory():
    if os.path.exists("vault/happy_memory.jpg"):
        img = Image.open("vault/happy_memory.jpg")
        st.image(img, caption="Here's something to make you smile 💛", use_column_width=True)
        speak_female("Here’s something to make you smile.")
    else:
        st.warning("No memory found. Add an image to /vault folder named 'happy_memory.jpg'.")

# Speech Recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info(" Listening for up to 30 seconds... Speak your thoughts.")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=30) #audio intake
            text = recognizer.recognize_google(audio) #text conversion
            return text
        except sr.WaitTimeoutError:
            return "Timeout: You didn’t speak in time."
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand what you said."
        except sr.RequestError:
            return "Sorry, speech service is unavailable right now."

# Streamlit UI Setup
st.set_page_config(page_title="LIFELINE AI", layout="centered") #page title
st.title("LIFELINE AI: Voice-Driven Emotional First-Aid")
st.markdown("A voice-based AI that listens, detects emotion, and helps when you’re feeling low.")#para tag

# Main Interaction
if st.button(" Talk to LIFELINE AI"): #if clicked button
    transcript = recognize_speech()
    st.subheader("You said:")
    st.write(transcript)

    if "sorry" in transcript.lower() or "timeout" in transcript.lower():
        st.warning("Try again. Ensure your microphone is working and speak clearly.")
    else:
        result = emotion_model(transcript)[0]
        label = result['label'] #result is in dictionary format
        score = result['score']
        st.subheader(f"Detected Emotion: `{label}` with {score:.2f} confidence")

        if label in ['sadness', 'fear', 'anger']:
            speak_female("I'm here for you. Don't worry.")
            st.markdown("*I'm here for you. Don't worry.*")
            show_memory()

            if label == 'sadness' and score > 0.85:
                if send_alert_email():
                    st.success("Emergency contact has been alerted.")
                    speak_female("I have alerted your emergency contact.")
                else:
                    st.error("Failed to send emergency email.")
        else:
            st.success("You sound okay! Stay positive and keep going!")
            speak_female("You sound okay! Stay positive and keep going!")

# Footer Info
st.markdown("---")
st.markdown("💡 Tip: Add your happy photo to a folder named `vault/` with the filename `happy_memory.jpg`.")
