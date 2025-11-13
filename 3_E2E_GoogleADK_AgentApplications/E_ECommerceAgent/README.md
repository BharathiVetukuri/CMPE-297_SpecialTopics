# 🛍️ E-Commerce Agent with Google ADK and AlloyDB

This project implements a production-quality AI-powered E-Commerce Agent using Google’s Agent Developer Kit (ADK) and AlloyDB following the official Google Codelab

## 🎥 Demo Video
🎬 Watch the full walkthrough here: https://youtu.be/DxUCDeCzgjk 

---

## 📸 Screenshots


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

