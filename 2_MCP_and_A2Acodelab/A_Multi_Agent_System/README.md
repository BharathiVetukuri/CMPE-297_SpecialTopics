# 🧠 Multi-Agent Image Scoring System using Google ADK, MCP & A2A

## 🎯 Overview

This project implements a **multi-agent system** using the **Google Agent Development Kit (ADK)** and **Action-to-Action (A2A)** protocol.  
It demonstrates how to design, deploy, and interact with agents that can:

- Generate high-quality images based on natural-language prompts  
- Score the generated images against defined content and design guidelines  
- Deploy seamlessly to **Vertex AI Agent Engine** for scalable inference  
- Interoperate via the **A2A API layer**

This project was completed as part of the **MCP and A2A Codelabs Assignment**.

---

## 🎥 Demo Video
🎬 Watch the full walkthrough here:

---

## 📸 Screenshots
Stage	Screenshot
ADK Web UI	
Vertex AI Deployment	
A2A Agent Test	
Generated Image in GCS	

---

## 🧩 Architecture

```mermaid
graph TD
A[ADK Root Agent] --> B[Image Generation Agent]
A --> C[Image Scoring Agent]
C --> D[Checker Agent]
D --> E[Vertex AI Agent Engine]
E --> F[GCS Bucket (for images & artifacts)]
A2A[A2A API Server] --> A

## Components

* image_scoring/	--- Contains the ADK-based root and sub-agents (generation + scoring).
* image_scoring_adk_a2a_server/ ---	Runs the A2A API server for agent-to-agent communication.
* testclient/	--- Local test scripts to trigger remote reasoning-engine calls.
* dist/	--- Wheel and build artifacts generated for deployment.
* Vertex AI Agent Engine	--- Managed runtime used to deploy and test the agent remotely.
* GCS Bucket	--- Stores generated images and deployment packages.

## 🚀 Execution Summary

**1️⃣ Local ADK Testing**

      adk web

→ Open the ADK web UI → test prompts like "Generate an image of a cat riding a bicycle"

**2️⃣ Deploy to Vertex AI Agent Engine**

      python3 -m image_scoring.deploy

→ Creates an Agent Engine on Vertex AI (us-central1)
→ Prints your reasoningEngine ID.

**3️⃣ Remote Test via Test Client**

      cd testclient
      python3 remote_test.py

→ Confirms the deployed agent generates and scores images remotely.

**4️⃣ Run A2A API Server**

      cd image_scoring_adk_a2a_server
      export GOOGLE_CLOUD_PROJECT=assignment2-476319
      export GOOGLE_CLOUD_LOCATION=us-central1
      export GCS_BUCKET_NAME=soumya-unique-bucket
      adk api_server --a2a --port 8001 remote_a2a

**5️⃣ Test A2A Agent**

      curl http://localhost:8001/a2a/image_scoring/.well-known/agent.json
      
      curl -X POST http://localhost:8001/a2a/image_scoring \
        -H 'Content-Type: application/json' \
        -d '{
          "id": "uuid-123",
          "params": {
            "message": {
              "messageId": "msg-456",
              "parts": [{"text": "Create an image of a Bengal cat with emerald eyes"}],
              "role": "user"
            }
          }
        }'
→ The image is generated, scored, and uploaded to your GCS bucket.

## 🧾 Sample Results
Generated Images:

      gs://soumya-unique-bucket/2025-10-28/af146911-a976-4efa-8063-3ed303e14b99/generated_image_0.png



## 🧰 Tech Stack

* Google ADK v1.8.0
* Vertex AI Agent Engine
* Google Cloud Storage
* Python 3.12 / Poetry
* A2A Protocol 0.2.6
* gcloud / gsutil CLI

## 🧹 Repository Structure


multiagenthandson/

│

├── image_scoring/                   # Root + sub-agents

│   ├── agent.py

│   ├── deploy.py

│   └── sub_agents/

│

├── image_scoring_adk_a2a_server/    # A2A server implementation

│

├── testclient/                      # Remote test scripts

│

├── dist/                            # Build artifacts (.whl, .tar.gz)

├── screenshots/                     # PNG/JPG screenshots for README

├── artifacts/                       # Synced GCS outputs (optional)

└── README.md
