# 🧠 The Contrarian

> Challenge your opinions with AI-powered counterarguments backed by Retrieval-Augmented Generation (RAG), MongoDB Vector Search, and Google Gemini.

![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react&logoColor=white)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?logo=mongodb&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google_Gemini-4285F4?logo=google&logoColor=white)
![Vercel](https://img.shields.io/badge/Frontend-Vercel-black?logo=vercel)
![Render](https://img.shields.io/badge/Backend-Render-46E3B7?logo=render)

---

## 🌐 Live Demo

### 🚀 Frontend
https://the-contrarian.vercel.app/

### ⚙️ Backend API
https://the-contrarian-api.onrender.com

### 💻 GitHub Repository
https://github.com/Yashasgatty10/the-contrarian

---

# 📖 About The Project

The Contrarian is an AI-powered debate assistant that respectfully challenges a user's opinion using logic, evidence, and critical thinking.

Instead of simply agreeing with the user, the system retrieves relevant knowledge from a MongoDB Atlas Vector Search database and combines it with Google's Gemini AI to generate structured counterarguments.

The project demonstrates Retrieval-Augmented Generation (RAG), semantic search, AI reasoning, and modern full-stack deployment.

---

# ✨ Features

- 🤖 AI-powered counterarguments
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 MongoDB Atlas Vector Search
- 📚 Context-aware responses
- 💬 Conversation history support
- 📝 Markdown formatted AI responses
- 📖 Source attribution
- 📱 Fully responsive UI
- ☁️ Cloud deployment with Vercel & Render

---

# 🏗️ Architecture

```text
                User
                  │
                  ▼
        React + Vite Frontend
                  │
             Axios API Calls
                  │
                  ▼
          FastAPI Backend
                  │
       ┌──────────┴──────────┐
       │                     │
       ▼                     ▼
MongoDB Atlas          Google Gemini
Vector Search          AI Model
       │                     │
       └──────────┬──────────┘
                  ▼
        AI Counterargument
                  │
                  ▼
             React Frontend
```

---

# 🛠️ Tech Stack

## Frontend
- React
- Vite
- Axios
- Tailwind CSS

## Backend
- FastAPI
- Python

## AI
- Google Gemini API

## Database
- MongoDB Atlas
- Vector Search

## Deployment
- Vercel
- Render

## Version Control
- Git
- GitHub

---

# 📂 Project Structure

```
the-contrarian
│
├── backend
│   ├── app
│   │   ├── database
│   │   ├── routes
│   │   ├── services
│   │   └── main.py
│   └── requirements.txt
│
├── frontend
│   ├── public
│   ├── src
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Yashasgatty10/the-contrarian.git
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

## Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend directory.

```env
MONGO_URI=your_mongodb_connection_string
GEMINI_API_KEY=your_google_gemini_api_key
```

---

# 📡 API Endpoint

### POST `/debate`

Request

```json
{
  "argument": "AI will replace software engineers.",
  "history": []
}
```

Response

```json
{
  "argument": "...",
  "rebuttal": "...",
  "retrieval_used": true,
  "used_additional_reasoning": true,
  "sources": []
}
```

---

# 🚀 Future Improvements

- 🔐 User Authentication
- 💾 Save Debate History
- 📄 Export Responses to PDF
- 🎙️ Voice Input
- 🔊 AI Voice Responses
- 📊 Debate Analytics Dashboard
- 🌍 Multi-language Support

---

# 👨‍💻 Author

**Yashas Gatty**

**GitHub**  
https://github.com/Yashasgatty10

**LinkedIn**  
https://www.linkedin.com/in/yashas-gatty10/

---

## ⭐ Support

If you found this project useful, consider giving it a **Star ⭐** on GitHub.
