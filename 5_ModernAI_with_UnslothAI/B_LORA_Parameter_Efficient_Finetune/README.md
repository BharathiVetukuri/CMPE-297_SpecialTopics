# 🧠 Unsloth LoRA Fine-Tuning — smollm2-135M

## 📘 Overview
This notebook demonstrates **parameter-efficient fine-tuning (LoRA)** of the **`smollm2-135M`** model using **[Unsloth.ai](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide)**.  
It is **Part (b)** of the *Modern AI with Unsloth.ai* assignment.

While Part (a) performed **full fine-tuning**, Part (b) fine-tunes only a small number of trainable **LoRA adapter parameters**, saving memory and time while achieving competitive performance.

---

## ✅ Artifacts

**📘 Colab Notebook:**

**📹 Demo Video:**

---

## 🎯 Objectives
- Fine-tune `unsloth/smollm2-135m` using **LoRA (Low-Rank Adaptation)**  
- Use the same dataset as in full fine-tuning (Alpaca-style instruction data)  
- Explain and demonstrate **parameter-efficient training**  
- Run **chat** and **coding** tasks with multiple **chat-template formats**  
- Record a **YouTube walkthrough** showing inputs, code, and results  

---

## 🧩 Key Differences vs Full Fine-Tuning

| Aspect | Full Fine-Tuning | LoRA Fine-Tuning |
|--------|------------------|------------------|
| Trainable Params | All model weights | Only small rank-r matrices |
| Memory Use | High (FP16/FP32) | Low (4-bit + adapters) |
| Training Speed | Slower | 4-10× faster |
| Storage | Large checkpoint | Tiny adapter file |
| Reusability | Single-task model | Reusable adapters for multiple tasks |

---

# 💬 Tasks Demonstrated

### 🗣️ Chat Task
Explain a concept in concise, conversational style using:

- **Alpaca Instruction/Input/Response template**
- **Llama-style** (`[INST] ... [/INST]`)
- **ChatML / Qwen format**
- **Gemma-style prompt**

<img width="826" height="344" alt="image" src="https://github.com/user-attachments/assets/7830a56a-97ad-4f51-ac70-272cf65be78b" />

---

### 👨‍💻 Coding Task
- “Write a Python function to check if a number is prime”
- “Fix a bug in a factorial function”

Each task is run through the various chat templates to show how prompt formatting influences responses.

<img width="926" height="836" alt="image" src="https://github.com/user-attachments/assets/dba6d0b5-62ab-4475-94d3-60a6e88fe4c8" />

<img width="926" height="836" alt="image" src="https://github.com/user-attachments/assets/dc5cab6f-6136-49b1-bcf7-1d13a31f3d86" />

---

### 🔁 Multi-Turn Chat
A simple two-turn dialogue is generated (support-assistant style) to illustrate conversational memory within a single prompt.

<img width="860" height="534" alt="image" src="https://github.com/user-attachments/assets/72a67601-f039-49ac-8467-58c1ade135e5" />

---

### ⚖️ Base vs LoRA Comparison
The same instruction is sent to both:
- the **base model**
- the **LoRA-tuned model**

to highlight differences in accuracy, structure, and tone.

<img width="860" height="536" alt="image" src="https://github.com/user-attachments/assets/ab0a0172-f26d-4e54-9197-a13dfce38623" />


---

## 📊 Results Summary

| Task | Observation |
|------|--------------|
| Chat explanation | LoRA model gives more structured and concise answers |
| Coding | Generates functional, testable Python code |
| Bug fix | Adds reasoning + correct patch |
| Chat templates | Alpaca and ChatML perform best (matching training format) |
| Multi-turn | Maintains consistent context style |
