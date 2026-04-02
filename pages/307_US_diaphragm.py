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

st.title("🩻 US DIAPHRAGM  Report by Bright")

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
    history = st.text_area("History", "Case of xx. Chest radiographs demonstrate persistent elevation of the x hemidiaphragm since x. The US was requested for evaluation.")
    techniques = st.text_area("Techniques", "Transthoracic US was performed using B mode and M mode.")
    comparison1 = smart_selectbox("Comparison1", options["us_compare1"])
    comparison2 = smart_selectbox("Comparison2", options["us_compare2"])

    st.write("---")
    
    st.subheader("Limitation")
    limit1 = smart_selectbox("Limitation1", options["us_limit"])
    limit2 = smart_selectbox("Limitation2", options["us_limit"])
 
    st.subheader("Right hemidiaphragm")
    rhd_thick = st.text_input("RHD thickness", "RHD thickness = $ mm", label_visibility="collapsed")
    rhd_orthograde = smart_selectbox("RHD orthograde", options["diaphr_orthograde"])
    rhd_paradox = smart_selectbox("RHD Paradox", options["diaphr_paradox"])
    rhd_pleural = st.text_input("RHD Pleural", "No pleural effusion or mass.")

    # Changed "Title" to be unique for each one!
    sub_rhdquiet = st.text_input("RHD Quiet Title", "Quiet breathing", label_visibility="collapsed")
    rhd_quiet = smart_selectbox("RHD Quiet", options["diaphr_excur"])
    sub_rhddeep = st.text_input("RHD Deep Title", "Deep breathing", label_visibility="collapsed")
    rhd_deep = smart_selectbox("RHD Deep", options["diaphr_excur"])
    sub_rhdsnif = st.text_input("RHD Sniff Title", "Voluntary sniffing", label_visibility="collapsed")
    rhd_snif = smart_selectbox("RHD sniffing", options["diaphr_excur2"])
    
    st.subheader("Left hemidiaphragm")
    lhd_thick = st.text_input("LHD thickness", "LHD thickness = $ mm", label_visibility="collapsed")
    lhd_orthograde = smart_selectbox("LHD orthograde", options["diaphr_orthograde"])
    lhd_paradox = smart_selectbox("LHD Paradox", options["diaphr_paradox"])
    lhd_pleural = st.text_input("LHD Pleural", "No pleural effusion or mass.")

    # Changed "Title" to be unique here too!
    sub_lhdquiet = st.text_input("LHD Quiet Title", "Quiet breathing", label_visibility="collapsed")
    lhd_quiet = smart_selectbox("LHD Quiet", options["diaphr_excur"])
    sub_lhddeep = st.text_input("LHD Deep Title", "Deep breathing", label_visibility="collapsed")
    lhd_deep = smart_selectbox("LHD Deep", options["diaphr_excur"])
    sub_lhdsnif = st.text_input("LHD Sniff Title", "Voluntary sniffing", label_visibility="collapsed")
    lhd_snif = smart_selectbox("LHD sniffing", options["diaphr_excur2"])

    st.write("---")

    st.subheader("IMPRESSION")
    diaphr_paraly = smart_selectbox("Weakness/Paralysis", options["diaphr_paraly"])
    diaphr_no = smart_selectbox("Diaphragm NO", options["diaphr_no"])
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
    
    report_text = f"{title} OF THE DIAPHRAGM\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"TECHNIQUES: {techniques}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"
    
    report_text += f"Right hemidiaphragm:\n{rhd_thick}\n"
    report_text += f"{rhd_orthograde} {rhd_paradox} {rhd_pleural}\n"
    report_text += f"Excursion\n"
    report_text += build_line(sub_rhdquiet, rhd_quiet)
    report_text += build_line(sub_rhddeep, rhd_deep)
    report_text += build_line(sub_rhdsnif, rhd_snif)

    report_text += f"\nLeft hemidiaphragm:\n{lhd_thick}\n"
    report_text += f"{lhd_orthograde} {lhd_paradox} {lhd_pleural}\n"
    report_text += f"Excursion\n"
    report_text += build_line(sub_lhdquiet, lhd_quiet)
    report_text += build_line(sub_lhddeep, lhd_deep)
    report_text += build_line(sub_lhdsnif, lhd_snif)
    
    report_text += f"\nIMPRESSION:\n- {diaphr_paraly}\n- {diaphr_no}\n- {imp_free}"

    # 1. Create the memory slot (I named it 'diaphragm_memory' for this specific page)
    if 'diaphragm_memory' not in st.session_state:
        st.session_state.diaphragm_memory = report_text 

    # 2. Create the save function
    def save_typing():
        st.session_state.diaphragm_memory = st.session_state.live_diaphragm_box

    # 3. Create the auto-saving text area
    st.text_area(
        "Edit and copy your report here:", 
        value=st.session_state.diaphragm_memory, 
        key="live_diaphragm_box", 
        on_change=save_typing, 
        height=900
    )