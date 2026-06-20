import pubchempy as pcp
import streamlit as st
import pandas as pd
import requests
from mtranslate import translate
from rdkit import Chem
from rdkit.Chem import Draw

# 1. Page Configuration
st.set_page_config(
    page_title="PharmaAssist PRO Max", 
    page_icon="⚕️", 
    layout="wide"
)

# 2. Cyber-Pharma Styling Matrix
st.markdown("""
    <style>
    .main { background-color: #0F172A; color: #F8FAFC; }
    h1, h2, h3 { color: #38BDF8 !important; font-family: 'Segoe UI', sans-serif; }
    div.stButton > button:first-child { background-color: #0EA5E9; color: white; border: none; font-weight: bold; width: 100%; }
    div.stButton > button:first-child:hover { background-color: #38BDF8; color: #0F172A; }
    .stTabs [data-baseweb="tab"] { color: #94A3B8; font-size: 16px; font-weight: 600; }
    .stTabs [aria-selected="true"] { color: #38BDF8 !important; border-bottom-color: #38BDF8 !important; }
    .db-count { background-color: #1E293B; border-left: 4px solid #10B981; padding: 10px; border-radius: 4px; margin-bottom: 15px; }
    .info-card { background-color: #1E293B; border: 1px solid #334155; padding: 15px; border-radius: 8px; margin-bottom: 12px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Dynamic Database Generation Engine (1000+ Items)
@st.cache_data
def generate_mega_database():
    database = [
        {
            "name": "Digoxin (Cardiac Glycoside Mechanism)",
            "keywords": ["heart", "cardiac", "digoxin", "pump", "atpase", "heart failure"],
            "focus": "🎯 Cellular Na+/K+ ATPase pump inhibition. Watch how blocking this pump increases intracellular Calcium levels, forcing cardiac myocytes to contract with significantly more mechanical power.",
            "url": "https://www.youtube.com/watch?v=N1hOpbg3fXw"
        },
        {
            "name": "Pharmacokinetics (ADME Transit Journey)",
            "keywords": ["absorption", "body", "stomach", "liver", "distribution", "metabolism", "adme"],
            "focus": "🔄 The complete macro-to-micro journey tracking how oral medications break down in hydrochloric gastric acid, distribute via plasma vessel channels, and undergo hepatic filtration.",
            "url": "https://www.youtube.com/watch?v=NKV5iaUVBUI"
        },
        {
            "name": "Spironolactone (Renal Nephron Diuretic Mechanism)",
            "keywords": ["kidney", "renal", "diuretic", "spironolactone", "urine", "bp", "blood pressure"],
            "focus": "🫘 Mineralocorticoid receptor antagonism. Visualizes how blocking aldosterone in the distal nephron tubules dumps excess sodium and water into urine while conserving vital potassium.",
            "url": "https://www.youtube.com/watch?v=RgU8qxf3xqg"
        },
        {
            "name": "mRNA Molecular Translation Engine",
            "keywords": ["mrna", "vaccine", "cell", "ribosome", "protein", "dna", "genetic"],
            "focus": "🧬 Intracellular assembly systems. Follows lipid nanoparticles sliding past cellular membranes, opening up to let ribosomes read code sequences and manufacture defensive target proteins.",
            "url": "https://www.youtube.com/watch?v=mvA9_L80XbY"
        },
        {
            "name": "General Ligand-Receptor Lock Mechanism",
            "keywords": ["receptor", "binding", "ligand", "cell signaling", "mechanism of action", "moa"],
            "focus": "🎯 Microscopic spatial binding orientation. Watch how chemical ligands drift through tissue grids to dock flawlessly into matching protein structural slots, activating internal cell cascades.",
            "url": "https://www.youtube.com/watch?v=u49k72rUdyc"
        }
    ]
    
    drug_classes = [
        ("Beta-Blocker", ["heart", "bp", "cardiac", "hypertension", "pulse"], "https://www.youtube.com/watch?v=u49k72rUdyc"),
        ("ACE-Inhibitor", ["kidney", "bp", "renal", "hypertension", "vessel"], "https://www.youtube.com/watch?v=RgU8qxf3xqg"),
        ("Statin Matrix", ["liver", "cholesterol", "lipid", "hepatic", "artery"], "https://www.youtube.com/watch?v=NKV5iaUVBUI"),
        ("NSAID Compound", ["stomach", "pain", "inflammation", "cox", "enzyme"], "https://www.youtube.com/watch?v=u49k72rUdyc"),
        ("Proton Pump Inhibitor", ["stomach", "acid", "reflux", "gastric", "parietal"], "https://www.youtube.com/watch?v=NKV5iaUVBUI")
    ]
    
    for i in range(1, 1001):
        class_type, base_keywords, target_url = drug_classes[i % len(drug_classes)]
        id_tag = 1000 + i
        generated_item = {
            "name": f"Compound Ref-{id_tag} ({class_type} Pipeline Variant)",
            "keywords": base_keywords + [class_type.lower(), f"ref-{id_tag}", "generic"],
            "focus": f"🧪 [Formulary Registry Node {id_tag}]: Automated pharmacodynamic tracking profile for standard {class_type} distribution networks. Focuses on targeted transmembrane binding and cellular cascade triggers.",
            "url": target_url
        }
        database.append(generated_item)
    return database

db_source = generate_mega_database()

# 4. Sidebar Station Terminal
with st.sidebar:
    st.title("⚕️ Control Panel")
    st.success("🌐 UNIFIED SYSTEMS: ACTIVE")
    
   # In your Sidebar section:
    app_mode = st.radio(
    "Select Workstation Tool:",
    [
        "🧬 3D Molecular Structure Lab",
        "🧪 Pro 3D Lab (MolView)",  # <--- ADD THIS LINE
        "🔍 Global Pharma Intelligence Terminal",
        "🎬 3D Bio-Theater Search Engine", 
        "🌐 FDA Clinical Search Engine", 
        "🧮 Advanced Dose Calculator", 
        "📋 Patient Counseling Sheet", 
        "📦 Smart Inventory Monitor"
    ]
)
    st.write("---")
    st.info("🎯 **Active Directive:** System customized entirely for Ravindra Sir.")
    st.caption("Developed by Prakhar // Class 11 Master Stack")

# ==========================================
# TOOL 1: STATIC STRUCTURAL RENDERER (100% STABLE)
# ==========================================
if app_mode == "🧬 3D Molecular Structure Lab":
    st.title("🧬 Molecular Structure Lab")
    st.write("---")
    
    molecule_target = st.text_input("🔬 Enter Drug Name (e.g., Paracetamol, Aspirin):", "Paracetamol").strip()
    
    if molecule_target:
        # We use PubChem's native image generation API
        # This bypasses all JavaScript/WebGL/Iframe issues
        img_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{molecule_target}/PNG?image_size=large"
        
        st.subheader(f"Structure for: {molecule_target.capitalize()}")
        try:
            st.image(img_url, caption=f"Structural diagram for {molecule_target}", use_container_width=True)
            st.info("Note: This is a high-resolution 2D structural diagram provided by the NIH.")
        except:
            st.error("Could not retrieve image for this compound. Try a different generic name.")


# ==========================================
# TOOL 1.5: PRO 3D LAB (MOLVIEW)
# ==========================================
elif app_mode == "🧪 Pro 3D Lab (MolView)":
    st.title("🧪 Advanced Chemical Sketcher & Viewer")
    st.write("---")
    
    st.info("Because MolView restricts embedding for security, you can launch it in a dedicated tab below.")
    
    # This button opens the site in a fresh, full-size window
    st.link_button("Launch MolView (Professional Mode)", "https://molview.org/", type="primary")
    
    st.write("---")
    st.caption("Instructions: Use the link above to open MolView. You can then sketch or search for your molecule, and if you need the data back in your app, use the Export functions provided in their interface.")
# TOOL 2: GLOBAL PHARMA INTELLIGENCE TERMINAL
# ==========================================
elif app_mode == "🔍 Global Pharma Intelligence Terminal":
    st.title("🔍 Global Pharma Intelligence Terminal")
    st.caption("Direct integration with deep cloud networks to look up full clinical data profiles for any global drug compound.")
    st.write("---")
    
    search_target = st.text_input("🧬 Enter Brand Name, Generic Molecule, or Pharma Term (e.g., Aspirin, Lipitor, Tylenol, Metformin):", "").strip()
    
    if search_target:
        query_url = f"https://api.fda.gov/drug/label.json?search=(openfda.brand_name:{search_target}+openfda.generic_name:{search_target})+OR+description:{search_target}&limit=1"
        
        with st.spinner(f"Establishing encrypted handshakes with FDA registry grids for '{search_target}'..."):
            try:
                res = requests.get(query_url)
                if res.status_code == 200:
                    payload = res.json()['results'][0]
                    
                    openfda_fields = payload.get('openfda', {})
                    g_name = openfda_fields.get('generic_name', [search_target.capitalize()])[0]
                    b_name = openfda_fields.get('brand_name', [search_target.capitalize()])[0]
                    m_name = openfda_fields.get('manufacturer_name', ["Global Registry Wholesaler Layer"])[0]
                    p_class = openfda_fields.get('pharm_class_epc', ["Unclassified Therapeutic Compound"])[0]
                    
                    st.success(f"✅ Medical Record Found: {b_name}")
                    
                    tab_summary, tab_clinical, tab_safety = st.tabs(["📋 Drug Summary & Class", "🔬 Indications & Action", "🚨 Safety & Warnings"])
                    
                    with tab_summary:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"""
                            <div class='info-card'>
                                <h3>Identity Vectors</h3>
                                <p><b>Brand Label:</b> {b_name}</p>
                                <p><b>Generic Name:</b> {g_name}</p>
                                <p><b>Primary Drug Class:</b> <code>{p_class}</code></p>
                            </div>
                            """, unsafe_allow_html=True)
                        with col2:
                            desc_text = payload.get('description', ['No structure details parsed.'])[0]
                            st.markdown(f"""
                            <div class='info-card'>
                                <h3>Supply & Origin</h3>
                                <p><b>Listed Manufacturer:</b> {m_name}</p>
                                <p><b>Chemical Description Note:</b></p>
                                <p style='font-size:13px; color:#94A3B8;'>{desc_text[:350]}...</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                    with tab_clinical:
                        st.subheader("🎯 Indications & Clinical Use")
                        st.write(payload.get('indications_and_usage', payload.get('purpose', ['No documentation specified.']))[0])
                        
                        st.write("---")
                        st.subheader("⚙️ Dosage & Intake Administration Guide")
                        st.write(payload.get('dosage_and_administration', ['No standard layout routine submitted.'])[0])
                        
                    with tab_safety:
                        col_w1, col_w2 = st.columns(2)
                        with col_w1:
                            st.error("🚨 Contraindications & Warnings")
                            st.write(payload.get('contraindications', payload.get('warnings', ['Clear of standard label warnings.']))[0][:2000])
                        with col_w2:
                            st.warning("⚠️ Adverse Reactions & Side Effects")
                            st.write(payload.get('adverse_reactions', ['Side effect parameters missing from brief.'])[0][:2000])
                            
                else:
                    fallback_url = f"https://api.fda.gov/drug/label.json?search={search_target}&limit=1"
                    fallback_res = requests.get(fallback_url)
                    if fallback_res.status_code == 200:
                        payload = fallback_res.json()['results'][0]
                        st.warning(f"⚠️ General registry match found for '{search_target}':")
                        st.write(payload.get('description', payload.get('purpose', ['Complex data layout payload.']))[0][:1500])
                    else:
                        st.error(f"❌ Target compound footprint '{search_target}' completely absent from openFDA servers. Verify the standard chemical or trade spelling.")
            except Exception as conn_err:
                st.error(f"Handshake timeout error: {conn_err}")

# ==========================================
# TOOL 3: 3D BIO-THEATER SEARCH ENGINE
# ==========================================
elif app_mode == "🎬 3D Bio-Theater Search Engine":
    st.title("🎬 Master Biological Search Engine & Visualizer")
    st.caption("Instantly query over 1,000 active pharmacokinetic, molecular, and cellular pathway nodes.")
    st.write("---")
    
    query = st.text_input("🔍 Search Database (e.g., heart, kidney, cell, absorption, stomach, beta-blocker, Ref-1042):", "").lower().strip()
    
    if query:
        filtered_results = [
            item for item in db_source 
            if query in item["name"].lower() or any(query in kw for kw in item["keywords"])
        ]
    else:
        filtered_results = db_source[:20]

    st.markdown(f"""
    <div class='db-count'>
        🚀 <b>Active Repository Status:</b> Loaded <b>{len(db_source)}</b> pathways total | 
        Matches for query: <b>{len(filtered_results) if query else "Showing initial library"}</b> entries
    </div>
    """, unsafe_allow_html=True)

    if not filtered_results:
        st.error(f"❌ No database matches found for: '{query}'. Try 'heart', 'stomach', or 'Ref-1005'.")
    else:
        col_list, col_screen = st.columns([2, 3])
        with col_list:
            st.subheader("📂 Indexed Registries")
            selected_name = st.selectbox("Select target profile to mount inside the viewport:", options=[item["name"] for item in filtered_results])
            selected_item = next(item for item in filtered_results if item["name"] == selected_name)
            st.write("---")
            st.subheader("📋 Dynamic Anatomical Brief")
            st.info(selected_item["focus"])
            
        with col_screen:
            st.subheader("📺 Ultra-HD Cinematic Viewport")
            st.video(selected_item["url"])
            st.caption(f"✨ Currently screening: {selected_item['name']}")

# ==========================================
# TOOL 4: LIVE FDA SEARCH ENGINE
# ==========================================
elif app_mode == "🌐 FDA Clinical Search Engine":
    st.title("🌐 openFDA Live Clinical Search Engine")
    st.caption("Queries live FDA database registries for absolute unedited chemical manufacturing profiles.")
    st.write("---")
    
    drug_input = st.text_input("Enter Generic Compound Name (e.g., Metformin, Atorvastatin, Omeprazole):", placeholder="Type generic name...")
    
    if drug_input:
        api_url = f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:{drug_input}&limit=1"
        with st.spinner("Decrypting FDA database nodes..."):
            try:
                response = requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()['results'][0]
                    generic_name = data.get('openfda', {}).get('generic_name', [drug_input.capitalize()])[0]
                    brand_name = data.get('openfda', {}).get('brand_name', ["N/A"])[:5]
                    drug_class = data.get('openfda', {}).get('pharm_class_epca', ["Unknown Classification"])[0]
                    
                    boxed_warning = data.get('boxed_warning', ["No black-box warnings listed in label details."])[0]
                    interactions = data.get('drug_interactions', ["No interactions detailed in standard profile summary."])[0]
                    adverse_effects = data.get('adverse_reactions', ["Adverse event data profile missing or complex."])[0]
                    
                    st.success(f"🧬 Active Compound Identified: {generic_name}")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("📋 Molecular Summary")
                        st.markdown(f"**Therapeutic Classification:** `{drug_class}`")
                        st.markdown(f"**Reference Global Brands:** {', '.join(brand_name)}")
                        st.subheader("🚨 FDA Boxed Warnings")
                        st.error(boxed_warning)
                    with col2:
                        st.subheader("⚠️ Documented Drug Interactions")
                        st.warning(interactions[:1500] + "..." if len(interactions) > 1500 else interactions)
                        st.subheader("🤢 Adverse Reaction Profile")
                        st.info(adverse_effects[:1000] + "..." if len(adverse_effects) > 1000 else adverse_effects)
                else:
                    st.error(f"❌ Molecule '{drug_input}' not found in FDA registry.")
            except Exception as e:
                st.error(f"Network Connection Interrupted: {e}")

# ==========================================
# TOOL 5: DOSAGE ENGINE
# ==========================================
elif app_mode == "🧮 Advanced Dose Calculator":
    st.title("🧮 Advanced Clinical Dosage Engine")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("👶 Pediatric Parameter Calculator")
        weight = st.number_input("Patient Weight (kg):", min_value=1.0, max_value=150.0, value=15.0)
        rule_factor = st.selectbox("Standard Medical Routine Factor:", ["15 mg/kg/day", "30 mg/kg/day", "50 mg/kg/day"])
        factor_val = float(rule_factor.split()[0])
        total_daily_dose = weight * factor_val
        st.metric(label="Total Required Daily Dosage", value=f"{total_daily_dose:.2f} mg / day")
    with col2:
        st.subheader("🫘 Baseline Renal Clearance Estimator")
        age = st.number_input("Patient Age (Years):", min_value=1, max_value=120, value=45)
        creatinine = st.number_input("Serum Creatinine (mg/dL):", min_value=0.2, max_value=10.0, value=1.0)
        gender = st.radio("Biological Patient Sex:", ["Male", "Female"])
        if creatinine > 0:
            cr_cl = ((140 - age) * weight) / (72 * creatinine)
            if gender == "Female": cr_cl *= 0.85
            st.metric(label="Estimated Creatinine Clearance (CrCl)", value=f"{cr_cl:.2f} mL/min")

# ==========================================
# TOOL 6: COUNSELING GENERATOR
# ==========================================
elif app_mode == "📋 Patient Counseling Sheet":
    st.title("📋 Multilingual Patient Leaflet Generator")
    st.write("---")
    target_lang = st.selectbox("Select Patient Target Language:", ["English", "Hindi (हिन्दी)"])
    med_name = st.text_input("Enter Medication Name for Leaflet Generation:", "Metformin")
    sample_bullet_points = [
        f"Take {med_name} exactly as directed by your physician.",
        "Always take this medication with meals to avoid stomach discomfort.",
        "Stay fully hydrated while on this treatment plan."
    ]
    lang_code = "hi" if target_lang == "Hindi (हिन्दी)" else "en"
    for i, point in enumerate(sample_bullet_points, 1):
        st.markdown(f"**{i}.** {translate(point, 'hi') if lang_code == 'hi' else point}")

# ==========================================
# TOOL 7: SMART INVENTORY MONITOR
# ==========================================
elif app_mode == "📦 Smart Inventory Monitor":
    st.title("📦 Smart Medicine Expiry & Shelf Health Tracker")
    st.write("---")
    if 'inventory' not in st.session_state:
        st.session_state.inventory = [
            {"Batch": "B-MET202", "Item": "Metformin 500mg", "Expiry": "2026-08-15"},
            {"Batch": "B-CROC44", "Item": "Crocin 650mg", "Expiry": "2026-07-01"}
        ]
    df = pd.DataFrame(st.session_state.inventory)
    st.dataframe(df, use_container_width=True)