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

st.title("🩻 CT C-spine NC Report by Bright")

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
    title = st.selectbox("Title", options["titleCT"])
    history = st.text_area("History", "Case of xx, presented with xx. Physical examination revealed GCS of E4V5M6 without focal neurological deficit and tender around x cervical region. The CT scan was requested to evaluate cervical spine injury.")
    techniques = st.text_area("Techniques", "Axial helical scan of the cervical spine with 2.5-mm (soft tissue) and 1.25-mm (bone) slice thicknesses with axial reformats.")
    comparison1 = smart_selectbox("Comparison1", options["compareneuro1"])
    comparison2 = smart_selectbox("Comparison2", options["compareneuro2"])

    st.write("---")
    
    st.subheader("Limitation")
    limit1 = smart_selectbox("Limit1", options["limit_neuro"])
    limit2 = smart_selectbox("Limit2", options["limit_neuro"])
 
    st.subheader("Alignment")
    sub_align = st.text_input("Alignment", "Alignment", label_visibility="collapsed")
    neck_align = smart_selectbox("Cervical lordosis", options["neck_align"], label_visibility="collapsed")
    neck_lith = smart_selectbox("Spondylolisthesis", options["neck_lith"], label_visibility="collapsed")

    st.subheader("Bone/fracture")
    sub_bone = st.text_input("Bone", "Bone", label_visibility="collapsed")
    neck_bone = smart_selectbox("Degen spine", options["neck_bone"], label_visibility="collapsed")
    bone_lytic = smart_selectbox("Lytic/Blastic lesions", options["neuro_bone_lytic"], label_visibility="collapsed")

    sub_c1c2 = st.text_input("C1-C2", "Occipital condyles and C1-2", label_visibility="collapsed")
    c1c2_frac = smart_selectbox("C1C2 Fracture", options["neck_frac"], label_visibility="collapsed")
    sub_c3c7 = st.text_input("C3-7", "C3-7", label_visibility="collapsed")
    c3c7_frac = smart_selectbox("C3-7 Fracture", options["neck_frac"], label_visibility="collapsed")
    sub_tho = st.text_input("Thoracic spine", "Visualized upper thoracic spine", label_visibility="collapsed")
    tho_frac = smart_selectbox("Thoracic Fracture", options["neck_frac"], label_visibility="collapsed")

    st.subheader("Skull base, calvarium and brain")
    sub_brain = st.text_input("Visualized skull base, calvarium and brain", "Visualized skull base, calvarium and brain", label_visibility="collapsed")
    visua_brain = st.text_area("Brain+Skull", "The visualized brain parenchyma appears unremarkable. No acute fracture.", label_visibility="collapsed")
  
    st.subheader("Soft tissues")
    sub_soft = st.text_input("Soft tissues", "Soft tissues", label_visibility="collapsed")
    neck_prever = st.text_input("Prevertebral soft tissue", "No prevertebral soft tissue thickening.", label_visibility="collapsed")
    neck_thyroid = smart_selectbox("Thyroid", options["neck_thyroid"], label_visibility="collapsed")
    neck_nodes = smart_selectbox("Cervical lymph nodes", options["neck_nodes"], label_visibility="collapsed")
    neck_cal = smart_selectbox("Calcification", options["neck_cal"], label_visibility="collapsed")

    st.subheader("Lung apices")
    sub_lung = st.text_input("Lung apices", "Lung apices", label_visibility="collapsed")
    neck_lung = st.text_area("Lung apices.", "No suspicious mass, consolidation, tree-in-bud appearance, pneumothorax or pleural effusion.", label_visibility="collapsed")

    st.write("---")

    st.subheader("IMPRESSION")
    imp_cerv = st.text_area("Cervical spine", "No evidence of cervical spine fracture.")
    imp_free = st.text_area("Free text", "")

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
    
    report_text = f"{title}OF THE CERVICAL SPINE\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"TECHNIQUES: {techniques}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"
    
    report_text += build_line(sub_align, neck_align, neck_lith)
    report_text += build_line(sub_bone, neck_bone, bone_lytic)
    report_text += build_line(sub_c1c2, c1c2_frac)
    report_text += build_line(sub_c3c7, c3c7_frac)
    report_text += build_line(sub_tho, tho_frac)
    report_text += build_line(sub_brain, visua_brain)
    report_text += build_line(sub_soft, neck_prever, neck_thyroid, neck_nodes, neck_cal)
    report_text += build_line(sub_lung, neck_lung)
        
    report_text += f"\nIMPRESSION:\n- {imp_cerv}\n- {imp_free}"

    
    st.text_area("Edit and copy your report here:", value=report_text, height=900)