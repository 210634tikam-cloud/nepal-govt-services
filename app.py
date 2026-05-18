import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Nepal Govt Services Hub",
    page_icon="🇳🇵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Native App Headers (No raw HTML styling to avoid version bugs)
st.title("🇳🇵 Nepal Government Services Directory")
st.write("All official utility portals, forms, and tender links in one single place.")

# Sidebar Disclaimer & Info
with st.sidebar:
    st.title("About Project")
    st.info("**Note:** Yeh ek navigation dashboard hai. Kisi bhi form ko fill karte waqt aap safe tarike se official .gov.np server par hi redirect honge.")
    st.warning("⚠️ Data Privacy: Yeh dashboard aapka koi bhi personal data ya password store nahi karta.")

# Complete Data Dictionary
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
        {"name": "Nepal Police Career Portal", "desc": "Online application for Inspectors, ASI, and Jawan.", "url": "https://career.nepalpolice.gov.np"}
    ],
    "Tenders & Procurement (Sarkari Tender)": [
        {"name": "e-GP Portal (PPMO / Bolpatra)", "desc": "Centralized portal for national/international bidding & tenders.", "url": "https://bolpatra.gov.np/egp"},
        {"name": "Public Procurement Monitoring Office", "desc": "Procurement guidelines, rules, and blacklisted data.", "url": "https://ppmo.gov.np"},
        {"name": "Department of Roads Tenders", "desc": "Specific road construction projects and bids notice.", "url": "https://dor.gov.np"}
    ],
    "Taxation & Business (Kar aur Company)": [
        {"name": "Inland Revenue Department (IRD)", "desc": "File D-1/D-2/D-3 tax returns, verify PAN, and get tax clearance.", "url": "https://ird.gov.np"},
        {"name": "Office of Company Registrar (OCR)", "desc": "Online private/public company registration & annual returns.", "url": "https://ocr.gov.np"},
        {"name": "Department of Commerce (DoC)", "desc": "Private firm and partnership registration portal.", "url": "https://doc.gov.np"}
    ],
    "Foreign Employment & Immigration (Bidesh Yatra)": [
        {"name": "FEIMS Portal (Labor Permit)", "desc": "Online Shram Swikriti and re-entry labor permit portal.", "url": "https://feims.dofe.gov.np"},
        {"name": "NepaliPort (Immigration Visa)", "desc": "Tourist visa on-arrival forms and trekking permits.", "url": "https://nepaliport.immigration.gov.np"}
    ],
    "Funds & Social Security (Sanchaya Kosh)": [
        {"name": "Social Security Fund (SSF)", "desc": "Online employee enrollment and medical claim submission.", "url": "https://ssf.gov.np"},
        {"name": "Employees Provident Fund (EPF)", "desc": "Sanchaya Kosh online KYC and special loan apply.", "url": "https://epfnepal.org.np"}
    ],
    "Local Government (Main Municipalities)": [
        {"name": "Kathmandu Metropolitan City", "desc": "KMC building permits, maps, and local tax portal.", "url": "https://kathmandu.gov.np"},
        {"name": "Lalitpur Metropolitan City", "desc": "LMC local citizen services and online forms.", "url": "https://lalitpurmun.gov.np"},
        {"name": "Pokhara Metropolitan City", "desc": "Pokhara city local governance and e-services.", "url": "https://pokharamun.gov.np"}
    ]
}

# Search Bar
search_query = st.text_input("🔍 Search for a service (e.g., License, Tender, PAN)...", "").strip().lower()

found_any = False

# Render Layout using Streamlit Native Containers
for category, services in services_data.items():
    filtered_services = [s for s in services if search_query in s['name'].lower() or search_query in s['desc'].lower()]
    
    if filtered_services:
        found_any = True
        st.header(category)
        
        cols = st.columns(3)
        for index, service in enumerate(filtered_services):
            col_to_use = cols[index % 3]
            with col_to_use:
                # Native container instead of raw HTML blocks
                with st.container(border=True):
                    st.subheader(service['name'])
                    st.write(service['desc'])
                    st.link_button("Open Official Site ↗", service['url'], use_container_width=True)

if not found_any:
    st.error("❌ No matching service found. Try another keyword.")
 
