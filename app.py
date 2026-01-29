from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from crawler import crawl_website

st.title("Website Crawler Test")

url = st.text_input("Enter website URL:")

if st.button("Crawl"):
    data, error = crawl_website(url)
    if error:
        st.error(error)
    else:
        st.success(f"Title: {data['title']}")
        st.write(data["text"][:500] + "...")  # show snippet
