import streamlit as st

# I changed this to "centered" because it usually looks much cleaner for a welcome screen!
st.set_page_config(page_title="Radiology Report Generator", layout="centered")

st.title("🏥 Welcome to the CT Report Generator by Bright")
st.write("Please select a reporting template from the sidebar on the left to get started!")

st.write("---")

# --- THE DISCLAIMER SECTION ---
st.subheader("Disclaimer")

st.warning("""
**For Medical Professionals Only**

* **Not an absolute silver bullet:** This structural reporting text generator may limit your creativity and imagination on your report. Your wordings and paraphrases should be determined on each unique case.
* **Not a Diagnostic Tool:** This application was designed solely to assist with workflow and dictation speed. It does not analyze images or provide clinical diagnoses.  
* **Radiologist Responsibility:** The generated text must be thoroughly reviewed and edited before use. The signing radiologist retains full and absolute responsibility for the accuracy, completeness, and clinical validity of the final report entered into the PACS/HIS system.
* **Data Privacy:** To ensure security, please **do not** enter Protected Health Information (PHI) such as patient names, Hospital Numbers (HN), or highly identifying clinical history into this application.
""")

st.info("Created by Bright x GeminiPro.")