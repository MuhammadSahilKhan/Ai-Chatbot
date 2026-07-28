import streamlit as st
import requests
import json
from pypdf import PdfReader
import speech_recognition as sr

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="LocalMind AI", layout="wide")
st.title("🤖 LocalMind AI")

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⚙️ Settings")

model = "phi3"

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.session_state.memory = []

# =========================
# MEMORY
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = []

def update_memory(user, ai):
    st.session_state.memory.append(f"User: {user} | AI: {ai}")
    st.session_state.memory = st.session_state.memory[-5:]

# =========================
# PDF UPLOAD
# =========================
pdf_text = ""
pdf_file = st.sidebar.file_uploader("📄 Upload PDF", type="pdf")

if pdf_file:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text

# =========================
# VOICE INPUT
# =========================
def voice_input():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("🎤 Listening...")
            audio = r.listen(source, timeout=5)
        return r.recognize_google(audio)
    except:
        return None

voice_text = None
if st.sidebar.button("🎤 Speak"):
    voice_text = voice_input()
    if voice_text:
        st.sidebar.success(voice_text)
    else:
        st.sidebar.error("Could not understand")

# =========================
# CHAT DISPLAY
# =========================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# RESPONSE FUNCTION
# =========================
def get_response(user_input):
    url = "http://localhost:11434/api/generate"

    prompt = """
You are a helpful AI assistant like ChatGPT.
Be clear, smart, and direct.
Do not give irrelevant answers.
"""

    # memory
    for m in st.session_state.memory:
        prompt += m + "\n"

    # history
    for msg in st.session_state.messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        prompt += f"{role}: {msg['content']}\n"

    prompt += f"User: {user_input}\nAssistant:"

    # PDF context
    if pdf_text:
        prompt += "\nDocument:\n" + pdf_text[:1200]

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        res = requests.post(url, json=payload)
        data = res.json()
        return data.get("response", "⚠️ No response from Phi model")

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# =========================
# INPUT
# =========================
user_input = st.chat_input("💬 Type your message...")

if voice_text:
    user_input = voice_text

if user_input:
    st.chat_message("user").markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("🤖 Thinking..."):
        reply = get_response(user_input)

    st.chat_message("assistant").markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    update_memory(user_input, reply)