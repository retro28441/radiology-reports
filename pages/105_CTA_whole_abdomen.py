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

st.title("🩻 CTA WHOLE Abdomen Report by Bright")

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
    history = st.text_area("History", "Case of .., presented with .. for ... The laboratory shows ... This CTA was requested to rule out ...")
    techniques = st.text_area("Techniques", "Axial helical scan of the whole abdomen with 2-mm slice thickness.")
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

    st.subheader("Lower thorax")
    sub_thorax = st.text_input("Thorax Title", "Lower thorax", label_visibility="collapsed")
    thorax_no = smart_selectbox("Thorax NO", options["thorax_no"])
    pleural_eff = smart_selectbox("pleural eff", options["pleural_eff"])
    heart_pericar = smart_selectbox("Heart&Pericardium", options["heart_pericar"])

    st.subheader("Liver")
    sub_liver = st.selectbox("Title", options["sub_liver"])
    liver_parenchyma = smart_selectbox("Liver Parenchyma", options["liver_parenchyma"])
    liver_lesion1 = smart_selectbox("Liver Lesion1", options["liver_lesion"])
    liver_lesion2 = smart_selectbox("Liver Lesion2", options["liver_lesion"])
    liver_no = smart_selectbox("Liver NO", options["liver_no"])
    liver_vessels = smart_selectbox("Liver Vessels", options["liver_vessels"])
    liver_collat = smart_selectbox("Portosystemic collateral", options["liver_collat"])

    st.subheader("Gallbladder")
    sub_gb = st.selectbox("Title", options["sub_gb"])
    gb_status = smart_selectbox("GB Status", options["gb_status"])
    bile_duct = smart_selectbox("Bile Ducts", options["bile_duct"])

    st.subheader("Pancreas")
    sub_pancreas = st.selectbox("Title", options["sub_pancreas"])
    pancreas_status = smart_selectbox("Status", options["pancreas_status"])
    pancreas_cyst = smart_selectbox("Cyst", options["pancreas_cyst"])
    mass_duct = st.text_input("Mass&Duct", "No focal mass or main ductal dilatation.")

    st.subheader("Spleen")
    sub_spleen = st.text_input("Spleen Title", "Spleen", label_visibility="collapsed")
    spleen_size = smart_selectbox("Size", options["spleen_size"])
    spleen_lesion = st.text_input("Lesion", "No focal lesion.")

    st.subheader("Adrenal glands")
    sub_adrenals = st.text_input("Adrenals Title", "Adrenal glands", label_visibility="collapsed")
    adrenal_nodule1 = smart_selectbox("Nodule1", options["adrenal_nodule1"])
    adrenal_nodule2 = smart_selectbox("Nodule2", options["adrenal_nodule2"])

    st.subheader("Kidneys")
    sub_kidneys = st.selectbox("Title", options["sub_kidney"])
    kidneys_status = smart_selectbox("Status", options["kidneys_status"])
    kidneys_cyst = smart_selectbox("Cyst", options["kidneys_cyst"])
    kidneys_stone = smart_selectbox("Stone", options["kidneys_stone"])
    kidneys_NO = smart_selectbox("Kidney NO", options["kidneys_NO"])

    st.subheader("Urinary bladder")
    sub_blad = st.text_input("Bladder Title", "Urinary bladder", label_visibility="collapsed")
    urinary_bladder = smart_selectbox("Bladder", options["urinary_bladder"])

    st.subheader("Reproductive organs")
    sub_repro = st.text_input("Repro Title", "Reproductive organs", label_visibility="collapsed")
    repro_female = smart_selectbox("Female", options["repro_female"])
    repro_male = smart_selectbox("Male", options["repro_male"])
    repro_cyst = smart_selectbox("Cyst", options["repro_cyst"])

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
    cta_abdo = st.text_area("CTA", "Patent mesenteric and bilateral renal arteries. No active contrast extravasation, aneurysm or dissection.")

    st.subheader("Bony structures")
    sub_bones = st.text_input("Bones Title", "Bony structures", label_visibility="collapsed")
    bone_spine = smart_selectbox("Spine", options["bone_spine"])
    bone_listhesis = smart_selectbox("Spondylolisthesis", options["bone_listhesis"])
    bone_lesion = smart_selectbox("Bone lesion", options["bone_lesion"])
    bone_lytic = smart_selectbox("Osteoblastic/lytic", options["bone_lytic"])

    st.write("---")

    st.subheader("IMPRESSION")
    CTA_NO = st.text_area("CTA NO", "No demonstrable active contrast extravasation, intramuscular hematoma, pneumoperitoneum or drainable fluid collection.")
    imp_free1 = st.text_area("Free text1", "")
    imp_free2 = st.text_area("Free text2", "")
    imp_gb = smart_selectbox("gallbladder", options["imp_gb"])

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
    
    report_text = f"{title}ANGIOGRAPHY OF THE WHOLE ABDOMEN\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"TECHNIQUES: {techniques}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"
    
    report_text += build_line(sub_tubes, val_tubes1, val_tubes2)
    report_text += build_line(sub_thorax, thorax_no, pleural_eff, heart_pericar)
    report_text += build_line(sub_liver, liver_parenchyma, liver_lesion1, liver_lesion2, liver_no, liver_vessels, liver_collat)
    report_text += build_line(sub_gb, gb_status, bile_duct)
    report_text += build_line(sub_pancreas, pancreas_status, pancreas_cyst, mass_duct)
    report_text += build_line(sub_spleen, spleen_size, spleen_lesion)
    report_text += build_line(sub_adrenals, adrenal_nodule1, adrenal_nodule2)
    report_text += build_line(sub_kidneys, kidneys_status, kidneys_cyst, kidneys_stone, kidneys_NO)
    report_text += build_line(sub_blad, urinary_bladder)
    report_text += build_line(sub_repro, repro_female, repro_male, repro_cyst)
    report_text += build_line(sub_bowel, bowel_wall1, bowel_wall2, bowel_diver, bowel_appendix)
    report_text += build_line(sub_nodes, nodes_abdo)
    report_text += build_line(sub_peritoneum, peritoneum)
    report_text += build_line(sub_vessels, vessels_abdo, cta_abdo)
    report_text += build_line(sub_bones, bone_spine, bone_listhesis, bone_lesion, bone_lytic)
    
    report_text += f"\nIMPRESSION:\n- {CTA_NO}\n- {imp_free1}\n- {imp_free2}\n- {imp_gb}"

    st.text_area("Edit and copy your report here:", value=report_text, height=900)