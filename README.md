# Jarvis – Voice Controlled Assistant (Python)

Jarvis is a simple voice-controlled desktop assistant built using Python.  
It listens for a wake word ("Jarvis") and performs basic tasks such as opening websites, playing music, and reading news headlines using an external API.

---

## 🚀 Features
- Wake word detection ("Jarvis")
- Open popular websites (Google, YouTube, LinkedIn, Facebook)
- Play predefined songs using voice commands
- Fetch and read business news headlines
- Text-to-speech responses

---

## 🛠 Tech Stack
- Python
- SpeechRecognition
- pyttsx3 (Text to Speech)
- Requests (API calls)
- NewsAPI
- dotenv (Environment variable management)

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/jarvis-ai-assistant.git
cd jarvis-ai-assistant

2. Install dependencies
pip install speechrecognition pyttsx3 requests python-dotenv

3. Environment Variable Setup

Create a .env file in the project root:

NEWS_API_KEY=your_newsapi_key_here


⚠️ The .env file is ignored using .gitignore to prevent exposing sensitive information.

▶️ How to Run
python main.py


Say "Jarvis" to activate the assistant and then give a command.

📌 Example Commands

"Open Google"

"Open YouTube"

"Play skyfall"

"Tell me the news"

🔮 Future Improvements

Add support for more commands

Improve natural language understanding

Integrate system-level controls

Add error handling and logging

👤 Author

Nirmal Sugandhi
