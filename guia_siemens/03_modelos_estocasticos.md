# 03 Modelos estocasticos

## Intuicion

Un modelo estocastico describe una variable que evoluciona con incertidumbre.

No responde solo:

```text
que valor espero?
```

Tambien responde:

```text
que distribucion de futuros posibles existe?
```

## Procesos de Markov

Un proceso de Markov cumple:

```text
el futuro depende del estado actual, no de toda la historia.
```

Ejemplo de estados para demanda energetica:

- baja;
- normal;
- alta;
- critica.

La dinamica se define con una matriz de transicion:

```text
P[i, j] = probabilidad de pasar del estado i al estado j
```

Aplicaciones:

- regimenes de precios;
- fallas de infraestructura;
- estados operativos;
- clima;
- credit risk;
- demanda por nivel.

## Random walk

Modelo simple donde cada paso suma un shock aleatorio:

```text
X[t+1] = X[t] + error
```

Es base para entender movimientos acumulativos.

## Movimiento Browniano

Proceso continuo con incrementos aleatorios normales.

Propiedades clave:

- empieza en cero;
- incrementos independientes;
- incrementos normalmente distribuidos;
- varianza crece con el tiempo.

Es una pieza central en finanzas cuantitativas.

## Geometric Brownian Motion

Modelo clasico de precios financieros:

```text
dS_t = mu*S_t*dt + sigma*S_t*dW_t
```

Forma discreta comun:

```text
S[t+1] = S[t] * exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z)
```

Donde:

- S: precio;
- mu: drift;
- sigma: volatilidad;
- dt: paso de tiempo;
- Z: shock normal estandar.

## Por que GBM usa lognormal

El precio simulado con GBM queda positivo porque se multiplica por una exponencial. Eso evita precios negativos, lo cual es util para acciones y algunos precios.

## Limitaciones de GBM

- volatilidad constante;
- no modela saltos;
- retornos normales;
- no captura colas pesadas;
- no captura cambios de regimen.

Modelos mas avanzados:

- jump diffusion;
- Heston;
- local volatility;
- stochastic volatility;
- regime switching.

## En energia

Los precios energeticos suelen ser mas dificiles que acciones:

- pueden tener spikes;
- mean reversion;
- estacionalidad;
- dependencia del clima;
- restricciones fisicas;
- regulacion;
- eventos extremos.

Por eso en energia a veces conviene combinar:

- modelos estadisticos;
- escenarios;
- Monte Carlo;
- restricciones operativas;
- conocimiento del negocio.

## Como explicar un proceso estocastico

"No estoy prediciendo una unica trayectoria. Estoy generando muchas trayectorias plausibles bajo supuestos claros para medir distribucion, riesgo y sensibilidad."

