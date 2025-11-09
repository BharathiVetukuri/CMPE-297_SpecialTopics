# 📘 Continued Pretraining

This README summarizes the **visible result cells** for your Continued Pretraining (Colab 5) notebook.  

---
# Artifacts

**📘 Colab Notebook:** https://colab.research.google.com/drive/1jOhaRfygFFaJ0ZCPWwAiMFGk3FwS_1d4?usp=sharing 

**📹 Demo Video:**

---

## ✅ What This Section Shows
- A quick **peek at training samples** (what the model learned from).
- **Side-by-side outputs**: Base model vs. Continued-pretrained (LoRA) model on French prompts.
- An **empathetic assistant demo** (useful if you used a mental-health or support tone dataset).
- A tiny **fluency proxy** (response length + accented characters) to visualize language adaptation.

---

## ▶️ How To Use
1. Run your training steps (through saving the continued-pretrained model).
2. Add the four visibility cells **after training**.
3. Execute them in order to print comparison outputs in the notebook.

---

## 🔎 Cells Included

### 1) Sample Preview — What the Model Saw
**Cell:** *Preview 3 samples from the training corpus*  
**Purpose:** Shows representative text pairs used in continued pretraining.

### 2) Base vs Continued — French Prompts
**Cell:** *Compare BASE vs CONTINUED model outputs on French prompts*  
**Purpose:** Demonstrates clearer, more natural French or better adherence to prompts after continued pretraining.

### 3) Empathetic Assistant Demo (Optional)
**Cell:** *Short empathetic response in French (or your target domain/language)*  
**Purpose:** Showcases tone/style gains (e.g., counseling or supportive phrasing).

### 4) Tiny Fluency Proxy (Optional)
**Cell:** *Length & accented-character count*  
**Purpose:** A quick, non-scientific proxy indicating more fluent, longer, or accent-rich responses after training.

---

## 🧪 Example Prompts Used
- “**Traduisez en français**: ‘The cat sits on the mat and watches the sunset.’”
- “**Explique en français**, en 2 phrases, la différence entre une **liste** et un **tuple** en Python.”
- “**Écris une brève description poétique** d’un matin pluvieux à Paris (2–3 phrases).”
- **Empathetic** support prompt in French for mental-health style guidance.

---

## 📂 Files Produced
- `continued_pretrain_model/` — your continued-pretrained model (adapters + tokenizer).
- This README — `README_ContinuedPretraining_Results.md`.

---

## 🔗 References
- Unsloth.ai — **Continued Pretraining** (basics)
- Unsloth.ai — **Export to Ollama** tutorial

---

## Screenshots

<img width="860" height="530" alt="image" src="https://github.com/user-attachments/assets/40507780-1bdf-4a61-add7-66d6d1877577" />

<img width="860" height="538" alt="image" src="https://github.com/user-attachments/assets/f47cec48-3a7e-47fe-b417-28131e632439" />


<img width="860" height="538" alt="image" src="https://github.com/user-attachments/assets/26eec5b6-8e69-458b-85fc-dc4b0502e6b4" />

