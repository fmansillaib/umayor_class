import sqlite3, random, csv, datetime as dt, os
random.seed(42)
regiones = {"Metropolitana":["Santiago","Providencia","Las Condes","Maipú","Puente Alto","Ñuñoa"],
 "Valparaíso":["Valparaíso","Viña del Mar","Quilpué"],"Biobío":["Concepción","Talcahuano"],
 "Antofagasta":["Antofagasta","Calama"],"La Araucanía":["Temuco"],"Los Lagos":["Puerto Montt","Osorno"]}
pesos_reg=[55,15,10,8,6,6]
nombres=["Camila","Benjamín","Valentina","Matías","Sofía","Vicente","Isidora","Agustín","Florencia","Tomás","Antonella","Joaquín","Catalina","Martín","Javiera","Lucas"]
apellidos=["González","Muñoz","Rojas","Díaz","Pérez","Soto","Contreras","Silva","Martínez","Sepúlveda","Morales","Rodríguez","López","Fuentes"]
cat={"Tecnología":{"Celulares":(150000,600000),"Audio":(15000,120000),"Computación":(300000,1200000)},
 "Hogar":{"Cocina":(8000,90000),"Decoración":(5000,60000),"Electrodomésticos":(40000,450000)},
 "Vestuario":{"Calzado":(20000,90000),"Ropa":(8000,60000)},
 "Supermercado":{"Abarrotes":(1000,8000),"Bebidas":(800,5000),"Limpieza":(1500,9000)},
 "Deporte":{"Fitness":(10000,150000),"Outdoor":(15000,200000)}}
# productos
prod=[]; pid=1
for c,subs in cat.items():
  for s,(lo,hi) in subs.items():
    for k in range(1,7):
      precio=round(random.uniform(lo,hi),-2); margen=random.uniform(0.15,0.45)
      prod.append((pid,f"{s} modelo {k:02d}",c,s,precio,round(precio*(1-margen),-1))); pid+=1
# clientes
cli=[]
for i in range(1,1501):
  r=random.choices(list(regiones),pesos_reg)[0]
  alta=dt.date(2022,1,1)+dt.timedelta(days=random.randint(0,1200))
  cli.append((i,f"{random.choice(nombres)} {random.choice(apellidos)}",random.choice(["F","M"]),
    random.choices(["18-25","26-35","36-45","46-60","60+"],[15,30,25,20,10])[0],r,random.choice(regiones[r]),
    random.choices(["Nuevo","Frecuente","Premium"],[50,35,15])[0],alta.isoformat()))
canales=[(1,"Web","Online"),(2,"App móvil","Online"),(3,"Tienda Santiago Centro","Presencial"),
 (4,"Tienda Viña del Mar","Presencial"),(5,"Tienda Concepción","Presencial"),(6,"Marketplace","Online")]
medios=["Tarjeta de crédito","Tarjeta de débito","Transferencia","Efectivo"]
# fechas
ini,fin=dt.date(2024,1,1),dt.date(2025,12,31)
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
fechas=[]; d=ini
while d<=fin:
  fechas.append((int(d.strftime("%Y%m%d")),d.isoformat(),d.year,(d.month-1)//3+1,d.month,meses[d.month-1],
    d.isocalendar()[1],d.day,dias[d.weekday()],1 if d.weekday()>=5 else 0)); d+=dt.timedelta(1)
# ordenes
def peso_fecha(d):
  w=1.0
  if d.month==12: w*=1.8
  if d.month==11: w*=1.3
  if d.weekday()>=5: w*=1.2
  if d.year==2025: w*=1.15
  return w
