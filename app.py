import streamlit as st

# 1. Page Layout & Configuration (Top par hona compulsory hai)
st.set_page_config(
    page_title="Nepal Govt Services Hub",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/2/23/Emblem_of_Nepal.svg", # Clean official logo
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Native App Headers
st.title("🇳🇵 Nepal Government Services Directory")
st.write("### All 56 Official Utility Portals, Forms, and Tender Links in One Place.")
st.write("---")

# 3. Sidebar Dashboard Info
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/23/Emblem_of_Nepal.svg", width=120)
    st.title("Project Controls")
    st.info("**Information Directory:** Yeh ek native navigation matrix hai. Kisi bhi form ko click karne par aap secure tarike se official `.gov.np` server par hi redirect honge.")
    st.warning("🔒 **Data Privacy Guarantee:** This application is serverless on the client-side. It does not store or intercept any PII, biometric data, or credentials.")

# 4. Complete 56 Portals Database Categorized Academically
services_data = {
    "1. Identity, Citizenship & Vital Events (Pehchan aur Darta)": [
        {"name": "National ID (NID) Portal", "desc": "Rastriya Parichayapatra pre-enrollment & biometric schedule.", "url": "https://citizenportal.donidcr.gov.np"},
        {"name": "Department of Passport", "desc": "e-Passport online application & appointment booking reservation.", "url": "https://nepalpassport.gov.np"},
        {"name": "Central Civil Registration System", "desc": "Online birth, death, marriage, and migration darta portal.", "url": "https://vital.donidcr.gov.np"},
        {"name": "National Voters Registration", "desc": "Voter ID card enrollment, update, and ward polling location details.", "url": "https://election.gov.np"}
    ],
    "2. Transport, Vehicles & Licensing (Yatayat Seva)": [
        {"name": "DOTM Driving License Portal", "desc": "New driving license application, category addition, and trial quota booking.", "url": "https://applydlnew.dotm.gov.np"},
        {"name": "National Transport Directory", "desc": "Verify smart card dispatch, electronic tracking, and print status.", "url": "http://dotm.gov.np"},
        {"name": "Koshi Transport Revenue", "desc": "Koshi province vehicle tax and bluebook digital clearance.", "url": "https://mopit.koshi.gov.np"},
        {"name": "Madhesh Transport Revenue", "desc": "Madhesh province vehicle tax and registration gateway.", "url": "https://mopit.madhesh.gov.np"},
        {"name": "Bagmati Transport Revenue", "desc": "Bagmati province bluebook renewal and vehicle tax calculations.", "url": "https://tmis.bagamati.gov.np"},
        {"name": "Gandaki Transport Revenue", "desc": "Gandaki province online road tax payment infrastructure.", "url": "https://mopit.gandaki.gov.np"},
        {"name": "Lumbini Transport Revenue", "desc": "Lumbini province vehicle profile, fine payment, and renewal.", "url": "https://tmis.lumbini.gov.np"},
        {"name": "Karnali Transport Revenue", "desc": "Karnali state transport administration data portal.", "url": "https://mopit.karnali.gov.np"},
        {"name": "Sudurpashchim Transport Revenue", "desc": "Sudurpashchim province smart driving tax platform.", "url": "https://mopit.sudurpashchim.gov.np"}
    ],
    "3. Jobs, Exams & Career Recruitment (Sarkari Jagir)": [
        {"name": "Federal Lok Sewa Aayog", "desc": "Civil Services (Nijamati) examinations, applications, and hall tickets.", "url": "https://psconline.psc.gov.np"},
        {"name": "Teacher Service Commission", "desc": "Sarkari school permanent teacher recruitment and licensing system.", "url": "https://online.tsc.gov.np"},
        {"name": "Koshi Province PSC", "desc": "Provincial public service job circulars and vacancy submissions.", "url": "https://ppsconline.koshi.gov.np"},
        {"name": "Madhesh Province PSC", "desc": "Madhesh state service structural recruitments.", "url": "https://ppsconline.madhesh.gov.np"},
        {"name": "Bagmati Province PSC", "desc": "Bagmati state service exams, evaluation, and vacancy submissions.", "url": "https://ppsconline.bagamati.gov.np"},
        {"name": "Gandaki Province PSC", "desc": "Gandaki state civil administrative notifications.", "url": "https://ppsconline.gandaki.gov.np"},
        {"name": "Lumbini Province PSC", "desc": "Lumbini provincial employment and exam registry.", "url": "https://ppsconline.lumbini.gov.np"},
        {"name": "Karnali Province PSC", "desc": "Karnali state public service dashboard.", "url": "https://ppsconline.karnali.gov.np"},
        {"name": "Sudurpashchim Province PSC", "desc": "Sudurpashchim state recruitment application systems.", "url": "https://ppsconline.sudurpashchim.gov.np"},
        {"name": "Nepal Police Career Portal", "desc": "Online dashboard for Inspector, ASI, and Jawan recruitment intake.", "url": "https://career.nepalpolice.gov.np"}
    ],
    "4. Revenue, Business Registration & Finance (Kar aur Vyapar)": [
        {"name": "IRD Integrated Portal", "desc": "PAN registration, VAT returns, and Income Tax filing (D-1, D-2, D-3).", "url": "https://ird.gov.np"},
        {"name": "Office of Company Registrar", "desc": "Private/Public Ltd company incorporation, share lagani, and filings.", "url": "https://ocr.gov.np"},
        {"name": "Department of Commerce", "desc": "Commercial trading firm and partnership business licensing matrix.", "url": "https://doc.gov.np"},
        {"name": "Cottage & Small Industries", "desc": "Gharelu tatha sana udyog registration, verification, and subsidies.", "url": "https://dcsi.gov.np"},
        {"name": "Nepal Customs Department", "desc": "Asycuda world customs declaration, tariff search, and EXIM registration.", "url": "https://customs.gov.np"},
        {"name": "Online Malpot (VIMS)", "desc": "Land transaction history, property registry verification, and land tax.", "url": "https://vims.dolrm.gov.np"},
        {"name": "NEPSE Investor Portal", "desc": "Nepal Stock Exchange NOTS system and investor account configurations.", "url": "https://nepalstock.com.np"}
    ],
    "5. Foreign Employment & Immigration (Bidesh Yatra aur Shram)": [
        {"name": "FEIMS Labor Portal", "desc": "Centralized Shram Swikriti (Labor Permit) processing and re-entry allocation.", "url": "https://feims.dofe.gov.np"},
        {"name": "NepaliPort Immigration", "desc": "On-arrival tourist visa data forms, visa extensions, and route permits.", "url": "https://nepaliport.immigration.gov.np"},
        {"name": "EPS Korea Section", "desc": "EPS-TOPIK Korean employment system, exam schedules, and rosters.", "url": "https://eps.nepal.gov.np"},
        {"name": "Consular Services Portal", "desc": "Grievance entry for citizens abroad, verification, and legal attestation.", "url": "https://online.nepalconsular.gov.np"}
    ],
    "6. Public Procurement & Engineering Tenders (Sarkari Tender)": [
        {"name": "e-GP Centralized Portal", "desc": "National e-Procurement system. Upload bidding files, BOQ data, and security.", "url": "https://bolpatra.gov.np/egp"},
        {"name": "PPMO Procurement Portal", "desc": "Sarkari procurement guidelines, framework circulars, and contractor blacklist.", "url": "https://ppmo.gov.np"},
        {"name": "Department of Roads Tenders", "desc": "Dedicated tracking matrix for nationwide highway and bridge project tenders.", "url": "https://dor.gov.np"},
        {"name": "NEA Procurement Systems", "desc": "Nepal Electricity Authority hydropower, line upgrades, and global bids.", "url": "https://nea.org.np"}
    ],
    "7. Citizen Funds, Insurance & Social Security (Bachat aur Kosh)": [
        {"name": "Social Security Fund (SSF)", "desc": "Formal/Informal worker registration, ledger payments, and claim forms.", "url": "https://ssf.gov.np"},
        {"name": "Employees Provident Fund (EPF)", "desc": "Sanchaya Kosh digital KYC, special corporate loan processing, and payouts.", "url": "https://epfnepal.org.np"},
        {"name": "Citizen Investment Trust (CIT)", "desc": "Nagarik Lagani Kosh contribution management and scheme registration.", "url": "https://nlk.org.np"},
        {"name": "Rastriya Beema Sansthan", "desc": "Sarkari standard life insurance schema processing and claims.", "url": "https://rbs.com.np"},
        {"name": "Pension Management Office", "desc": "Retired civil service database, updates, and digital pension tracking.", "url": "https://pension.gov.np"}
    ],
    "8. Local Governance & Main Metropolitan Cities": [
        {"name": "Kathmandu Metro Portal", "desc": "KMC building layout registration, maps, local tax clearance protocols.", "url": "https://kathmandu.gov.np"},
        {"name": "Lalitpur Metro Portal", "desc": "LMC infrastructure updates, business verification, and localized complaints.", "url": "https://lalitpurmun.gov.np"},
        {"name": "Pokhara Metro Portal", "desc": "Tourism logistics clearance, enterprise filings, and localized service tracking.", "url": "https://pokharamun.gov.np"},
        {"name": "Bharatpur Metro Portal", "desc": "Bharatpur local municipal taxes, permits, and dynamic ward charts.", "url": "https://bharatpurmun.gov.np"},
        {"name": "Biratnagar Metro Portal", "desc": "Eastern region central commercial local filings and digital certificates.", "url": "https://biratnagarmun.gov.np"},
        {"name": "Birgunj Metro Portal", "desc": "Industrial hub land registrations, environmental clearances, and permits.", "url": "https://birgunjmun.gov.np"},
        {"name": "MoFAGA Integrated Directory", "desc": "Direct routing directory for all remaining 747 local municipalities.", "url": "https://mofaga.gov.np"}
    ],
    "9. Education, Infrastructure Utilities & Health": [
        {"name": "MOEST Scholarship Portal", "desc": "National database for Engineering, Medical, and Overseas education scholarship applications.", "url": "https://scholarship.moest.gov.np"},
        {"name": "NEB Online Portal", "desc": "Class 11/12 registration matrices, transcript processing, and retotaling.", "url": "https://neb.gov.np"},
        {"name": "Tribhuvan University Exam Board", "desc": "TU central exam form submission, evaluation status, and convocation tracking.", "url": "https://tuexam.edu.np"},
        {"name": "NEA Customer Counter", "desc": "Apply for a new electricity meter connection and verify bill ledgers online.", "url": "https://nea.org.np"},
        {"name": "KUKL Water Portal", "desc": "Kathmandu valley tap installation applications and digital bill clearance.", "url": "https://kathmanduwater.org"},
        {"name": "Department of Health Services", "desc": "Medical setup permissions, professional registry tracking, and compliance data.", "url": "https://dohs.gov.np"}
    ]
}

# 5. Live Fuzzy Search Box
search_query = st.text_input("🔍 Search exactly what you need (e.g., 'Tender', 'License', 'PAN', 'Kathmandu', 'PSC')...", "").strip().lower()

found_any = False

# 6. Render Engine Using Crash-Free Components
for category, services in services_data.items():
    # Filter matrix by search token
    filtered_services = [s for s in services if search_query in s['name'].lower() or search_query in s['desc'].lower()]
    
    if filtered_services:
        found_any = True
        
        # UI Blocks grouped dynamically inside high-contrast native headers
        st.header(category)
        
        # Grid Structure: 3 Solid responsive columns
        cols = st.columns(3)
        for index, service in enumerate(filtered_services):
            col_to_use = cols[index % 3]
            with col_to_use:
                # Border component acts as a solid card shell
                with st.container(border=True):
                    st.subheader(service['name'])
                    st.caption(service['desc'])
                    # Action button mapped strictly to destination architecture
                    st.link_button("Go to Form / Portal ↗", service['url'], use_container_width=True)
        st.write("") # Margin element

# Null State Matrix
if not found_any:
    st.error("❌ No official government portal matched your specific filter keyword. Try searching 'Tender', 'PSC', or 'License'.")
 
