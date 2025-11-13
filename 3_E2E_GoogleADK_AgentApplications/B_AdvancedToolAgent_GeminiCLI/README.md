# 🚀 Gemini CLI on ADK — Automated Code Intelligence Agent

> **Advanced Tool Agent Assignment**  
> *Build an advanced tool agent which uses Gemini CLI as a tool inside an ADK pipeline.*

---

## 🎥 Demo Video

**🔗 https://youtu.be/Mh2f4zksPkE**

---

## 📖 Overview

This project integrates **Gemini CLI’s non-interactive mode** into a **Google ADK (Agent Development Kit)** pipeline, creating a powerful autonomous development assistant capable of:

- Intelligent file and module analysis  
- Automated test-plan generation and code refactoring  
- Context-aware file editing and development command execution  
- Running seamlessly inside **ADK Dev UI** and **Cloud Run**

It combines **LLM reasoning** with **tool execution** to form a developer agent that can understand your codebase, perform real-world engineering tasks, and respond conversationally.

---

## ✨ Key Features

| Feature | Description |
|----------|--------------|
| ✅ **Gemini CLI Integration** | Wraps Gemini CLI’s headless mode; executes deep code analysis and file discovery. |
| ⚙️ **Automated Software Development Tasks** | Generate test plans, create unit tests, explain code modules, suggest improvements, and refactor code. |
| 🤖 **ADK Integration** | Exposes Gemini CLI as a callable tool inside a Google ADK Agent; accessible via Dev UI or CLI. |
| ☁️ **Cloud-Ready Deployment** | Includes Cloud Build + Cloud Run configs for one-click deployment. |
| 🧠 **End-to-End Intelligence** | Combines Gemini CLI reasoning with ADK’s agent orchestration and FastAPI-based UI. |

---

## 🧩 Project Structure

      gemini-cli-on-adk/
      ├── app/ # Core ADK agent + Gemini CLI tool
      │ ├── agent.py # Main agent integrating Gemini CLI
      │ ├── server.py # FastAPI server powering ADK Dev UI
      │ └── utils/ # Helper utilities
      ├── deployment/ # Cloud Run deployment configs
      ├── notebooks/ # Experiments & exploratory notebooks
      ├── tests/ # Unit tests and automation scripts
      ├── cloudbuild.yaml # Cloud Build pipeline for deployment
      ├── Dockerfile # Container image configuration
      ├── pyproject.toml # Poetry / dependency management
      └── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

      git clone https://github.com/your-username/gemini-cli-on-adk.git
      cd gemini-cli-on-adk

### 2️⃣ Install Dependencies

      pip install -U pip poetry
      poetry install --no-root

### 3️⃣ Configure Gemini CLI

      Install Gemini CLI globally:
      
      nvm install 20
      npm install -g @google/gemini-cli
      gemini

      Then create a .env file:

      cat > .env << 'EOF'
      # Gemini CLI Configuration
      GEMINI_CLI_BIN="gemini"
      GEMINI_CLI_TIMEOUT="120"
      EOF

---

## ▶️ Running the Project

### Run Agent in CLI Mode
      

      poetry run adk run app
      
      
      You’ll enter an interactive chat session:
      
      Running agent gemini_cli_agent. Type exit to quit.

### Run ADK Dev UI (FastAPI)

      poetry run uvicorn app.server:app --host 0.0.0.0 --port 8080

---

## Prompts Used and Agent Response in Web UI

### 1. Explain the codebase

<img width="840" height="527" alt="Screenshot 2025-11-12 at 8 39 28 PM" src="https://github.com/user-attachments/assets/24c99914-b3ad-461d-9de5-873354fe3849" />

### 2. Generate a test plan for this project.

<img width="840" height="527" alt="Screenshot 2025-11-12 at 8 39 40 PM" src="https://github.com/user-attachments/assets/5e086b2a-4763-4d85-b57f-ca4d75fb12fa" />

### 3. Can you create a readme.md file for this?

<img width="840" height="527" alt="Screenshot 2025-11-12 at 8 43 38 PM" src="https://github.com/user-attachments/assets/037b19ba-263b-4803-90a4-d28e8c587269" />

---

##  🧱 Architecture Overview


            User (Prompt)
                   │
                   ▼
              ┌──────────────────────────────┐
              │  ADK Agent (app/agent.py)   │
              │  ─ Handles conversation      │
              │  ─ Invokes tools             │
              └──────────────┬───────────────┘
                             │
                             ▼
                   ┌─────────────────────┐
                   │ Gemini CLI Tool     │
                   │ (non-interactive)   │
                   ├─────────────────────┤
                   │  Code discovery     │
                   │  Deep analysis      │
                   │  Test generation    │
                   │  Refactoring        │
                   └─────────────────────┘
                             │
                             ▼
                    ┌────────────────────┐
                    │  FastAPI / ADK UI │
                    │  Cloud Run Ready   │
                    └────────────────────┘

---

## 🧠 How It Works

| Component | Role |
|------------|------|
| **Gemini CLI** | Performs actual code intelligence using non-interactive mode. |
| **ADK Agent (`app/agent.py`)** | Acts as orchestrator; passes user tasks to Gemini CLI. |
| **FastAPI Server (`app/server.py`)** | Exposes Dev UI and REST endpoints. |
| **Cloud Build + Run** | Enables deployment of the interactive agent as a microservice. |





