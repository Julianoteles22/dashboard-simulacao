import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import binom
from scipy.stats import norm
import pandas as pd
from PIL import Image
import subprocess
import warnings
warnings.filterwarnings("ignore")

# Criação de abas para diferentes distribuições
tab1, tab2, tab3, tab4 = st.tabs(["Distribuição Binomial", "Distribuição Poisson", "Distribuição Normal", "Simulação de ROI em um Call Center"])

# Aba da Distribuição Binomial
with tab1:
    st.header("Distribuição Binomial")
    st.markdown("### Simulação de Overbooking")

    # Títulos dos sliders em azul
    st.markdown("<h4 style='color: #003366;'>Probabilidade de Comparecimento (p)</h4>", unsafe_allow_html=True)
    p = st.slider("", min_value=0.8, max_value=1.00, value=0.88, step=0.01)  
    st.markdown("<h4 style='color: #003366;'>Número de Assentos Vendidos</h4>", unsafe_allow_html=True)
    seats_sold = st.slider("", min_value=451, max_value=500, value=461, step=1)

    st.markdown("<h4 style='color: #003366;'>Nível de Risco Aceito (%)</h4>", unsafe_allow_html=True)
    risk_level = st.slider("", min_value=0.01, max_value=0.50, value=0.05, step=0.01) 
    
    # Calcular probabilidade
    probability = 1 - binom.cdf(450, seats_sold, p)

    # Gráfico dinâmico usando Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=np.arange(451, seats_sold + 1), 
                             y=1 - binom.cdf(450, np.arange(451, seats_sold + 1), p),
                             mode='lines', line=dict(color='#003366', width=3)))

    fig.add_hline(y=risk_level, line_dash="dash", line_color="red", line_width=1)  # Dinamicamente ajustado

    fig.update_layout(title="Risco de Overbooking para mais de 450 passageiros",
                      xaxis_title="Assentos Vendidos",
                      yaxis_title="Probabilidade de mais de 450 passageiros aparecerem",
                      xaxis=dict(tickmode='linear', tick0=451, dtick=1),
                      yaxis=dict(range=[0, 1]),
                      plot_bgcolor="white",
                      width=800,
                      height=400)

    st.plotly_chart(fig, use_container_width=True)