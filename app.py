import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Konfiguracija strani (ostane ista)
st.set_page_config(page_title="Pro Hub", layout="wide")

# 2. VARNA funkcija za nalaganje animacij
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# Uporabi te NOVE, preverjene povezave (direktni JSON dostopi)
lottie_rocket = load_lottieurl("https://raw.githubusercontent.com/pypa/warehouse/main/warehouse/static/dist/images/loading.json") # Primer stabilne animacije
# Alternativno lahko uporabiš lokalne JSON datoteke, če jih naložiš na GitHub

# 3. Prikaz animacije (VARNA VERZIJA)
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Dobrodošli v Pro Hub")
    with col2:
        if lottie_rocket:
            st_lottie(lottie_rocket, height=250, key="rocket")
        else:
            st.write("🚀") # Če animacija ne dela, pokaži emoji (da se app ne sesuje)
