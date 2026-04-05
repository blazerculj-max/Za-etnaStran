import streamlit as st
import time
from streamlit_extras.add_vertical_space import add_vertical_space

# Konfiguracija za pro izgled
st.set_page_config(page_title="Sales AI Coach", page_icon="🚀", layout="centered")

# Custom CSS za Apple-like gumbe in kartice
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #007AFF;
        color: white;
        font-weight: bold;
        border: none;
    }
    .status-card {
        padding: 20px;
        border-radius: 15px;
        background-color: #f0f2f6;
        border-left: 5px solid #007AFF;
    }
    </style>
    """, unsafe_allow_html=True)

# Naslovna stran
st.title("🧠 Sales AI Mentor")
st.caption("Verzija 1.0 | Optimizirano za prodajne ekipe")

add_vertical_space(2)

# Vnosni del
with st.container():
    st.markdown("### 🎯 Premagaj ugovor")
    objection = st.text_input("Kaj je rekla stranka?", placeholder="Npr. Vaša ponudba je predraga...")
    
    col1, col2 = st.columns(2)
    with col1:
        persona = st.selectbox("Tip sogovornika", ["Direktor (Analitik)", "Nabavnik (Skeptik)", "Uporabnik (Navdušenec)"])
    with col2:
        urgency = st.select_slider("Stopnja nujnosti", options=["Nizka", "Srednja", "Visoka"])

if st.button("GENERIRAJ STRATEGIJO ⚡"):
    if not objection:
        st.error("Najprej vpiši ugovor!")
    else:
        with st.spinner("AI analizira psihologijo prodaje..."):
            time.sleep(1.5) # Simulacija procesiranja
            
            # Rezultat v lepi obliki
            st.markdown("---")
            st.subheader("💡 Zmagovalna strategija")
            
            st.markdown(f"""
            <div class="status-card">
                <strong>Odgovor:</strong> "Razumem vašo skrb glede investicije. Če pogledava donos v 6 mesecih, boste opazili, da se sistem povrne že v prvem kvartalu..."
                <br><br>
                <strong>Zakaj to deluje?</strong> Pri tipu <em>{persona}</em> je ključna logika, ne emocija.
            </div>
            """, unsafe_allow_html=True)
            
            add_vertical_space(1)
            
            with st.expander("📝 Nasvet za coacha"):
                st.write("Sodelavca opomni na 'Power Posing' pred klicem in uporabo nižjega, avtoritativnega tona.")
            
            st.balloons()

add_vertical_space(3)
st.info("Nasvet: To orodje uporabi 5 minut pred klicem za najboljše rezultate.")
