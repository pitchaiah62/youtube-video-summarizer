import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎬")

st.title("🎬 YouTube Video Summarizer")
st.write("Paste your YouTube transcript and get an AI summary instantly!")

api_key = st.text_input("Enter your Gemini API Key", type="password")

st.markdown("**How to get transcript:**")
st.markdown("1. Open any YouTube video")
st.markdown("2. Click '...' → 'Show transcript'")
st.markdown("3. Copy all text and paste below")

transcript_text = st.text_area("Paste YouTube Transcript Here", height=200)

def summarize(transcript, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    You are an expert video summarizer.
    Summarize this YouTube transcript in clear bullet points.
    Cover all key points and main ideas.
    Keep it concise and easy to understand.
    Transcript: {transcript}
    """
    response = model.generate_content(prompt)
    return response.text

if st.button("Summarize Video 🚀"):
    if not api_key or not transcript_text:
        st.warning("Please enter both API key and transcript!")
    else:
        with st.spinner("Generating summary..."):
            try:
                summary = summarize(transcript_text, api_key)
                st.success("Summary Generated!")
                st.markdown(summary)
            except Exception as e:
                st.error(f"Error: {str(e)}")
