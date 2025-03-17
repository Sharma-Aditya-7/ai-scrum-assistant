# SprintMate - AI-Powered Agile Assistant

## 🚀 Overview
SprintMate is an AI-powered Scrum Assistant designed to automate Agile workflows, provide insights, and improve team efficiency. It uses OpenAI's GPT-4 to generate Agile best practices, backlog refinements, and sprint insights.

## 📂 Project Structure
```
/ai-scrum-assistant
│── app.py              # Main Flask API
│── requirements.txt    # Dependencies
│── README.md           # Project Documentation
└── .gitignore          # Git ignore file
```

## 🛠️ Setup Instructions
### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/your-username/ai-scrum-assistant.git
 cd ai-scrum-assistant
```

### 2️⃣ Create a Virtual Environment
```sh
 python -m venv venv
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```sh
 pip install flask openai
```

### 4️⃣ Set Up OpenAI API Key
Replace `your-api-key-here` in `app.py` with your OpenAI API key.

### 5️⃣ Run the Application
```sh
 python app.py
```
The server will start at `http://127.0.0.1:5000/`

## 🔥 Usage
### API Endpoint: `/ask`
Send a POST request to interact with the AI Scrum Assistant.
```sh
 curl -X POST http://127.0.0.1:5000/ask \
      -H "Content-Type: application/json" \
      -d '{"prompt": "How can I improve my daily standups?"}'
```
**Example Response:**
```json
{
  "response": "Keep standups short, focus on blockers, and avoid status updates."
}
```

## 📌 Next Steps
- ✅ Add Jira/Linear API Integration
- ✅ Implement AI-Powered Sprint Planning
- ✅ Create a Frontend for the Assistant

## 🏗 Contributors
- Aditya Sharma (@Sharma-Aditya7)
- C Kaustubh (@your-github)

