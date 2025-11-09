# 🤖 Reinforcement Learning with Preference Dataset

## 📘 Overview
This notebook demonstrates **Reinforcement Learning (RL)** using a **preference-based dataset** containing:
- An **input prompt**
- A **preferred (chosen) response**
- A **rejected (unpreferred) response**

The model learns to assign higher probability to the preferred output using **Direct Preference Optimization (DPO)** or similar algorithms.  
This corresponds to **Part (c)** of the assignment.

---

## 🎯 Objective
- Implement **Reinforcement Learning** using Unsloth.ai on a dataset with `prompt`, `chosen`, and `rejected` fields.
- Fine-tune a small open-weights model (e.g., `unsloth/smollm2-135m`) for preference alignment.
- Demonstrate improved preference-aligned generation after training.
- Record a **YouTube walkthrough** showing the setup, dataset, and results.

---

| Aspect | Observation |
|--------|--------------|
| **Preference Learning** | Model begins to favor high-quality, concise responses similar to “chosen” outputs |
| **Training Stability** | Stable convergence within a few epochs |
| **Output Quality** | Rejected-style verbosity and hallucination reduced |
| **Generalization** | Model applies alignment behavior to unseen prompts |

---

## References

* Unsloth Reinforcement Learning Guide — https://docs.unsloth.ai/get-started/reinforcement-learning-rl-guide

* Dahoas/full-hh-rlhf Dataset — https://huggingface.co/datasets/Dahoas/full-hh-rlhf

* TRL Library — DPOTrainer Docs — https://huggingface.co/docs/trl/main/en/dpo_trainer

---

## Screenshots

<img width="860" height="640" alt="image" src="https://github.com/user-attachments/assets/954bff4d-606d-4a5d-bc53-dda6fac85b1b" />

