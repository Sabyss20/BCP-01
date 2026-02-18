import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PIL import Image
import random

st.set_page_config(page_title="Centro de Control Inteligente - BCP", layout="wide")

# Cargar CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Logo
logo = Image.open("logo.png")
st.image(logo, width=130)

st.markdown("<h1 class='main-title'>Centro de Control Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Sistema Predictivo AIOps - Infraestructura Digital</p>", unsafe_allow_html=True)

st.divider()

# -----------------------------
# PASO 1 - MONITOREO CONSTANTE
# -----------------------------
st.subheader("🔹 Monitoreo en Tiempo Real (Doctor Digital)")

col1, col2, col3, col4 = st.columns(4)

usuarios = random.randint(800000, 1500000)
memoria = random.randint(40, 95)
latencia = random.randint(80, 350)
trafico_sospechoso = random.choice(["Normal", "Anómalo"])

with col1:
    st.metric("Usuarios Activos", f"{usuarios:,}")

with col2:
    st.metric("Uso de Memoria (%)", f"{memoria}%")

with col3:
    st.metric("Latencia (ms)", f"{latencia}")

with col4:
    st.metric("Tráfico", trafico_sospechoso)

# Gráfico de tráfico
horas = pd.date_range(start="00:00", periods=24, freq="H")
carga = np.random.randint(200, 1000, size=24)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=horas,
    y=carga,
    mode='lines+markers',
    line=dict(color='#005DAA', width=3)
))

fig.update_layout(
    title="Carga Transaccional",
    plot_bgcolor="white",
    paper_bgcolor="white"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------------
# PASO 2 - PREDICCIÓN
# -----------------------------
st.subheader("🔹 Predicción Inteligente")

riesgo = random.randint(20, 90)

if riesgo < 50:
    estado = "Estable"
    clase = "status-green"
elif riesgo < 75:
    estado = "Riesgo Moderado"
    clase = "status-yellow"
else:
    estado = "Riesgo Alto - Saturación en 20 min"
    clase = "status-red"

st.markdown(f"<div class='{clase}'>Nivel de Riesgo: {riesgo}% - {estado}</div>", unsafe_allow_html=True)

st.divider()

# -----------------------------
# PASO 3 - ACCIÓN AUTOMÁTICA
# -----------------------------
st.subheader("🔹 Acción Automática del Sistema")

if riesgo >= 75:
    st.markdown("✅ Autoescalado activado: +4 servidores en nube")
    st.markdown("✅ Balanceador de carga redistribuyendo tráfico")
    st.markdown("✅ Firewall bloqueando tráfico sospechoso")
elif riesgo >= 50:
    st.markdown("⚙ Activando servidores preventivos")
else:
    st.markdown("✔ Infraestructura operando normalmente")

st.divider()

# -----------------------------
# PASO 4 - COMUNICACIÓN INTELIGENTE
# -----------------------------
st.subheader("🔹 Comunicación Inteligente")

if riesgo >= 75:
    mensaje_usuario = "Estamos experimentando alta demanda. Tiempo estimado de normalización: 8 minutos."
else:
    mensaje_usuario = "Sistema estable. No se detectan incidencias críticas."

st.markdown(f"<div class='card'>{mensaje_usuario}</div>", unsafe_allow_html=True)

# Chatbot
st.markdown("### 🤖 Chatbot IA")

if riesgo >= 75:
    respuesta = "Entendemos tu preocupación. Estamos reforzando la infraestructura para garantizar tus operaciones."
else:
    respuesta = "Hola 👋 El sistema está monitoreando todo en tiempo real y funciona con normalidad."

st.markdown(f"<div class='chatbox'>{respuesta}</div>", unsafe_allow_html=True)

st.divider()

# Blockchain
st.subheader("🔹 Registro en Blockchain")
st.markdown("📌 Incidente registrado con hash criptográfico para auditoría y trazabilidad.")
