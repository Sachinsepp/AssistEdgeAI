# Project Documentation: AssistEdgeAI

**AssistEdgeAI** is a lightweight, responsive, and elegant AI-powered web assistant built using Python, Flask, and the OpenRouter API. It allows users to quickly query a Large Language Model (GPT-3.5-Turbo by default) to answer questions, summarize complex texts, and brainstorm creative content directly from their browser.

---

## 📂 Codebase Structure

The project has a clean directory layout:

- 🐍 **[app.py](./app.py)**: The main Flask backend containing the server initialization, OpenRouter API request configuration, route definitions, and local logging functions.
- 🎨 **[templates/index.html](./templates/index.html)**: The single-page frontend user interface, incorporating vanilla CSS variables, responsive container layout, forms, dynamic Jinja2 templating, and basic state-clearing JavaScript.
- 🔑 **[.env](./.env)**: A local environment variables configuration file hosting the OpenRouter API key (`OPENROUTER_API_KEY`).
- 📝 **[requirements.txt](./requirements.txt)**: Specifies project library dependencies (`Flask`, `requests`, `python-dotenv`).
- 🛑 **[.gitignore](./.gitignore)**: Standard file specifying which directories and configurations to ignore (e.g., `.env`, local Python virtual environments `venv/`, `env/`, and PDF documentation).
- 💬 **[feedback.txt](./feedback.txt)**: A plain text logging store where user queries and feedback options (thumbs up/down ratings) are logged in UTF-8 format.

---

## ⚙️ Backend Architecture ([app.py](./app.py))

The Flask application processes data on a single view route and links to OpenRouter's endpoints.

### 1. API Client Function (`get_response` in [app.py](./app.py))
The function `get_response(prompt)` initiates a synchronous HTTP POST request to the OpenRouter Completions API:
- **Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
- **Headers**:
  - `Authorization: Bearer <API_KEY>` (securely retrieved using `dotenv` from `.env`)
  - `Content-Type: application/json`
- **Payload**:
  - `model`: `"openai/gpt-3.5-turbo"` (customizable model tag)
  - `messages`: A list containing the prompt as a user message.
- **Exception Handling**: Catches network/API exceptions and displays a custom warning emoji `⚠️ Error: [description]` to prevent server crashes.

### 2. Main Route Handler (`index` in [app.py](./app.py))
Registered at the root url `'/'` for both `GET` and `POST` methods.
- **GET Request**: Sets default variables (`result = ""`, `user_input = ""`, `task = ""`) and returns the clean page layout.
- **POST Request (New Query)**:
  - Captures `task` (the prompt prefix/category) and `user_input`.
  - Prefix modifiers are appended to standard tasks (e.g., creative writing or summarization).
  - Queries OpenRouter using `get_response(prompt)` and sets the output as `result`.
- **POST Request (Feedback Submission)**:
  - Activated when `feedback` is present in the form parameters.
  - Skips calling the OpenRouter API to prevent redundant queries.
  - Reads the previously cached `result` and `user_input` fields.
  - Logs the prompt and feedback rating to **[feedback.txt](./feedback.txt)**.
- **Rendering Context**: Returns variables (`result`, `user_input`, `task`) to Jinja2 to maintain UI state persistence and avoid blanking fields upon post requests.

---

## 🎨 UI & UX Design ([templates/index.html](./templates/index.html))

The user interface uses a modern, responsive layout built using CSS.

### Key CSS Features
- **Branding Typography & Palette**: Built using a modern Sans-Serif font-family with CSS `:root` variables:
  - `--primary`: Classic cobalt blue (`#0074cc`) for primary headings, focus states, and main submit buttons.
  - `--background`: Sky-blue hue (`#eaf4fc`) for an inviting page background.
  - `--white` / `--shadow`: Drop shadows (`rgba(0, 0, 0, 0.1)`) create a card layer effect.
- **Tagline**: Placed beneath the logo header highlighting key functionalities.
- **Format Preservation**: The response container (`.result p`) uses `white-space: pre-wrap;` to ensure markdown-like formatting (bullet points, linebreaks, code blocks) returned from the LLM displays perfectly on screen.

### UX Features
- **Active Task State Retention**: Options selected in the dropdown menu (`💬 Ask a question`, `📝 Summarize the text`, `🎨 Generate creative content`) remain selected after clicking submit using conditional Jinja2 clauses.
- **Reset Logic**: Integrated a JavaScript function `clearInputAndResponse()` that triggers `onchange` of the task selector. It automatically clears previous text inputs and response blocks to avoid clutter when switching tasks.
- **Feedback Form**: A feedback form appears conditionally after a response is generated. When feedback is submitted, a green-themed confirmation block replaces the form and outputs: *“✅ Thank you for your feedback!”*.

---

## 🚀 Execution & Command Reference

### Starting the Server
1. Navigate to the project directory:
   ```bash
   cd d:\Users\Assistify
   ```
2. Activate your virtual environment:
   ```bash
   # Windows cmd / powershell:
   .\venv\Scripts\activate
   ```
3. Run the entry point:
   ```bash
   python app.py
   ```
4. Access the site in your browser at `http://127.0.0.1:5000`.

### Database & Logging
User submissions and ratings are written on the fly to **[feedback.txt](./feedback.txt)** in the following format:
```text
Prompt: Summarize this text briefly:
[User's input text]
Feedback: yes

Prompt: Create something based on this idea: [User's input idea]
Feedback: no
```
