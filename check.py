import streamlit as st
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

st.header("Video Transcript Modifier 🎬")

youtube_video = st.text_input("Enter video link", "")

if st.button("Get Summary"):
    video_id = youtube_video.split("=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    summarizer = pipeline('summarization')
    result = ""
    for i in transcript:
        result += ' ' + i['text']

    num_iters = int(len(result)/1000)
    summarized_text = []

    for i in range(0, num_iters + 1):
        start = i * 1000
        end = (i + 1) * 1000
        chunk = result[start:end]
        out = summarizer(chunk)
        out = out[0]
        out = out['summary_text']
        summarized_text.append(out)

    # Display only the final summary
    st.write("Final Summary:", "\n".join(summarized_text))
