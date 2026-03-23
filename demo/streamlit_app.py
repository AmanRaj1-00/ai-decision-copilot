import streamlit as st
import pandas as pd

from app.etl import load_sales, clean_sales, aggregate_monthly
from app.signals import detect_revenue_drop
from app.decision_engine import generate_decisions
from app.ai_layer import generate_ai_explanation

st.set_page_config(page_title="AI Decision Dashboard", layout="wide")

st.title("🚀 AI Decision Intelligence Dashboard")

st.write("Upload your sales data to generate AI-driven business decisions.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:

    # Load data
    df = pd.read_csv(uploaded_file, parse_dates=["date"])
    df_clean = clean_sales(df)
    monthly = aggregate_monthly(df_clean)

    # =======================
    # 📈 KEY METRICS
    # =======================
    st.subheader("📈 Key Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", f"{monthly['revenue'].sum():,.0f}")
    col2.metric("Total Profit", f"{monthly['profit'].sum():,.0f}")
    col3.metric("Regions", monthly['region'].nunique())

    # =======================
    # 📊 DATA VIEW
    # =======================
    st.divider()
    st.subheader("📊 Monthly Revenue Data")
    st.dataframe(monthly.head())

    # =======================
    # ⚠️ SIGNALS
    # =======================
    signals = detect_revenue_drop(monthly)

    st.divider()
    st.subheader("⚠️ Detected Signals")
    st.json(signals)

    # =======================
    # 💡 DECISIONS + AI
    # =======================
    decisions = generate_decisions(signals)

    st.divider()
    st.subheader("💡 Recommended Actions")

    if not decisions:
        st.info("No major issues detected. System is stable.")
    else:
        for i, d in enumerate(decisions[:3]):

            st.markdown(f"### 🔹 Decision {i+1}")

            st.write(f"**Action:** {d['action']}")
            st.write(f"**Reason:** {d['reason']}")
            st.write(f"**Impact:** {d['impact']}")
            st.write(f"**Confidence:** {d['confidence']}")

            with st.spinner("Generating AI insight..."):
                ai_text = generate_ai_explanation(d)

            st.markdown("**🤖 AI Insight:**")
            st.write(ai_text)

            st.divider()
