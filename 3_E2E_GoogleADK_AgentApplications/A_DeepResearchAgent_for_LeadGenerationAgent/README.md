# 🤖 Deep Research Lead Generation Agent using Google ADK

## 📘 Overview
This project implements an **end-to-end Deep Research Agent** for **lead generation**, built using **Google’s Agent Development Kit (ADK)**.  
It follows the official [Google Cloud Blog Codelab](https://cloud.google.com/blog/products/ai-machine-learning/build-a-deep-research-agent-with-google-adk) and replicates the workflow of the open-source project [MagnIeeT/leadGenerationAgentADK](https://github.com/MagnIeeT/leadGenerationAgentADK).

The agent performs **pattern discovery** and **lead generation** by analyzing successful companies in a target industry and geography, then identifying similar potential leads.  

This repository demonstrates:
- Local agent execution via ADK CLI
- Cloud deployment to **Vertex AI Reasoning Engine**
- Cloud testing and interaction
- Logging, configuration, and environment setup for reproducibility

---

# 🎥 Video Walkthrough: https://youtu.be/Cx_VfDOlhqo 

---

## 🧠 Project Architecture

<img width="704" height="568" alt="image" src="https://github.com/user-attachments/assets/29b9c4d6-07e2-4d7a-acea-35085c0d96cf" />


The agent orchestrates research and reasoning sub-agents to extract insights and generate high-quality business leads.

---

## ⚙️ Environment Setup

### 1️⃣ Clone the repository

            git clone https://github.com/<your-username>/LeadGenerationAgentADK.git
            cd LeadGenerationAgentADK

### 2️⃣ Install dependencies

            pip install poetry
            poetry install

### 3️⃣ Configure environment

            GOOGLE_CLOUD_PROJECT=st-assignment3
            GOOGLE_CLOUD_LOCATION=us-central1
            GOOGLE_GENAI_USE_VERTEXAI=True
            GOOGLE_CLOUD_STORAGE_BUCKET=myassignment3bucket
            GEN_FAST_MODEL=gemini-2.0-flash
            GEN_ADVANCED_MODEL=gemini-2.5-pro
            REASONING_ENGINE_ID="projects/170443623105/locations/us-central1/reasoningEngines/4193145922198175744"

### 4️⃣ Authenticate to Google Cloud

            gcloud auth application-default login
            gcloud config set project st-assignment3
            gcloud services enable aiplatform.googleapis.com

### 🧩 Running Locally

            poetry run adk run LeadGenerationResearch

### Sample Interaction

            [user]: Find fintech leads in Thailand
            [InteractiveLeadGenerator]: It seems the Thai fintech market is dominated by local companies.
            [user]: Find 5 leads for SaaS companies expanding into Brazil.
            [InteractiveLeadGenerator]: The SaaS market in Brazil shows similar domestic dominance.

### 🚀 Deploying to Vertex AI Reasoning Engine

            poetry run python deployment/deploy.py --create

### ☁️ Testing the Cloud-Hosted Agent

            poetry run python deployment/test_deploy.py

### Sample Session:

            Running cloud agent InteractiveLeadGenerator
            [user]: Find fintech leads in Thailand
            [Agent]: The Thai fintech market is primarily domestic-driven.

---

# 📸 Screenshots

### Agent Interaction

<img width="864" height="450" alt="image" src="https://github.com/user-attachments/assets/912b20e2-8051-4ff9-ad5c-606e72152311" />


### Successful Deployment

<img width="864" height="450" alt="image" src="https://github.com/user-attachments/assets/118c4555-6cee-4af5-99a3-1958b0b02797" />


### Logs

<img width="864" height="450" alt="image" src="https://github.com/user-attachments/assets/d82af0a8-f877-4eb5-b451-51d6ec003dda" />

---

## 🗂️ Repository Structure

            leadGenerationAgentADK/
            │
            ├── LeadGenerationResearch/        # Agent source code
            ├── deployment/                    # Deployment & test scripts
            ├── publish/                       # AgentSpace publishing utilities
            ├── screenshots/                   # Demo screenshots
            ├── .env, env_example              # Environment configuration
            ├── README.md                      # Project documentation
            ├── pyproject.toml, poetry.lock    # Dependency management
---

# 🧠 Learnings & Reflections

* Learned to use Google ADK for multi-agent orchestration

* Explored Reasoning Engine deployment on Vertex AI

* Understood pattern discovery and lead generation pipelines

* Encountered and resolved deployment URI issues (e.g., gs://gs://bucket fix)

---

# 🏁 Conclusion

- This project demonstrates how to design and deploy a deep research agent for lead generation using Google Cloud ADK and Vertex AI Reasoning Engines.

- It integrates intelligent orchestration, pattern analysis, and scalable deployment — showcasing a modern agentic architecture for enterprise research workflows.
