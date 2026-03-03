import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎬")

st.title("🎬 YouTube Video Summarizer")
st.write("Paste any YouTube link and get an AI summary instantly!")

api_key = st.text_input("Enter your Gemini API Key", type="password")
youtube_url = st.text_input("Enter YouTube Video URL")

def summarize(url, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    Please watch and summarize this YouTube video: {url}
    
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
    response = model.generate_content(prompt)
    return response.text

if st.button("Summarize Video 🚀"):
    if not api_key or not youtube_url:
        st.warning("Please enter both API key and YouTube URL!")
    else:
        with st.spinner("AI is watching and summarizing the video..."):
            try:
                summary = summarize(youtube_url, api_key)
                st.success("Summary Generated! ✅")
                st.markdown(summary)
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("---")
st.markdown("Built with ❤️ by Pitchaiah | Powered by Google Gemini AI")
