import sqlite3, random, csv, datetime as dt, os, calendar
random.seed(7)
regiones={"Metropolitana":["Santiago","Providencia","Las Condes","Maipú","Puente Alto","Ñuñoa","La Florida"],
 "Valparaíso":["Valparaíso","Viña del Mar","Quilpué"],"Biobío":["Concepción","Talcahuano"],
 "Antofagasta":["Antofagasta","Calama"],"La Araucanía":["Temuco"],"Los Lagos":["Puerto Montt","Osorno"]}
pw=[55,15,10,8,6,6]
nom=["Camila","Benjamín","Valentina","Matías","Sofía","Vicente","Isidora","Agustín","Florencia","Tomás","Antonella","Joaquín","Catalina","Martín","Javiera","Lucas"]
ape=["González","Muñoz","Rojas","Díaz","Pérez","Soto","Contreras","Silva","Martínez","Sepúlveda","Morales","Rodríguez","López","Fuentes"]
# segmentos de riesgo: (prob pagar total, prob pagar mínimo, prob pago parcial<min, prob no pagar)
riesgo={"A":(0.75,0.20,0.04,0.01),"B":(0.50,0.38,0.08,0.04),"C":(0.25,0.45,0.15,0.15),"D":(0.10,0.40,0.20,0.30)}
productos={"Clásica":(300000,1200000),"Gold":(1000000,3000000),"Platinum":(2500000,6000000),"Black":(5000000,15000000)}
renta_prod={"Hasta 600 mil":["Clásica"],"600 mil - 1,2 MM":["Clásica","Gold"],"1,2 - 2,5 MM":["Gold","Platinum"],"Más de 2,5 MM":["Platinum","Black"]}
# clientes y tarjetas
cli=[];tar=[]
for i in range(1,2501):
  r=random.choices(list(regiones),pw)[0]
  renta=random.choices(list(renta_prod),[35,35,20,10])[0]
  seg=random.choices("ABCD",[30,35,22,13])[0]
  alta=dt.date(2019,1,1)+dt.timedelta(days=random.randint(0,2100))
  cli.append((i,f"{random.choice(nom)} {random.choice(ape)}",random.choice(["F","M"]),
    random.choices(["18-25","26-35","36-45","46-60","60+"],[12,30,27,21,10])[0],r,random.choice(regiones[r]),renta,seg,alta.isoformat()))
  prod=random.choice(renta_prod[renta]); lo,hi=productos[prod]
  emis=alta+dt.timedelta(days=random.randint(0,60))
  tar.append([i,i,f"**** {random.randint(1000,9999)}",prod,int(round(random.uniform(lo,hi),-4)),emis.isoformat(),"Activa"])
# comercios (rubro, mcc, ticket lo-hi, peso, cuotas posibles)
rubros=[("Supermercados","5411",(3000,90000),28,False),("Combustible","5541",(10000,60000),10,False),
 ("Restaurantes","5812",(6000,60000),14,False),("Farmacias","5912",(3000,40000),8,False),
 ("Vestuario","5651",(15000,150000),8,True),("Tecnología","5732",(30000,1200000),4,True),
 ("Viajes y aerolíneas","4511",(60000,900000),2,True),("Hogar y construcción","5200",(10000,400000),5,True),
 ("Suscripciones digitales","5815",(3000,15000),9,False),("Transporte y apps","4121",(2500,20000),9,False),
 ("Salud","8099",(15000,250000),3,True)]
pref={"Supermercados":["Supermercado Andino","Mercado Central Express","SuperAhorro"],"Combustible":["Estación Ruta Sur","Copec-tipo Norte","Bencinera Austral"],
 "Restaurantes":["Sushi Bahía","Parrilla Los Robles","Café Plaza","Pizzería Mapocho"],"Farmacias":["Farmacia Vital","Farmacia Popular"],
 "Vestuario":["Tienda Moda Sur","Outlet Urbano"],"Tecnología":["TecnoStore","Mundo Digital"],"Viajes y aerolíneas":["Vuela Sur","Agencia Horizonte"],
 "Hogar y construcción":["Casa & Obra","Ferretería Central"],"Suscripciones digitales":["StreamPlus","MúsicaYa","NubeDocs"],
 "Transporte y apps":["RideApp","Taxi Express"],"Salud":["Clínica Santa Elena","Centro Dental Sonrisa"]}
