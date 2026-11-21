# Inventory & Stockout Intelligence Dashboard

**End-to-End Inventory Analytics | Demand Fulfillment | Stockout Analysis | Revenue at Risk**

An end-to-end inventory and stockout analytics project built around a simulated quick-commerce retail network. The project demonstrates how daily inventory records can be transformed into operational insights using Python, SQL, Power BI measures, and an interactive browser-based dashboard.

The central business question:

**How do inventory shortages affect demand fulfillment, sales revenue, and product availability across stores, and where should replenishment efforts be prioritized?**

> **Data disclosure:** This is a synthetic retail case study. All stores, products, inventory records, revenue figures, and findings are simulated. They do not represent actual company performance or verified business savings.

## Executive Summary

The project simulates inventory operations across eight quick-commerce dark stores over a 180-day period.

| Business KPI | Result |
|---|---:|
| Number of stores | 8 |
| Number of products | 36 |
| Analysis period | 180 days |
| Store-product-day records | 51,840 |
| Total demand | 371,133 units |
| Units sold | 369,687 units |
| Lost sales | 1,446 units |
| Fulfillment rate | 99.61% |
| Stockout observation rate | 0.41% |
| Realized revenue | ₹5,07,01,420.43 |
| Estimated lost revenue | ₹2,14,356.78 |

**Key takeaway:** Overall fulfillment is high at 99.61%, but the analysis identifies differences in stockout exposure across product categories and cities. These differences help prioritize inventory investigation instead of treating every stockout observation equally.

## 1. Business Problem

Inventory availability plays an important role in retail and quick-commerce operations. When products are unavailable at the time of customer demand, businesses may experience lost sales opportunities, reduced fulfillment, and inconsistent customer experiences.

Inventory and replenishment teams need visibility into:

- Products experiencing recurring stockouts.
- Demand versus actual units fulfilled.
- Revenue exposure associated with unmet demand.
- Product categories with higher inventory shortages.
- Stores and cities experiencing replenishment gaps.
- Monthly inventory and revenue trends.
- Products approaching or falling below safety stock levels.

**Project objective:** Develop an inventory intelligence solution that connects demand, inventory availability, fulfillment, and estimated lost revenue to support data-driven replenishment prioritization.

## 2. Dataset Overview

The project uses three synthetic datasets generated using Python.

| Dataset | Records | Business purpose |
|---|---:|---|
| Stores | 8 | Store-level reference data |
| Products | 36 | Product catalog, categories, and inventory reference attributes |
| Daily Inventory | 51,840 | Daily demand, sales, inventory movement, and stockout records |
| **Total** | **51,884** | **Combined dataset records** |

### Dataset coverage

- Analysis period: January 1, 2026 – June 29, 2026.
- Stores: 8.
- Cities: Chennai, Bengaluru, Hyderabad, and Coimbatore.
- Products: 36.
- Categories: 6.
- Daily observations: 180 days.

The daily inventory dataset follows this grain:

**One record per store × product × date.**

## 3. Tools and Methodology

| Tool | Application |
|---|---|
| Python | Synthetic dataset generation and validation |
| Pandas / Python | Data preparation and processing where applicable |
| SQL (SQLite) | KPI calculations, category analysis, store performance, and reorder candidate identification |
| HTML / CSS / JavaScript | Interactive browser-based dashboard |
| JSON | Dashboard summary metrics |
| Power BI / DAX | Optional Power BI data model and KPI measures |
| Git & GitHub | Version control and project documentation |

### Analytical workflow

1. **Business problem definition:** Identified inventory availability, lost sales, fulfillment, and replenishment as the main analytical areas.
2. **Data generation:** Generated store, product, and daily inventory datasets using Python.
3. **Data validation:** Checked inventory conservation, demand fulfillment, chronological stock continuity, and dataset completeness.
4. **Data modeling:** Connected daily inventory records with store and product reference tables.
5. **SQL analysis:** Developed queries for executive KPIs, category performance, store bottlenecks, monthly trends, and reorder candidates.
6. **Dashboard development:** Built an interactive browser-based dashboard with KPI summaries, city and category filters, and visual analysis.
7. **Power BI preparation:** Created reusable DAX measures for an optional native Power BI implementation.
8. **Business interpretation:** Identified inventory exposure areas and proposed targeted replenishment investigation.

## 4. Dashboard and Visual Analysis

The project includes a self-contained interactive HTML dashboard.

**Dashboard location:** `dashboard/index.html`

The dashboard supports city and category filtering and displays KPI summaries and inventory performance visualizations.

### Dashboard analysis areas

