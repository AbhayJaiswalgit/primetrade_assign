import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("📊 Trader Behavior vs Market Sentiment Dashboard")

# Load data
merged = pd.read_csv("dashboard_merged.csv")
accounts = pd.read_csv("dashboard_accounts.csv")

# Sidebar filters
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=merged['sentiment'].unique(),
    default=list(merged['sentiment'].unique())
)

cluster_filter = st.sidebar.multiselect(
    "Select Trader Cluster",
    options=accounts['cluster'].unique(),
    default=list(accounts['cluster'].unique())
)

filtered = merged[merged['sentiment'].isin(sentiment_filter)]

# KPIs
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Daily PnL", round(filtered['daily_pnl'].mean(), 2))
col2.metric("Avg Trades", round(filtered['trades'].mean(), 2))
col3.metric("Avg Win Rate", round(filtered['win_rate'].mean(), 2))

st.divider()

# Plot 1 — PnL Distribution
st.subheader("Daily PnL Distribution by Sentiment")
fig1, ax1 = plt.subplots()
sns.boxplot(data=filtered, x='sentiment', y='daily_pnl', ax=ax1)
st.pyplot(fig1)

# Plot 2 — Trade Size vs Win Rate
st.subheader("Trade Size vs Win Rate")
fig2, ax2 = plt.subplots()
sns.scatterplot(
    data=accounts[accounts['cluster'].isin(cluster_filter)],
    x='avg_trade_size',
    y='overall_win_rate',
    hue='cluster',
    ax=ax2
)
st.pyplot(fig2)

# Plot 3 — Trades vs PnL
st.subheader("Trades vs Daily PnL")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=filtered, x='trades', y='daily_pnl', hue='sentiment', ax=ax3)
st.pyplot(fig3)

st.divider()

st.subheader("Cluster Summary")
st.dataframe(
    accounts.groupby('cluster')[
        ['total_trades','avg_trade_size','overall_win_rate','total_pnl']
    ].mean()
)
