import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    return pd.read_csv("ltv_profitability_dataset.csv")

df = load_data()

st.sidebar.title("LTV App Navigation")
view = st.sidebar.radio("Choose View", ["Search by Customer", "Channel Summary", "Segment Insights"])

st.title("🛍️ LTV Profitability Dashboard")

if view == "Search by Customer":
    customer_id = st.selectbox("Select Customer ID", df["customer_unique_id"].unique())
    cust = df[df["customer_unique_id"] == customer_id].iloc[0]
    
    st.subheader(f"Customer: {customer_id}")
    st.metric("📈 Predicted LTV", f"R$ {cust.future_ltv:.2f}")
    st.metric("💸 CAC", f"R$ {cust.cac:.2f}")
    st.metric("📊 Margin", f"R$ {cust.margin:.2f}")
    st.metric("📊 LTV/CAC", f"{cust.ltv_cac_ratio:.2f}")
    st.metric("🏷️ Segment", cust.roi_segment)

elif view == "Channel Summary":
    st.subheader("📊 Avg Metrics by Channel")
    grouped = df.groupby("channel").agg({
        "future_ltv": "mean",
        "cac": "mean",
        "margin": "mean",
        "ltv_cac_ratio": "mean"
    }).sort_values("ltv_cac_ratio", ascending=False)

    st.dataframe(grouped.style.format("{:.2f}"))

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=df, x="channel", y="ltv_cac_ratio", ci=None)
    plt.axhline(1, color='red', linestyle='--', label="Break Even")
    plt.axhline(3, color='green', linestyle='--', label="Target ROI")
    plt.legend()
    st.pyplot(fig)

elif view == "Segment Insights":
    st.subheader("📈 Customers by ROI Segment")
    seg_counts = df["roi_segment"].value_counts()
    st.bar_chart(seg_counts)

    st.write("Detailed Table:")
    st.dataframe(df.groupby("roi_segment").agg({
        "future_ltv": "mean",
        "margin": "mean",
        "ltv_cac_ratio": "mean",
        "customer_unique_id": "count"
    }).rename(columns={"customer_unique_id": "customer_count"}))
