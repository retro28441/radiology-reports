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

st.title("🩻 CT brain + Facial bone NC Report by Bright")

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
    history = st.text_area("History", "Case of xx, presented with xx. Physical examination revealed GCS of E4V5M6 without focal neurological deficit and xx. The CT scan was requested for evaluation.")
    techniques = st.text_area("Techniques", "Non-contrast axial helical CT scans of the brain and face was performed using 2.5-mm (soft tissue) and 1.25-mm (bone) slice thicknesses with multiplanar reconstructions.")
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

    st.write("---")
 
    st.subheader("FACE")

    sub_nasal = st.text_input("Nasal, nasopharyngeal and oropharyngeal airways", "Nasal, nasopharyngeal and oropharyngeal airways")
    nasal_air = st.text_area("Nasal", "Patent. No nasal septal hematoma. Nasal septal in midline.", label_visibility="collapsed")
    orbit_nose1 = smart_selectbox("Orbit/Nose1", options["orbit_nose"], label_visibility="collapsed")

    sub_orbit = st.text_input("Bony orbits and globes", "Bony orbits and globes")
    orbit_bone = st.text_area("Orbit", "Normal orbital apices. No CT evidence of globe injury.", label_visibility="collapsed")
    orbit_nose2 = smart_selectbox("Orbit/Nose2", options["orbit_nose"], label_visibility="collapsed")

    sub_max = st.text_input("Maxilla and maxillary sinuses", "Maxilla and maxillary sinuses")
    max_bone = st.text_area("Maxilla", "No fracture.", label_visibility="collapsed")
    max_sinus = smart_selectbox("Maxillary sinus", options["sinus_misc"], label_visibility="collapsed")

    sub_pte = st.text_input("Pterygoid plates", "Pterygoid plates")
    pte_bone = st.text_area("Pterygoid", "No fracture.", label_visibility="collapsed")
  
    sub_zygo = st.text_input("Zygoma and zygomatic arches", "Zygoma and zygomatic arches")
    zygo_bone = st.text_area("Zygoma", "No fracture.", label_visibility="collapsed")
    
    sub_eth = st.text_input("Nasal bones and nasoethmoidal complex", "Nasal bones and nasoethmoidal complex")
    eth_bone = st.text_area("Nasoethmoidal", "No fracture.", label_visibility="collapsed")
    eth_sinus = smart_selectbox("Ethmoid sinus", options["sinus_misc"], label_visibility="collapsed")

    sub_fron = st.text_input("Frontal sinuses", "Frontal sinuses")
    fron_bone = st.text_area("Frontal", "No fracture.", label_visibility="collapsed")
    fron_sinus = smart_selectbox("Frontal sinus", options["sinus_misc"], label_visibility="collapsed")

    sub_tmj = st.text_input("Mandible and temporomandibular joints (TMJs)", "Mandible and temporomandibular joints (TMJs)")
    tmj_bone = st.text_area("Mandible/TMJs", "No fracture or dislocation.", label_visibility="collapsed")

    sub_sphen = st.text_input("Sphenoid bones, sphenoid sinuses, skull base, sella and mastoid air cells", "Sphenoid bones, sphenoid sinuses, skull base, sella and mastoid air cells")
    sphen_bone = st.text_area("Sphenoid+Mastoid", "No fracture.", label_visibility="collapsed")
    sphen_sinus = smart_selectbox("Sphenoid sinus", options["sinus_misc"], label_visibility="collapsed")
    sinus_mastoid = smart_selectbox("Mastoid air cells", options["sinus_mastoid"], label_visibility="collapsed")

    sub_tooth = st.text_input("Teeth and periapical structures", "Teeth and periapical structures")
    tooth_bone = st.text_area("Teeth", "Unremarkable.", label_visibility="collapsed")

    sub_cerv = st.text_input("Visualized upper cervical spine", "Visualized upper cervical spine")
    cerv_spine = st.text_area("upper cervical spine", "No fracture.", label_visibility="collapsed")

    sub_soft = st.text_input("Soft tissues", "Soft tissues")
    soft_tissue = st.text_area("Soft tissue", "Unremarkable.", label_visibility="collapsed")
    sinus_tube = smart_selectbox("Tubes", options["sinus_tube"])

    st.write("---")

    st.subheader("IMPRESSION")
    imp_brain = smart_selectbox("Brain", options["imp_brain"])
    imp_facial = st.text_area("Facial bone", "No evidence of facial bone fracture.")
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
    
    report_text = f"{title}OF THE BRAIN AND FACIAL BONE\n\n"
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

    report_text += f"\nFACE\n"
    report_text += build_line(sub_nasal, nasal_air, orbit_nose1)
    report_text += build_line(sub_orbit, orbit_bone, orbit_nose2)
    report_text += build_line(sub_max, max_bone, max_sinus)
    report_text += build_line(sub_pte, pte_bone)
    report_text += build_line(sub_zygo, zygo_bone)
    report_text += build_line(sub_eth, eth_bone, eth_sinus)
    report_text += build_line(sub_fron, fron_bone, fron_sinus)
    report_text += build_line(sub_tmj, tmj_bone)
    report_text += build_line(sub_sphen, sphen_bone, sphen_sinus, sinus_mastoid)
    report_text += build_line(sub_tooth, tooth_bone)
    report_text += build_line(sub_cerv, cerv_spine)
    report_text += build_line(sub_soft, soft_tissue, sinus_tube)
        
    report_text += f"\nIMPRESSION:\n- {imp_brain}\n- {imp_facial}\n- {imp_small}{imp_lacun}\n- {imp_free}"

    
    st.text_area("Edit and copy your report here:", value=report_text, height=900)