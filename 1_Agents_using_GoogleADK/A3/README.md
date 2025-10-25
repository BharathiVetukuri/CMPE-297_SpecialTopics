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
