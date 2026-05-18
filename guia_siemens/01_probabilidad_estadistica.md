# 01 Probabilidad y estadistica aplicada

## Para que sirve

La estadistica es la base para decidir si un patron en datos es real, ruido o una conclusion demasiado apresurada. En Siemens te ayuda a responder preguntas como:

- La demanda subio por una causa real o por variacion normal?
- La temperatura explica el consumo electrico?
- Un cambio en precios tiene efecto estadisticamente significativo?
- Que tan confiable es un forecast?

## Conceptos esenciales

### Variable aleatoria

Una cantidad cuyo valor no conocemos con certeza. Ejemplos:

- demanda electrica manana;
- precio del gas el proximo mes;
- numero de fallas en un centro de datos;
- retorno diario de un activo.

### Esperanza

Valor promedio esperado a largo plazo.

```text
E[X] = promedio ponderado de los posibles valores
```

En negocio, puede interpretarse como caso central o costo esperado.

### Varianza y desviacion estandar

Miden dispersion. Dos escenarios pueden tener el mismo valor esperado pero distinto riesgo.

```text
Var(X) = E[(X - E[X])^2]
```

### Covarianza y correlacion

Miden como se mueven dos variables juntas.

- Covarianza positiva: tienden a subir juntas.
- Covarianza negativa: una sube cuando la otra baja.
- Correlacion: version normalizada entre -1 y 1.

Importante: correlacion no implica causalidad.

## Distribuciones que debes dominar

| Distribucion | Uso tipico |
|---|---|
| Normal | Errores, ruido agregado, aproximaciones |
| Lognormal | Precios positivos, GBM, activos financieros |
| Bernoulli | Evento si/no |
| Binomial | Numero de exitos en n intentos |
| Poisson | Conteo de eventos: fallas, llegadas, incidentes |
| Exponencial | Tiempo entre eventos |

## Inferencia estadistica

### Hipotesis nula

La hipotesis conservadora. Ejemplo:

```text
H0: la temperatura no tiene efecto sobre la demanda electrica.
H1: la temperatura si tiene efecto.
```

### p-value

Probabilidad de observar un resultado tan extremo como el obtenido si la hipotesis nula fuera cierta.

Regla practica:

- p < 0.05: evidencia estadistica comunmente considerada fuerte.
- p >= 0.05: no hay suficiente evidencia para rechazar H0.

No significa "probabilidad de que H0 sea verdadera".

### Intervalo de confianza

Rango plausible para un parametro. Es mas informativo que solo reportar un p-value.

Ejemplo ejecutivo:

> Estimamos que cada grado adicional aumenta la demanda entre 1.8 y 2.5 MWh, con 95% de confianza.

## Pruebas comunes

### t-test

Compara medias entre dos grupos.

Ejemplo: consumo promedio antes vs despues de una intervencion.

### ANOVA

Compara medias entre mas de dos grupos.

Ejemplo: demanda promedio por tipo de cliente.

### Regresion lineal

Modelo base para cuantificar relaciones:

```text
y = beta0 + beta1*x1 + beta2*x2 + error
```

En energia:

```text
demanda = beta0 + beta1*temperatura + beta2*dia_semana + beta3*precio + error
```

## Validacion y limites

Antes de creer un resultado:

- Revisa outliers.
- Revisa sesgo de muestreo.
- Revisa si hay leakage temporal.
- Revisa supuestos de independencia.
- Revisa si el efecto es relevante en negocio, no solo estadisticamente significativo.

## Errores comunes

- Confundir correlacion con causalidad.
- Usar random split en datos temporales.
- Reportar solo el promedio y ocultar dispersion.
- Creer que p < 0.05 vuelve verdadera una conclusion.
- Ignorar cambios estructurales: pandemia, regulaciones, shocks de mercado.

## Frase profesional

"El resultado es estadisticamente significativo, pero debemos revisar si el tamano del efecto justifica una decision operativa."

