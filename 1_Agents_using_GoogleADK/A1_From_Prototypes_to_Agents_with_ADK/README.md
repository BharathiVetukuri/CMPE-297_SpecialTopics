# A1 — From Prototypes to Agents with ADK

Build a **Renovation Proposal Agent** using Google’s **Agent Development Kit (ADK)**.  
The agent generates a contract-ready kitchen remodel proposal and (optionally) saves a PDF to Cloud Storage.  
If you run into quota/model issues, an **offline fallback** script still produces a Markdown + PDF proposal you can submit.

---

## 📺 Video Walkthrough
**YouTube:** https://youtu.be/rzKgwSqIUKM 

---

## 🗂 Project Layout

renovation_agent/
├─ init.py
├─ agent.py # exposes root_agent
├─ requirements.txt
├─ .env # environment variables (see below)
├─ outputs/
│ └─ proposals/ # generated .md and .pdf (offline mode)
└─ (optional) root_agent.yaml

## ✅ Prerequisites

 * Python 3.11+ (Cloud Shell has Python 3.12)
 * A GCP project with billing enabled
 * Permission to enable APIs and create Cloud Storage buckets
 * Google Cloud Shell / Linux/macOS

## ⚙️ Install

    cd renovation_agent

    # Create & activate a virtual environment
    python3 -m venv .venv
    source .venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt

    # If adk isn’t available after the install, run:
      pip install google-adk

## ▶️ Run the Agent (ADK)

    Option 1 — Dev UI

    # Run from the folder that contains your app folder
    cd ..
    adk web
    # Open the printed Dev UI URL and select the app

    Option 2 — CLI

    cd renovation_agent
    adk run .

    Test Prompt

    Hello. Generate Proposal Document for the kitchen remodel requirement in a proper format that applies to a renovation contract. Remember     this text will eventually be stored as a pdf file so make sure to have the formatting appropriate. I have no other specification.

## ✅ Expected Result

* Agent returns a well-formatted renovation proposal (UI/CLI) OR

* Offline script produces Markdown + PDF you can submit

* PDF appears in your GCS bucket
