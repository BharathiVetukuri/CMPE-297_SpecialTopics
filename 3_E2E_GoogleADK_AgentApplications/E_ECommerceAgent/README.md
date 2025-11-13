# 🛍️ E-Commerce Agent with Google ADK and AlloyDB

This project implements a production-quality AI-powered E-Commerce Agent using Google’s Agent Developer Kit (ADK) and AlloyDB following the official Google Codelab

## 🎥 Demo Video
Watch the full walkthrough here: https://youtu.be/dzwmOLKzNMI 

---

## 📘 Overview

The E-Commerce Agent is a conversational AI system that integrates Google Vertex AI, AlloyDB, and ADK (Agent Developer Kit) to enable intelligent product discovery, recommendation, and customer interaction.

It demonstrates:

* Secure backend integration with AlloyDB for relational + vector search

* Vertex AI integration for model inference and embeddings

* Role-based authorization and protection against prompt injection

* Cloud-native deployment practices with production-ready setup

---
## 🔗 References

**Codelab Tutorial:**

Build Production Quality E-Commerce Agent with ADK

**Source Code:**

GitHub: mtoscano84/sports-agent-adk-mcp-alloydb

---

## ⚙️ Steps Followed

I completed every step from the official Google Codelab, including:

**1. Environment Setup**

* Created a new GCP project and enabled required APIs
(aiplatform.googleapis.com, alloydb.googleapis.com, etc.)

* Configured Cloud Shell and cloned the reference repository

**2. AlloyDB Setup**

* Created an AlloyDB cluster and instance

* Enabled Public IP Connectivity

* Authorized Cloud Shell IP range (e.g., 10.88.0.0/16)

**3. Vertex AI Integration**

* Retrieved the Project Number and granted IAM roles
(roles/aiplatform.user) to the AlloyDB service account

**4. Database Initialization**

* Accessed AlloyDB Studio

* Created required tables (users, products, orders, etc.)

* Inserted a sample user record matching my GCP email ID

**5. Authorization Service Setup**

* Enabled PostGIS extension for spatial queries

* Added sample data and verified access controls

**6. Application Deployment**

* Built and ran the ADK E-Commerce Agent locally

* Tested connection to Vertex AI and AlloyDB

* Verified end-to-end flow: query → model → DB → response

---

## 🧱 Tech Stack

| Component | Technology Used |
|------------|----------------|
| **Database** | AlloyDB (PostgreSQL-compatible with vector support) |
| **AI Services** | Vertex AI (models + embeddings) |
| **Agent Framework** | Google Agent Developer Kit (ADK) |
| **Backend** | Python / Node.js (as per Codelab reference) |
| **Deployment** | Google Cloud Shell & GCP Console |
| **Security** | IAM Roles, OAuth Client, Authorization Service |

---

## 🧩 Key Learnings

* Seamless integration of AlloyDB with Vertex AI for hybrid relational-vector workloads

* Using ADK to rapidly build secure, production-grade conversational agents

* Practical experience with IAM roles, Public IP configuration, and service account permissions

* Understanding PostGIS for location-based data storage

---

## 📦 Repository Contents

      E_ECommerceAgent/
       ├── sports-agent-adk-mcp-alloydb/
       │   ├── src/
       │   ├── scripts/
       │   ├── .env.example
       │   ├── requirements.txt / package.json
       │   └── README.md  ← (this file)

---

## 🚀 Running the Agent

      # 1. Clone the repo
      git clone https://github.com/BharathiVetukuri/CMPE-297_SpecialTopics.git
      cd 3_E2E_GoogleADK_AgentApplications/E_ECommerceAgent/sports-agent-adk-mcp-alloydb
      
      # 2. Install dependencies
      npm install   # or pip install -r requirements.txt
      
      # 3. Configure environment variables
      cp .env.example .env
      # Add your CLIENT_ID, PROJECT_ID, and DB credentials
      
      # 4. Start the agent
      npm start
      # or python main.py

---

## 📸 Screenshots

#### AlloyDB Cluster

<img width="880" height="400" alt="image" src="https://github.com/user-attachments/assets/a2f64a5f-92b5-41b5-aac2-56d0b583faa9" />


#### Loading Database

<img width="840" height="468" alt="Screenshot 2025-11-13 at 12 06 38 AM" src="https://github.com/user-attachments/assets/4171e3a3-f6b1-4c51-b583-f91b98d7e4bf" />

<img width="840" height="445" alt="Screenshot 2025-11-13 at 12 12 35 AM" src="https://github.com/user-attachments/assets/db4de32e-f652-424f-bf01-82827dddb7ed" />


<img width="840" height="443" alt="Screenshot 2025-11-13 at 12 18 56 AM" src="https://github.com/user-attachments/assets/bb8f1104-3939-41ed-b99c-06482717f435" />


#### Authorization Service Setup

<img width="840" height="420" alt="Screenshot 2025-11-13 at 12 20 56 AM" src="https://github.com/user-attachments/assets/0c03a85b-7a70-4ec3-b69d-00469aea8bf9" />

<img width="840" height="456" alt="Screenshot 2025-11-13 at 12 24 30 AM" src="https://github.com/user-attachments/assets/b22675c4-be57-40aa-9813-3aa4b81cf82b" />

<img width="840" height="456" alt="Screenshot 2025-11-13 at 12 25 46 AM" src="https://github.com/user-attachments/assets/2bef80d4-c1a7-484d-8385-19194f75bb2c" />


<img width="840" height="356" alt="Screenshot 2025-11-13 at 12 26 23 AM" src="https://github.com/user-attachments/assets/4b1e68b6-8a3d-4399-8f20-3b7bb954d50d" />


<img width="840" height="376" alt="Screenshot 2025-11-13 at 12 28 43 AM" src="https://github.com/user-attachments/assets/485916dc-0662-40d1-b011-7362e0b0560b" />


#### MCP ToolBox Setup

<img width="840" height="376" alt="Screenshot 2025-11-13 at 12 38 04 AM" src="https://github.com/user-attachments/assets/6f7bcaad-b327-4423-bebf-bb9169ab0ee8" />

<img width="840" height="376" alt="Screenshot 2025-11-13 at 12 38 14 AM" src="https://github.com/user-attachments/assets/d8345ae4-93cd-46ea-93df-b4b144144029" />

<img width="840" height="584" alt="Screenshot 2025-11-13 at 12 38 58 AM" src="https://github.com/user-attachments/assets/1f684750-0c38-49d4-acee-bcb915205075" />


#### Agent Build on ADK

<img width="940" height="238" alt="Screenshot 2025-11-13 at 12 52 53 AM" src="https://github.com/user-attachments/assets/4eebbfed-ba24-4a6f-830e-394287c78510" />


#### Frontend Deployment

<img width="940" height="554" alt="Screenshot 2025-11-13 at 12 57 43 AM" src="https://github.com/user-attachments/assets/c4620946-8997-4049-bf5a-9e1a3abf3111" />


<img width="940" height="554" alt="Screenshot 2025-11-13 at 12 58 01 AM" src="https://github.com/user-attachments/assets/8c32ea4c-2eb8-4011-ab52-5f38a014528f" />


#### Run Agent and Prompts Testing

<img width="940" height="554" alt="Screenshot 2025-11-13 at 12 59 46 AM" src="https://github.com/user-attachments/assets/adfd3e95-536c-49f1-805a-60e96cd2c05e" />


<img width="940" height="554" alt="Screenshot 2025-11-13 at 1 00 28 AM" src="https://github.com/user-attachments/assets/23a42a5c-b9f8-407b-8662-5bcad01d77f2" />
