
# 📊 Trader Behavior vs Market Sentiment — Hyperliquid Analysis

🔗 **Live Streamlit Dashboard**  
https://primetradeassign-dhbph6b9kferpvkg4t9hk7.streamlit.app/

This project analyzes how Bitcoin market sentiment (Fear/Greed) influences trader behavior and performance on Hyperliquid. The objective is to uncover actionable insights that can inform smarter trading strategies, risk management rules, and trader segmentation.

---

## 🚀 Project Highlights

- Data cleaning and alignment of sentiment and trader history  
- Behavioral and performance analysis across Fear vs Greed days  
- Trader segmentation (risk, frequency, consistency)  
- Five strong, data-backed insights  
- Practical strategy recommendations  
- Bonus implementations:
  - Predictive ML model for next-day profitability and volatility
  - Trader archetypes using clustering
  - Interactive Streamlit dashboard

---

## 🗂 Repository Structure

```
├── trader_sentiment_analysis.ipynb   # Complete analysis notebook
├── app.py                           # Streamlit dashboard
├── requirements.txt
├── runtime.txt                      # Forces Python 3.11 on Streamlit Cloud
├── dashboard_merged.csv             # Data for dashboard
├── dashboard_accounts.csv           # Cluster data
```

---

## ⚙️ Setup Instructions

Recommended Python Version: **Python 3.11**

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run This Project Locally (Step-by-Step)

### Step 1 — Create a Python 3.11 Environment (Recommended)

Using conda:

```bash
conda create -n primetrade python=3.11 -y
conda activate primetrade
```

Or using venv:

```bash
python -m venv primetrade
primetrade\\Scripts\\activate   # Windows
```

### Step 2 — Install Dependencies

From the project folder:

```bash
pip install -r requirements.txt
```

### Step 3 — Run the Analysis Notebook

Open and execute:

```
trader_sentiment_analysis.ipynb
```

This will:
- Clean and merge datasets
- Generate insights
- Train ML models
- Create `dashboard_merged.csv` and `dashboard_accounts.csv`

### Step 4 — Run the Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📈 Methodology

Datasets used:

1. Bitcoin Fear/Greed sentiment (daily)
2. Hyperliquid trader execution history

Processing steps:

- Standardized and cleaned both datasets
- Converted timestamps and aligned data at daily level
- Created trader-day metrics (PnL, win rate, trades, trade size, long/short ratio)
- Merged sentiment with trader behavior
- Performed performance, behavioral, and segmentation analysis

---

## 🔍 Key Insights

1. Performance differs between Fear and Greed days
2. Traders overtrade during Fear without better win rate
3. Stronger long bias during Fear
4. Frequent traders adapt better to sentiment shifts
5. High-risk traders are highly sentiment sensitive

---

## 🧠 Strategy Recommendations

- Reduce leverage for high-risk traders during Fear days
- Encourage frequent traders during Greed periods
- Limit overtrading for infrequent traders during Fear
- Use sentiment + behavior for dynamic risk control
- Segment traders into archetypes for personalized rules

---

## 🤖 Bonus — Predictive Modeling

Models predict next-day profitability and volatility using trader behavior + sentiment features. Important features include win rate, trade frequency, sentiment, and fear/greed score.

---

## 🧩 Bonus — Trader Archetypes (Clustering)

| Cluster | Behavior | Characteristics |
|---------|----------|-----------------|
| Cluster 0 | Retail / Casual | Lower trades, smaller size, lower win rate |
| Cluster 1 | Professional / Aggressive | Very high trades, large size, high win rate, high PnL |

---

## 📊 Interactive Dashboard

Use the dashboard to explore:
- Sentiment filters
- PnL, win rate, trade behavior
- Trader clusters

Live App: https://primetradeassign-dhbph6b9kferpvkg4t9hk7.streamlit.app/

---

## ✅ What This Project Demonstrates

- Strong data preprocessing
- Insightful analytics
- Practical strategy extraction
- ML + clustering applications
- Interactive data visualization