1. Overall demand and fulfillment performance.
2. Total units sold and lost sales.
3. Realized revenue and estimated lost revenue.
4. Inventory stockout observation rate.
5. Category-level fulfillment and lost revenue.
6. City-level inventory performance.
7. Monthly revenue and lost revenue trends.

### Interactive dashboard

Open `dashboard/index.html` in a browser to explore the dashboard.

The dashboard works locally without requiring a server, installation, or internet connection.

## 5. Key Business Findings

### 5.1 Overall Inventory Fulfillment

The simulated retail network records:

- Total demand: 371,133 units.
- Units sold: 369,687 units.
- Lost sales: 1,446 units.
- Fulfillment rate: 99.61%.

**Business interpretation:** The overall fulfillment rate is high, but the remaining unmet demand represents opportunities to investigate product availability and replenishment effectiveness.

### 5.2 Product Category Performance

| Category | Realized Revenue | Estimated Lost Revenue | Fulfillment |
|---|---:|---:|---:|
| Produce | ₹1,40,03,520.43 | ₹1,23,439.59 | 99.09% |
| Beverages | ₹93,84,765.63 | ₹35,686.77 | 99.64% |
| Dairy | ₹88,84,217.69 | ₹54,448.17 | 99.52% |
| Snacks | ₹68,34,766.04 | ₹782.25 | 99.99% |
| Staples | ₹68,02,192.17 | ₹0.00 | 100.00% |
| Personal Care | ₹47,91,958.47 | ₹0.00 | 100.00% |

**Key observation:** Produce has the highest estimated lost revenue at approximately ₹1.23 lakh and the lowest category fulfillment rate at 99.09%.

**Business interpretation:** Produce is the first category worth investigating for demand patterns, inventory availability, and replenishment frequency.

### 5.3 City-Level Inventory Performance

| City | Realized Revenue | Estimated Lost Revenue | Fulfillment |
|---|---:|---:|---:|
| Chennai | ₹1,26,75,529.10 | ₹52,722.67 | 99.60% |
| Bengaluru | ₹1,26,47,990.66 | ₹54,546.80 | 99.61% |
| Hyderabad | ₹1,26,89,432.01 | ₹54,585.48 | 99.62% |
| Coimbatore | ₹1,26,88,468.66 | ₹52,501.83 | 99.62% |

**Key observation:** Hyderabad has the highest estimated lost revenue, approximately ₹54,585, closely followed by Bengaluru.

**Business interpretation:** City-level comparisons help identify where store-level replenishment practices should be investigated further.

### 5.4 Monthly Revenue and Lost Revenue

The project analyzes six months of simulated inventory and revenue activity.

| Month | Realized Revenue | Estimated Lost Revenue |
|---|---:|---:|
| January 2026 | ₹87,60,655.48 | ₹16,930.91 |
| February 2026 | ₹79,00,600.60 | ₹30,773.59 |
| March 2026 | ₹87,52,375.54 | ₹33,524.95 |
| April 2026 | ₹84,09,684.40 | ₹55,000.25 |
| May 2026 | ₹87,69,043.63 | ₹39,604.65 |
| June 2026 | ₹81,09,060.78 | ₹38,522.43 |

**Key observation:** April records the highest estimated lost revenue during the simulated period, at ₹55,000.25.

**Business interpretation:** Monthly analysis helps identify periods requiring additional investigation into demand patterns and inventory availability.

## 6. KPI Definitions

| KPI | Calculation |
|---|---|
| Total Demand | Sum of demand units |
| Units Sold | Sum of fulfilled sales units |
| Lost Sales Units | Demand units − Units sold |
| Fulfillment Rate | Units sold ÷ Total demand × 100 |
| Stockout Observation Rate | Stockout observations ÷ Total store-product-day records × 100 |
| Realized Revenue | Units sold × listed selling price |
| Estimated Lost Revenue | Unmet demand units × listed selling price |
| Average Closing Stock | Average of daily closing inventory |

**Important distinction:** Stockout observation rate measures the percentage of store-product-day records with unmet demand. It does not measure the percentage of products out of stock at one particular moment.

Estimated lost revenue represents a potential sales opportunity, not realized profit or guaranteed recoverable revenue.

## 7. SQL Analysis

The project includes reusable SQLite-compatible queries in:

`sql/analysis_queries.sql`

The SQL analysis covers:

1. Executive KPI summary.
2. Category-level inventory performance.
3. Store and city-level bottleneck analysis.
4. Monthly revenue and lost revenue trends.
5. Reorder candidates based on latest closing stock against product safety stock.

These queries demonstrate how inventory datasets can be analyzed using SQL joins, aggregations, calculated metrics, grouping, and common table expressions.

## 8. Power BI Implementation

The repository includes:

`powerbi/PowerBI_Measures.dax`

The DAX file provides measures for:

