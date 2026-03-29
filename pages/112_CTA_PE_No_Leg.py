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

st.title("🩻 CTA for PE (no leg) Report by Bright")

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
    history = st.text_area("History", "Case of xx, presented with xx. The current CT was requested to rule out acute pulmonary embolism.")
    techniques = st.text_area("Techniques", "Axial helical CTA scan of the pulmonary arteries (1-mm slice thickness).")
    comparison1 = smart_selectbox("Comparison1", options["compareCTMR1"])
    comparison2 = smart_selectbox("Comparison2", options["compareCTMR2"])

    st.write("---")
    
    st.subheader("Limitation")
    limit1 = smart_selectbox("Limit1", options["limit"])
    limit2 = smart_selectbox("Limit2", options["limit"])
    
    st.subheader("Pulmonary arteries")
    sub_pulmo = st.text_input("Title", "Pulmonary arteries", label_visibility="collapsed")
    pulmo_adeq = smart_selectbox("Adequacy of study", options["adeq"], label_visibility="collapsed")
    pulmo_emboli = smart_selectbox("Pulmonay embolism", options["pulmo_emboli"])
    pulmo_branch = smart_selectbox("Pulmonay artery branch", options["pulmo_branch"], label_visibility="collapsed")
    pulmo_misc = smart_selectbox("Pulmonay Misc", options["pulmo_misc"], label_visibility="collapsed")
    pulmo_artery = smart_selectbox("Pulmonay artery size", options["pulmo_artery"])
    pulmo_no = st.text_input("PA No", "No pulmonary artery pseudoaneurysm or active contrast extravasation.")

    st.subheader("Right ventricular (RV) evaluation on apical four-chamber view")
    sub_rv = st.text_input("Title", "Right ventricular (RV) evaluation on apical four-chamber view", label_visibility="collapsed")
    rv_lv = st.text_input("RV:LV", "RV:LV = $", label_visibility="collapsed")
    rv_sep = st.text_input("Intervent", "No straightening of the interventricular septum.", label_visibility="collapsed")
    rv_reflux = st.text_input("Reflux", "No reflux of IV contrast into the IVC or hepatic veins.", label_visibility="collapsed")

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
    sub_great = st.text_input("Title", "Heart and great vessel", label_visibility="collapsed")
    heart_pericar = smart_selectbox("Heart&Pericardium", options["heart_pericar"])
    valve_cal = smart_selectbox("Calcified valve", options["valve_cal"])
    vessels_chest = smart_selectbox("Vessel chest", options["vessels_chest"])

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
    CTA_no = st.text_input("CTA NO", "No evidence of acute pulmonary embolism.")
    imp_free1 = st.text_area("Free text1", "")
    imp_free2 = st.text_area("Free text2", "")
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
    
    report_text = f"{title}PULMONARY ANGIOGRAPHY\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"TECHNIQUES: {techniques}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"

    report_text += f"CTA\n"
    report_text += f"Adequacy of study: {pulmo_adeq}\n"
    report_text += f"{sub_pulmo}:\n"
    report_text += f"- {pulmo_emboli}{pulmo_branch} {pulmo_misc}\n"
    report_text += f"- {pulmo_artery} {pulmo_no}\n"
    report_text += build_line(sub_rv, rv_lv, rv_sep, rv_reflux)
    
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
    report_text += build_line(sub_great, heart_pericar, valve_cal, vessels_chest)
    report_text += build_line(sub_medias, nodes_chest)
    report_text += build_line(sub_esophagus, thorax_eso)
    report_text += build_line(sub_wall, thyroid_breast1, thyroid_breast2, supraclav_axilla)
    report_text += build_line(sub_upabd, upper_abd)
    report_text += build_line(sub_bones, bone_spine, bone_listhesis, bone_lesion, bone_lytic)
    
    report_text += f"\nIMPRESSION:\n- {CTA_no}\n- {imp_free1}\n- {imp_free2}\n- {imp_nodule}\n- "

    st.text_area("Edit and copy your report here:", value=report_text, height=900)