import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configurations
st.set_page_config(
    page_title="Radiology Report Formatter",
    layout="wide"
)

st.title("Dynamic Radiology Report Formatter (RTE)")

st.write("Welcome to your interactive formatting workstation. Use this page to prepare your final dictation with professional bolded headers and key findings.")

# Read the entire HTML file
# Ensure the file is named exactly as saved in step 1
html_file_path = os.path.join(os.getcwd(), 'Rad_Formatter.html')

if os.path.exists(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as f:
        formatter_html = f.read()

    st.write("This embedded editor allows you to apply Bold, Italic, and Underline formatting to your past-in text.")

    # Embed the formatter as a large HTML component
    components.html(formatter_html, height=800, scrolling=True)
else:
    st.error(f"Error: The HTML formatter file ('Rad_Formatter.html') was not found. Please ensure it is saved in your main project folder next to app.py.")