"""Check inventory conservation, stockout logic and row counts. stdlib only."""
import csv,collections,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
with (root/'data'/'inventory_daily.csv').open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
assert len(rows)==8*36*180, f"Unexpected row count: {len(rows)}"
previous={}
for r in rows:
 key=(r['store_id'],r['product_id'])
 op,recv,dem,sold,lost,close=[int(r[k]) for k in ['opening_stock','received_units','demand_units','units_sold','lost_sales_units','closing_stock']]
 assert op+recv-sold==close and dem-sold==lost and close>=0
 assert int(r['stockout_flag'])==int(lost>0)
 if key in previous: assert previous[key]==op, f'Broken continuity: {key}'
 previous[key]=close
print(f'PASS: {len(rows):,} daily records, inventory balance and continuity verified')
