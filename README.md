# 🏥 Medical Chatbot using Ollama, LangChain & Pinecone

## 📌 Overview
This project is a **Generative AI Medical Chatbot** that leverages **Ollama (Gemma 3B), LangChain, Pinecone, and Flask** to provide intelligent responses based on medical knowledge.

## 🚀 Features
- **Local LLM** powered by **Ollama (Gemma 3B)**
- **Vector search** using **Pinecone**
- **Retrieval-Augmented Generation (RAG)** with **LangChain**
- **Flask-based API** for chatbot interaction
- **Medical knowledge extraction** from **The Gale Encyclopedia of Medicine**

## 🛠️ Tech Stack
- **Python 3.10**
- **Ollama** (Gemma 3B)
- **LangChain**
- **Pinecone**
- **Flask**
- **Sentence Transformers**
- **pypdf** (for document parsing)

## 🔧 Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Hari-2782/medical-chatbot.git
cd medical-chatbot
```
### **2️⃣ Set Up Environment**
```bash
conda create --name medic-chatbot-env python=3.10
conda activate medic-chatbot-env
```
### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
### **4️⃣ Install Ollama & Pull Model**
```bash
curl -fsSL https://ollama.com/install.sh | sh  # For macOS/Linux
ollama pull gemma:3b
```
### **5️⃣ Set Up Pinecone**
**Create a .env file and add:
```env
PINECONE_API_KEY=your_pinecone_api_key
```
### **6️⃣ Run the Chatbot**
```bash
python app.py
```
Access the chatbot at: http://localhost:8000

# License
This project is licensed under the MIT License. See the LICENSE file for details.

### **📺 Demo Video**


https://github.com/user-attachments/assets/54a761fb-30cc-4c0a-9023-74fbb97ca753



