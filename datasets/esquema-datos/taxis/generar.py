import sqlite3, random, csv, datetime as dt, os, math
random.seed(11)
nom=["Camila","Benjamín","Valentina","Matías","Sofía","Vicente","Isidora","Agustín","Florencia","Tomás","Antonella","Joaquín","Catalina","Martín","Javiera","Lucas","Pedro","Carlos","Luis","Jorge","Patricio","Rodrigo"]
ape=["González","Muñoz","Rojas","Díaz","Pérez","Soto","Contreras","Silva","Martínez","Sepúlveda","Morales","Rodríguez","López","Fuentes","Araya","Espinoza"]
# zonas: comuna, sector, lat, lon, peso origen, es_aeropuerto
zonas=[("Santiago Centro","Centro",-33.4489,-70.6693,14),("Providencia","Oriente",-33.4314,-70.6093,13),
 ("Las Condes","Oriente",-33.4110,-70.5670,13),("Vitacura","Oriente",-33.3900,-70.5720,5),("Lo Barnechea","Oriente",-33.3500,-70.5180,3),
 ("Ñuñoa","Oriente",-33.4569,-70.5970,9),("La Reina","Oriente",-33.4450,-70.5390,3),("Macul","Sur-Oriente",-33.4870,-70.5990,3),
 ("Peñalolén","Sur-Oriente",-33.4870,-70.5330,3),("La Florida","Sur-Oriente",-33.5220,-70.5980,5),("Puente Alto","Sur",-33.6110,-70.5750,4),
 ("San Miguel","Sur",-33.4970,-70.6510,3),("Maipú","Poniente",-33.5100,-70.7570,5),("Estación Central","Poniente",-33.4600,-70.6990,4),
 ("Pudahuel","Poniente",-33.4400,-70.7600,2),("Quilicura","Norte",-33.3600,-70.7300,2),("Recoleta","Norte",-33.4060,-70.6400,3),
 ("Independencia","Norte",-33.4170,-70.6650,2),("Huechuraba","Norte",-33.3700,-70.6350,2),("Aeropuerto AMB","Aeropuerto",-33.3930,-70.7858,4)]
Z=[(i+1,)+z for i,z in enumerate(zonas)]
zw=[z[5] for z in Z]
def dist(a,b):
  dx=(a[4]-b[4])*92.0; dy=(a[3]-b[3])*111.0
  return math.hypot(dx,dy)*1.3  # factor de calles
# servicios: tarifa base, por km, por min, mínima, peso, comisión
serv={"Básico":(700,520,110,2500,55,0.25),"Confort":(900,680,140,3500,20,0.25),"XL":(1200,820,160,4500,8,0.25),"Taxi tradicional":(500,550,110,2000,17,0.15)}
regiones_pas=["Metropolitana"]*9+["Extranjero"]
# conductores y vehículos
marcas={"Básico":[("Chevrolet","Sail"),("Suzuki","Swift"),("Kia","Rio"),("Hyundai","Accent")],"Confort":[("Toyota","Corolla"),("Hyundai","Elantra"),("Nissan","Sentra")],
 "XL":[("Kia","Carnival"),("Hyundai","H-1"),("Chevrolet","Spin")],"Taxi tradicional":[("Nissan","V16"),("Toyota","Corolla"),("Chevrolet","Sail")]}
con=[];veh=[]
for i in range(1,601):
  s=random.choices(list(serv),[50,22,8,20])[0]
  alta=dt.date(2019,1,1)+dt.timedelta(days=random.randint(0,2150))
  hab=random.gauss(4.82,0.08)
  con.append([i,f"{random.choice(nom)} {random.choice(ape)}",random.choices(["M","F"],[85,15])[0],
    random.choices(["18-25","26-35","36-45","46-60","60+"],[8,30,30,25,7])[0],alta.isoformat(),
    random.choices(["Completa","Parcial","Fin de semana"],[45,40,15])[0],round(min(5,hab),2),"Activo"])
  mk,md=random.choice(marcas[s]); anio=random.randint(2016,2025)
  pat="".join(random.choice("BCDFGHJKLPRSTVWXYZ") for _ in range(4))+f"{random.randint(10,99)}"
  veh.append((i,i,pat,mk,md,anio,s,4 if s!="XL" else 6,random.choices(["Bencina","Híbrido","Eléctrico"],[80,13,7])[0]))
