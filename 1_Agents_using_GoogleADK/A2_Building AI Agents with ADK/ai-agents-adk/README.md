# A2 — Building AI Agents with ADK: Empowering with Tools

This project extends a Google **ADK** agent with **tools** to:
- Convert currency
- Check weather
- Search Wikipedia
- (Optional) Save outputs to PDF / upload to Cloud Storage

You’ll see each tool demonstrated in the **ADK Dev UI**, with screenshots placed in order below.

---

## 📺 Video Walkthrough
👉 **YouTube:** https://youtu.be/-JRJVEUOZh0 

---

## 🗂 Project Layout

ai-agents-adk/
├─ init.py
├─ agent.py # exposes root_agent and registers tools
├─ requirements.txt
├─ .env
└─ images/ # 📷 screenshots

## ⚙️ Install

    cd ai-agents-adk
    
    # Create and activate venv
    python3 -m venv .venv
    source .venv/bin/activate
    
    # Install deps
    pip install -r requirements.txt
    
    # If adk CLI is missing:
    pip install google-adk


## ▶️ Run
Option 1 — Dev UI
    # From the folder that CONTAINS your app folder
    cd ..
    adk web
    # Open the printed URL and select the app (ai-agents-adk)

Option 2 — CLI
    cd ai-agents-adk
    adk run .

## 🧪 Demo Flow (with Screenshot Slots)

1) Start a New Session (Greeting)


Prompt:
Hi! What can you do?

Expected: Agent lists capabilities (currency conversion, weather check, Wikipedia search).

<img width="1439" height="858" alt="Screenshot 2025-10-23 at 9 56 24 PM" src="https://github.com/user-attachments/assets/8835fbbc-22a2-4ff6-b867-6b0ea1b14109" />

![Agent Greeting & Capabilities](images/01-greeting-capabilities.png)



2) Currency Conversion Tool

Prompt (example):
Convert 125 EUR to USD.

Expected: Tool is invoked; agent responds with converted amount and (optionally) rate.

📷 Insert: images/02-currency-conversion.png
<img width="1439" height="858" alt="Screenshot 2025-10-23 at 10 00 18 PM" src="https://github.com/user-attachments/assets/edec856e-ad07-4b2f-9814-28674117fb31" />

![Currency Conversion Result](images/02-currency-conversion.png)

3) Weather Check Tool

Prompt (example):
What’s the weather in San Jose, CA right now?

Expected: Tool returns current conditions (temp/summary), possibly a short forecast.

📷 Insert: images/03-weather-check.png
<img width="1439" height="858" alt="Screenshot 2025-10-23 at 10 08 01 PM" src="https://github.com/user-attachments/assets/4538f706-50c2-4a75-bcb8-f63ab6f34b38" />

![Weather Check Result](images/03-weather-check.png)


<img width="1439" height="858" alt="Screenshot 2025-10-23 at 10 09 01 PM" src="https://github.com/user-attachments/assets/48da53b8-3632-4843-b9ef-6f30a07005ee" />


4) Wikipedia Search Tool

Prompt (example):
Search Wikipedia for "Basel Switzerland" and summarize the key highlights in 4 bullet points.

Expected: Tool returns a concise summary with bullet points and a source mention.
<img width="1439" height="379" alt="Screenshot 2025-10-23 at 10 12 52 PM" src="https://github.com/user-attachments/assets/fb0194ef-9c8d-4769-b62b-5486520ba31c" />
<img width="1439" height="860" alt="Screenshot 2025-10-23 at 10 13 22 PM" src="https://github.com/user-attachments/assets/6c4a9361-6acf-4b2d-b676-65be24dfe8d1" />


## ✅ Expected Results

Dev UI shows tool calls and agent responses for:

* Currency conversion
* Weather lookup
* Wikipedia search

