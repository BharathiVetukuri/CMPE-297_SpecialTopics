# Education Path Advisor (ADK)

An AI agent (built with Google’s Agent Development Kit) that guides students on education & career pathways—degrees, courses, skills, and next steps—using multi-agent orchestration.

### 🎥 Demo Video: 
https://youtu.be/HVWtdzB9MIw 

## 🖼️ Screenshots

1. Agent Interaction in Terminal

<img width="2878" height="1720" alt="image" src="https://github.com/user-attachments/assets/361c8209-371c-4817-8189-5cc8db1752f6" />


2. Agent Interaction in Web UI

<img width="2878" height="1720" alt="image" src="https://github.com/user-attachments/assets/c2762bcd-9305-41aa-b21b-036c4a58ca7b" />


## ✨ What it does

* Answers “what can you do for me?” with capabilities overview

* Suggests education paths based on interests, background, and goals

* Compares related paths (e.g., Data Science vs. Software Engineering)

* Proposes course sequences, skills to build, projects, and timelines

* Generates action plans (short-term / long-term)

## 📁 Project Structure

education_path_advisor/
├─ education_advisor/
│  ├─ agent.py
│  ├─ prompt.py
│  └─ sub_agents/
├─ tests/
├─ eval/
├─ .env.example
├─ pyproject.toml
└─ README.md


## ✅ Prerequisites

Cloud Shell or local machine with Python 3.10+

Poetry (Cloud Shell usually has it; otherwise install with pipx install poetry)

A Gemini API key (or use Vertex AI—see optional setup below)

Get an API key: https://aistudio.google.com/app/apikey

## ⚙️ Setup

Clone the repo and enter the project folder:

  git clone https://github.com/awesome-adk-agents/education-path-advisor.git
  cd education-path-advisor   # or: awesome-adk-agents/my-adk-agents/education_path_advisor


  Create .env (Gemini API key mode):

  cat > .env << 'EOF'
  GOOGLE_GENAI_USE_VERTEXAI=FALSE
  GOOGLE_API_KEY=REPLACE_WITH_YOUR_KEY
  EOF


Install dependencies with Poetry:

  poetry install

## ▶️ Run the Agent
A) Terminal (interactive)
    poetry run adk run .


B) Web UI (ADK Dev UI)
    poetry run adk web


## 🙏 Credits

Original hackathon project list: awesome-adk-agents ( https://github.com/Sri-Krishna-V/awesome-adk-agents )

Built with Google Agent Development Kit (ADK) and Gemini
