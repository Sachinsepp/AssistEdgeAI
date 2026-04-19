from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#OpenRouter API Setup
# 🔐 API key and model setup
import os
from dotenv import load_dotenv

# 🌱 Load environment variables from .env file
load_dotenv()

# 🔐 Securely get the API key from .env
API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "openai/gpt-3.5-turbo"

def get_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=15)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    prompt_type = ""
    user_input = ""
    feedback = ""
    feedback_submitted = False

    if request.method == 'POST':
        prompt_type = request.form.get('task', '')
        user_input = request.form.get('user_input', '')
        feedback = request.form.get('feedback', '')

        if prompt_type == 'question':
            prompt = user_input
        elif prompt_type == 'summary':
            prompt = f"Summarize this text briefly:\n{user_input}"
        elif prompt_type == 'creative':
            prompt = f"Create something based on this idea: {user_input}"
        else:
            prompt = user_input

        # ✍️ Log feedback if submitted, otherwise query API
        if feedback:
            result = request.form.get('result', '')
            with open("feedback.txt", "a", encoding="utf-8") as f:
                f.write(f"Prompt: {prompt}\nFeedback: {feedback}\n\n")
            feedback_submitted = True
        else:
            result = get_response(prompt)

    return render_template("index.html", result=result, user_input=user_input, task=prompt_type, feedback_submitted=feedback_submitted)

if __name__ == "__main__":
    app.run(debug=True)
