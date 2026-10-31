# Business case and interview explanation

## Problem
A simulated network of eight quick-commerce dark stores experiences variable demand and imperfect replenishment. Leaders need visibility into lost sales, availability, and which product categories and locations deserve attention.

## Scope and source
All data is **synthetic** and generated with a deterministic Python script. It is a portfolio simulation, not an analysis of real retailer data. The simulation covers 180 days, 8 stores and 36 products.

## Analytical workflow
1. Define KPIs: demand, units sold, fulfillment, stockout observation rate, realized revenue and estimated lost revenue.
2. Generate store, product and daily inventory tables with Python.
3. Validate inventory conservation: opening + received - sold = closing; demand - sold = lost.
4. Join fact data with product/store dimensions using SQL or Power BI relationships.
5. Analyze category, city and monthly patterns.
6. Present findings in the browser dashboard; reproduce in Power BI using included DAX.
7. Recommend targeted replenishment and monitor whether stockout and lost revenue measures improve.

## Interpretation cautions
- Stockout observation rate = fraction of store-product-day records with unmet demand; **not** fraction of products out of stock at a single moment.
- Estimated lost revenue = unmet units multiplied by list selling price; it is **not** realized profit or a guaranteed recoverable sale.
- Reorder candidates based on safety stock are an illustration, not a production replenishment algorithm.
- Sales simulation is stylized; no external dataset or actual company results were used.

## 60-second interview pitch
“I built an Inventory and Stockout Intelligence project to understand how replenishment gaps affect sales in a simulated eight-store retail network. I generated six months of store-product daily records in Python, validated stock balance and unmet demand, and modeled the data using product and store dimensions. I calculated fulfillment rate, stockout frequency, realized revenue and estimated lost revenue, then analyzed trends by city, category and month. I delivered a browser-based dashboard, reusable SQL queries and Power BI measures. The business value is prioritizing inventory interventions by likely revenue exposure rather than reacting to every stockout equally. Because this is synthetic data, the results demonstrate my analytical process rather than claiming real-world impact.”

## Interview questions
**Why did you choose these KPIs?** They connect availability to customer demand and business value.

**How did you check data quality?** Arithmetic constraints, chronological stock continuity and deterministic row counts in the validation script.

**What is the grain?** One row per store, product and date.

**What would you improve with real data?** Lead-time variability, promotions, supplier reliability, substitution, returns, seasonality and actual margins.

**How would you act on the analysis?** Rank store-category pairs by estimated lost revenue, investigate replenishment cadence and lead times, pilot revised reorder points, and monitor post-change metrics.

**What is the difference between stockout rate and fill rate?** Stockout observation rate measures incidence of any unmet demand per row; fill rate measures units fulfilled divided by units demanded.
