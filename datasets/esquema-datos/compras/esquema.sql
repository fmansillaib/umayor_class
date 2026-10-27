
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
