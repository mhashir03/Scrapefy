import streamlit as st 
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content,
    extract_body_content,
)
from parse import parse_with_ollama

# title and text input for the streamlit interface
st.title("Scrapefy")
url = st.text_input("Enter a Website URL: ")

# button to trigger website scraping
if st.button("Scrape Site"):
    st.write("Scraping the website")
    
    # scrape the website content and process it 
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    # store the cleaned content in the session state for later use
    st.session_state.dom_content = cleaned_content
    
    # display the scraped and cleaned DOM content in an expandable text area
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

# check if the DOM content exists in session state        
if "dom_content" in st.session_state:
    # input field for the user to describe what content they want to parse
    parse_description = st.text_area("Describe what you want to parse?")
    
    # button to trigger the parsing process
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            
            # split the DOM content into chunks and parse using the Ollama model
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)