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

st.title("🩻 CTA WHOLE AORTA Report by Bright")

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
    title = smart_selectbox("Title", options["titleCT"])
    history = st.text_area("History", "Case of xx, presented with xx. This CT was requested to rule-out aortic dissection.")
    techniques = st.text_area("Techniques", "Axial helical scan of the whole aorta with 1.25-mm slice thickness.")
    comparison1 = smart_selectbox("Comparison1", options["compareCTMR1"])
    comparison2 = smart_selectbox("Comparison2", options["compareCTMR2"])

    st.write("---")
    
    st.subheader("Limitation")
    limit1 = smart_selectbox("Limit1", options["limit"])
    limit2 = smart_selectbox("Limit2", options["limit"])

    st.subheader("Aorta")
    sub_aorta = st.text_input("Aorta", "Aorta", label_visibility="collapsed")
    aorta_athero = st.text_area("Athero", "Aortic atherosclerosis seen as multifocal calcified and soft plaques along ascending aorta, aortic arch, descending thoracic aorta and abdominal aorta, and coronary arteries.")
    aorta_no = smart_selectbox("Aorta No", options["aorta_no"])
    aorta_sinus = st.text_input("Aorta diameter", "Aortic sinuses of Valsalva xx cm")
    aorta_junc =  st.text_input("STJ", "Sinotubular junction xx cm", label_visibility="collapsed")
    aorta_midas =  st.text_input("Mid ascending", "Mid ascending aorta xx cm", label_visibility="collapsed")
    aorta_prox =  st.text_input("Proximal arch", "Proximal aortic arch (between LCCA and SCA) xx cm", label_visibility="collapsed")
    aorta_desd =  st.text_input("Proxiaml descending", "Proximal descending thoracic aorta (2 cm distal to SCA) xx cm", label_visibility="collapsed")
    aorta_middes =  st.text_input("Mid descending", "Mid descending aorta xx cm", label_visibility="collapsed")
    aorta_diaphr =  st.text_input("Aorta diaphragm", "Aorta at diaphragm xx cm", label_visibility="collapsed")
    aorta_celiac =  st.text_input("Aorta celiac", "Abdominal aorta at celiac axis origin xx cm", label_visibility="collapsed")
    aorta_rra =  st.text_input("Aorta RRA", "Abdominal aorta at right renal artery origin xx cm", label_visibility="collapsed")
    aorta_infra =  st.text_input("Aorta infrarenal", "Abdominal aorta at mid-point between renal and bifurcation xx cm", label_visibility="collapsed")
    aorta_bifurc =  st.text_input("Aorta Bifurc", "Abdominal aorta just above bifurcation xx cm", label_visibility="collapsed")
  
    st.subheader("Aortic branches")
    sub_aorbranch = st.text_input("Aortic branches", "Aortic branches", label_visibility="collapsed")
    aorta_branch = st.text_area("Athero", "Patent celiac trunk, SMA, IMA and bilateral renal arteries. No aneurysm or dissection. No aneurysm or dissection.")
 
    st.subheader("Iliac artery diameters")
    sub_iliac = st.text_input("Iliac artery diameters", "Iliac artery diameters", label_visibility="collapsed")
    iliac_athero = st.text_area("Athero", "Multifocal calcified and soft plaques at bilateral common iliac, internal iliac and external iliac arteries.")
    iliac_common =  st.text_input("Common iliac a.", "Right/left common iliac arteries x and x cm, respectively.", label_visibility="collapsed")
    iliac_external =  st.text_input("External iliac a.", "Right/left external iliac arteries x and x cm, respectively.", label_visibility="collapsed")
    
    st.subheader("Periaortic tissues")
    sub_periaortic = st.text_input("Periaortic tissues", "Periaortic tissues", label_visibility="collapsed")
    aorta_peri = st.text_area("Hematoma", "No periaortic, mediastinal or retroperitoneal hematoma.")

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

    st.subheader("Heart and other great vessels")
    sub_great = st.text_input("Title", "Heart and other great vessel", label_visibility="collapsed")
    heart_pericar = smart_selectbox("Heart&Pericardium", options["heart_pericar"])
    valve_cal = smart_selectbox("Calcified valve", options["valve_cal"])
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

    st.write("---")

    st.subheader("Liver")
    sub_liver = st.selectbox("Title", options["sub_liver"], label_visibility="collapsed")
    liver_parenchyma = smart_selectbox("Liver Parenchyma", options["liver_parenchyma"])
    liver_lesion1 = smart_selectbox("Liver Lesion1", options["liver_lesion"])
    liver_lesion2 = smart_selectbox("Liver Lesion2", options["liver_lesion"])
    liver_no = smart_selectbox("Liver NO", options["liver_no"])
    liver_vessels = smart_selectbox("Liver Vessels", options["liver_vessels"])
    liver_collat = smart_selectbox("Portosystemic collateral", options["liver_collat"])

    st.subheader("Gallbladder")
    sub_gb = st.selectbox("Title", options["sub_gb"], label_visibility="collapsed")
    gb_status = smart_selectbox("GB Status", options["gb_status"])
    bile_duct = smart_selectbox("Bile Ducts", options["bile_duct"])

    st.subheader("Pancreas")
    sub_pancreas = st.selectbox("Title", options["sub_pancreas"], label_visibility="collapsed")
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
    sub_kidneys = st.selectbox("Title", options["sub_kidney"], label_visibility="collapsed")
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

    st.subheader("Bony structures")
    sub_bones = st.text_input("Bones Title", "Bony structures", label_visibility="collapsed")
    bone_spine = smart_selectbox("Spine", options["bone_spine"])
    bone_listhesis = smart_selectbox("Spondylolisthesis", options["bone_listhesis"])
    bone_lesion = smart_selectbox("Bone lesion", options["bone_lesion"])
    bone_lytic = smart_selectbox("Osteoblastic/lytic", options["bone_lytic"])

    st.write("---")

    st.subheader("IMPRESSION")
    imp_freecta = st.text_area("Free CTA", "")
    imp_freenonvas = st.text_area("Free Non-vascular", "")
    imp_nodule = smart_selectbox("Lung nodule", options["imp_nodule"])
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
    
    report_text = f"{title}ANGIOGRAPHY OF THE WHOLE AORTA\n\n"
    report_text += f"HISTORY: {history}\n"
    report_text += f"TECHNIQUES: {techniques}\n"
    report_text += f"COMPARISON: {comparison1}{comparison2}\n\n"
    report_text += f"FINDINGS: {limit1} {limit2}\n"

    report_text += f"CTA\n"
    report_text += f"{sub_aorta}:\n- {aorta_athero} \n- {aorta_no}\n"
    report_text += f"Aortic diameters:\n{aorta_sinus} \n{aorta_junc} \n{aorta_midas} \n {aorta_prox}\n {aorta_desd}\n {aorta_middes}\n {aorta_diaphr}\n {aorta_celiac}\n {aorta_rra}\n {aorta_infra}\n {aorta_bifurc}\n "
    report_text += build_line(sub_aorbranch, aorta_branch)
    report_text += build_line(sub_iliac, iliac_athero)
    report_text += f"{iliac_common} \n{iliac_external} \n"
    report_text += build_line(sub_periaortic, aorta_peri)
    
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
    report_text += build_line(sub_great, heart_pericar, valve_cal, pulmo_artery)
    report_text += build_line(sub_medias, nodes_chest)
    report_text += build_line(sub_esophagus, thorax_eso)
    report_text += build_line(sub_wall, thyroid_breast1, thyroid_breast2, supraclav_axilla)

    report_text += f"\nABDOMEN\n"
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
    report_text += build_line(sub_bones, bone_spine, bone_listhesis, bone_lesion, bone_lytic)
    
    report_text += f"\nIMPRESSION:\nVascular\n- {imp_freecta} \n"
    report_text += f"Non-vascular\n- {imp_freenonvas}\n- {imp_nodule}\n- {imp_gb}"

    st.text_area("Edit and copy your report here:", value=report_text, height=900)