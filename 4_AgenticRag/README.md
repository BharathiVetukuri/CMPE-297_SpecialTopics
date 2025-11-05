# 🧾 Personal Expense Assistant (Multimodal Agentic RAG App)

## 📘 Overview
This project implements a **Full-Stack End-to-End Multimodal Agentic Application** using the **Google Agent Development Kit (ADK)** and **Vertex AI Gemini 2.5** model.

The application is a **Personal Expense Assistant** capable of:
- Extracting and analyzing information from receipts (images + text)  
- Storing and querying expense data  
- Providing natural-language answers and insights about your expenses  
- Integrating frontend, backend, database, and RAG (Retrieval-Augmented Generation) components

This project demonstrates a **complete multimodal agent workflow**:  
Frontend → Backend (API) → ADK Agent → Vertex AI Model → Database.

---

## 🎥 Demo Video
🎬 Watch the full walkthrough here: https://youtu.be/B-Zt-b04IZs 

---

## 📸 Screenshots

**Firestone Indexes**

<img width="900" height="700" alt="image" src="https://github.com/user-attachments/assets/aacb1290-6117-4203-b899-9da8bbf272c3" />

---

**Agent Web UI**

<img width="900" height="700" alt="image" src="https://github.com/user-attachments/assets/e34ce165-483b-4e43-9cfb-416ab09217b9" />

<img width="900" height="700" alt="image" src="https://github.com/user-attachments/assets/48975d05-6916-48ef-93c0-9f939c390c29" />

<img width="900" height="700" alt="image" src="https://github.com/user-attachments/assets/271b6349-1572-4c5d-b72f-50d7763a327f" />

---

**Frontend Service Using Gradio**

<img width="900" height="200" alt="image" src="https://github.com/user-attachments/assets/de911203-e42f-44be-ad62-1a2c9016c591" />

---

## 🏗️ Project Structure

    personal-expense-assistant/
    │
    ├── expense_manager_agent/
    │ ├── agent.py # Main ADK agent definition
    │ ├── tools.py # Functions to handle DB + storage operations
    │ ├── callbacks.py # Pre-processing hooks for image data
    │ ├── task_prompt.md # Agent prompt instructions
    │ └── init.py
    │
    ├── backend/
    │ ├── main.py # FastAPI backend (REST endpoints)
    │ ├── db_utils.py # Database connection & query logic
    │ └── requirements.txt
    │
    ├── frontend/
    │ └── index.html / app.js / ... # Simple web frontend for user interaction
    │
    ├── settings.yaml # Project + environment configuration
    ├── requirements.txt # Python dependencies
    ├── README.md # This file
    └── .env / .venv # Environment setup

---

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/e76b9e59-4cb4-47b7-8e4e-5ad0acdbadf9" />





