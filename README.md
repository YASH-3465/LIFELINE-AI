#  LIFELINE AI: Voice-Driven Emotional First-Aid

> A voice-based mental health assistant that listens, detects emotion, comforts, and alerts when needed.

---

##  Overview

LIFELINE AI is a **streamlit-based voice-driven emotional support system**. It uses natural language processing to recognize your emotions through voice and responds accordingly — by showing comforting memories, speaking kind words, or alerting a trusted contact in case of emotional distress.

This is just the **first step** in my vision. Future versions will integrate this into a mobile app that:
- Records calls (with permission),
- Classifies emotional state,
- Sends memory notifications,
- Sends images to email in critical cases.

---

##  Features

-  **Voice Input:** Speak your thoughts — no typing needed.
-  **Emotion Detection:** Uses a transformer-based NLP model to analyze your mood.
-  **Human-like Voice Output:** Comforting responses using female text-to-speech with natural speed.
-  **Memory Boost:** Displays a happy memory image when you're feeling low.
-  **Emergency Email:** Sends alert to your contact when high sadness is detected.
-  **Offline Interaction:** Works without storing or uploading sensitive user data.


##  Tech Stack

- **Python**
- **Streamlit** – UI Framework
- **SpeechRecognition** – Voice input
- **Transformers (Hugging Face)** – Emotion classification
- **pyttsx3** – Offline text-to-speech engine
- **smtplib** – Email alerts
- **PIL** – Image handling


##  Project Folder Structure

```
LIFELINE-AI/
│
├── app.py                # Main Streamlit app
├── vault/
│   └── happy_memory.jpg  # Your happy photo to show when you're sad
└── README.md
```

---

##  How to Run

1. Clone this repository:
```bash
git clone https://github.com/yourusername/lifeline-ai.git
cd lifeline-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Place a comforting image named `happy_memory.jpg` inside a folder called `vault/`.

4. Run the app:
```bash
streamlit run app.py
```

##  Configuration

To enable email alerts, update the `send_alert_email()` function with your own Gmail credentials or set up environment variables:

```python
server.login("your_email@gmail.com", "your_app_password")
server.sendmail("your_email@gmail.com", "emergency_contact_email", message)
```


##  Future Scope

-  App-based voice call monitoring (with permissions)
-  Cloud storage and real-time analysis
-  Android/iOS App with chatbot interface
-  Integration with therapy platforms and support services

