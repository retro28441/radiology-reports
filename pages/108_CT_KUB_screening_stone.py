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

st.title("🩻 CT KUB screening stone Report by Bright")

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
    history = st.text_area("History", "Case of .., presented with .. for ... This CT was requested to rule out KUB stone.")
    techniques = st.text_area("Techniques", "Non-contrast axial helical scan of the KUB with 2.5-mm slice thickness.")
    comparison1 = smart_selectbox("Comparison1", options["compareCTMR1"])
    comparison2 = smart_selectbox("Comparison2", options["compareCTMR2"])

    st.write("---")
    
    st.subheader("Limitation")
    limit1 = smart_selectbox("Limit1", options["limit"])
    limit2 = smart_selectbox("Limit2", options["limit"])

    st.subheader("Tubes and lines")
    sub_tubes = st.text_input("Tubes Title", "Tube and lines", label_visibility="collapsed")
    val_tubes1 = smart_selectbox("Tubes1", options["tubes1"])
    val_tubes2 = smart_selectbox("Tubes2", options["tubes2"])

    st.subheader("Right Kidney")
    sub_rtkidney = st.text_input("Title", "Right Kidney and ureter", label_visibility="collapsed")
    rtkidney_status = st.text_input("Size right", "Normal size, measuring about xx cm in length.")
    rtkidney_cyst = smart_selectbox("Cyst right", options["kidneys_cyst"])
    rtkidney_stone = smart_selectbox("Stone right", options["kidneys_stone"])
    rtkidney_NO = smart_selectbox("Right NO", options["kidneys_NO"])
    rtkidney_ure = st.text_input("Right ureter", "No hydroureter.")

    st.subheader("Left Kidney")
    sub_ltkidney = st.text_input("Title", "Left Kidney and ureter", label_visibility="collapsed")
    ltkidney_status = st.text_input("Size left", "Normal size, measuring about xx cm in length.")
    ltkidney_cyst = smart_selectbox("Cyst left", options["kidneys_cyst"])
    ltkidney_stone = smart_selectbox("Stone left", options["kidneys_stone"])
    ltkidney_NO = smart_selectbox("Left NO", options["kidneys_NO"])
    ltkidney_ure = st.text_input("Left ureter", "No hydroureter.")
    
    st.subheader("Urinary bladder")
    sub_blad = st.text_input("Bladder Title", "Urinary bladder", label_visibility="collapsed")
    urinary_bladder = smart_selectbox("Bladder", options["urinary_bladder"])

    st.subheader("Reproductive organs")
    sub_repro = st.text_input("Repro Title", "Reproductive organs", label_visibility="collapsed")
    repro_female = smart_selectbox("Female", options["repro_female"])
    repro_male = smart_selectbox("Male", options["repro_male"])
    repro_cyst = smart_selectbox("Cyst", options["repro_cyst"])

    st.subheader("Visualized upper abdomen")
    sub_upabd = st.text_input("Title", "Visualized upper abdomen", label_visibility="collapsed")
    upper_abdo = st.text_area("Upper abdomen", "The imaged liver, stomach, spleen, pancreas, and adrenal glands appear unremarkable.")

    st.subheader("Bowel")
    sub_bowel = st.text_input("Bowel Title", "Bowel and mesentery", label_visibility="collapsed")
    bowel_wall1 = smart_selectbox("Bowel Wall1", options["bowel_wall1"])
    bowel_wall2 = smart_selectbox("Bowel Wall2", options["bowel_wall2"])
    bowel_diver = smart_selectbox("Diverticulum", options["bowel_diver"])
    bowel_appendix = smart_selectbox("Appendix", options["bowel_appendix"])

    st.subheader("Lymph nodes")
    sub_nodes = st.text_input("Nodes Title", "Lymph nodes", label_visibility="collapsed")
    nodes_abdo = smart_selectbox("Lymph Nodes", options["nodes_abdo"])

    st.subheader("Peritoneum")
    sub_peritoneum = st.text_input("Peritoneum Title", "Peritoneum, retroperitoneum and abdominal wall", label_visibility="collapsed")
    peritoneum = smart_selectbox("Peritoneum", options["peritoneum"])

    st.subheader("Vessels")
    sub_vessels = st.text_input("Vessels Title", "Vessels", label_visibility="collapsed")
    vessels_abdo = smart_selectbox("Vessels", options["vessels_abdo"])

    st.subheader("Bony structures")
    sub_bones = st.text_input("Bones Title", "Bony structures", label_visibility="collapsed")
    bone_spine = smart_selectbox("Spine", options["bone_spine"])
    bone_listhesis = smart_selectbox("Spondylolisthesis", options["bone_listhesis"])
    bone_lesion = smart_selectbox("Bone lesion", options["bone_lesion"])
    bone_lytic = smart_selectbox("Osteoblastic/lytic", options["bone_lytic"])

    st.subheader("Lower thorax")
    sub_thorax = st.text_input("Thorax Title", "Lower thorax", label_visibility="collapsed")
    thorax_no = smart_selectbox("Thorax NO", options["thorax_no"])

    st.write("---")

    st.subheader("IMPRESSION")
    stone_no = st.text_area("Stone NO", "No identifiable calcified KUB stone, gross mass, or hydronephrosis.")
    imp_free1 = st.text_area("Free text1", "")

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
    
    report_text = f"{title}OF THE KUB SYSTEM (SCREENING KUB STONE PROTOCOL)\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"TECHNIQUES: {techniques}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: Limited evaluation of solid organs and vascular structures due to non-contrast study. {limit1} {limit2}\n"
    
    report_text += build_line(sub_tubes, val_tubes1, val_tubes2)
    report_text += build_line(sub_rtkidney, rtkidney_status, rtkidney_cyst, rtkidney_stone, rtkidney_NO, rtkidney_ure)
    report_text += build_line(sub_ltkidney, ltkidney_status, ltkidney_cyst, ltkidney_stone, ltkidney_NO, ltkidney_ure)
    report_text += build_line(sub_blad, urinary_bladder)
    report_text += build_line(sub_repro, repro_female, repro_male, repro_cyst)
    report_text += build_line(sub_upabd, upper_abdo)
    report_text += build_line(sub_bowel, bowel_wall1, bowel_wall2, bowel_diver, bowel_appendix)
    report_text += build_line(sub_nodes, nodes_abdo)
    report_text += build_line(sub_peritoneum, peritoneum)
    report_text += build_line(sub_vessels, vessels_abdo)
    report_text += build_line(sub_bones, bone_spine, bone_listhesis, bone_lesion, bone_lytic)
    report_text += build_line(sub_thorax, thorax_no)
    
    report_text += f"\nIMPRESSION:\n- {stone_no} \n- {imp_free1}\n - "

    st.text_area("Edit and copy your report here:", value=report_text, height=900)