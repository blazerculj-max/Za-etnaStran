import streamlit as st
import time

# Konfiguracija
st.set_page_config(page_title="Pro Sales Architect", layout="wide")

# CSS za vizualno ločevanje blokov (Pro Look)
st.markdown("""
    <style>
    .playbook-card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }
    .step-header {
        color: #007AFF;
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.8rem;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 Sales Playbook Generator")
st.write("Pretvori ugovor v priložnost z metodologijo 4 korakov.")

# Vnosni parametri
col_in1, col_in2 = st.columns(2)
with col_in1:
    objection = st.text_area("Vpiši ugovor stranke (npr. 'Previsoka cena')", height=100)
with col_in2:
    context = st.selectbox("Faza prodaje", ["Hladni klic", "Prva predstavitev", "Pogajanja o pogodbi"])
    industry = st.text_input("Industrija stranke", "Npr. IT, Proizvodnja, Farmacija")

if st.button("IZDELAJ KONKRETEN NAČRT ⚡"):
    if not objection:
        st.warning("Najprej vpiši vsebino ugovora.")
    else:
        with st.spinner("Generiram Playbook..."):
            time.sleep(2) # Tukaj bi bil klic na LLM API
            
            st.markdown("### 📘 Tvoj načrt napada")
            
            # --- 1. KORAK: PSIHOLOGIJA ---
            with st.container():
                st.markdown(f"""
                <div class="playbook-card">
                    <div class="step-header">KORAK 1: PSIHOLOŠKA PRIPRAVA</div>
                    <p>Stranka v fazi <b>{context}</b> ne zavrača produkta, ampak išče <b>varnost</b>. 
                    Njen ugovor v industriji <b>{industry}</b> običajno pomeni strah pred neuspešno implementacijo.</p>
                </div>
                """, unsafe_allow_html=True)

            # --- 2. KORAK: SKRIPT (WORD-FOR-WORD) ---
            st.markdown("#### 💬 Skript (Word-for-word)")
            c1, c2 = st.columns(2)
            
            with c1:
                st.info("**A) Empatija & Potrditev**\n\n'Povsem vas razumem, v {industry} je danes vsaka investicija pod drobnogledom. Pravzaprav bi me skrbelo, če vas donosnost ne bi zanimala.'")
            with c2:
                st.success("**B) Preokvirjanje (The Pivot)**\n\n'Vendar, ali se pogovarjava o ceni same licence ali o skupnem strošku, ki ga imate trenutno z neučinkovitim procesom?'")

            # --- 3. KORAK: DOKAZ ---
            st.markdown(f"""
            <div class="playbook-card" style="border-left: 5px solid #34C759;">
                <div class="step-header">KORAK 3: DOKAZ (Social Proof)</div>
                <p>Uporabi to referenco: <i>"Podobno podjetje v {industry} je s prehodom na naš sistem zmanjšalo operativne stroške za 22 % v prvem letu, kar je pokrilo razliko v ceni v 4 mesecih."</i></p>
            </div>
            """, unsafe_allow_html=True)

            # --- 4. KORAK: ZAPIRANJE ---
            st.warning("**KORAK 4: Vprašanje za prevzem kontrole**\n\n'Če vam pokažem izračun, kjer se investicija povrne v manj kot pol leta, bi bili pripravljeni pogledati podrobnosti specifikacije?'")
            
            st.balloons()