- Total Demand.
- Units Sold.
- Lost Units.
- Revenue INR.
- Estimated Lost Revenue INR.
- Fulfillment Rate.
- Stockout Observation Rate.
- Stockout Observations.
- Average Closing Stock.

### Suggested Power BI implementation

1. Open Power BI Desktop.
2. Select **Get Data → Text/CSV**.
3. Import:
   - `data/inventory_daily.csv`
   - `data/products.csv`
   - `data/stores.csv`
4. Create relationships between the inventory fact table and the product/store dimension tables.
5. Add the DAX measures from `powerbi/PowerBI_Measures.dax`.
6. Create KPI cards for demand, units sold, fulfillment, revenue, and estimated lost revenue.
7. Add category and city-level charts.
8. Create a monthly revenue trend.
9. Add slicers for city and product category.

**Note:** A Power BI `.pbix` file is not included. The finished interactive visualization supplied in this repository is the HTML dashboard.

## 9. Recommended Business Actions

| Business area | Recommended action | Objective |
|---|---|---|
| Produce inventory | Investigate demand variation and replenishment frequency | Reduce unmet demand exposure |
| City-level operations | Examine store-level stockout patterns in Hyderabad and Bengaluru | Identify replenishment bottlenecks |
| Inventory planning | Review products approaching or falling below safety stock | Improve inventory availability |
| Demand planning | Monitor monthly demand and lost revenue patterns | Improve replenishment planning |
| Category management | Compare demand, fulfillment, and revenue exposure | Prioritize operational interventions |
| Performance monitoring | Track fulfillment and stockout observation rates regularly | Monitor inventory availability |

These actions are recommendations based on the simulated analysis. Their real-world effectiveness would need to be tested using actual operational data.

## 10. Data Validation and Quality Checks

The Python validation script checks:

- Expected dataset record counts.
- Inventory conservation: opening stock + received units − units sold = closing stock.
- Demand reconciliation: demand units − units sold = lost sales units.
- Chronological stock continuity.
- Dataset consistency and integrity.

The data generation process is deterministic, allowing the synthetic dataset to be reproduced consistently.

## 11. Repository Structure

```text
inventory-stockout-intelligence/
│
├── dashboard/
│   ├── index.html
│   └── metrics.json
│
├── data/
│   ├── stores.csv
│   ├── products.csv
│   └── inventory_daily.csv
│
├── docs/
│   └── BUSINESS_CASE.md
│
├── powerbi/
│   └── PowerBI_Measures.dax
│
├── scripts/
│   ├── build_dataset.py
│   ├── generate_data.py
│   └── validate_data.py
│
├── sql/
│   └── analysis_queries.sql
│
├── .gitignore
└── README.md
```

## 12. How to Run the Project

### Option 1: Explore the dashboard

No installation is required.

1. Download or clone the repository.
2. Open the `dashboard` folder.
3. Double-click `index.html`.
4. Explore the interactive dashboard.
5. Use the city and category filters.

### Option 2: Validate the dataset

Install Python if it is not already available.

Run:

```bash
python scripts/validate_data.py
```

### Option 3: Regenerate the synthetic dataset

Run:

```bash
python scripts/generate_data.py
```

The generator uses standard-library Python only.

### Option 4: Run SQL analysis

Import the three CSV files into SQLite using the table names:

- `inventory_daily`
- `products`
- `stores`

Execute the queries from:

`sql/analysis_queries.sql`

## 13. Project Limitations

- All data is synthetic and generated for portfolio demonstration.
- The simulation uses a simplified demand and replenishment model.
- Selling prices are fixed in the simulated dataset.
- Estimated lost revenue is not equivalent to lost profit.
- Safety-stock-based reorder candidates are illustrative, not a production replenishment algorithm.
- Real-world inventory planning would require supplier lead-time variability, promotions, seasonality, returns, actual margins, and supplier reliability data.
- No actual business savings or operational improvements are claimed.

## 14. Skills Demonstrated

**Supply Chain & Operations:** Inventory Management, Stockout Analysis, Demand Fulfillment, Replenishment Prioritization, Safety Stock Analysis, Lost Sales Analysis, Retail Operations Analytics.

**Data & Technical:** Python, SQL, SQLite, Power BI, DAX, Data Modeling, Data Validation, HTML, JavaScript, JSON, Git, GitHub.

**Business Analytics:** KPI Development, Revenue Analysis, Root-Cause Investigation, Category Performance, City-Level Analysis, Management Reporting, Data-Driven Decision Support.

---

**Project Type:** Supply Chain Analytics | Inventory Management | Operations Analytics

**Case Study:** Simulated Quick-Commerce Dark Store Network

**Repository:** https://github.com/vignesh-sathishkumar/inventory-stockout-intelligence
