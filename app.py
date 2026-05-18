import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Nepal Govt Services Hub",
    page_icon="🇳🇵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling and block design
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Helvetica Neue', sans-serif;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #555555;
        margin-bottom: 30px;
    }
    .category-header {
        color: #B91C1C;
        border-bottom: 2px solid #B91C1C;
        padding-bottom: 5px;
        margin-top: 20px;
        margin-bottom: 15px;
        font-weight: bold;
    }
    .service-box {
        background-color: #F3F4F6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1E40AF;
        margin-bottom: 15px;
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .service-title {
        font-size: 16px;
        font-weight: bold;
        color: #1F2937;
        margin-bottom: 5px;
    }
    .service-desc {
        font-size: 13px;
        color: #4B5563;
        margin-bottom: 10px;
    }
    a.visit-btn {
        background-color: #1E40AF;
        color: white !important;
        padding: 6px 12px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 13px;
        border-radius: 5px;
        font-weight: bold;
    }
    a.visit-btn:hover {
        background-color: #1D4ED8;
    }
    </style>
""", unsafe_allowed_html=True)

# App Headers
st.markdown("<h1 class='main-title'>🇳🇵 Nepal Government Services Directory</h1>", unsafe_allowed_html=True)
st.markdown("<p class='sub-title'>All official utility portals, forms, and tender links in one single place.</p>", unsafe_allowed_html=True)

# Sidebar Disclaimer & Info
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/23/Emblem_of_Nepal.svg", width=100)
    st.title("About Project")
    st.info("""
        **Note:** Yeh ek navigation dashboard hai. Kisi bhi form ko fill karte waqt aap safe tarike se official `.gov.np` server par hi redirect honge.
    """)
    st.warning("⚠️ Data Privacy: Yeh dashboard aapka koi bhi personal data ya password store nahi karta.")

# Complete Data Dictionary of 50+ Portals organized by Categories
services_data = {
    "Identity & Personal Documents (Pehchan)": [
        {"name": "National ID (NID) Portal", "desc": "Rastriya Parichayapatra pre-enrollment form & status.", "url": "https://citizenportal.donidcr.gov.np"},
        {"name": "Department of Passport", "desc": "e-Passport online application & appointment booking.", "url": "https://nepalpassport.gov.np"},
        {"name": "Civil Registration (DONIDCR)", "desc": "Online birth, death, and marriage registration portal.", "url": "https://donidcr.gov.np"},
        {"name": "Department of DoFE (Caste/Verified)", "desc": "Verification and citizen portal.", "url": "https://dofe.gov.np"}
    ],
    "Transport & Licensing (Yatayat)": [
        {"name": "Online Driving License (DOTM)", "desc": "New license apply, category add, and renewal portal.", "url": "https://applydlnew.dotm.gov.np"},
        {"name": "Transport Management Information System", "desc": "Check driving license print status and smart card info.", "url": "http://dotm.gov.np"},
        {"name": "Bagmati Province Vehicle Tax", "desc": "Online bluebook renewal and vehicle tax calculations.", "url": "https://tmis.bagamati.gov.np"},
        {"name": "Koshi Province Transport Portal", "desc": "Vehicle tax and services for Koshi state.", "url": "https://mopit.koshi.gov.np"}
    ],
    "Jobs, Exams & Career (Naukri/Sewa)": [
        {"name": "Federal Lok Sewa Aayog", "desc": "Apply online for Civil Services (Nijamati) exams.", "url": "https://psconline.psc.gov.np"},
        {"name": "Teacher Service Commission (TSC)", "desc": "Government school teacher recruitment portal.", "url": "https://online.tsc.gov.np"},
        {"name": "Bagmati Province PSC", "desc": "Provincial public service vacancy forms.", "url": "https://ppsconline.bagamati.gov.np"},
        {"name": "Lumbini Province PSC", "desc": "Lumbini provincial vacancy application form.", "url": "https://ppsconline.lumbini.gov.np"},
        {"name": "Nepal Police Career Portal", "desc": "Online application for Inspectors, ASI, and Jawan.", "url": "https://career.nepalpolice.gov.np"},
        {"name": "Armed Police Force (APF) Recruitment", "desc": "APF recruitment application forms.", "url": "https://www.apf.gov.np"}
    ],
    "Tenders & Procurement (Sarkari Tender)": [
        {"name": "e-GP Portal (PPMO / Bolpatra)", "desc": "Centralized portal for national/international bidding & tenders.", "url": "https://bolpatra.gov.np/egp"},
        {"name": "Public Procurement Monitoring Office", "desc": "Procurement guidelines, rules, and blacklisted data.", "url": "https://ppmo.gov.np"},
        {"name": "Department of Roads Tenders", "desc": "Specific road construction projects and bids notice.", "url": "https://dor.gov.np"}
    ],
    "Taxation & Business (Kar aur Company)": [
        {"name": "Inland Revenue Department (IRD)", "desc": "File D-1/D-2/D-3 tax returns, verify PAN, and get tax clearance.", "url": "https://ird.gov.np"},
        {"name": "Office of Company Registrar (OCR)", "desc": "Online private/public company registration & annual returns.", "url": "https://ocr.gov.np"},
        {"name": "Department of Commerce (DoC)", "desc": "Private firm and partnership registration portal.", "url": "https://doc.gov.np"},
        {"name": "Nepal Customs Portal (Asycuda)", "desc": "Exim code registration and customs declaration forms.", "url": "https://customs.gov.np"}
    ],
    "Foreign Employment & Immigration (Bidesh Yatra)": [
        {"name": "FEIMS Portal (Labor Permit)", "desc": "Online Shram Swikriti and re-entry labor permit portal.", "url": "https://feims.dofe.gov.np"},
        {"name": "NepaliPort (Immigration Visa)", "desc": "Tourist visa on-arrival forms and trekking permits.", "url": "https://nepaliport.immigration.gov.np"},
        {"name": "Department of Foreign Employment", "desc": "Main directory for manpower status and complaints.", "url": "https://dofe.gov.np"}
    ],
    "Funds & Social Security (Sanchaya Kosh)": [
        {"name": "Social Security Fund (SSF)", "desc": "Online employee enrollment and medical claim submission.", "url": "https://ssf.gov.np"},
        {"name": "Employees Provident Fund (EPF)", "desc": "Sanchaya Kosh online KYC and special loan apply.", "url": "https://epfnepal.org.np"},
        {"name": "Citizen Investment Trust (CIT)", "desc": "Nagarik Lagani Kosh online statements and system.", "url": "https://nlk.org.np"}
    ],
    "Local Government (Main Municipalities)": [
        {"name": "Kathmandu Metropolitan City", "desc": "KMC building permits, maps, and local tax portal.", "url": "https://kathmandu.gov.np"},
        {"name": "Lalitpur Metropolitan City", "desc": "LMC local citizen services and online forms.", "url": "https://lalitpurmun.gov.np"},
        {"name": "Pokhara Metropolitan City", "desc": "Pokhara city local governance and e-services.", "url": "https://pokharamun.gov.np"},
        {"name": "MoFAGA Local Portal Directory", "desc": "Access links for all 753 local bodies/Gaunpalika.", "url": "https://mofaga.gov.np"}
    ]
}

# Live Search Bar Implementation
search_query = st.text_input("🔍 Kisi bhi service ya keyword ko dhoondhein (e.g., License, Tender, PAN, Passport)...", "").strip().lower()

# Render Logic
found_any = False

for category, services in services_data.items():
    # Filter services based on search query
    filtered_services = [s for s in services if search_query in s['name'].lower() or search_query in s['desc'].lower()]
    
    if filtered_services:
        found_any = True
        st.markdown(<div class='category-header'>{category}</div>, unsafe_allowed_html=True)
        
        # Grid System: 3 Columns per row
        cols = st.columns(3)
        for index, service in enumerate(filtered_services):
            col_to_use = cols[index % 3]
            with col_to_use:
                block_html = f"""
                <div class="service-box">
                    <div>
                        <div class="service-title">{service['name']}</div>
                        <div class="service-desc">{service['desc']}</div>
                    </div>
                    <div>
                        <a href="{service['url']}" target="_blank" class="visit-btn">Open Official Site ↗</a>
                    </div>
                </div>
                """
                st.markdown(block_html, unsafe_allowed_html=True)

if not found_any:
    st.error("❌ Oops! Aapke search se match karta hua koi portal nahi mila. Kripya doosra keyword try karein.")
