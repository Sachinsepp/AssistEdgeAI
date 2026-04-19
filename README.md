# Assistify

Assistify is an AI-powered web assistant built with Flask and the OpenRouter API. It allows users to query an AI model for answering questions, summarizing text, or generating creative content, all from a simple, elegant web interface.

## Features
- **Ask Questions**: Quickly get answers to any questions.
- **Summarize Text**: Paste block descriptions and summarize them effortlessly.
- **Creative Content**: Ask the AI to write stories, brainstorm ideas, and more.
- **Feedback Collection**: Easily track user satisfaction to see if the responses were helpful or not.

## Prerequisites
- Python 3.7+
- OpenRouter API Key

## Setup & Installation

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd Assistify
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenRouter API Key in a `.env` file at the root of the project directory:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Access the application:
   Go to `http://127.0.0.1:5000` in your web browser.

## Tech Stack
- Backend: Flask
- Frontend: HTML/CSS/Jinja
- API: OpenRouter (OpenAI GPT-3.5-Turbo defaults)
