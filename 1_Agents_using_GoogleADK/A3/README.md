# Travel Agent using MCP Toolbox for Databases + Google ADK

This project implements a simple Hotel/Travel Agent that talks to an MCP Database Toolbox to query a hotels dataset and answer user requests like:

* “What can you do for me?”

* “I would like to search for hotels.”

* “Yes, a specific city → Basel.”

* “Search by hotel name → Hilton.”

---

### 🎥 YouTube demo:

https://youtu.be/YOUR_VIDEO_ID


### Screenshots

1. 


MCP Toolbox UI

<img width="1439" height="860" alt="Screenshot 2025-10-25 at 11 31 27 PM" src="https://github.com/user-attachments/assets/bfb33568-2e60-4922-b7ff-d86cea91aabf" />


MCP Toolbox UI - Hotel Search by Location

<img width="1439" height="860" alt="Screenshot 2025-10-25 at 11 34 21 PM" src="https://github.com/user-attachments/assets/36a10d4a-790b-4233-a69f-37452ee833bb" />



MCP Toolbox UI - Hotel Search by Name

<img width="1439" height="860" alt="Screenshot 2025-10-25 at 11 35 04 PM" src="https://github.com/user-attachments/assets/b515b890-ffb3-4a4b-a9c2-57031919b0e0" />


Gemini CLI

<img width="2878" height="1720" alt="image" src="https://github.com/user-attachments/assets/f8559fe8-9f18-4464-93b0-6bfad356d5f0" />

Hotel Agent App

<img width="1439" height="860" alt="Screenshot 2025-10-25 at 11 52 43 PM" src="https://github.com/user-attachments/assets/a514fff5-e802-4d61-abd8-99bf8ad69501" />


Connecting Agents to Tools

<img width="2878" height="1720" alt="image" src="https://github.com/user-attachments/assets/88d813f7-9e2c-4a89-b4ce-df91f65f4004" />


### 🧭 Overview

The MCP Toolbox for Databases runs as a local MCP server exposing tools such as:

* search-hotels-by-location

* search-hotels-by-name

The ADK Agent (“hotel_agent”) invokes those tools during a conversation and formats the result for the user.

    User ↔ ADK Agent (hotel_agent) ↔ MCP Toolbox (DB tools) ↔ Database

### ✅ Prerequisites

* Google Cloud Shell (or a local terminal with Python 3.10+)

* A Google Cloud project (only needed if you choose Vertex AI; the sample also works with a Gemini API key)

* ADK installed in your virtualenv (the codelab bootstrap adds this)

* MCP Toolbox for Databases binary

### Configure the ADK agent

From the codelab, an ADK agent skeleton called hotel-agent-app is created:

my-agents/

└─ hotel-agent-app/
   
   ├─ .env
   
   ├─ agent.py
   
   └─ __init__.py
