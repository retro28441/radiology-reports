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

st.title("🩻 CTA brain Report by Bright")

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
    history = st.text_area("History", "Case of xx, presented with xx. The CTA was requested to evaluate xx.")
    techniques = st.text_area("Techniques", "Plain, CTA and contrast-enhanced CT scans of the brain were performed using 2.5-mm and 1.25-mm slice thicknesses with multiplanar reconstruction.")
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
    cerebral_contrast = st.text_area("Post contrast", "After IV contrast administration, there is no abnormal enhancing lesion or abnormal leptomeningeal enhancement.")

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

    st.subheader("Visualized upper cervical spine")
    sub_cerv = st.text_input("Visualized upper cervical spine", "Visualized upper cervical spine", label_visibility="collapsed")
    cerv_spine = st.text_input("upper cervical spine", "No fracture identified.", label_visibility="collapsed")

    st.write("---")
 
    st.subheader("CTA")
    sub_mca = st.text_input("MCA", "Bilateral middle cerebral arteries (MCAs)")
    cta_mca = smart_selectbox("MCA stenosis", options["cta_mca"], label_visibility="collapsed")
    cta_mca2 = smart_selectbox("MCA stenosis2", options["cta_mca2"], label_visibility="collapsed")
    mca_no = smart_selectbox("MCA NO", options["cta_no"], label_visibility="collapsed")
    
    sub_ica = st.text_input("ICA", "Bilateral intracranial internal carotid arteries (ICAs)")
    ica_athero = st.text_area("ICA Athero", "Atherosclerotic change, seen as multifocal calcified and soft plaques along cavernous and supraclinoid segments of bilateral ICAs.", label_visibility="collapsed")
    cta_ica = smart_selectbox("ICA stenosis", options["cta_ica"], label_visibility="collapsed")
    cta_ica2 = smart_selectbox("ICA stenosis2", options["cta_ica2"], label_visibility="collapsed")
    ica_no = smart_selectbox("ICA NO", options["cta_no"], label_visibility="collapsed")

    sub_aca = st.text_input("ACA", "Bilateral anterior cerebral arteries (ACAs)")
    cta_aca = smart_selectbox("ACA stenosis", options["cta_aca"], label_visibility="collapsed")
    aca_no = smart_selectbox("ACA NO", options["cta_no"], label_visibility="collapsed")
    
    sub_acoa = st.text_input("ACoA", "Anterior communicating artery (ACoA)")
    cta_acoa = smart_selectbox("ACoA intact", options["cta_acoa"], label_visibility="collapsed")

    sub_collat = st.text_input("Collateral", "Collateral grading")
    cta_collat = smart_selectbox("Collat score", options["cta_collat"], label_visibility="collapsed")

    sub_va = st.text_input("VA", "Bilateral intracranial vertebral arteries (VAs)")
    va_hypo = smart_selectbox("VA hypoplasia", options["va_hypo"], label_visibility="collapsed")
    cta_va = smart_selectbox("VA stenosis", options["cta_va"], label_visibility="collapsed")
    cta_va2 = smart_selectbox("VA stenosis2", options["cta_va2"], label_visibility="collapsed")
    va_no = smart_selectbox("VA NO", options["cta_no"], label_visibility="collapsed")
 
    sub_ba = st.text_input("BA", "Basilar artery (BA)")
    cta_ba = smart_selectbox("BA stenosis", options["cta_ba"], label_visibility="collapsed")
    ba_no = smart_selectbox("BA NO", options["cta_no"], label_visibility="collapsed")

    sub_pca = st.text_input("PCA", "Bilateral posterior cerebral arteries (PCAs)")
    pca_fetal = smart_selectbox("PCA Fetal", options["pca_fetal"], label_visibility="collapsed")
    cta_pca = smart_selectbox("PCA stenosis", options["cta_pca"], label_visibility="collapsed")
    cta_pca2 = smart_selectbox("PCA stenosis2", options["cta_pca2"], label_visibility="collapsed")
    pca_no = smart_selectbox("PCA NO", options["cta_no"], label_visibility="collapsed")
   
    sub_pcoa = st.text_input("PCoA", "Posterior communicating arteries (PCoA)")
    cta_pcoa = smart_selectbox("PCoA intact", options["cta_pcoa"], label_visibility="collapsed")

    st.subheader("Venous structures")
    sub_venous = st.text_input("Venous structures", "Venous structures", label_visibility="collapsed")
    venous_throm = st.text_area("Venous thrombosis", "Patent. No obvious thrombosis.", label_visibility="collapsed")

    st.write("---")

    st.subheader("IMPRESSION")
    imp_braincon = smart_selectbox("Brain", options["imp_braincon"])
    imp_small = smart_selectbox("White matter changes", options["imp_small"])
    imp_lacun = smart_selectbox("Chronic lacunar infarct/Dilated perivascular space", options["imp_lacun"])
    imp_freenc = st.text_area("Free text Non-vascular", "")
    imp_ctano = smart_selectbox("CTA NO", options["imp_ctano"])
    imp_athero = smart_selectbox("CTA Atherosclerosis", options["imp_athero"])
    imp_freecta = st.text_area("Free text Vascular", "")

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
    
    report_text = f"{title}ANGIOGRAPHY OF THE BRAIN\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"TECHNIQUES: {techniques}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"
    
    report_text += f"HEAD/BRAIN\n"
    report_text += build_line(sub_cerebral, cerebral_volume, num_ber1, cerebral_gliotic, cerebral_infarc, num_ber2, wm_hypo, wm_loca, wm_disease, num_ber3, lacunar_perivas, cerebral_rest, cerebral_no, cerebral_contrast)
    report_text += build_line(sub_postfossa, cerebell_stem)
    report_text += build_line(sub_extraax, extra_axial)
    report_text += build_line(sub_ventricle, ven_tricle)
    report_text += build_line(sub_midline, mid_shift)
    report_text += build_line(sub_herniat, brain_herniat)
    report_text += build_line(sub_scalp, skull_brain)
    report_text += build_line(sub_skullbase, skull_base)
    report_text += build_line(sub_sinus, sinus_tube, sinus_misc1, sinus_misc2, orbit_nose1, orbit_nose2, sinus_mastoid1, sinus_mastoid2, sinus_no)
    report_text += build_line(sub_cerv, cerv_spine)
 
    report_text += f"\nCTA\nBrain vasculature:\nAnterior circulation:\n"
    report_text += build_line(sub_mca, cta_mca, cta_mca2, mca_no)
    report_text += build_line(sub_ica, ica_athero, cta_ica, cta_ica2, ica_no)
    report_text += build_line(sub_aca, cta_aca, aca_no)
    report_text += build_line(sub_acoa, cta_acoa)
    report_text += build_line(sub_collat, cta_collat)
    report_text += f"\nPosterior circulation:\n"
    report_text += build_line(sub_va, va_hypo, cta_va, cta_va2, va_no)
    report_text += build_line(sub_ba, cta_ba, ba_no)
    report_text += build_line(sub_pca, pca_fetal, cta_pca, cta_pca2, pca_no)
    report_text += build_line(sub_pcoa, cta_pcoa)
    report_text += f"\n"
    report_text += build_line(sub_venous, venous_throm)
        
    report_text += f"\nIMPRESSION:\nNon-vascular:\n- {imp_braincon}\n- {imp_small}{imp_lacun}\n- {imp_freenc}\n"
    report_text += f"Vascular:\n- {imp_ctano}\n- {imp_athero}\n- {imp_freecta}\n"
    
    st.text_area("Edit and copy your report here:", value=report_text, height=900)