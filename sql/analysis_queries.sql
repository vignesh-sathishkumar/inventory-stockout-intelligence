-- SQLite-compatible queries. Import CSVs as tables: inventory_daily, products, stores.
-- 1. Executive KPIs
SELECT COUNT(*) AS store_product_days, SUM(demand_units) AS demand_units, SUM(units_sold) AS sold_units,
ROUND(100.0*SUM(units_sold)/NULLIF(SUM(demand_units),0),2) AS fulfillment_pct,
ROUND(100.0*SUM(stockout_flag)/COUNT(*),2) AS stockout_observation_pct,
ROUND(SUM(revenue_inr),2) AS revenue_inr, ROUND(SUM(estimated_lost_revenue_inr),2) AS estimated_lost_revenue_inr
FROM inventory_daily;

-- 2. Category performance
SELECT p.category, SUM(i.demand_units) AS demand_units, SUM(i.lost_sales_units) AS lost_units,
ROUND(100.0*SUM(i.units_sold)/NULLIF(SUM(i.demand_units),0),2) AS fulfillment_pct,
ROUND(SUM(i.estimated_lost_revenue_inr),2) AS lost_revenue_inr
FROM inventory_daily i JOIN products p ON p.product_id=i.product_id
GROUP BY p.category ORDER BY lost_revenue_inr DESC;

-- 3. Store / city bottlenecks
SELECT s.city,s.store_name,ROUND(100.0*SUM(i.stockout_flag)/COUNT(*),2) AS stockout_pct,
ROUND(SUM(i.estimated_lost_revenue_inr),2) AS lost_revenue_inr
FROM inventory_daily i JOIN stores s ON s.store_id=i.store_id
GROUP BY s.city,s.store_name ORDER BY lost_revenue_inr DESC;

-- 4. Monthly trend
SELECT SUBSTR(date,1,7) AS month, ROUND(SUM(revenue_inr),2) AS revenue_inr,
ROUND(SUM(estimated_lost_revenue_inr),2) AS estimated_lost_revenue_inr
FROM inventory_daily GROUP BY SUBSTR(date,1,7) ORDER BY month;

-- 5. Reorder candidates (latest closing stock against safety stock)
WITH latest AS (SELECT store_id,product_id,MAX(date) AS latest_date FROM inventory_daily GROUP BY store_id,product_id)
SELECT i.store_id,i.product_id,p.product_name,i.closing_stock,p.safety_stock_units,p.lead_time_days
FROM inventory_daily i JOIN latest l ON i.store_id=l.store_id AND i.product_id=l.product_id AND i.date=l.latest_date
JOIN products p ON i.product_id=p.product_id WHERE i.closing_stock<=p.safety_stock_units
ORDER BY i.closing_stock ASC;