com=[];cid=1;com_by_rubro={}
for rb,mcc,_,_,_ in rubros:
  for n in pref[rb]:
    online=rb in("Suscripciones digitales","Transporte y apps") or random.random()<0.25
    extr = rb in ("Suscripciones digitales","Viajes y aerolíneas") and random.random()<0.5
    com.append((cid,n,rb,mcc,"Extranjero" if extr else random.choices(list(regiones),pw)[0],"Online" if online else "Presencial"))
    com_by_rubro.setdefault(rb,[]).append(com[-1]); cid+=1
# fechas
ini,fin=dt.date(2025,1,1),dt.date(2025,12,31)
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
fechas=[];d=ini
while d<=fin+dt.timedelta(days=45):
  fechas.append((int(d.strftime("%Y%m%d")),d.isoformat(),d.year,(d.month-1)//3+1,d.month,meses[d.month-1],d.isocalendar()[1],d.day,dias[d.weekday()],int(d.weekday()>=5)));d+=dt.timedelta(1)
estac={1:0.95,2:0.9,3:1.0,4:0.95,5:1.0,6:0.95,7:1.0,8:1.0,9:1.15,10:1.0,11:1.15,12:1.45}
TASA=0.024  # interés mensual rotativo
tx=[];ec=[];tid=1
rw=[r[3] for r in rubros]
cli_seg={c[0]:c[7] for c in cli}
for t in tar:
  id_t,id_c,_,prod,cupo,emis,_=t; seg=cli_seg[id_c]
  actividad=random.choices([0,1],[8,92])[0]
  base=random.uniform(5,22)*min(2.0,(cupo/1e6)**0.5)
  saldo_ant=0; mora=0; bloqueada=False
  for m in range(1,13):
    y=2025; nd=calendar.monthrange(y,m)[1]
    n=0 if not actividad or bloqueada else max(0,int(random.gauss(base*estac[m],4)))
    usado=saldo_ant; fact=0
    corte=False
    for _ in range(n):
      if corte: break
      rb=random.choices(rubros,rw)[0]; c=random.choice(com_by_rubro[rb[0]])
      dia=random.randint(1,nd); h=random.choices(range(24),[1,1,1,1,1,2,3,5,7,8,9,10,11,10,9,9,9,9,10,10,9,7,4,2])[0]
      fh=dt.datetime(y,m,dia,h,random.randint(0,59),random.randint(0,59))
      monto=int(round(random.uniform(*rb[2])*random.uniform(0.4,0.9)*min(1.0,(cupo/1.5e6)**0.5),-1))
      moneda="USD" if c[4]=="Extranjero" else "CLP"
      cuotas=random.choices([1,3,6,12],[60,20,12,8])[0] if rb[4] and monto>50000 else 1
      fraude=0; estado="Aprobada"; motivo=None
      if random.random()<0.004:
        fraude=1; fh=fh.replace(hour=random.choice([1,2,3,4])); monto=int(round(monto*random.uniform(2,5),-1))
        if random.random()<0.55: estado="Rechazada"; motivo="Sospecha de fraude"
      if estado=="Aprobada" and usado+monto>cupo:
        estado="Rechazada"; motivo="Cupo insuficiente"; corte=random.random()<0.8
      elif estado=="Aprobada" and random.random()<0.012: estado="Rechazada"; motivo=random.choice(["Clave incorrecta","Error de comunicación"])
      if estado=="Aprobada":
        usado+=monto; fact+= monto//cuotas if cuotas>1 else monto
      tx.append((tid,id_t,c[0],int(fh.strftime("%Y%m%d")),fh.isoformat(sep=" "),"Compra",monto,moneda,cuotas,c[5],estado,motivo,fraude)); tid+=1
    # avance en efectivo ocasional (más en riesgo C/D)
    if n and random.random()<{"A":0.02,"B":0.05,"C":0.10,"D":0.15}[seg]:
      monto=int(round(random.uniform(50000,min(500000,cupo*0.3)),-4)); fh=dt.datetime(y,m,random.randint(1,nd),random.randint(9,20),random.randint(0,59))
      ok=usado+monto<=cupo
      tx.append((tid,id_t,None,int(fh.strftime("%Y%m%d")),fh.isoformat(sep=" "),"Avance en efectivo",monto,"CLP",random.choice([1,6,12]),"Cajero",
        "Aprobada" if ok else "Rechazada",None if ok else "Cupo insuficiente",0)); tid+=1
      if ok: usado+=monto; fact+=monto
    # estado de cuenta
    interes=int(round(saldo_ant*TASA)) if saldo_ant>0 else 0
    if interes:
      fi=dt.datetime(y,m,nd,23,59); tx.append((tid,id_t,None,int(fi.strftime("%Y%m%d")),fi.isoformat(sep=" "),"Interés",interes,"CLP",1,"Sistema","Aprobada",None,0)); tid+=1
    facturado=saldo_ant+fact+interes
    if facturado<=0 and saldo_ant==0:
      continue
    minimo=int(round(max(min(facturado,10000),facturado*0.05),-1))
    venc=dt.date(y,m,nd)+dt.timedelta(days=15)
    pt,pm,pp,pn=riesgo[seg]
    if mora>0: pn=min(0.85,pn*2.5)
    comp=random.choices(["total","minimo","parcial","no_paga"],[pt,pm,pp,pn])[0]
    pago={"total":facturado,"minimo":minimo,"parcial":int(minimo*random.uniform(0.2,0.8)),"no_paga":0}[comp]
    pago=int(round(pago,-1)) if comp!="total" else facturado
    if pago>0:
      fp=venc-dt.timedelta(days=random.randint(0,10)) if pago>=minimo else venc+dt.timedelta(days=random.randint(1,20))
      fpd=dt.datetime.combine(fp,dt.time(random.randint(8,22),random.randint(0,59)))
      tx.append((tid,id_t,None,int(fp.strftime("%Y%m%d")),fpd.isoformat(sep=" "),"Pago",-pago,"CLP",1,"Transferencia","Aprobada",None,0)); tid+=1
    mora = 0 if pago>=minimo else mora+30
    if mora>=90: bloqueada=True
    estado_m="Al día" if mora==0 else ("Mora 1-30" if mora<=30 else "Mora 31-60" if mora<=60 else "Mora 61-90" if mora<=90 else "Mora +90")
    ec.append((len(ec)+1,id_t,f"{y}-{m:02d}",int(dt.date(y,m,nd).strftime("%Y%m%d")),cupo,saldo_ant,fact,interes,facturado,minimo,venc.isoformat(),pago,mora,estado_m))
    saldo_ant=max(0,facturado-pago)
  if bloqueada: t[6]="Bloqueada por mora"
  elif not actividad: t[6]="Inactiva"
tar=[tuple(t) for t in tar]
schema="""
CREATE TABLE dim_cliente(id_cliente INTEGER PRIMARY KEY, nombre TEXT, genero TEXT, tramo_edad TEXT, region TEXT, comuna TEXT, tramo_renta TEXT, segmento_riesgo TEXT, fecha_alta DATE);
CREATE TABLE dim_tarjeta(id_tarjeta INTEGER PRIMARY KEY, id_cliente INTEGER REFERENCES dim_cliente(id_cliente), numero_enmascarado TEXT, producto TEXT, cupo_total INTEGER, fecha_emision DATE, estado_tarjeta TEXT);
CREATE TABLE dim_comercio(id_comercio INTEGER PRIMARY KEY, nombre_comercio TEXT, rubro TEXT, mcc TEXT, ubicacion TEXT, tipo_canal TEXT);
CREATE TABLE dim_fecha(id_fecha INTEGER PRIMARY KEY, fecha DATE, anio INTEGER, trimestre INTEGER, mes INTEGER, nombre_mes TEXT, semana_iso INTEGER, dia INTEGER, dia_semana TEXT, es_fin_semana INTEGER);
CREATE TABLE transaccion(id_transaccion INTEGER PRIMARY KEY, id_tarjeta INTEGER REFERENCES dim_tarjeta(id_tarjeta), id_comercio INTEGER REFERENCES dim_comercio(id_comercio), id_fecha INTEGER REFERENCES dim_fecha(id_fecha), fecha_hora DATETIME, tipo_transaccion TEXT, monto_clp INTEGER, moneda_origen TEXT, cuotas INTEGER, canal TEXT, estado TEXT, motivo_rechazo TEXT, es_fraude INTEGER);
CREATE TABLE estado_cuenta(id_estado INTEGER PRIMARY KEY, id_tarjeta INTEGER REFERENCES dim_tarjeta(id_tarjeta), periodo TEXT, id_fecha_cierre INTEGER REFERENCES dim_fecha(id_fecha), cupo_total INTEGER, saldo_anterior INTEGER, compras_periodo INTEGER, intereses INTEGER, monto_facturado INTEGER, pago_minimo INTEGER, fecha_vencimiento DATE, monto_pagado INTEGER, dias_mora INTEGER, estado_mora TEXT);
CREATE VIEW v_transacciones AS
SELECT t.*, ta.producto, ta.cupo_total, c.id_cliente, c.segmento_riesgo, c.tramo_renta, c.region, co.nombre_comercio, co.rubro, co.mcc, f.mes, f.nombre_mes, f.dia_semana
FROM transaccion t JOIN dim_tarjeta ta USING(id_tarjeta) JOIN dim_cliente c USING(id_cliente)
LEFT JOIN dim_comercio co USING(id_comercio) JOIN dim_fecha f USING(id_fecha);
"""
if os.path.exists("tarjetas.db"): os.remove("tarjetas.db")
con=sqlite3.connect("tarjetas.db"); con.executescript(schema)
tabs={"dim_cliente":cli,"dim_tarjeta":tar,"dim_comercio":com,"dim_fecha":fechas,"transaccion":tx,"estado_cuenta":ec}
for t,rows in tabs.items():
  con.executemany(f"INSERT INTO {t} VALUES({','.join('?'*len(rows[0]))})",rows)
  cols=[x[1] for x in con.execute(f"PRAGMA table_info({t})")]
  with open(f"csv/{t}.csv","w",newline="",encoding="utf-8-sig") as fh: w=csv.writer(fh); w.writerow(cols); w.writerows(rows)
con.commit(); open("esquema.sql","w",encoding="utf-8").write(schema)
tot=0
for t in tabs:
  n=con.execute(f"select count(*) from {t}").fetchone()[0]; tot+=n; print(t,n)
print("TOTAL",tot)
print(con.execute("select tipo_transaccion,estado,count(*),sum(monto_clp) from transaccion group by 1,2").fetchall())
print(con.execute("select avg(es_fraude) from transaccion where tipo_transaccion='Compra'").fetchone())
print(con.execute("select c.segmento_riesgo, round(avg(e.dias_mora>=90)*100,1), round(avg(e.dias_mora>0)*100,1) from estado_cuenta e join dim_tarjeta t using(id_tarjeta) join dim_cliente c using(id_cliente) where periodo='2025-12' group by 1").fetchall())
print(con.execute("select estado_tarjeta,count(*) from dim_tarjeta group by 1").fetchall())
print(con.execute("select count(*) from transaccion where id_fecha not in (select id_fecha from dim_fecha)").fetchone())
