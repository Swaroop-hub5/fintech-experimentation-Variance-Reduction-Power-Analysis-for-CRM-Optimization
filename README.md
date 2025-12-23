# 📌 Project Overview
In high-frequency environments like Exness, trading volumes are naturally volatile. Traditional A/B testing often fails because "Market Noise" masks the actual impact of CRM interventions (e.g., deposit bonuses, reactivation journeys).

This project is a modular Python-based experimentation suite designed to:

Plan: Conduct Power Analysis to ensure experiments are statistically sound before launch.

Analyze: Implement CUPED (Controlled-experiment using Pre-Experiment Data) to "denoise" results, reducing variance and shortening the time-to-significance.🛠️ Tech Stack
Language: Python 3.10+

## UI Framework: Streamlit (for interactive stakeholder reporting)
## Stats Engine: scipy.stats, statsmodels (Power Analysis, Welch's T-Test)
## Data Ops: pandas, numpy
## Visualization: plotly (Dynamic variance comparison)

# 📖 User & Interpretation Guide
Tab 1: Pre-Experiment Planning (Strategic Alignment)
What it does: Calculates the required sample size based on your business goals.

Why it matters for Exness: Prevents "underpowered" tests. If the CRM team has a budget for 50k users but the tool says you need 100k to see a 1% lift, you saved the company from a failed, inconclusive experiment.

Key Metric: MDE (Minimum Detectable Effect). Setting this to 1-2% mimics the thin margins of fintech growth where small improvements lead to massive revenue.

Tab 2: Live Analysis & CUPED (The "Signal Finder")
The Problem: Traditional T-tests often show high P-values (e.g., 0.90) because one "Whale" trader can skew the entire dataset.

The CUPED Solution: This module uses a trader's historical baseline to adjust their current performance. It effectively asks: "Is this trader doing better than THEIR OWN average?" rather than just comparing them to a generic group mean.

Visual Interpretation:

Histogram Spread: Look at the Dark Blue (CUPED) bars. They are tighter and more centered than the Raw data. This "shrinking" of the distribution is what allows us to reach statistical significance 30-50% faster.

P-Value Delta: If the Standard P-Value is 0.20 (Insignificant) but the CUPED P-Value is 0.04 (Significant), you have successfully identified a winning product feature that a standard analyst would have missed.

📈 Impact on Product Decision-Making
By implementing this framework, a Product Analyst can:

Reduce Experiment Duration: Reach conclusions faster, allowing for more experiments per quarter.

Increase ROI: Detect small but profitable "Lifts" in CRM journeys that are usually hidden by market volatility.

Data Integrity: Ensure that "Outlier" traders don't lead to false-positive or false-negative business decisions.