# 🛒 Purchasing Concierge A2A — Google Agent-to-Agent Action Engine

## 📘 Overview
This project implements **Codelab 3: Getting Started with A2A Action Engine**, part of the **MCP and A2A Codelabs Assignment**.  
It demonstrates building and deploying a **Purchasing Concierge Agent** that interacts with seller agents through the **A2A (Agent-to-Agent)** protocol using **Google ADK** and **A2A SDK**.

The app features a simple **Gradio UI** for users to interact with the purchasing agent and test multi-agent communication.

---
# 🎥 Demo Video: 
---

## 🧠 Key Concepts Demonstrated
- Multi-agent system using **Google ADK + A2A SDK**
- Python environment management using **uv**
- **Gradio** front-end interface for interaction
- Agent communication via **A2A Action Engine**
- Deployment to **Google Cloud Run** (serverless container)
- Clean DevOps workflow with **Dockerfile** + **deploy script**

---

## 🧩 Directory Structure

    purchasing-concierge-a2a/
    │
    ├── purchasing_concierge_ui.py # Main Gradio app
    ├── purchasing_concierge/ # Agent implementation
    ├── remote_seller_agents/ # Seller agent simulation
    │
    ├── pyproject.toml # Dependencies (uv / poetry style)
    ├── uv.lock # Dependency lock file
    ├── Dockerfile # For Cloud Run container build
    ├── deploy_to_cloud_run.sh # Deployment script
    │
    ├── README.md # Project documentation
    └── README-DEPLOY.md # Technical deployment guide


# Screenshots

### 1. Workshop Development Setup**

<img width="906" height="602" alt="image" src="https://github.com/user-attachments/assets/61625bed-c474-4523-9bb1-fd0fda851fdd" />

### 2. Deploying Burger Seller Agent - A2A Server

**a. Service Deployment:**

<img width="906" height="602" alt="image" src="https://github.com/user-attachments/assets/0dbcc629-ecf3-43e4-9976-c14ff9067a57" />

**b. burger agent card information:**

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/1f2fc658-98bb-4d5f-bba3-537c0dc9ebce" />

**c. Updating the Burger Agent URL Value on Agent Card via Environment Variable**

<img width="604" height="409" alt="Screenshot 2025-10-30 at 9 28 30 PM" src="https://github.com/user-attachments/assets/194f0fa1-cf91-4991-8177-a8900ca3fac2" />

**d. Updated Card Information:**

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/64925800-62d0-4c65-b22a-403344878d9f" />


### 3. Deploying Pizza Seller Agent

**a. Service Deployment:**

<img width="908" height="424" alt="image" src="https://github.com/user-attachments/assets/0dc41927-aeb1-4a27-af68-887bdf5b8f97" />


**b. Pizza agent card information:**

<img width="842" height="438" alt="image" src="https://github.com/user-attachments/assets/253cb750-2d96-4adc-bcf7-18e79800b30c" />

**c. Updated Card Information After HOST_OVERRIDE:**

<img width="904" height="498" alt="image" src="https://github.com/user-attachments/assets/94b3446d-d009-4722-b07e-85bd08884a92" /> 

## 4. Deploying the Purchasing Concierge - A2A Client to Agent Engine

<img width="936" height="482" alt="image" src="https://github.com/user-attachments/assets/34037904-7897-4358-b16a-94e4e83996cb" />

**Testing the Deployed Agent on Agent Engine:**

<img width="2836" height="896" alt="image" src="https://github.com/user-attachments/assets/7f9b3b0e-7986-4940-a19b-93d19af2bb37" />

### 5. Integration Testing and Payload Inspection

<img width="906" height="532" alt="image" src="https://github.com/user-attachments/assets/1581834d-2750-4154-8863-f1c15f896a6b" />

<img width="906" height="532" alt="image" src="https://github.com/user-attachments/assets/88041277-a2a2-4c78-b0b9-a448aded1092" />

<img width="906" height="532" alt="image" src="https://github.com/user-attachments/assets/a8e663c4-db0b-4255-bd76-3f98e2f7c333" />

<img width="906" height="532" alt="image" src="https://github.com/user-attachments/assets/67f5405a-ce24-482b-b4d3-fc45372a265a" />







