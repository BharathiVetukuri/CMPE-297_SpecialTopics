# 🧠 Code Review Assistant — Built with Google ADK and Gemini Models

This project implements a **production-quality multi-agent Code Review Assistant** using the **Google Agent Development Kit (ADK)** and **Vertex AI Gemini models**.  
It follows the official codelab: [Build a Code Review Assistant](https://codelabs.developers.google.com/adk-code-reviewer-assistant/instructions?hl=en).

---

## Youtube Demo Video:

**https://youtu.be/e5jwdzMrm1I**

---

## 🚀 Overview

The **Code Review Assistant** performs an intelligent multi-stage review of Python code using a sequence of agents:

1. **Code Analyzer** — Parses code structure via Python AST.  
2. **Style Checker** — Runs `pycodestyle` and reports PEP8 issues.  
3. **Test Runner** — Executes synthetic tests and evaluates robustness.  
4. **Feedback Synthesizer** — Combines insights into a human-readable review.

Each agent runs asynchronously and shares state through ADK’s built-in context management system, delivering a realistic simulation of a collaborative AI review pipeline.

---

## 🧩 Project Structure

  adk-code-review-assistant/
  │
  ├── code_review_assistant/
  │ ├── agent.py # Root agent orchestration (root_agent)
  │ ├── tools.py # AST analyzer, helpers, and utilities
  │ ├── config.py # Project configuration (.env loader)
  │ ├── constants.py # Shared state keys
  │ ├── sub_agents/
  │ │ └── review_pipeline/ # Individual stage agents
  │ │ ├── code_analyzer.py
  │ │ ├── style_checker.py
  │ │ ├── test_runner.py
  │ │ └── feedback_synthesizer.py
  │ └── init.py
  │
  ├── tests/
  │ └── test_code_analyzer.py # Unit test for code analysis tool
  │
  ├── .env # Environment configuration
  ├── pyproject.toml # Poetry / pip configuration
  ├── adk.yaml # ADK entrypoint: code_review_assistant.agent:root_agent
  └── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

  git clone https://github.com/ayoisio/adk-code-review-assistant.git
  cd adk-code-review-assistant

### 2️⃣ Create and Activate a Virtual Environment

  python -m venv .venv
  source .venv/bin/activate   # (on Windows: .venv\Scripts\activate)

### 3️⃣ Install Dependencies

  pip install -r code_review_assistant/requirements.txt
  pip install -e .

### 4️⃣ Configure Environment Variables

  Create a .env file in the project root:
  
  GOOGLE_CLOUD_PROJECT=
  GOOGLE_CLOUD_LOCATION=
  GOOGLE_GENAI_USE_VERTEXAI=TRUE

---
## 🔐 IAM and API Setup

Enable the required APIs and grant Cloud Build permissions:

  gcloud services enable aiplatform.googleapis.com compute.googleapis.com
  
  PROJECT_NUMBER=$(gcloud projects describe $GOOGLE_CLOUD_PROJECT --format="value(projectNumber)")
  SERVICE_ACCOUNT="${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com"
  
  for ROLE in roles/run.admin roles/iam.serviceAccountUser roles/cloudsql.admin roles/storage.admin
  do
    gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
      --member="serviceAccount:${SERVICE_ACCOUNT}" --role="$ROLE"
  done

---

## 🧪 Local Testing
  
**Run the analyzer test**

  python tests/test_code_analyzer.py

**Expected output:**

  INFO:code_review_assistant.tools:Tool: Analysis complete - 2 functions, 1 classes
  === Analyzer Response ===
  * Functions Found: 2
  * Classes Found: 1
  * No syntax errors detected.

## 🧠 Running the Agent (CLI Mode)

**Start the interactive Code Review Assistant:**

  adk run code_review_assistant
  
  
  Then at the [user]: prompt, enter:
  
  Please analyze this code:
  def add(a,b): return a+b


**Expected multi-agent output:**

  [CodeAnalyzer]: 1 function, 0 classes
  [StyleChecker]: 85/100 style score (E704, E231, E226, W292)
  [TestRunner]: All 20 synthetic tests passed
  [FeedbackSynthesizer]: Function works correctly; recommend adding docstring

---

## 📸 Screenshots

**First Agent - Deployment**

<img width="880" height="516" alt="image" src="https://github.com/user-attachments/assets/65d95feb-7861-4d2a-9bca-5a5115db70b5" />

<img width="880" height="516" alt="image" src="https://github.com/user-attachments/assets/f8f96bd7-c367-491b-8681-acbe508ed91b" />


**Successful Code Analyzer Setup**

<img width="880" height="514" alt="image" src="https://github.com/user-attachments/assets/428699a5-ef97-4936-83a5-f4f313cb298d" />

**Web UI**

<img width="880" height="450" alt="image" src="https://github.com/user-attachments/assets/effb6d58-c6e6-43b1-8aa7-e8fc3333988e" />


**Successful Multi Agent Pipeline Run**

<img width="2880" height="1726" alt="image" src="https://github.com/user-attachments/assets/6b6d66c3-6540-485f-8409-89eed894dafd" />

---

## ✅ Key Learnings

* Implemented multi-agent orchestration using SequentialAgent.

* Integrated Gemini-2.5-Flash and Gemini-2.5-Pro via Vertex AI.

* Performed deterministic analysis with Python AST.

* Demonstrated asynchronous execution with shared ADK state.

* Produced human-readable, educational feedback for code quality.


