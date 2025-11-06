# Modern AI with Unsloth.ai — Fine-Tuning & Inference (Colab)

This repo contains two Google Colab notebooks demonstrating modern LLM training with Unsloth.ai:

* Full Fine-Tuning (SmolLM2-135M): 

* LoRA + 4-bit Quantization (Gemma-3-1B-IT) + Chat UI: 

### 📹 YouTube Video

* Colab 1 Video: https://youtu.be/your-video-link-1

* Colab 2 Video: https://youtu.be/your-video-link-2


## 🚀 What’s Inside

### 1) Colab 1 — Full Fine-Tuning: SmolLM2 (135M)

* Model: unsloth/smollm2-135m

* Technique: Full-parameter fine-tuning (no LoRA)

* Dataset: Alpaca subset (tatsu-lab/alpaca, 1k examples)

* Why: Fastest demonstration of complete fine-tuning pipeline on a tiny model

* Highlights: Before/after inference comparison, training logs, clean outputs

### 2) Colab 2 — LoRA + 4-bit Quantization + Chat UI

* Model: unsloth/gemma-3-1b-it-unsloth-bnb-4bit

* Technique: LoRA (parameter-efficient) on a 4-bit quantized base

* Dataset: Alpaca subset (500 examples)

* Why: Demonstrates modern memory-efficient fine-tuning and a Gradio chat interface

* Highlights: Minimal manual training loop (stable on T4), saved adapters, CPU-safe inference, chat demo

## 🧠 Models & Training

### 1. Full Fine-Tuning

* Model: unsloth/smollm2-135m

* Epochs: 1

* Batch size: 4 (grad accumulation 4)

* Max length: 512

* Optimizer/Trainer: 🤗 Trainer (float32 configuration, safe on T4)

* Output dir: ./smollm2-finetuned

### 2. LoRA + 4-bit

* Base: unsloth/gemma-3-1b-it-unsloth-bnb-4bit (4-bit quantized)

* LoRA: r=8, lora_alpha=16, dropout=0.05, target ["q_proj","v_proj"]

* Training: Simple manual PyTorch loop (stable on T4; no AMP)

* Output dir: ./gemma1b-lora-finetuned

## Screenshots

<img width="840" height="372" alt="Screenshot 2025-11-05 at 5 41 46 PM" src="https://github.com/user-attachments/assets/0811ce4e-1683-4281-a419-71554bac3b25" />
