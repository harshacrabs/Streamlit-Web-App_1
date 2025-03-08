#Import packages
import streamlit as st

# NLP packages
from textblob import TextBlob
import spacy
import neattext as nt

# Visualization packages
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")
from wordcloud import WordCloud

def main():
    """NLP web app with Streamlit"""
    st.title("NLP Web App")

    activity = ["Text Analysis", "Translation","Sentiment Analysis", "About"]
    choice = st.sidebar.selectbox("Menu",activity)

    if choice == "Text Analysis":
        st.subheader("Text Analysis")
        st.write("")

    if choice == "Translation":
        st.subheader("Translation")
        st.write("")
    
    if choice == "Sentiment Analysis":
        st.subheader("Sentiment Analysis")
        st.write("")

    if choice == "About":
        st.subheader("About")
        st.write("")

        st.markdown("""
        #### NLP web app made with Streamlit
                    
        for info:
        - [streamlit](https://streamlit.io)
        """)
    


if __name__ == "__main__":
    main()