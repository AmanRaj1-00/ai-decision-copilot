# 🚀 AI Decision Intelligence Platform

An AI-powered system that transforms business data into actionable managerial decisions with explainable insights.

---

## 📌 Overview

This project simulates a real-world decision intelligence system used by managers and consultants.

Users can upload business data, and the system:
- Detects critical signals (e.g., revenue drops)
- Generates business decisions
- Uses AI to explain reasoning, strategy, and risks

---

## ⚙️ Features

- 📊 Data Processing (ETL pipeline)
- ⚠️ Automated Signal Detection (Revenue drops)
- 💡 Decision Engine for business actions
- 🤖 AI Insights using Llama3 (via Ollama)
- 📈 Interactive Dashboard (Streamlit)

---

## 🧠 Architecture
Data → ETL → Signal Detection → Decision Engine → AI (LLM) → Dashboard

---

## 🛠️ Tech Stack

- Python (Pandas, NumPy)
- Streamlit
- Local LLM (Llama3 via Ollama)
- Modular backend (ETL + logic layers)

---

## 🚀 How to Run

### 1. Clone repo
bash - 
git clone https://github.com/yourusername/ai-decision-copilot.git
cd ai-decision-copilot

Run Setup: 
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

TO RUN THE APP 
PYTHONPATH=. streamlit run demo/streamlit_app.py