fl=[dt.date.fromisoformat(f[1]) for f in fechas]; fw=[peso_fecha(x) for x in fl]
seg_w={"Nuevo":1,"Frecuente":3,"Premium":5}
cw=[seg_w[c[6]] for c in cli]
ords=[]; det=[]; did=1
for oid in range(1,12001):
  f=random.choices(fl,fw)[0]; c=random.choices(cli,cw)[0]
  can=random.choices(canales,[30,30,12,8,8,12])[0]
  medio=random.choices(medios,[45,35,15,5] if can[2]=="Presencial" else [55,30,15,0])[0]
  estado=random.choices(["Completada","Devuelta","Anulada"],[93,4,3])[0]
  envio=0 if can[2]=="Presencial" else random.choice([0,2990,3990,4990])
  ords.append((oid,int(f.strftime("%Y%m%d")),f.isoformat(),c[0],can[0],medio,estado,envio))
  for p in random.sample(prod,random.choices([1,2,3,4,5],[40,25,18,10,7])[0]):
    q=random.choices([1,2,3,4],[70,18,8,4])[0] if p[2]!="Supermercado" else random.randint(1,6)
    desc=random.choices([0,0.05,0.10,0.20],[65,15,12,8])[0]
    if f.month in (11,12) and random.random()<0.3: desc=max(desc,0.15)
    pu=p[4]; bruto=pu*q; mdesc=round(bruto*desc); neto=bruto-mdesc
    det.append((did,oid,p[0],q,pu,desc,mdesc,neto,round(neto/1.19),round(neto-neto/1.19),p[5]*q)); did+=1
schema="""
CREATE TABLE dim_cliente(id_cliente INTEGER PRIMARY KEY, nombre TEXT, genero TEXT, tramo_edad TEXT, region TEXT, comuna TEXT, segmento TEXT, fecha_alta DATE);
CREATE TABLE dim_producto(id_producto INTEGER PRIMARY KEY, nombre_producto TEXT, categoria TEXT, subcategoria TEXT, precio_lista INTEGER, costo_unitario INTEGER);
CREATE TABLE dim_canal(id_canal INTEGER PRIMARY KEY, canal TEXT, tipo_canal TEXT);
CREATE TABLE dim_fecha(id_fecha INTEGER PRIMARY KEY, fecha DATE, anio INTEGER, trimestre INTEGER, mes INTEGER, nombre_mes TEXT, semana_iso INTEGER, dia INTEGER, dia_semana TEXT, es_fin_semana INTEGER);
CREATE TABLE orden(id_orden INTEGER PRIMARY KEY, id_fecha INTEGER REFERENCES dim_fecha(id_fecha), fecha DATE, id_cliente INTEGER REFERENCES dim_cliente(id_cliente), id_canal INTEGER REFERENCES dim_canal(id_canal), medio_pago TEXT, estado TEXT, costo_envio INTEGER);
CREATE TABLE detalle_orden(id_detalle INTEGER PRIMARY KEY, id_orden INTEGER REFERENCES orden(id_orden), id_producto INTEGER REFERENCES dim_producto(id_producto), cantidad INTEGER, precio_unitario INTEGER, pct_descuento REAL, monto_descuento INTEGER, monto_neto INTEGER, monto_sin_iva INTEGER, iva INTEGER, costo_total INTEGER);
CREATE VIEW v_ventas AS
SELECT d.id_detalle, o.id_orden, o.fecha, f.anio, f.mes, f.nombre_mes, c.id_cliente, c.segmento, c.region, c.comuna,
 ca.canal, ca.tipo_canal, o.medio_pago, o.estado, p.categoria, p.subcategoria, p.nombre_producto,
 d.cantidad, d.precio_unitario, d.monto_descuento, d.monto_neto, d.monto_sin_iva, d.costo_total,
 d.monto_sin_iva - d.costo_total AS margen
FROM detalle_orden d JOIN orden o USING(id_orden) JOIN dim_producto p USING(id_producto)
JOIN dim_cliente c ON c.id_cliente=o.id_cliente JOIN dim_canal ca ON ca.id_canal=o.id_canal
JOIN dim_fecha f ON f.id_fecha=o.id_fecha;
"""
if os.path.exists("compras.db"): os.remove("compras.db")
con=sqlite3.connect("compras.db"); con.executescript(schema)
tabs={"dim_cliente":cli,"dim_producto":prod,"dim_canal":canales,"dim_fecha":fechas,"orden":ords,"detalle_orden":det}
for t,rows in tabs.items():
  con.executemany(f"INSERT INTO {t} VALUES({','.join('?'*len(rows[0]))})",rows)
  cols=[x[1] for x in con.execute(f"PRAGMA table_info({t})")]
  with open(f"csv/{t}.csv","w",newline="",encoding="utf-8-sig") as fh:
    w=csv.writer(fh); w.writerow(cols); w.writerows(rows)
con.commit()
open("esquema.sql","w",encoding="utf-8").write(schema)
for t in tabs: print(t,con.execute(f"select count(*) from {t}").fetchone()[0])
print(con.execute("select anio, estado, sum(monto_neto) from v_ventas group by 1,2").fetchall())
