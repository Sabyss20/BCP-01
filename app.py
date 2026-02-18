import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PIL import Image
import random

st.set_page_config(page_title="BCP AIOps", layout="wide")

# Cargar CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.image("logo.png", width=120)
st.sidebar.title("Centro AIOps")
st.sidebar.markdown("Infraestructura Digital BCP")

st.sidebar.markdown("### Estado General")
estado_global = random.choice(["Estable", "Monitoreo Preventivo", "Riesgo Alto"])

if estado_global == "Estable":
    st.sidebar.success("🟢 Sistema Estable")
elif estado_global == "Monitoreo Preventivo":
    st.sidebar.warning("🟡 Prevención Activa")
else:
    st.sidebar.error("🔴 Riesgo Alto")

# HEADER
col_logo, col_title = st.columns([1,5])
with col_logo:
    st.image("logo.png", width=100)

with col_title:
    st.markdown("<div class='main-title'>Centro de Control Inteligente</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Sistema Predictivo AIOps - Infraestructura Digital</div>", unsafe_allow_html=True)

st.divider()

# ==========================
# PASO 1 - MONITOREO
# ==========================
st.subheader("🔹 Monitoreo en Tiempo Real")

col1, col2, col3, col4 = st.columns(4)

usuarios = random.randint(900000, 1500000)
memoria = random.randint(40, 95)
latencia = random.randint(90, 350)
trafico = random.choice(["Normal", "Anómalo"])

with col1:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Usuarios Activos", f"{usuarios:,}")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Uso de Memoria (%)", f"{memoria}%")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Latencia (ms)", f"{latencia}")
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Tráfico", trafico)
    st.markdown("</div>", unsafe_allow_html=True)

# Gráfico más limpio
horas = pd.date_range(start="00:00", periods=24, freq="H")
carga = np.random.randint(200, 1000, size=24)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=horas,
    y=carga,
    mode='lines',
    line=dict(color='#005DAA', width=3)
))

fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=20,r=20,t=40,b=20)
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# PASO 2 - PREDICCIÓN
# ==========================
st.subheader("🔹 Predicción IA")

riesgo = memoria + (latencia / 5)

if riesgo < 100:
    clase = "status-green"
    mensaje = "Sistema estable. Sin riesgo de saturación."
elif riesgo < 130:
    clase = "status-yellow"
    mensaje = "Riesgo moderado. Escalabilidad preventiva activada."
else:
    clase = "status-red"
    mensaje = "🚨 Saturación estimada en 20 minutos."

st.markdown(f"<div class='status-banner {clase}'>Nivel de Riesgo Calculado: {int(riesgo)}% - {mensaje}</div>", unsafe_allow_html=True)

st.divider()

# ==========================
# PASO 3 - ACCIÓN AUTOMÁTICA
# ==========================
st.subheader("🔹 Acción Automática")

if riesgo >= 130:
    st.write("✔ Autoescalado activado (+5 servidores cloud)")
    st.write("✔ Balanceador redistribuyendo carga")
    st.write("✔ Firewall bloqueando tráfico sospechoso")
else:
    st.write("Infraestructura operando dentro de parámetros normales.")

st.divider()

# ==========================
# PASO 4 - COMUNICACIÓN
# ==========================
st.subheader("🔹 Comunicación Inteligente")

if riesgo >= 130:
    st.markdown("<div class='metric-card'>Estamos experimentando alta demanda. Tiempo estimado: 8 minutos.</div>", unsafe_allow_html=True)
    respuesta = "Entendemos tu preocupación. Estamos reforzando la infraestructura."
else:
    st.markdown("<div class='metric-card'>Sistema estable. Operaciones normales.</div>", unsafe_allow_html=True)
    respuesta = "Hola 👋 Todo funciona con normalidad."
