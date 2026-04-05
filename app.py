import streamlit as st

# 1. Konfiguracija strani (Mora biti prva vrstica!)
st.set_page_config(
    page_title="OneDrive Pro Hub",
    page_icon="🚀",
    layout="wide"
)

# 2. CSS za "Apple-like" izgled (zaokroženi robovi, sence)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        border-radius: 10px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Naslovna vrstica
st.title("📂 OneDrive Produktivni Center")
st.write("Dobrodošli v osrednjem vozlišču za našo ekipo.")

# 4. Navigacija z zavihki (Hitreje in bolj tekoče)
tab1, tab2, tab3 = st.tabs(["🏠 Domov", "☁️ OneDrive Datoteke", "📊 Analitika"])

with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Pregled statusa")
        st.info("Vse storitve delujejo nemoteno. Zadnja sinhronizacija: Pred 2 minutama.")
        st.markdown("""
        ### Navodila za uporabo:
        1. Izberi zavihek **OneDrive Datoteke**.
        2. Avtoriziraj se s službenim računom.
        3. Prenesi ali uredi dokumente neposredno tukaj.
        """)
    with col2:
        st.image("https://img.icons8.com/clouds/200/000000/cloud-sync.png")

with tab2:
    st.subheader("Dostop do OneDrive datotek")
    # Tukaj pride tvoja O365 logika
    st.warning("Povezava z Microsoft Graph API... Prosim, počakajte.")
    
    # Simulacija datotek za "vau" efekt
    files = ["Projekt_A.xlsx", "Marketinski_plan_2026.pdf", "Zapisnik_sestanka.docx"]
    for f in files:
        col_f1, col_f2 = st.columns([3, 1])
        col_f1.write(f"📄 {f}")
        if col_f2.button("Odpri", key=f):
            st.success(f"Odpiram {f}...")

with tab3:
    st.subheader("Funkcionalnosti v pripravi")
    st.progress(65, text="Razvoj avtomatizacije poročil")
    st.write("Tukaj bodo vizualizirani podatki neposredno iz tvojih Excel tabel na OneDrive-u.")
