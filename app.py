import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Centro de Control Inteligente - BCP",
    layout="wide"
)

# Cargar CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Logo
logo = Image.open("logo.png")
st.image(logo, width=150)

# Título
st.markdown("<h1 class='main-title'>Centro de Control Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Sistema Predictivo AIOps - Infraestructura BCP</h3>", unsafe_allow_html=True)

# -----------------------------
# Simulación de datos
# -----------------------------

time = pd.date_range(start="00:00", periods=24, freq="H")
traffic = np.random.randint(200, 800, size=24)
risk = np.random.randint(10, 90)

# -----------------------------
# Layout
# -----------------------------

col1, col2, col3 = st.columns(3)

# Métricas
with col1:
    st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
    st.metric("Usuarios Activos", "1,245,892", "+4%")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
    st.metric("Servidores Activos", "32", "+2")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
    st.metric("Nivel de Riesgo", f"{risk}%", "")
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Gráfico de tráfico
# -----------------------------

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=time,
    y=traffic,
    mode='lines+markers',
    name='Tráfico',
    line=dict(color='#005DAA', width=3)
))

fig.update_layout(
    title="Monitoreo de Carga Transaccional (Tiempo Real)",
    xaxis_title="Hora",
    yaxis_title="Transacciones",
    plot_bgcolor="white",
    paper_bgcolor="white"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Indicador de Estado
# -----------------------------

if risk < 40:
    st.success("🟢 Sistema Estable - Operando con normalidad")
elif risk < 70:
    st.warning("🟡 Riesgo Moderado - Escalabilidad preventiva activada")
else:
    st.error("🔴 Riesgo Alto - Autoescalado y protocolos activados")

# -----------------------------
# Chatbot simulado
# -----------------------------

st.markdown("### Asistente Inteligente")
st.info("Hola 👋 El sistema está monitoreando la infraestructura en tiempo real. Actualmente no se detectan amenazas críticas.")
