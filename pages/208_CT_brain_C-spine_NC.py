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

st.title("🩻 CT brain + C-spine NC Report by Bright")

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
    history = st.text_area("History", "Case of xx, presented with xx. Physical examination revealed GCS of E4V5M6 without focal neurological deficit and tender around x cervical region. The CT scan was requested to evaluate intracranial hemorrhage and cervical spine injury.")
    techniques = st.text_area("Techniques", "Axial helical scan of the brain and cervical spine with 2.5-mm (brain and soft tissue) and 1.25-mm (bone) slice thicknesses with axial reformats.")
    comparison1 = smart_selectbox("Comparison1", options["compareneuro1"])
    comparison2 = smart_selectbox("Comparison2", options["compareneuro2"])

    st.write("---")
    
    st.subheader("Limitation")
    limit1 = smart_selectbox("Limit1", options["limit_neuro"])
    limit2 = smart_selectbox("Limit2", options["limit_neuro"])

    st.subheader("Cerebral parenchyma")
    sub_cerebral = smart_selectbox("Cerebral parenchyma", options["title_cerebral"], label_visibility="collapsed")
    cerebral_volume = smart_selectbox("Brain volume", options["cerebral_volume"])

    num_ber1 = smart_selectbox("Infarction", options["num_ber"])
    cerebral_gliotic = smart_selectbox("Hypodense", options["cerebral_gliotic"], label_visibility="collapsed")
    cerebral_infarc = smart_selectbox("Infarct", options["cerebral_infarc"], label_visibility="collapsed")

    num_ber2 = smart_selectbox("White matter changes", options["num_ber"])
    wm_hypo =  smart_selectbox("WM hypodense", options["wm_hypo"], label_visibility="collapsed")
    wm_loca = smart_selectbox("WM location", options["wm_loca"], label_visibility="collapsed")
    wm_disease = smart_selectbox("WM Disease", options["wm_disease"], label_visibility="collapsed")

    num_ber3 = smart_selectbox("Chronic lacunar infarct/Dilated perivascular space", options["num_ber"])
    lacunar_perivas = smart_selectbox("well-defined hypodense", options["lacunar_perivas"], label_visibility="collapsed")

    cerebral_rest = smart_selectbox("Cerebral NO", options["cerebral_rest"])
    cerebral_no = smart_selectbox("Cerebral NO2", options["cerebral_no"], label_visibility="collapsed")

    st.subheader("Cerebellum and posterior fossa")
    sub_postfossa = st.text_input("Cerebellum and posterior fossa", "Cerebellum and posterior fossa", label_visibility="collapsed")
    cerebell_stem = st.text_area("Cerebellum and posterior fossa2", "Normal given a limited evaluation of the brainstem due to beam-hardening artifacts. The cerebellum appears unremarkable.", label_visibility="collapsed")

    st.subheader("Extra-axial spaces")
    sub_extraax = st.text_input("Extra-axial spaces", "Extra-axial spaces", label_visibility="collapsed")
    extra_axial = st.text_area("Extra-axial spaces2", "No extra-axial hemorrhage or collection.", label_visibility="collapsed")

    st.subheader("Ventricles")
    sub_ventricle = st.text_input("Ventricles", "Ventricles", label_visibility="collapsed")
    ven_tricle = smart_selectbox("Ventricles2", options["ven_tricle"], label_visibility="collapsed")

    st.subheader("Midline shift")
    sub_midline = st.text_input("Midline shift", "Midline shift", label_visibility="collapsed")
    mid_shift = st.text_input("Midline shift2", "None.", label_visibility="collapsed")

    st.subheader("Brain herniation")
    sub_herniat = st.text_input("Brain herniation", "Brain herniation", label_visibility="collapsed")
    brain_herniat = st.text_input("Brain herniation2", "None.", label_visibility="collapsed")

    st.subheader("Vascular system")
    sub_vascular = st.text_input("Vascular system", "Vascular system", label_visibility="collapsed")
    vascular_nc = smart_selectbox("Vascular system2", options["vascular_nc"], label_visibility="collapsed")

    st.subheader("Calvarium and scalp")
    sub_scalp = st.text_input("Calvarium and scalp", "Calvarium and scalp", label_visibility="collapsed")
    skull_brain = smart_selectbox("Calvarium and scalp2", options["skull_brain"], label_visibility="collapsed")

    st.subheader("Skull base, sella and temporomandibular joints (TMJs)")
    sub_skullbase = st.text_input("skull base", "Skull base, sella and temporomandibular joints (TMJs)", label_visibility="collapsed")
    skull_base = st.text_input("skull base2", "Unremarkable.", label_visibility="collapsed")

    st.subheader("Visualized orbits, paranasal sinuses and mastoid air cells")
    sub_sinus = st.text_input("Sinus", "Visualized orbits, paranasal sinuses and mastoid air cells", label_visibility="collapsed")
    sinus_tube = smart_selectbox("Tubes", options["sinus_tube"])
    sinus_misc1 = smart_selectbox("Sinus", options["sinus_misc"])
    sinus_misc2 = smart_selectbox("Sinus2", options["sinus_misc"], label_visibility="collapsed")
    orbit_nose1 = smart_selectbox("Orbit/Nose", options["orbit_nose"])
    orbit_nose2 = smart_selectbox("Orbit/Nose2", options["orbit_nose"], label_visibility="collapsed")
    sinus_mastoid1 = smart_selectbox("Mastoid air cells", options["sinus_mastoid"])
    sinus_mastoid2 = smart_selectbox("Mastoid air cells2", options["sinus_mastoid"], label_visibility="collapsed")
    sinus_no = smart_selectbox("Sinus NO", options["sinus_no"])

    st.write("---")
 
    st.subheader("C-spine")
    sub_align = st.text_input("Alignment", "Alignment")
    neck_align = smart_selectbox("Cervical lordosis", options["neck_align"], label_visibility="collapsed")
    neck_lith = smart_selectbox("Spondylolisthesis", options["neck_lith"], label_visibility="collapsed")

    sub_bone = st.text_input("Bone", "Bone")
    neck_bone = smart_selectbox("Degen spine", options["neck_bone"], label_visibility="collapsed")
    bone_lytic = smart_selectbox("Lytic/Blastic lesions", options["neuro_bone_lytic"], label_visibility="collapsed")

    sub_c1c2 = st.text_input("C1-C2", "Occipital condyles and C1-2")
    c1c2_frac = smart_selectbox("C1C2 Fracture", options["neck_frac"], label_visibility="collapsed")
    sub_c3c7 = st.text_input("C3-7", "C3-7")
    c3c7_frac = smart_selectbox("C3-7 Fracture", options["neck_frac"], label_visibility="collapsed")
    sub_tho = st.text_input("Thoracic spine", "Visualized upper thoracic spine")
    tho_frac = smart_selectbox("Thoracic Fracture", options["neck_frac"], label_visibility="collapsed")
  
    sub_soft = st.text_input("Soft tissues", "Soft tissues")
    neck_prever = st.text_input("Prevertebral soft tissue", "No prevertebral soft tissue thickening.", label_visibility="collapsed")
    neck_thyroid = smart_selectbox("Thyroid", options["neck_thyroid"], label_visibility="collapsed")
    neck_nodes = smart_selectbox("Cervical lymph nodes", options["neck_nodes"], label_visibility="collapsed")
    neck_cal = smart_selectbox("Calcification", options["neck_cal"], label_visibility="collapsed")

    sub_lung = st.text_input("Lung apices", "Lung apices")
    neck_lung = st.text_area("Lung apices.", "No suspicious mass, consolidation, tree-in-bud appearance, pneumothorax or pleural effusion.", label_visibility="collapsed")

    st.write("---")

    st.subheader("IMPRESSION")
    imp_brain = smart_selectbox("Brain", options["imp_brain"])
    imp_cerv = st.text_area("Cervical spine", "No evidence of cervical spine fracture.")
    imp_small = smart_selectbox("White matter changes", options["imp_small"])
    imp_lacun = smart_selectbox("Chronic lacunar infarct/Dilated perivascular space", options["imp_lacun"])
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
    
    report_text = f"{title}OF THE BRAIN AND CERVICAL SPINE\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"TECHNIQUES: {techniques}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"
    
    report_text += f"HEAD/BRAIN\n"
    report_text += build_line(sub_cerebral, cerebral_volume, num_ber1, cerebral_gliotic, cerebral_infarc, num_ber2, wm_hypo, wm_loca, wm_disease, num_ber3, lacunar_perivas, cerebral_rest, cerebral_no)
    report_text += build_line(sub_postfossa, cerebell_stem)
    report_text += build_line(sub_extraax, extra_axial)
    report_text += build_line(sub_ventricle, ven_tricle)
    report_text += build_line(sub_midline, mid_shift)
    report_text += build_line(sub_herniat, brain_herniat)
    report_text += build_line(sub_vascular, vascular_nc)
    report_text += build_line(sub_scalp, skull_brain)
    report_text += build_line(sub_skullbase, skull_base)
    report_text += build_line(sub_sinus, sinus_tube, sinus_misc1, sinus_misc2, orbit_nose1, orbit_nose2, sinus_mastoid1, sinus_mastoid2, sinus_no)
    
    report_text += f"\nCERVICAL SPINE\n"
    report_text += build_line(sub_align, neck_align, neck_lith)
    report_text += build_line(sub_bone, neck_bone, bone_lytic)
    report_text += build_line(sub_c1c2, c1c2_frac)
    report_text += build_line(sub_c3c7, c3c7_frac)
    report_text += build_line(sub_tho, tho_frac)
    report_text += build_line(sub_soft, neck_prever, neck_thyroid, neck_nodes, neck_cal)
    report_text += build_line(sub_lung, neck_lung)
        
    report_text += f"\nIMPRESSION:\n- {imp_brain}\n- {imp_cerv}\n- {imp_small}{imp_lacun}\n- {imp_free}"

    
    st.text_area("Edit and copy your report here:", value=report_text, height=900)