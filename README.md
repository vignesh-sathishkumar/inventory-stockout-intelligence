# Inventory & Stockout Intelligence Dashboard

**Project 2 | Business Analytics / Operations Portfolio**

A complete, GitHub-ready synthetic retail analytics project demonstrating demand fulfillment, inventory stockouts, revenue at risk and replenishment priorities. **All data is simulated, not real business results.**

## Quick start
1. Download and extract the ZIP.
2. Open `dashboard/index.html` in a browser. No installation, server or internet connection is needed.
3. Run `python scripts/validate_data.py` to validate the included dataset.
4. Optionally regenerate with `python scripts/generate_data.py`. Standard-library Python only.

## Project contents
- `data/stores.csv` - 8 store dimension records.
- `data/products.csv` - 36 product dimension records.
- `data/inventory_daily.csv` - 51,840 daily fact records (8 stores × 36 products × 180 days).
- `dashboard/index.html` - self-contained interactive dashboard with city/category filters and KPI charts.
- `dashboard/metrics.json` - independently readable summary metrics.
- `scripts/build_dataset.py` / `generate_data.py` - reproducible synthetic data generator.
- `scripts/validate_data.py` - integrity checks.
- `sql/analysis_queries.sql` - reusable SQLite queries.
- `powerbi/PowerBI_Measures.dax` - measures for an optional native Power BI dashboard.
- `docs/BUSINESS_CASE.md` - business interpretation and interview walkthrough.

## Data model
`inventory_daily` (fact) joins `stores` on `store_id` and `products` on `product_id`. Grain: **one store × one product × one day**.

## Important measures
- **Fulfillment rate:** units sold / units demanded.
- **Stockout observation rate:** store-product-days with lost demand / all store-product-days.
- **Estimated lost revenue:** unmet demand units × listed selling price (opportunity estimate, not profit).
- **Realized revenue:** units sold × listed selling price.

## GitHub publishing
Create a new public repository, e.g. `inventory-stockout-intelligence`, then from this extracted folder:
```bash
git init
git add .
git commit -m "Add inventory stockout intelligence portfolio project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/inventory-stockout-intelligence.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your own username and create the repository on GitHub before pushing.

## Power BI steps
Get Data > Text/CSV for all three CSV files. Use Model view to relate dimension IDs to the fact table. Add the DAX measures from `powerbi/PowerBI_Measures.dax`. Create KPI cards, a bar chart by category, a city chart and monthly revenue trend. Save as `.pbix` locally if desired. **A `.pbix` file is not included; the working HTML dashboard is the included finished visualization.**

## Limitations
The dataset uses a simplified demand/replenishment simulation and fixed selling prices. Do not present the numerical findings as company results or real-world savings.
