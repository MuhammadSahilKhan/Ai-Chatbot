# 🤖 LocalMind AI

A lightweight **ChatGPT-like AI assistant** that runs completely **offline** using **Ollama** and the **Phi-3** language model. Built with **Python** and **Streamlit**, LocalMind AI provides an interactive conversational experience with support for **voice input**, **PDF-based question answering**, and **short-term conversation memory**.

---

## 📌 Overview

LocalMind AI is a local desktop AI assistant designed to deliver intelligent conversations without relying on cloud-based AI services. The application combines modern Natural Language Processing (NLP) with an intuitive user interface, allowing users to chat with an AI model, ask questions about PDF documents, and interact using voice commands.

This project was developed as part of an **Artificial Intelligence Internship** to gain practical experience in integrating local Large Language Models (LLMs) into real-world applications.

---

## ✨ Features

* 🤖 ChatGPT-like conversational interface
* 🧠 Short-term memory for contextual conversations
* 📄 Upload PDF files and ask questions about their content
* 🎤 Voice input using Speech Recognition
* 💬 Interactive chat interface built with Streamlit
* 🔒 Runs completely offline using Ollama
* ⚡ Fast inference with the Phi-3 language model
* 🗑️ Clear chat history with one click

---

## 🖼️ Application Workflow

1. Launch the Streamlit application.
2. Load the local Phi-3 model through Ollama.
3. Start chatting with the AI assistant.
4. Upload a PDF to ask document-related questions.
5. Use voice input for hands-free interaction.
6. The chatbot remembers recent conversations to provide better contextual responses.

---

## 🛠️ Technologies Used

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Core programming language |
| Streamlit         | Web application interface |
| Ollama            | Local LLM runtime         |
| Phi-3             | Language model            |
| SpeechRecognition | Voice input               |
| PyPDF             | PDF text extraction       |
| Requests          | API communication         |

---

## 📂 Project Structure

```text
LocalMind-AI/
│
├── app.py                 # Main Streamlit application
└── README.md              # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/LocalMind-AI.git
cd LocalMind-AI
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Libraries

```text
streamlit
requests
pypdf
SpeechRecognition
PyAudio
```

Install manually if needed:

```bash
pip install streamlit requests pypdf SpeechRecognition PyAudio
```

---

## 🤖 Install Ollama

Download and install Ollama from the official website.

After installation, pull the Phi-3 model:

```bash
ollama pull phi3
```

Start Ollama if it is not already running.

---

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

The application will open automatically in your web browser.

---

## 💬 Example Usage

* Ask general questions.
* Upload a PDF and ask questions about its content.
* Speak using your microphone instead of typing.
* Continue conversations with contextual memory.

---

---

## 🚀 Future Improvements

* Long-term conversation memory
* Image understanding (Vision AI)
* Multiple local AI model support
* Chat history export
* Dark/Light theme switch
* Streaming responses
* Multi-language support
* Retrieval-Augmented Generation (RAG)
* Document embeddings using vector databases

---

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

* Large Language Models (LLMs)
* Natural Language Processing (NLP)
* Local AI deployment
* Streamlit application development
* API integration
* Prompt engineering
* PDF document processing
* Voice recognition
* Building real-world AI applications

---

## 👨‍💻 Author

**Muhammad Sahil Khan**

BS Artificial Intelligence Student

Institute of Space Technology (IST), Islamabad

GitHub: https://github.com/MuhammadSahilKhan

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project helpful, consider giving it a **Star ⭐** on GitHub. Your support is greatly appreciated and motivates future improvements.

---

## 📄 License

This project is released under the **MIT License**. Feel free to use, modify, and contribute according to the license terms.
