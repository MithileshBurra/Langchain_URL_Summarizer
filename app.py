import streamlit as st 
import validators 
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document
##
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")

with st.sidebar:
    api_key = st.text_input('groq_api_key',type = "password")

generic_url = st.text_input("Enter your url here")

def load_youtube_url(url):

    if "watch?v=" in url:
        video_id = url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be" in url:
        video_id = url.split("youtu.be" )[-1].split("?")[0]
    else:
        raise ValueError("Could not extract YouTube video ID from URL")
    ytt_api = YouTubeTranscriptApi()  # instantiate first
    transcript = ytt_api.fetch(video_id)
    full_text = " ".join(entry.text for entry in transcript)
    return [Document(page_content = full_text)]



template = """ Provide a summary of the following content, The summary should be accurate and include important points in bullet points:
Content:{text}"""
prompt = PromptTemplate(input_variables = ['text'],template = template)

if st.button("Summarize"):
    if not api_key or not generic_url.strip():
        st.error("Please enter complete details")
    elif not validators.url(generic_url):
        st.error("Please Enter Valid URL")
    else:
        try:
            llm = ChatGroq(groq_api_key = api_key,model = "llama-3.3-70b-versatile",streaming = True)
            if "youtube.com" in generic_url:
                docs = load_youtube_url(generic_url)
            else:
                loader = UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                               headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
    
                docs = loader.load()
            chain = load_summarize_chain(llm = llm, chain_type ="stuff", prompt = prompt)
            output_summary=chain.run(docs)
            st.success(output_summary)
        except Exception as e:
            st.exception(f"Error ocurred {e}")
        