# pasajeros
pas=[]
for i in range(1,8001):
  alta=dt.date(2020,1,1)+dt.timedelta(days=random.randint(0,2150))
  pas.append((i,f"{random.choice(nom)} {random.choice(ape)}",random.choice(["F","M"]),
    random.choices(["18-25","26-35","36-45","46-60","60+"],[22,32,22,16,8])[0],random.choice(regiones_pas),
    random.choices(["Ocasional","Frecuente","Corporativo"],[60,30,10])[0],alta.isoformat(),random.choice(Z[:-1])[0]))
pw=[{"Ocasional":1,"Frecuente":4,"Corporativo":3}[p[5]] for p in pas]
# fechas
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
feriados={"2025-01-01","2025-04-18","2025-04-19","2025-05-01","2025-05-21","2025-06-20","2025-06-29","2025-07-16","2025-08-15","2025-09-18","2025-09-19","2025-10-12","2025-10-31","2025-11-01","2025-12-08","2025-12-25"}
fechas=[];d=dt.date(2025,1,1)
while d.year==2025:
  fechas.append((int(d.strftime("%Y%m%d")),d.isoformat(),d.year,(d.month-1)//3+1,d.month,meses[d.month-1],d.isocalendar()[1],d.day,dias[d.weekday()],int(d.weekday()>=5),int(d.isoformat() in feriados)));d+=dt.timedelta(1)
# lluvia: días de lluvia en invierno
lluvia={f[1] for f in fechas if random.random()<{5:0.2,6:0.3,7:0.3,8:0.22,9:0.1}.get(f[4],0.02)}
estac={1:0.85,2:0.75,3:1.05,4:1.0,5:1.0,6:1.05,7:0.95,8:1.0,9:1.05,10:1.05,11:1.05,12:1.15}
hw_lab=[2,1,1,1,1,2,4,9,11,7,5,5,6,6,5,5,6,8,10,9,6,5,4,3]
hw_fds=[6,5,4,2,1,1,1,2,3,4,5,6,7,6,6,6,6,6,7,7,7,7,8,8]
con_by_s={}
for c,v in zip(con,veh): con_by_s.setdefault(v[6],[]).append(c[0])
vj=[];vid=1
for f in fechas:
  dte=dt.date.fromisoformat(f[1]); fds=f[9] or f[10]; rain=f[1] in lluvia
  n=int(random.gauss(480,30)*estac[f[4]]*(1.15 if f[8] in("Viernes","Sábado") else 1)*(1.25 if rain else 1))
  hw=hw_fds if fds else hw_lab
  for _ in range(n):
    h=random.choices(range(24),hw)[0]
    ts=dt.datetime.combine(dte,dt.time(h,random.randint(0,59),random.randint(0,59)))
    p=random.choices(pas,pw)[0]
    o=random.choices(Z,zw)[0]
    if p[5]=="Corporativo" and not fds and random.random()<0.5: dz=random.choice([z for z in Z if z[2]=="Oriente"])
    else:
      dz=random.choices(Z,[z[5]/(1+(dist(o,z)/4)**2)*(0 if z[0]==o[0] and z[2]=="Aeropuerto" else 0.5 if z[0]==o[0] else 1) for z in Z])[0]
    s=random.choices(list(serv),[s[4] for s in serv.values()])[0]
    if p[5]=="Corporativo" and random.random()<0.5: s="Confort"
    base,pkm,pmin,minima,_,comis=serv[s]
    km=round(max(0.8,dist(o,dz)*random.uniform(0.85,1.25) if o[0]!=dz[0] else random.uniform(1,5)),1)
    punta=(not fds) and h in(7,8,9,18,19,20)
    vel=random.uniform(15,22) if punta else random.uniform(24,34)
    if rain: vel*=0.8
    mins=round(km/vel*60+random.uniform(1,4),1)
    dyn=1.0
    if punta: dyn+=random.choice([0,0.2,0.3,0.5])
    if rain: dyn+=random.choice([0.2,0.4,0.6])
    if fds and h in(0,1,2,3): dyn+=random.choice([0,0.2,0.4])
    if s=="Taxi tradicional": dyn=1.0
    espera=round(random.uniform(2,8)*(1.6 if rain or punta else 1),1)
    r=random.random()
    estado="Completado"; motivo=None
    if r<0.06+(0.04 if espera>9 else 0): estado="Cancelado por pasajero"; motivo=random.choice(["Tiempo de espera alto","Cambio de planes","Tarifa alta","Pidió otro medio"])
    elif r<0.09+(0.04 if espera>9 else 0): estado="Cancelado por conductor"; motivo=random.choice(["Pasajero no se presentó","Destino lejano","Problema con vehículo"])
    cid=random.choice(con_by_s[s])
    medio=random.choices(["Tarjeta de crédito","Tarjeta de débito","Efectivo","Cuenta corporativa","Billetera digital"],
      [35,25,22 if s=="Taxi tradicional" else 12,0,15])[0]
    if p[5]=="Corporativo": medio="Cuenta corporativa"
    peaje=0
    if "Aeropuerto" in (o[2],dz[2]) or (o[2]!=dz[2] and random.random()<0.25): peaje=random.choice([1200,1800,2600,3200])
    if estado=="Completado":
      tarifa=max(minima,int(round((base+pkm*km+pmin*mins)*dyn,-1)))
      prop=0 if medio=="Efectivo" or random.random()<0.82 else random.choice([500,1000,1500,2000])
      total=tarifa+peaje+prop; comision=int(round(tarifa*comis))
      cal_p=random.choices([5,4,3,2,1],[78,14,4,2,2])[0] if random.random()<0.7 else None
      cal_c=random.choices([5,4,3,2,1],[85,10,3,1,1])[0] if random.random()<0.6 else None
      fin=ts+dt.timedelta(minutes=espera+mins)
    else:
      tarifa=1500 if estado=="Cancelado por pasajero" and random.random()<0.3 else 0
      km=0;mins=0;dyn=1.0;peaje=0;prop=0;total=tarifa;comision=int(round(tarifa*comis));cal_p=cal_c=None
      fin=ts+dt.timedelta(minutes=random.uniform(1,6))
    vj.append((vid,f[0],ts.isoformat(sep=" "),fin.isoformat(sep=" "),p[0],cid,cid,o[0],dz[0],s,estado,motivo,espera,km,mins,round(dyn,1),
      tarifa,peaje,prop,total,comision,total-comision,medio,cal_p,cal_c,int(rain))); vid+=1
# rating promedio y estado conductor
rs={}
for v in vj:
  if v[23]: rs.setdefault(v[5],[]).append(v[23])
for c in con:
  r=rs.get(c[0],[]); 
  if r: c[6]=round(sum(r)/len(r),2)
  if random.random()<0.06: c[7]="Inactivo"
con=[tuple(c) for c in con]
schema="""
CREATE TABLE dim_pasajero(id_pasajero INTEGER PRIMARY KEY, nombre TEXT, genero TEXT, tramo_edad TEXT, procedencia TEXT, segmento TEXT, fecha_registro DATE, id_zona_residencia INTEGER REFERENCES dim_zona(id_zona));
CREATE TABLE dim_conductor(id_conductor INTEGER PRIMARY KEY, nombre TEXT, genero TEXT, tramo_edad TEXT, fecha_ingreso DATE, jornada TEXT, calificacion_promedio REAL, estado TEXT);
CREATE TABLE dim_vehiculo(id_vehiculo INTEGER PRIMARY KEY, id_conductor INTEGER REFERENCES dim_conductor(id_conductor), patente TEXT, marca TEXT, modelo TEXT, anio INTEGER, tipo_servicio TEXT, capacidad INTEGER, combustible TEXT);
CREATE TABLE dim_zona(id_zona INTEGER PRIMARY KEY, comuna TEXT, sector TEXT, latitud REAL, longitud REAL, peso_demanda INTEGER);
CREATE TABLE dim_fecha(id_fecha INTEGER PRIMARY KEY, fecha DATE, anio INTEGER, trimestre INTEGER, mes INTEGER, nombre_mes TEXT, semana_iso INTEGER, dia INTEGER, dia_semana TEXT, es_fin_semana INTEGER, es_feriado INTEGER);
CREATE TABLE viaje(id_viaje INTEGER PRIMARY KEY, id_fecha INTEGER REFERENCES dim_fecha(id_fecha), fecha_hora_solicitud DATETIME, fecha_hora_fin DATETIME, id_pasajero INTEGER REFERENCES dim_pasajero(id_pasajero), id_conductor INTEGER REFERENCES dim_conductor(id_conductor), id_vehiculo INTEGER REFERENCES dim_vehiculo(id_vehiculo), id_zona_origen INTEGER REFERENCES dim_zona(id_zona), id_zona_destino INTEGER REFERENCES dim_zona(id_zona), tipo_servicio TEXT, estado TEXT, motivo_cancelacion TEXT, minutos_espera REAL, distancia_km REAL, duracion_min REAL, factor_dinamico REAL, tarifa INTEGER, peaje INTEGER, propina INTEGER, monto_total INTEGER, comision_plataforma INTEGER, ingreso_conductor INTEGER, medio_pago TEXT, calificacion_a_conductor INTEGER, calificacion_a_pasajero INTEGER, con_lluvia INTEGER);
CREATE VIEW v_viajes AS
SELECT v.*, f.mes, f.nombre_mes, f.dia_semana, f.es_fin_semana, f.es_feriado, CAST(strftime('%H',v.fecha_hora_solicitud) AS INTEGER) AS hora,
 zo.comuna AS comuna_origen, zo.sector AS sector_origen, zd.comuna AS comuna_destino, zd.sector AS sector_destino,
 p.segmento AS segmento_pasajero, c.nombre AS conductor, ve.marca, ve.modelo, ve.combustible
FROM viaje v JOIN dim_fecha f USING(id_fecha) JOIN dim_zona zo ON zo.id_zona=v.id_zona_origen JOIN dim_zona zd ON zd.id_zona=v.id_zona_destino
JOIN dim_pasajero p USING(id_pasajero) JOIN dim_conductor c USING(id_conductor) JOIN dim_vehiculo ve USING(id_vehiculo);
"""
if os.path.exists("taxis.db"): os.remove("taxis.db")
db=sqlite3.connect("taxis.db"); db.executescript(schema)
tabs={"dim_pasajero":pas,"dim_conductor":con,"dim_vehiculo":veh,"dim_zona":Z,"dim_fecha":fechas,"viaje":vj}
tot=0
for t,rows in tabs.items():
  db.executemany(f"INSERT INTO {t} VALUES({','.join('?'*len(rows[0]))})",rows)
  cols=[x[1] for x in db.execute(f"PRAGMA table_info({t})")]
  with open(f"csv/{t}.csv","w",newline="",encoding="utf-8-sig") as fh: w=csv.writer(fh); w.writerow(cols); w.writerows(rows)
  tot+=len(rows); print(t,len(rows))
db.commit(); open("esquema.sql","w",encoding="utf-8").write(schema); print("TOTAL",tot)
q=lambda s: print(db.execute(s).fetchall())
q("select estado,count(*),round(100.0*count(*)/(select count(*) from viaje),1) from viaje group by 1")
q("select tipo_servicio,count(*),round(avg(distancia_km),1),round(avg(tarifa)),round(avg(duracion_min),1) from viaje where estado='Completado' group by 1")
q("select sum(monto_total),sum(comision_plataforma) from viaje")
q("select con_lluvia,round(avg(factor_dinamico),2),round(avg(minutos_espera),1) from viaje where estado='Completado' group by 1")
q("select hora,count(*) from v_viajes where es_fin_semana=0 group by 1 order by 2 desc limit 3")
q("select comuna_origen,comuna_destino,count(*),round(avg(tarifa)) from v_viajes where estado='Completado' and (comuna_origen like 'Aero%' ) group by 1,2 order by 3 desc limit 3")
