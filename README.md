# 🛍️ AI-Driven LTV Profitability Dashboard

An end-to-end production-grade project that predicts customer lifetime value (LTV) and calculates marketing profitability using real-world e-commerce data.

![Streamlit Screenshot](./screenshot.png)

---

## 🚀 What This Project Does

✅ Predicts future LTV using RFM features + ML  
✅ Calculates CAC, margin, and LTV:CAC ratios  
✅ Segments customers into High / Break-even / Low ROI  
✅ Visual dashboard built in Streamlit  
✅ Ready for deployment or business decisioning

---

## 📊 Tech Stack

- `Python`, `pandas`, `matplotlib`, `seaborn`
- `scikit-learn` / `xgboost` for LTV regression
- `Streamlit` for app and UI
- Simulated CAC data per marketing channel

---

## 🖥️ Features

| Feature               | Description |
|-----------------------|-------------|
| Customer Lookup       | View LTV, CAC, margin, ROI segment |
| Channel Summary       | Aggregated marketing performance |
| Segment Insights      | ROI segment distribution & breakdown |
| Custom charts & logic | Styled dashboard with business value |

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/ltv-dashboard.git
cd ltv-dashboard
pip install -r requirements.txt
streamlit run app.py
