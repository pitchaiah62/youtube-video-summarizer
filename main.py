import streamlit as st
from google import genai

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎬")

st.title("🎬 YouTube Video Summarizer")
st.write("Paste any YouTube link and get an AI summary instantly!")

api_key = st.text_input("Enter your Gemini API Key", type="password")
youtube_url = st.text_input("Enter YouTube Video URL")

def summarize(url, api_key):
    client = genai.Client(api_key=api_key)
    prompt = f"""
    Please summarize this YouTube video: {url}
    
    Provide:
    ## 🎯 Main Topic
    What is this video about in 2 sentences.
    
    ## 📌 Key Points
    5 most important bullet points from the video.
    
    ## 💡 Key Takeaways
    3 actionable takeaways the viewer should remember.
    
    ## 📝 Overall Summary
    A short paragraph summarizing everything.
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

if st.button("Summarize Video 🚀"):
    if not api_key or not youtube_url:
        st.warning("Please enter both API key and YouTube URL!")
    else:
        with st.spinner("AI is summarizing the video..."):
            try:
                summary = summarize(youtube_url, api_key)
                st.success("Summary Generated! ✅")
                st.markdown(summary)
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("---")
st.markdown("Built with ❤️ by Pitchaiah | Powered by Google Gemini AI")
