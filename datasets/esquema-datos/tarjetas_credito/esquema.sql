
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
