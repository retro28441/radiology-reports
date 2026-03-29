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

st.title("🩻 CTA coronary arteries Report by Bright")

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
    history = st.text_area("History", "Case of xx, presented with dyspnea on exertion/atypical chest pain. The CTA was requested for evaluation.")
    techniques = st.text_area("Techniques", "Using multidetector computed tomography scanner with retrospective ECG gating:\n1) Non-enhanced axial CT for the coronary calcification using 2.5-mm slice thickness. \n2) Cardiac CTA using 0.63-mm and 1.25-mm slice thickness. \n3) Contrast-enhanced axial CT scan of the chest using 0.63-mm and 2.0-mm slice thickness. \n4) Multiplanar MIP with post processing 3D volume rendering reconstruction.")
    comparison1 = smart_selectbox("Comparison1", options["compareCTMR1"])
    comparison2 = smart_selectbox("Comparison2", options["compareCTMR2"])

    st.write("---")
    
    st.subheader("Limitation")
    limit1 = smart_selectbox("Limit1", options["limit"])
    limit2 = smart_selectbox("Limit2", options["limit"])

    st.subheader("Coronary and heart")
    sub_coro = st.text_input("Coronary and heart", "Coronary and heart", label_visibility="collapsed")
    coro_quality = smart_selectbox("Image quality", options["coro_quality"])
    coro_hr = st.text_input("Heart rate", "x beats/min")
    coro_dominant = smart_selectbox("Dominant", options["coro_dominant"])
    coro_anomaly = st.text_area("Anomaly", "No anomalous origin of coronary artery.")
    coro_calcium = st.text_input("Coronary artery calcification", "Total calcium score = x")
    coro_lvef = st.text_input("Left ventricular function", "LVEF = x %")

    st.subheader("RCA")
    sub_rca = st.text_input("RCA", "RCA", label_visibility="collapsed")
    coro_rca = st.text_input("RCA2", "originates from the right coronary cusp.", label_visibility="collapsed")
    coro_rcas1 = smart_selectbox("Proximal (S1)", options["coro_stenosis"])
    coro_rcas2 = smart_selectbox("Mid (S2)", options["coro_stenosis"])
    coro_rcas3 = smart_selectbox("Distal (S3)", options["coro_stenosis"])
    coro_rcas4 = smart_selectbox("PDA (S4)", options["coro_stenosis"])
    coro_rcapl = smart_selectbox("PL", options["coro_stenosis"])

    st.subheader("LMA")
    sub_lma = st.text_input("LMA", "LMA", label_visibility="collapsed")
    coro_lma = st.text_input("LMA2", "originates from the left coronary cusp and gives off LAD and LCX.", label_visibility="collapsed")
    coro_lmas5 = smart_selectbox("LMA3", options["coro_stenosis"], label_visibility="collapsed")

    st.subheader("LAD")
    sub_lad = st.text_input("LAD", "LAD", label_visibility="collapsed")
    coro_lads6 = smart_selectbox("Proximal (S6)", options["coro_stenosis"])
    coro_lads7 = smart_selectbox("Mid (S7)", options["coro_stenosis"])
    coro_lads8 = smart_selectbox("Distal (S8)", options["coro_stenosis"])
    coro_lads9 = smart_selectbox("DG-1 (S9)", options["coro_stenosis"])
    coro_lads10 = smart_selectbox("DG-2 (S10)", options["coro_stenosis"])
    coro_laddg3 = smart_selectbox("DG-3", options["coro_stenosis"])

    st.subheader("LCX")
    sub_lcx = st.text_input("LCX", "LCX", label_visibility="collapsed")
    coro_lcxs11 = smart_selectbox("Proximal (S11)", options["coro_stenosis"])
    coro_lcxs13 = smart_selectbox("Mid/distal (S13)", options["coro_stenosis"])
    coro_lcxs12 = smart_selectbox("OM-1 (S12)", options["coro_stenosis"])
    coro_lcxs14 = smart_selectbox("OM-2 (S14)", options["coro_stenosis"])
    coro_lcxom3 = smart_selectbox("OM-3", options["coro_stenosis"])

    st.write("---")

    st.subheader("Tubes and lines")
    sub_tubes = st.text_input("Tubes Title", "Tube and lines", label_visibility="collapsed")
    val_tubes1 = smart_selectbox("Tubes1", options["tubes1"])
    val_tubes2 = smart_selectbox("Tubes2", options["tubes2"])

    st.subheader("Lung parenchyma")
    sub_lung = st.selectbox("Title", options["sub_lung"], label_visibility="collapsed")
    thorax_num1 = smart_selectbox("Nodule1", options["thorax_num"])
    thorax_nodule1 = smart_selectbox("Nod1", options["thorax_nodule"], label_visibility="collapsed")
    thorax_segment11 = smart_selectbox("Segment1", options["thorax_segmentrt"])
    thorax_segment12 = smart_selectbox("Seg12", options["thorax_segmentlt"], label_visibility="collapsed")
    thorax_segment13 = smart_selectbox("Seg13", options["thorax_lobe"], label_visibility="collapsed")
    thorax_num2 = smart_selectbox("Nodule2", options["thorax_num"])
    thorax_nodule2 = smart_selectbox("Nod2", options["thorax_nodule"], label_visibility="collapsed")
    thorax_segment21 = smart_selectbox("Segment2", options["thorax_segmentrt"])
    thorax_segment22 = smart_selectbox("Seg22", options["thorax_segmentlt"], label_visibility="collapsed")
    thorax_segment23 = smart_selectbox("Seg23", options["thorax_lobe"], label_visibility="collapsed")
    thorax_emphy = smart_selectbox("Emphysema/Cyst", options["thorax_emphy"])
    thorax_no = smart_selectbox("Thorax NO", options["thorax_no"])
    
    st.subheader("Central airways")
    sub_air = st.text_input("Title", "Central airways", label_visibility="collapsed")
    cent_air = st.text_input("Central airways", "Patent trachea and both main bronchi.", label_visibility="collapsed")

    st.subheader("Pleural cavity")
    sub_pleu = st.text_input("Title", "Pleural cavity", label_visibility="collapsed")
    pleural_eff = smart_selectbox("Pleural effusion", options["pleural_eff"])
    pneumothorax = st.text_input("Pneumothorax", "No pneumothorax.")

    st.subheader("Heart and great vessels")
    sub_great = st.text_input("Title", "Heart and great vessels", label_visibility="collapsed")
    heart_pericar = smart_selectbox("Heart&Pericardium", options["heart_pericar"])
    valve_cal = smart_selectbox("Calcified valve", options["valve_cal"])
    vessels_chest = smart_selectbox("Vessel chest", options["vessels_chest"])
    pulmo_artery = smart_selectbox("Pulmonay artery size", options["pulmo_artery"])

    st.subheader("Mediastinum")
    sub_medias = st.text_input("Title", "Mediastinum", label_visibility="collapsed")
    nodes_chest = smart_selectbox("Lymph node", options["nodes_chest"])

    st.subheader("Esophagus")
    sub_esophagus = st.text_input("Title", "Esophagus", label_visibility="collapsed")
    thorax_eso = smart_selectbox("Status", options["thorax_eso"], label_visibility="collapsed")
    
    st.subheader("Chest wall and lower neck")
    sub_wall = st.text_input("Title", "Chest wall and lower neck", label_visibility="collapsed")
    thyroid_breast1 = smart_selectbox("Thyroid&Breast1", options["thyroid_breast1"])
    thyroid_breast2 = smart_selectbox("Thyroid&Breast2", options["thyroid_breast2"])
    supraclav_axilla = st.text_input("Supraclav&axilla", "No supraclavicular or axillary lymph node enlargement.")

    st.subheader("Included upper abdomen")
    sub_upabd = st.text_input("Title", "Included upper abdomen", label_visibility="collapsed")
    upper_abd = smart_selectbox("appear", options["rest_upabd"], label_visibility="collapsed")

    st.subheader("Bony structures")
    sub_bones = st.text_input("Bones Title", "Bony structures", label_visibility="collapsed")
    bone_spine = smart_selectbox("Spine", options["bone_spine"])
    bone_listhesis = smart_selectbox("Spondylolisthesis", options["bone_listhesis"])
    bone_lesion = smart_selectbox("Bone lesion", options["bone_lesion"])
    bone_lytic = smart_selectbox("Osteoblastic/lytic", options["bone_lytic"])

    st.write("---")

    st.subheader("IMPRESSION")
    cad_rad = smart_selectbox("CAD-RADS", options["cad_rad"])
    imp_coro = st.text_area("Free Coro", "No demonstrated coronary artery stenosis or coronary artery calcification.")
    imp_free = st.text_area("Free text", "")
    imp_nodule = smart_selectbox("Lung nodule", options["imp_nodule"])

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
    
    report_text = f"{title}ANGIOGRAPHY OF THE CORONARY ARTERIES\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"TECHNIQUES: {techniques}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"
    
    report_text += f"{sub_coro}:\nImage quality = {coro_quality} HR = {coro_hr}\n{coro_dominant} {coro_anomaly}\n"
    report_text += f"Coronary artery calcification: {coro_calcium}\n"
    report_text += f"Left ventricular function: {coro_lvef}\n"
   
    report_text += f"\nCTA coronary arteries: \n"
    report_text += build_line(sub_rca, coro_rca)
    report_text += f"Proximal (S1): {coro_rcas1}\n"
    report_text += f"Mid (S2): {coro_rcas2}\n"
    report_text += f"Distal (S3): {coro_rcas3}\n"
    report_text += f"PDA (S4): {coro_rcas4}\n"
    report_text += f"PL: {coro_rcapl}\n\n"

    report_text += build_line(sub_lma, coro_lma, coro_lmas5)

    report_text += f"\n{sub_lad}: \n"
    report_text += f"Proximal (S6): {coro_lads6}\n"
    report_text += f"Mid (S7): {coro_lads7}\n"
    report_text += f"Distal (S8): {coro_lads8}\n"
    report_text += f"DG-1 (S9): {coro_lads9}\n"
    report_text += f"DG-2 (S10): {coro_lads10}\n"
    report_text += f"DG-3: {coro_laddg3}\n"

    report_text += f"\n{sub_lcx}: \n"
    report_text += f"Proximal (S11): {coro_lcxs11}\n"
    report_text += f"Mid/distal (S13): {coro_lcxs13}\n"
    report_text += f"OM-1 (S12): {coro_lcxs12}\n"
    report_text += f"OM-2 (S14): {coro_lcxs14}\n"
    report_text += f"OM-3 : {coro_lcxom3}\n"    

    report_text += f"\nCHEST\n"
    report_text += build_line(sub_tubes, val_tubes1, val_tubes2)
    report_text += f"{sub_lung}:\n"
    report_text += f"- \n"
    report_text += f"- {thorax_num1}{thorax_nodule1}{thorax_segment11}{thorax_segment12}{thorax_segment13}\n"
    report_text += f"- {thorax_num2}{thorax_nodule2}{thorax_segment21}{thorax_segment22}{thorax_segment23}\n"
    report_text += f"- {thorax_emphy}\n"
    report_text += f"- {thorax_no}\n"
    report_text += build_line(sub_air, cent_air)
    report_text += build_line(sub_pleu, pleural_eff, pneumothorax)
    report_text += build_line(sub_great, heart_pericar, valve_cal, vessels_chest, pulmo_artery)
    report_text += build_line(sub_medias, nodes_chest)
    report_text += build_line(sub_esophagus, thorax_eso)
    report_text += build_line(sub_wall, thyroid_breast1, thyroid_breast2, supraclav_axilla)
    report_text += build_line(sub_upabd, upper_abd)
    report_text += build_line(sub_bones, bone_spine, bone_listhesis, bone_lesion, bone_lytic)
    
    report_text += f"\nIMPRESSION:\n- CAD-RADS assessment: {cad_rad}, details as followed; \n- {imp_coro} \n\nOther:\n- {imp_free}\n- {imp_nodule}\n"

    report_text += f"\nAbbreviation: LMA = left main coronary artery, LAD = left anterior descending artery, LCX = left circumflex artery, RCA = right coronary artery, DG = diagonal branch, OM = obtuse marginal branch\n\nCAD RAD version 2.0: coronary artery disease-reporting and data system, published in 2016 by Society of Cardiovascular Computed Tomography (SCCT), the American Society for Cardiovascular Imaging (NASCI) and endorsed by the American College of Cardiology (ACC)\nCAD RADs: Assessment of stenosis degree\nCAD RADs 0: no stenosis\nCAD RADs 1: 1-24% stenosis\nCAD RADs 2: 25-49% stenosis\nCAD RADs 3: 50-70% stenosis\nCAD RADs 4: A 70-99% stenosis in 1 or 2 vessel. B: >50% stenosis in left main or > 70% stenosis in 3 vessels\nCAD RADs 5: 100% stenosis, total occlusion. "

    st.text_area("Edit and copy your report here:", value=report_text, height=900)