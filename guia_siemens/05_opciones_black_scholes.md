# 05 Opciones, Black-Scholes y Greeks

## Que es una opcion

Una opcion da el derecho, no la obligacion, de comprar o vender un activo a un precio acordado.

- Call: derecho a comprar.
- Put: derecho a vender.

Componentes:

- S: precio actual del subyacente.
- K: strike.
- T: tiempo a vencimiento.
- r: tasa libre de riesgo.
- sigma: volatilidad.
- premium: precio de la opcion.

## Payoff al vencimiento

Call:

```text
max(S_T - K, 0)
```

Put:

```text
max(K - S_T, 0)
```

## Intuicion de valor

Una opcion vale mas cuando:

- aumenta la volatilidad;
- aumenta el tiempo a vencimiento;
- para calls, sube el subyacente;
- para puts, baja el subyacente;
- cambia la tasa de interes.

## Black-Scholes

Formula clasica para opciones europeas.

Call:

```text
C = S0*N(d1) - K*exp(-rT)*N(d2)
```

Put:

```text
P = K*exp(-rT)*N(-d2) - S0*N(-d1)
```

Con:

```text
d1 = [ln(S0/K) + (r + 0.5*sigma^2)T] / [sigma*sqrt(T)]
d2 = d1 - sigma*sqrt(T)
```

## Supuestos

- El subyacente sigue GBM.
- Volatilidad constante.
- Tasa libre de riesgo constante.
- No hay costos de transaccion.
- Mercados continuos y liquidos.
- Opcion europea.

## Greeks

### Delta

Sensibilidad del precio de la opcion ante cambios en el subyacente.

### Gamma

Sensibilidad del delta ante cambios en el subyacente.

### Vega

Sensibilidad ante cambios en volatilidad.

### Theta

Sensibilidad ante paso del tiempo. Muchas opciones pierden valor temporal conforme se acerca el vencimiento.

### Rho

Sensibilidad ante cambios en tasa de interes.

## Monte Carlo vs Black-Scholes

Black-Scholes da formula cerrada bajo supuestos estrictos.

Monte Carlo permite:

- payoffs mas complejos;
- varios factores de riesgo;
- escenarios;
- path dependency;
- simulacion de estrategias.

Pero Monte Carlo:

- tiene error de simulacion;
- requiere muchas corridas;
- depende fuertemente de supuestos.

## Como destacar

No memorices solo la formula. Aprende a decir:

"El precio depende de la distribucion esperada del subyacente al vencimiento, descontada bajo una medida neutral al riesgo. La volatilidad importa porque aumenta la dispersion de payoffs, y la opcion captura el upside mientras limita el downside al premium."

