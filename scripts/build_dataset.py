from pathlib import Path
import csv,random,datetime,json,collections,statistics,math,subprocess,sys,zipfile,textwrap
root=Path(__file__).resolve().parents[1]
random.seed(20261030)
start=datetime.date(2026,1,1); days=180
cities=['Chennai','Bengaluru','Hyderabad','Coimbatore']; cats=['Dairy','Produce','Beverages','Snacks','Staples','Personal Care']; stores=[{'store_id':f'S{i:02d}','store_name':f'{city} Dark Store {j}','city':city} for i,(city,j) in enumerate([(c,j) for c in cities for j in (1,2)],1)]
products=[]
for i in range(1,37):
 cat=cats[(i-1)//6]; cost=round(random.uniform(25,180),2); products.append({'product_id':f'P{i:03d}','product_name':f'{cat} Item {((i-1)%6)+1}','category':cat,'unit_cost_inr':cost,'selling_price_inr':round(cost*random.uniform(1.17,1.52),2),'lead_time_days':random.choice([2,3,4,5,7]),'safety_stock_units':random.choice([12,16,20,25,30])})
def write(name,rows):
 with (root/'data'/name).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
write('stores.csv',stores);write('products.csv',products)
transactions=[];daily=[]; dates=[start+datetime.timedelta(days=i) for i in range(days)]; states={}
for store in stores:
 for p in products:
  key=(store['store_id'],p['product_id']); states[key]=random.randint(80,180)
  for date in dates:
   opening=states[key]; base={'Dairy':8,'Produce':10,'Beverages':7,'Snacks':6,'Staples':5,'Personal Care':4}[p['category']]; demand=max(0,round(random.gauss(base,base*.32)*(1.25 if date.weekday()>=5 else 1)))
   # replenishment on scheduled cadence; occasional disruption causes stockouts
   received=0
   if date.day%7==1 or (opening<base*4 and date.day%3==0):
    received=random.randint(25,75) if random.random()>.14 else 0
   available=opening+received; sold=min(demand,available); lost=demand-sold; closing=available-sold; states[key]=closing
   daily.append({'date':date.isoformat(),'store_id':store['store_id'],'product_id':p['product_id'],'opening_stock':opening,'received_units':received,'demand_units':demand,'units_sold':sold,'lost_sales_units':lost,'closing_stock':closing,'stockout_flag':int(lost>0),'revenue_inr':round(sold*p['selling_price_inr'],2),'estimated_lost_revenue_inr':round(lost*p['selling_price_inr'],2)})
write('inventory_daily.csv',daily)
# Aggregate from raw daily records, no external packages
rev=sum(r['revenue_inr'] for r in daily); lostrev=sum(r['estimated_lost_revenue_inr'] for r in daily); demand=sum(r['demand_units'] for r in daily); sold=sum(r['units_sold'] for r in daily); lost=sum(r['lost_sales_units'] for r in daily); stockout=sum(r['stockout_flag'] for r in daily)
bycat=collections.defaultdict(lambda:{'revenue_inr':0,'lost_revenue_inr':0,'demand_units':0,'sold_units':0,'stockout_days':0,'observations':0}); pmap={p['product_id']:p for p in products}
bycity=collections.defaultdict(lambda:{'revenue_inr':0,'lost_revenue_inr':0,'demand_units':0,'sold_units':0,'stockout_days':0,'observations':0}); smap={s['store_id']:s for s in stores}
monthly=collections.defaultdict(lambda:{'revenue_inr':0,'lost_revenue_inr':0,'demand_units':0,'sold_units':0})
for r in daily:
 for bucket in [bycat[pmap[r['product_id']]['category']],bycity[smap[r['store_id']]['city']]]:
  bucket['revenue_inr']+=r['revenue_inr'];bucket['lost_revenue_inr']+=r['estimated_lost_revenue_inr'];bucket['demand_units']+=r['demand_units'];bucket['sold_units']+=r['units_sold'];bucket['stockout_days']+=r['stockout_flag'];bucket['observations']+=1
 b=monthly[r['date'][:7]];b['revenue_inr']+=r['revenue_inr'];b['lost_revenue_inr']+=r['estimated_lost_revenue_inr'];b['demand_units']+=r['demand_units'];b['sold_units']+=r['units_sold']
metrics={'project':'Inventory & Stockout Intelligence','data_type':'Synthetic simulated retail data; not actual company performance','period_start':dates[0].isoformat(),'period_end':dates[-1].isoformat(),'stores':len(stores),'products':len(products),'store_product_days':len(daily),'total_demand_units':demand,'units_sold':sold,'lost_sales_units':lost,'fulfillment_rate_pct':round(100*sold/demand,2),'stockout_observation_rate_pct':round(100*stockout/len(daily),2),'revenue_inr':round(rev,2),'estimated_lost_revenue_inr':round(lostrev,2),'categories':{k:{**{x:round(y,2) if isinstance(y,float) else y for x,y in v.items()},'fulfillment_rate_pct':round(100*v['sold_units']/v['demand_units'],2),'stockout_rate_pct':round(100*v['stockout_days']/v['observations'],2)} for k,v in bycat.items()},'cities':{k:{**{x:round(y,2) if isinstance(y,float) else y for x,y in v.items()},'fulfillment_rate_pct':round(100*v['sold_units']/v['demand_units'],2),'stockout_rate_pct':round(100*v['stockout_days']/v['observations'],2)} for k,v in bycity.items()},'months':{k:{x:round(y,2) if isinstance(y,float) else y for x,y in v.items()} for k,v in sorted(monthly.items())}}
(root/'dashboard'/'metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
