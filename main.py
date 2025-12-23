import streamlit as st
import plotly.express as px
from src.simulation import generate_experiment_data
from src.engine import get_cuped_adjusted_metric, calculate_statistics
from src.power import calculate_required_sample_size

st.set_page_config(page_title="Experimentation Lab", layout="wide")

st.title("🚀 Analytics: Experimentation Lab")

tab1, tab2 = st.tabs(["Pre-Experiment Planning", "Live Analysis & CUPED"])

# --- TAB 1: PLANNING ---
with tab1:
    st.header("Step 1: Power Analysis (Sample Size Planning)")
    st.markdown("Determine how many users you need before launching the campaign.")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        base_vol = st.number_input("Average Monthly Trading Volume ($)", value=1000)
        std_vol = st.number_input("Standard Deviation of Volume", value=500)
    with col_p2:
        mde = st.slider("Minimum Detectable Effect (MDE %)", 1.0, 10.0, 2.0) / 100
        desired_power = st.slider("Statistical Power", 0.7, 0.95, 0.8)

    req_n = calculate_required_sample_size(base_vol, std_vol, mde, power=desired_power)
    
    st.success(f"### Required Sample Size: **{req_n:,} users per group**")
    st.info(f"To detect a {mde*100}% change with {desired_power*100}% confidence, you need a total of {req_n*2:,} users.")

# --- TAB 2: ANALYSIS ---
with tab2:
    st.header("Step 2: Live Analysis & Variance Reduction")
    
    st.sidebar.header("Live Simulation Settings")
    n_users = st.sidebar.number_input("Actual Sample Size (Users)", value=req_n if req_n < 10000 else 5000)
    lift_pct = st.sidebar.slider("Observed Lift (%)", 0.0, 10.0, 3.0)
    
    # Run simulation and stats
    data = generate_experiment_data(n_users, lift_pct/100)
    data_adj, theta = get_cuped_adjusted_metric(data, 'post_period', 'pre_period')
    
    p_raw, _ = calculate_statistics(data_adj, 'post_period')
    p_cuped, var_cuped = calculate_statistics(data_adj, 'cuped_metric')
    
    # Show Results
    c1, c2 = st.columns(2)
    c1.metric("Standard T-Test P-Value", f"{p_raw:.4f}")
    c2.metric("CUPED Adjusted P-Value", f"{p_cuped:.4f}", delta="More Sensitive!")
    
    st.plotly_chart(px.histogram(data_adj, x=["post_period", "cuped_metric"], barmode="overlay", title="Variance Comparison"))