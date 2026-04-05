import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

# 1. Konfiguracija strani za "Pro" izgled
st.set_page_config(
    page_title="Ekipa Pro | Nadzorna Plošča",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed" # Skrijemo stransko vrstico za čistejši videz
)

# 2. Funkcija za nalaganje Lottie animacij z interneta
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Povezave do modernih animacij (Lahko zamenjaš na lottiefiles.com)
lottie_rocket = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xlw4axdy.json")
lottie_data = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_qpwb4wda.json")
lottie_success = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_uu0v2365.json")

# 3. Napreden CSS za vizualni presežek
st.markdown("""
    <style>
    /* Globalne spremembe */
    .main {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }
    
    /* Stil za kartice (Glassmorphism efekt) */
    div[data-testid="stMetricValue"] {
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 15px;
        padding: 15px;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Animacija za gumbe */
    .stButton>button {
        background: linear-gradient(45deg, #2193b0, #6dd5ed);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(33, 147, 176, 0.3);
    }
    
    /* Skrijemo standardni Streamlit header */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. Glavna vsebina (Naslov in glavna animacija)
st.markdown("<br>", unsafe_allow_html=True) # Malo prostora na vrhu

with st.container():
    col_title, col_anim = st.columns([2, 1])
    
    with col_title:
        st.markdown("""
            <h1 style='font-size: 3rem; font-weight: 800; color: #1a1a1a; margin-bottom: 0;'>
                Dobrodošli v <span style='color: #2193b0;'>Pro Hub</span>
            </h1>
            <p style='font-size: 1.2rem; color: #555; margin-top: 10px;'>
                Vaše osrednje vozlišče za hitro delo, analitiko in sodelovanje.
            </p>
            """, unsafe_allow_html=True)
        
        # Interaktivni gumb z Micro-interakcijo
        if st.button("Začni Delo 🚀"):
            st.balloons() # Takojšnja vgrajena animacija
            st.success("Uspešno zagnano! Poglejte zavihke spodaj.")
            
    with col_anim:
        # Prikažemo raketo (hitrost: 1.5x)
        st_lottie(lottie_rocket, height=250, key="rocket")

st.markdown("<hr style='border: 0; border-top: 1px solid #ddd; margin: 40px 0;' >", unsafe_allow_html=True)

# 5. Spodnji del z metrikami in animacijami
st.markdown("### 📊 Pregled Ključnih Kazalnikov")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st_lottie(lottie_data, height=100, key="data_anim")
    st.metric(label="Aktivni Projekti", value="14", delta="2 ta teden")

with col2:
    st_lottie(lottie_success, height=100, key="success_anim")
    st.metric(label="Dokončane Naloge", value="89%", delta="5%")

with col3:
    # Uporabimo ikono namesto animacije za raznolikost
    st.markdown("<h1 style='text-align: center;'>⏱️</h1>", unsafe_allow_html=True)
    st.metric(label="Povprečni čas odziva", value="1.2 h", delta="-0.3 h", delta_color="normal")

with col4:
    # Simulacija nalaganja
    st.markdown("<h1 style='text-align: center;'>🔄</h1>", unsafe_allow_html=True)
    st.metric(label="Osvežitev Podatkov", value="V živo")

# 6. Simulacija "Super hitrosti" pri preklopu zavihkov
st.markdown("<br><br>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["🚀 Hitra Navigacija", "🛠️ Orodja", "👥 Ekipa"])

with tab1:
    st.markdown("""
        ### Najpogosteje uporabljeno:
        - 📄 Poročilo o prodaji (Excel)
        - 🔗 Link do Jira table
        - 📧 Predloga za teden korespondenco
    """)
    if st.button("Odpri vse ⚡"):
        with st.spinner("Odpiram..."):
            time.sleep(0.5) # Simuliramo hitrost
            st.success("Vse odprto v novih zavihkih!")

with tab2:
    st.write("Tukaj bodo tvoja interna orodja.")

with tab3:
    st.write("Seznam sodelavcev in prisotnost.")
