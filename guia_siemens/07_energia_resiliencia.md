# 07 Energia, demanda y resiliencia

## Contexto

En Siemens, los modelos no viven aislados: ayudan a tomar decisiones sobre infraestructura, electrificacion, costos, resiliencia y propuestas a clientes.

## Casos probables

### Electrificacion de flotillas

Preguntas:

- Cuanta energia necesitara una flotilla electrica?
- En que horarios se cargara?
- Cual sera el pico de demanda?
- Que pasa si sube el precio electrico?
- Conviene carga inteligente?

Variables:

- kilometros recorridos;
- eficiencia kWh/km;
- horario de llegada;
- capacidad de bateria;
- potencia del cargador;
- tarifa electrica;
- temperatura.

### Hogares electrificados

Preguntas:

- Como cambia la demanda si se electrifican calefaccion, cocina o vehiculos?
- Cual es el nuevo perfil horario?
- Que ahorro o sobrecosto se genera?

### Centros de datos

Preguntas:

- Que pasa si falla una fuente de energia?
- Cual es el costo esperado de downtime?
- Que nivel de redundancia conviene?
- Como afecta la demanda a resiliencia y costo?

Variables:

- carga IT;
- PUE;
- precio energia;
- probabilidad de outage;
- duracion de outage;
- respaldo disponible;
- costo por hora de interrupcion.

## Modelos utiles

### Forecasting

Para predecir demanda, consumo o precios.

### Monte Carlo

Para escenarios de incertidumbre.

### Markov

Para estados operativos:

- normal;
- degradado;
- falla parcial;
- falla total.

### Optimizacion

Para minimizar costo sujeto a restricciones:

- capacidad;
- resiliencia;
- emisiones;
- presupuesto;
- niveles de servicio.

## KPIs importantes

- demanda pico;
- consumo total;
- costo esperado;
- probabilidad de exceder capacidad;
- probabilidad de outage critico;
- percentil 95 de costo;
- energia no servida;
- CO2 evitado;
- ahorro neto;
- payback period.

## Como comunicar

Evita:

```text
El modelo predice 120 MWh.
```

Mejor:

```text
Bajo el escenario base, la demanda esperada es 120 MWh. En el percentil 95 sube a 155 MWh, lo que excede la capacidad actual por 12%. El riesgo se concentra entre 6pm y 9pm.
```

## Preguntas buenas para tu jefe

- Que decisiones se toman con este modelo?
- Cual es el costo de equivocarse hacia arriba vs hacia abajo?
- Que variables son controlables por Siemens o por el cliente?
- Que horizonte temporal importa?
- Que nivel de explicabilidad esperan?
- Que supuestos ya usa el equipo?
- Hay datos historicos confiables?
- Como validan hoy sus simulaciones?

