import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎬")

st.title("🎬 YouTube Video Summarizer")
st.write("Paste any YouTube link and get an AI summary instantly!")

api_key = st.text_input("Enter your Gemini API Key", type="password")
youtube_url = st.text_input("Enter YouTube Video URL")

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def get_transcript(video_id):
    try:
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id)
        return " ".join([t.text for t in transcript])
    except Exception:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t["text"] for t in transcript])

def summarize(transcript, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    You are an expert video summarizer.
    Summarize this YouTube transcript in clear bullet points.
    Cover all key points and main ideas.
    Transcript: {transcript}
    """
    response = model.generate_content(prompt)
    return response.text

if st.button("Summarize Video 🚀"):
    if not api_key or not youtube_url:
        st.warning("Please enter both API key and YouTube URL!")
    else:
        with st.spinner("Generating summary..."):
            try:
                video_id = get_video_id(youtube_url)
                transcript = get_transcript(video_id)
                summary = summarize(transcript, api_key)
                st.success("Done!")
                st.markdown(summary)
            except Exception as e:
                st.error(f"Error: {str(e)}")
