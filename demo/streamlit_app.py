import streamlit as st
import pandas as pd
import ollama

from app.etl import clean_sales, aggregate_monthly
from app.signals import detect_revenue_drop
from app.decision_engine import generate_decisions
from app.ai_layer import generate_ai_explanation

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(page_title="AI Decision Dashboard", layout="wide")

# ======================
# CUSTOM CSS
# ======================
st.markdown("""
<style>
.main {background-color: #0f172a;}
h1, h2, h3 {color: #e2e8f0;}
.stMetric {background-color: #1e293b; padding: 15px; border-radius: 12px;}
.ai-box {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #22c55e;
}
</style>
""", unsafe_allow_html=True)

# ======================
# TITLE
# ======================
st.title("🚀 AI Decision Intelligence Dashboard")

# ======================
# SIDEBAR
# ======================
st.sidebar.title("⚙️ Controls")

threshold = st.sidebar.slider(
    "Revenue Drop Threshold",
    min_value=0.05,
    max_value=0.3,
    value=0.1
)

# ======================
# FILE UPLOAD
# ======================
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file, parse_dates=["date"])
    df_clean = clean_sales(df)
    monthly = aggregate_monthly(df_clean)

    # ======================
    # TABS
    # ======================
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Dashboard",
        "⚠️ Signals",
        "💡 Decisions",
        "💬 AI Chat",
        "🧪 Simulator"
    ])

    # ======================
    # TAB 1: DASHBOARD
    # ======================
    with tab1:

        st.subheader("📈 Key Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Revenue", f"{monthly['revenue'].sum():,.0f}")
        col2.metric("Total Profit", f"{monthly['profit'].sum():,.0f}")
        col3.metric("Regions", monthly["region"].nunique())

        st.divider()

        st.subheader("📈 Revenue Trend")

        pivot_df = monthly.pivot(index="month", columns="region", values="revenue")
        st.line_chart(pivot_df)

        st.divider()

        region_filter = st.selectbox("Select Region", monthly["region"].unique())
        filtered_df = monthly[monthly["region"] == region_filter]

        st.subheader(f"📊 {region_filter} Performance")
        st.line_chart(filtered_df.set_index("month")["revenue"])

    # ======================
    # TAB 2: SIGNALS
    # ======================
    with tab2:

        st.subheader("⚠️ Detected Signals")

        with st.spinner("Analyzing data..."):
            signals = detect_revenue_drop(monthly, threshold)

        st.json(signals)

    # ======================
    # TAB 3: DECISIONS
    # ======================
    with tab3:

        signals = detect_revenue_drop(monthly, threshold)
        decisions = generate_decisions(signals)

        st.subheader("💡 Recommended Actions")

        if not decisions:
            st.success("No major issues detected.")
        else:
            for i, d in enumerate(decisions[:3]):

                st.markdown(f"""
                <div style="background-color:#1e293b;padding:15px;border-radius:12px;margin-bottom:10px">
                <h4>🔹 Decision {i+1}</h4>
                <p><b>Action:</b> {d['action']}</p>
                <p><b>Reason:</b> {d['reason']}</p>
                <p><b>Impact:</b> {d['impact']}</p>
                <p><b>Confidence:</b> {d['confidence']}</p>
                </div>
                """, unsafe_allow_html=True)

                if st.button(f"Accept Decision {i+1}"):
                    st.success("Decision accepted")

                with st.spinner("Generating AI insight..."):
                    ai_text = generate_ai_explanation(d)

                st.markdown(f"""
                <div class="ai-box">
                <b>🤖 AI Insight:</b><br>{ai_text}
                </div>
                """, unsafe_allow_html=True)

                st.divider()

    # ======================
    # TAB 4: AI CHAT
    # ======================
    with tab4:

        st.subheader("💬 Ask AI About Your Business")

        user_question = st.text_input("Ask a question:")

        if user_question:
            context = monthly.to_string()

            prompt = f"""
            You are a business analyst.

            Data:
            {context}

            Question:
            {user_question}
            """

            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )

            st.write(response["message"]["content"])

    # ======================
    # TAB 5: SIMULATOR
    # ======================
    with tab5:

        st.subheader("🧪 Decision Simulator")

        price_change = st.slider("Change Price (%)", -20, 20, 0)

        simulated_revenue = monthly["revenue"].sum() * (1 + price_change / 100)

        st.write(f"Projected Revenue: {simulated_revenue:,.0f}")

        if st.button("Analyze Scenario"):

            prompt = f"""
            If price changes by {price_change}%,
            what business impact can we expect?
            """

            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )

            st.write(response["message"]["content"])
