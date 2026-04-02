import streamlit as st
import json

st.set_page_config(page_title="CT Report Generator", layout="wide")

# --- THE STICKY SCROLL MAGIC (UPDATED FOR SCROLLING) ---
st.markdown(
    """
    <style>
    div[data-testid="stColumn"]:nth-of-type(2) {
        position: -webkit-sticky !important; 
        position: sticky !important;
        top: 4rem !important;
        align-self: flex-start !important;
        z-index: 99 !important;
        /* These two new lines add the independent scrollbar! */
        max-height: 85vh !important; 
        overflow-y: auto !important; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- LOAD THE DICTIONARY ---
with open('dictionary.json', 'r', encoding='utf-8') as f:
    options = json.load(f)

st.title("🩻 US LOWER ABDOMEN Report by Bright")

# --- SIDE-BY-SIDE LAYOUT ---
col1, col2 = st.columns(2)

def smart_selectbox(label, options_data, **kwargs):
    """A custom dropdown that handles both lists and short-name dictionaries, and edits '$'"""
    
    # 1. Check if the JSON data is a dictionary (Short Name -> Long Text)
    is_dict = isinstance(options_data, dict)
    
    # 2. If it's a dict, show the short names. If it's a normal list, show the list.
    display_options = list(options_data.keys()) if is_dict else options_data
    
    # 3. Show the normal dropdown
    selected_option = st.selectbox(label, display_options, **kwargs)
    
    # 4. Grab the actual full sentence for the final report
    full_sentence = options_data[selected_option] if is_dict else selected_option
    
    # 5. Look for your universal '$' trigger in the FULL sentence
    if "$" in full_sentence:
        edited_choice = st.text_area(
            f"✏️ Edit the full sentence for {label}:", 
            value=full_sentence, 
            height=100,
            key=f"edit_{label}_{selected_option}" 
        )
        return edited_choice
            
    # If there is no '$', return the full long sentence to the right side of the screen
    return full_sentence

with col1:
    
    st.subheader("Clinical Data")
    title = smart_selectbox("Title", options["us_title"])
    history = st.text_area("History", "Case of xx; follow-up.")

    comparison1 = smart_selectbox("Comparison1", options["us_compare1"])
    comparison2 = smart_selectbox("Comparison2", options["us_compare2"])

    st.write("---")
    
    st.subheader("Limitation")
    limit1 = smart_selectbox("Limitation1", options["us_limit"])
    limit2 = smart_selectbox("Limitation2", options["us_limit"])
 
    st.subheader("Urinary bladder")
    sub_blad = st.text_input("Title", "Urinary bladder", label_visibility="collapsed")
    urinary_bladder = smart_selectbox("Bladder", options["urinary_blad"], label_visibility="collapsed")

    st.subheader("Reproductive organs")
    sub_pelvic = smart_selectbox("Title", options["sub_pelvic"], label_visibility="collapsed")
    us_female = smart_selectbox("Female", options["us_female"])
    us_male = smart_selectbox("Male", options["us_male"])
    repro_cyst = smart_selectbox("Cyst", options["us_repro_cyst"])

    st.subheader("Others")
    sub_other = st.text_input("Title", "Others", label_visibility="collapsed")
    us_peritoneum = smart_selectbox("Peritoneum", options["us_peritoneum"])
    other_free = st.text_input("Free text", "---", label_visibility="collapsed")

    st.write("---")

    st.subheader("IMPRESSION")
    imp_free = st.text_area("Free text1", "")
   
# --- TEXT GENERATOR LOGIC ---
def build_line(subtitle, *texts):
    """Combines text in pure plain text, skips if '---' is selected."""
    valid_texts = [t for t in texts if t and t != "---"]
    if valid_texts:
        # Notice there is no space before the colon now!
        return f"{subtitle}: {' '.join(valid_texts)}\n"
    return ""

with col2:
    st.header("📄 Final Report")
    
    report_text = f"{title} OF THE LOWER ABDOMEN\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"
    
    report_text += build_line(sub_blad, urinary_bladder)
    report_text += build_line(sub_pelvic, us_female, us_male, repro_cyst)
    report_text += build_line(sub_other, us_peritoneum, other_free)
    
    report_text += f"\nIMPRESSION:\n- {imp_free}\n- "

    st.text_area("Edit and copy your report here:", value=report_text, height=900)