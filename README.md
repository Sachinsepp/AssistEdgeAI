# 🤖 Assistify

![Python Badge](https://img.shields.io/badge/Python-3.7%2B-blue)
![Flask Badge](https://img.shields.io/badge/Framework-Flask-green)
![API Badge](https://img.shields.io/badge/Model-GPT--3.5--Turbo-orange)

Assistify is a lightweight, elegant, AI-powered web assistant built using the **Flask** framework and the **OpenRouter API**. It allows users to query a modern LLM (GPT-3.5-Turbo by default) to fulfill various tasks seamlessly from their browser.

## ✨ Core Features
- **💬 Ask Questions**: Query general knowledge and get instant, smart answers.
- **📝 Summarize Text**: Condense long emails, articles, and text drops effortlessly.
- **🎨 Creative Content**: Brainstorm ideas, draft stories, or write poems.
- **✅ Feedback Loop System**: After receiving a response, users can submit feedback (Thumbs up / Thumbs down). This is correctly logged locally without triggering redundant loops.
- **💅 Beautiful UI**: Features a modern, responsive, pre-formatted design with elegant state retention and error handling.

## 🛠 Prerequisites
- Python 3.7+
- OpenRouter API Key (Get one at [OpenRouter.ai](https://openrouter.ai/))

## 🚀 Setup & Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Sachinsepp/Assistify.git
   cd Assistify
   ```

2. **Create a virtual environment** (optional but highly recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Environment Variables**:
   Create a `.env` file at the root of the project directory and insert your API key:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Web Interface**:
   Open a browser and navigate to `http://127.0.0.1:5000`

## 🧠 Tech Stack Overview
- **Backend Architecture**: Flask (Python)
- **Frontend**: Custom HTML/CSS with Jinja2 Templating
- **AI Infrastructure**: OpenRouter API (`openai/gpt-3.5-turbo`)

## 📝 Recent Updates
- Enhanced text rendering (`white-space: pre-wrap`) so AI outputs like lists and paragraphs retain their format.
- Resolved feedback submission loop bug, ensuring correct UI behaviors post-feedback.
- Added API timeout handling to prevent server hanging during OpenRouter outages.
- Select-box state persistance across queries to improve UX.
