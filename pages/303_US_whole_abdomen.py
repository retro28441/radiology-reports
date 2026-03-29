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

st.title("🩻 US WHOLE Abdomen Report by Bright")

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

    st.subheader("Liver")
    sub_liver = st.text_input("Title", "Liver", label_visibility="collapsed")
    liver_size = smart_selectbox("Size", options["liver_size"])
    liver_parenchyma = smart_selectbox("Parenchyma", options["liver_paren_us"])
    liver_lesion1 = smart_selectbox("Liver Lesions", options["liver_lesion1_us"])
    liver_lesion2 = smart_selectbox("Liver Lesion2", options["liver_lesion2_us"], label_visibility="collapsed")
    
    st.subheader("Gallbladder and biliary system")
    sub_gb = st.text_input("Title", "Gallbladder and biliary system", label_visibility="collapsed")
    gb_status = smart_selectbox("GB Status", options["us_gb"])
    gb_thick = st.text_area("Wall thikening/pericholecystic", "No gallbladder wall thickening or pericholecystic fluid.")
    bile_duct = smart_selectbox("Bile Ducts", options["us_bileduct"])
    bile_cbd = st.text_input("CBD size", "Common bile duct size $ mm.", label_visibility="collapsed")

    st.subheader("Spleen")
    sub_spleen = st.text_input("Title", "Spleen", label_visibility="collapsed")
    spleen_size = smart_selectbox("Size", options["us_spleen"], label_visibility="collapsed")

    st.subheader("Pancreas")
    sub_pancreas = st.text_input("Title", "Pancreas", label_visibility="collapsed")
    pan_creas = smart_selectbox("Status", options["pan_creas"], label_visibility="collapsed")

    st.subheader("Kidneys")
    sub_kidneys = st.text_input("Title", "Kidneys", label_visibility="collapsed")
    kidneys_sizeparen = smart_selectbox("Status", options["kidneys_sizeparen"])
    kidneys_cyst = smart_selectbox("Cyst", options["us_kid_cyst"])
    kidneys_stone = smart_selectbox("Stone", options["us_kid_stone"])
    kidneys_NO = smart_selectbox("Kidney NO", options["us_kid_NO"])

    st.subheader("Urinary bladder")
    sub_blad = st.text_input("Title", "Urinary bladder", label_visibility="collapsed")
    urinary_bladder = smart_selectbox("Bladder", options["urinary_blad"], label_visibility="collapsed")

    st.subheader("Reproductive organs")
    sub_pelvic = smart_selectbox("Title", options["sub_pelvic"], label_visibility="collapsed")
    us_female = smart_selectbox("Female", options["us_female"])
    us_male = smart_selectbox("Male", options["us_male"])
    repro_cyst = smart_selectbox("Cyst", options["us_repro_cyst"])

    st.subheader("Aorta")
    sub_aorta = st.text_input("Title", "Aorta", label_visibility="collapsed")
    us_aorta = smart_selectbox("Aorta", options["us_aorta"], label_visibility="collapsed")

    st.subheader("Peritoneum")
    sub_peritoneum = st.text_input("Title", "Peritoneum", label_visibility="collapsed")
    us_peritoneum = smart_selectbox("Peritoneum", options["us_peritoneum"])

    st.write("---")

    st.subheader("IMPRESSION")
    imp_free = st.text_area("Free text1", "")
    imp_fatty = smart_selectbox("Fatty liver", options["imp_fatty"])
    imp_gb = smart_selectbox("Gallbladder", options["imp_us_gb"])
    imp_paren1 = smart_selectbox("Parenchymatous1", options["imp_paren"])
    imp_paren2 = smart_selectbox("Parenchymatous2", options["imp_paren"])

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
    
    report_text = f"{title} OF THE WHOLE ABDOMEN\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"
    
    report_text += build_line(sub_liver, liver_size, liver_parenchyma, liver_lesion1, liver_lesion2)
    report_text += build_line(sub_gb, gb_status, gb_thick, bile_duct, bile_cbd)
    report_text += build_line(sub_spleen, spleen_size,)
    report_text += build_line(sub_pancreas, pan_creas)
    report_text += build_line(sub_kidneys, kidneys_sizeparen, kidneys_cyst, kidneys_stone, kidneys_NO)
    report_text += build_line(sub_blad, urinary_bladder)
    report_text += build_line(sub_pelvic, us_female, us_male, repro_cyst)
    report_text += build_line(sub_aorta, us_aorta)
    report_text += build_line(sub_peritoneum, us_peritoneum)
    
    report_text += f"\nIMPRESSION:\n- {imp_free}\n- {imp_fatty}\n- {imp_gb}\n- {imp_paren1}\n- {imp_paren2}"

    st.text_area("Edit and copy your report here:", value=report_text, height=900)