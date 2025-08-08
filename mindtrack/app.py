import streamlit as st
from analyzer import analyze_sentiment

st.set_page_config(page_title="MindTrack Journal Analyzer")

st.title("🧠 MindTrack - Mental Health Journal Analyzer")

# Input area
entry = st.text_area("Write your journal entry here:", height=200)

if st.button("Analyze Entry"):
    if entry.strip():
        polarity, subjectivity = analyze_sentiment(entry)

        st.subheader("📝 Sentiment Analysis")
        st.write(f"**Polarity:** {polarity:.2f}")
        st.write(f"**Subjectivity:** {subjectivity:.2f}")

        if polarity > 0.2:
            mood = "😊 Positive"
        elif polarity < -0.2:
            mood = "😞 Negative"
        else:
            mood = "😐 Neutral"

        st.write(f"**Mood Classification:** {mood}")
    else:
        st.warning("Please write something before analyzing.")
