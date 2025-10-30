# 🧠 Getting Started with ADK, MCP, and A2A

## 🎯 Goal
This codelab demonstrates how to build and expose an **AI Agent** that connects to a **Model Context Protocol (MCP) Server** using the **Agent Development Kit (ADK)** and exposes itself via the **Agent-to-Agent (A2A)** protocol.

The objective is to understand:
- How MCP enables tools to be discovered and called by agents.
- How ADK simplifies building agents that consume MCP tools.
- How A2A allows agents to communicate securely and consistently.

---
## Youtube Video: https://youtu.be/5URfZ5liFXQ 

---


## 🏗️ Project Overview

**Codelab:** [Getting Started with ADK, MCP, and A2A](https://codelabs.developers.google.com/codelabs/currency-agent#0)

This project implements a **Currency Agent** that can answer currency conversion queries using a remote **MCP server** deployed on **Cloud Run**.

The project includes:
1. **MCP Server (`mcp-server/`)** – exposes a `get_exchange_rate` tool calling the [Frankfurter API](https://www.frankfurter.app/).
2. **Currency Agent (`currency_agent/`)** – an ADK-based agent consuming the MCP tool.
3. **A2A Server** – exposes the agent for other agents/clients using the A2A protocol.
4. **A2A Client Test (`currency_agent/test_client.py`)** – sends requests and validates agent responses.

---

## 🧩 Folder Structure

      currency-agent/
      │
      ├── mcp-server/ # MCP server code and deployment configs
      │ ├── server.py # Main MCP server entrypoint
      │
      ├── currency_agent/ # Currency ADK agent implementation
      │ ├── agent.py # Defines agent + to_a2a() wrapper
      │ ├── test_client.py # A2A test client script
      │ └── ...
      │
      ├── .env # Environment variables (Vertex AI + Project)
      ├── pyproject.toml
      ├── uv.lock
      └── README.md 

---

## ⚙️ Setup & Execution

### 1. Clone and configure project

      git clone https://github.com/<your-username>/currency-agent.git
      cd currency-agent
      export PROJECT_ID=assignment2-476319
      gcloud config set project $PROJECT_ID
      
### 2. Enable necessary APIs

      gcloud services enable cloudresourcemanager.googleapis.com \
                             servicenetworking.googleapis.com \
                             run.googleapis.com \
                             cloudbuild.googleapis.com \
                             artifactregistry.googleapis.com \
                             aiplatform.googleapis.com \
                             compute.googleapis.com
                             
### 3. Deploy the MCP server to Cloud Run

      cd mcp-server
      gcloud run deploy mcp-server --no-allow-unauthenticated --region=us-central1 --source .

### 4. Start Cloud Run proxy (Terminal 1)

      gcloud run services proxy mcp-server --region=us-central1

### 5. Test remote MCP server (Terminal 2)

      cd ~/currency-agent
      uv run mcp-server/test_server.py

Expected:

{
  "amount": 1.0,
  "base": "USD",
  "date": "2025-05-26",
  "rates": { "EUR": 0.87866 }
}

### 6. Start the A2A Agent server (Terminal 2)

      cd ~/currency-agent
      uv run uvicorn currency_agent.agent:a2a_app --host localhost --port 10000

Output:

INFO: Uvicorn running on http://localhost:10000 (Press CTRL+C to quit)

### 7. Verify the Agent Card (Terminal 3)

      curl http://localhost:10000/.well-known/agent.json | python -m json.tool

### 8. Run A2A Test Client

      cd ~/currency-agent
      uv run currency_agent/test_client.py

Expected:

--- ✅ Connection successful. ---
--- 📥 Single Turn Request Response ---
Based on the current exchange rate, 1 USD = 1.37 CAD. 100 USD = 137 CAD.

### 9. Check Cloud Run Logs

      gcloud run services logs read mcp-server --region=us-central1 --limit 10

Look for get_exchange_rate call confirmation.


## 🧠 Learning Outcomes

* Deploying an MCP server securely on Cloud Run.

* Integrating MCP tools into an ADK-based agent.

* Exposing and testing an agent with the A2A protocol.

Understanding agent-to-agent communication flow.

## Screenshots

### 1. Start MCP Server

<img width="940" height="861" alt="Screenshot 2025-10-27 at 11 30 11 PM" src="https://github.com/user-attachments/assets/4c511962-133a-4401-9f01-fd73209772ab" />


### 2. Local MCP Server

<img width="940" height="66" alt="Screenshot 2025-10-27 at 11 59 22 PM" src="https://github.com/user-attachments/assets/87863868-a736-4f02-abaa-2f504476c2b4" />

### 3. Test Remote MCP Server

<img width="940" height="130" alt="Screenshot 2025-10-28 at 12 00 01 AM" src="https://github.com/user-attachments/assets/cba731b7-a8b2-4347-a740-8357dbca460c" />

### 4. Deploy MCP Server

<img width="940" height="190" alt="Screenshot 2025-10-27 at 11 46 00 PM" src="https://github.com/user-attachments/assets/4c9a3b1f-bdb7-4a49-ac2c-dad0943359e4" />

### 5. Authenticating MCP Clients

<img width="940" height="224" alt="Screenshot 2025-10-27 at 11 47 28 PM" src="https://github.com/user-attachments/assets/0d4c22f8-6f8a-4b9f-8293-58615fae9b26" />


### 6. Currency Agent

<img width="940" height="317" alt="Screenshot 2025-10-28 at 12 03 47 AM" src="https://github.com/user-attachments/assets/c7f46791-799b-4d03-be0f-2eab4a6e4b0d" />

### 7. Test the A2A Server

<img width="940" height="652" alt="Screenshot 2025-10-28 at 12 57 06 AM" src="https://github.com/user-attachments/assets/c5d85dd5-49ba-4442-93b4-7b5c41cb9a58" />




