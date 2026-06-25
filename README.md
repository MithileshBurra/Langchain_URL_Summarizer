# 🦜 LangChain: YT & Website Summarizer

A Streamlit web application that summarizes content from **YouTube videos** and **websites** using LangChain and Groq's LLaMA 3.3 70B model.

---

## 🚀 Demo

Paste any YouTube or website URL → enter your Groq API key → get a clean 300-word summary instantly.

---

## ✨ Features

- Summarizes **YouTube videos** and **websites** in 300 words
- Supports both standard (`youtube.com/watch?v=`) and shortened (`youtu.be/`) YouTube URL formats
- Secure API key input via sidebar — no hardcoded credentials
- Fast inference powered by **Groq** + **LLaMA 3.3 70B Versatile**
- Clean and minimal Streamlit UI

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| LangChain | Summarization chain (`load_summarize_chain`) |
| Groq / LLaMA 3.3 70B | LLM inference |
| youtube-transcript-api | YouTube transcript extraction |
| LangChain UnstructuredURLLoader | Website content loading |
| Streamlit | Frontend UI |

---

## ⚙️ How It Works

1. Enter your **Groq API key** in the sidebar
2. Paste a **YouTube or website URL**
3. Click **Summarize**
4. The app extracts content from the URL (transcript or webpage text)
5. LangChain's stuff summarization chain passes the content to LLaMA 3.3 70B
6. A **300-word summary** is displayed instantly

---

## 📦 Installation

```bash
git clone https://github.com/MithileshBurra/yt-website-summarizer
cd yt-website-summarizer
pip install -r requirements.txt
streamlit run app.py
```

---

## 📋 Requirements

```txt
streamlit
langchain
langchain-groq
langchain-classic
langchain-community
langchain-core
youtube-transcript-api
validators
unstructured
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key

This app requires a **free Groq API key**.

Get yours at → [console.groq.com](https://console.groq.com)

Once you have it, enter it in the sidebar when the app loads.

---

## 📁 Project Structure

```
yt-website-summarizer/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🖥️ Usage

**YouTube URL formats supported:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/dQw4w9WgXcQ
```

**Website URL example:**
```
https://en.wikipedia.org/wiki/LangChain
```

---

## ⚠️ Limitations

- YouTube videos must have **captions/transcripts** enabled
- Age-restricted or region-blocked YouTube videos may not work
- Some websites may block automated content fetching

---

## 👨‍💻 Author

**Mithilesh Burra**  
[GitHub](https://github.com/MithileshBurra) · [LinkedIn](https://www.linkedin.com/in/mithileshburra)