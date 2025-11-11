# 🧠 Software Bug Assistant — Google ADK + MCP Tools

> **A Multi-Tool AI Agent built in Google Cloud using the Agent Development Kit (ADK) and Model Context Protocol (MCP)**  
> _Helps developers search, debug, and triage software issues automatically using real-time web, Stack Overflow, and GitHub context._

---

## 🎥 Demo Video

**🎬 👉 : https://youtu.be/6X2zhDFyU4I**

---

## 🧩 Project Overview

This project implements a **Software Bug Assistant** that uses **Google’s ADK (Agent Development Kit)** and **MCP tools** to assist developers with debugging and information retrieval.  

The assistant leverages multiple tool integrations:

| Tool Type | Integration | Description |
|------------|--------------|--------------|
| **Built-in Tool** | `google_search` | Queries real-time CVE and vulnerability info via Google Search |
| **Third-Party Tool** | `StackExchangeTool` (LangChain) | Retrieves relevant developer Q&A discussions from Stack Overflow |
| **MCP Tool** | `MCPToolset` (GitHub API) | Searches GitHub repositories, issues, and pull requests dynamically |
| **Optional Tool** | `Toolbox MCP` | Handles internal ticket creation and retrieval from a database |

---

## 🧠 Architecture Diagram

        ┌──────────────────────────────────────────────────────┐
        │                   ADK Web Interface                   │
        │    (Chat-based Software Bug Assistant running in GCP) │
        └───────────────┬───────────────────────────────────────┘
                        │
                        ▼
   ┌─────────────────────────────────────────────────────────────┐
   │                      ADK Agent Layer                        │
   │  - Model: Gemini 2.5 Flash                                  │
   │  - Agent Tools:                                             │
   │      1️⃣ GoogleSearchTool                                    │
   │      2️⃣ LangChain StackExchangeTool                         │
   │      3️⃣ MCP GitHub Toolset                                  │
   │                                                             │
   └─────────────────────────────────────────────────────────────┘
                        │
                        ▼
      ┌───────────────────────────────────────────┐
      │          External Knowledge Sources        │
      │  🌐 Google Search   💬 Stack Overflow       │
      │  🧑‍💻 GitHub MCP     🗄️ Local/Cloud SQL DB   │
      └───────────────────────────────────────────┘

## 🖼️ Screenshots

#### 1️⃣ Base Agent Greeting

<img width="1432" height="675" alt="Screenshot 2025-11-11 at 2 48 30 PM" src="https://github.com/user-attachments/assets/ab2dda74-5524-4dda-85c7-f9bcb0e30dec" />


#### 2️⃣ Built-in Google Search — CVE Example

<img width="1432" height="797" alt="Screenshot 2025-11-11 at 2 56 30 PM" src="https://github.com/user-attachments/assets/a8713f69-319d-4b25-8d71-cc90d7b3e790" />


#### 3️⃣ Stack Overflow Integration

#### 4️⃣ GitHub MCP Tool in Action

<img width="1432" height="840" alt="Screenshot 2025-11-11 at 3 14 45 PM" src="https://github.com/user-attachments/assets/d412db23-90e3-4b98-ac17-c53f38d188e0" />

<img width="1432" height="840" alt="Screenshot 2025-11-11 at 3 01 51 PM" src="https://github.com/user-attachments/assets/8cb44595-8a0e-4b25-88f6-9f2f7daf831c" />

<img width="1432" height="840" alt="Screenshot 2025-11-11 at 2 58 38 PM" src="https://github.com/user-attachments/assets/1bf34968-402d-42ca-bad1-1dc5625a88e7" />

---

## 🔍 Demonstrated Features

* ✅ Base Agent Initialization using Gemini 2.5 Flash
* ✅ Built-in Tool (Google Search) for CVE lookups
* ✅ Third-Party Integration (LangChain StackOverflow)
* ✅ MCP Tool (GitHub) for issue search
* ✅ Automatic tool chaining & reasoning
* ✅ Event-level trace and function call inspection via ADK Web UI

---

## 💡 Key Learnings

* ADK simplifies multi-tool agent creation — you can attach built-in, third-party, and MCP tools declaratively.

* MCP brings structured context from sources like GitHub and internal databases.

* Google Cloud Shell + ADK Web provide a fully managed environment for live development and debugging.

* Gemini 2.5 Flash powers reasoning, summarization, and tool orchestration seamlessly.
