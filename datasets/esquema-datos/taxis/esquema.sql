
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
