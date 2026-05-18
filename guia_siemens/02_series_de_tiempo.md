# 02 Series de tiempo y forecasting

## Que es una serie de tiempo

Una serie de tiempo es una variable observada en orden temporal:

- demanda electrica por hora;
- precios diarios de energia;
- carga de flotillas electricas;
- temperatura;
- trafico de un centro de datos;
- precio de un activo financiero.

La diferencia contra datos normales es que el orden importa.

## Componentes principales

### Tendencia

Movimiento persistente hacia arriba o abajo.

### Estacionalidad

Patrones repetidos:

- horas pico;
- fines de semana;
- verano/invierno;
- cierre de mes;
- ciclos anuales.

### Ruido

Variacion no explicada.

### Autocorrelacion

Relacion entre el valor actual y valores pasados.

## Estacionariedad

Una serie estacionaria tiene media, varianza y estructura de autocorrelacion relativamente estables en el tiempo.

Muchos modelos clasicos como ARIMA funcionan mejor con series estacionarias.

Tecnicas para acercarse a estacionariedad:

- diferencias;
- log transform;
- remover tendencia;
- remover estacionalidad;
- usar retornos en vez de precios.

## Modelos clasicos

### Naive forecast

Predice que el siguiente valor sera igual al ultimo.

Sirve como baseline. Si tu modelo complejo no le gana, algo anda mal.

### Media movil

Promedia los ultimos n periodos. Simple, interpretable y util como referencia.

### ARIMA

Combina:

- AR: autoregression, dependencia de valores pasados.
- I: integration, diferenciacion.
- MA: moving average, dependencia de errores pasados.

Notacion:

```text
ARIMA(p, d, q)
```

### SARIMA

ARIMA con estacionalidad:

```text
SARIMA(p,d,q)(P,D,Q,s)
```

Muy relevante en energia porque la demanda suele tener patrones diarios, semanales y anuales.

### VAR

Vector Autoregression. Modela varias series juntas.

Ejemplo:

- demanda;
- precio;
- temperatura;
- carga de EVs.

### GARCH

Modela volatilidad cambiante en el tiempo. Muy usado en finanzas para retornos, riesgo y derivados.

## Modelos modernos

### Prophet

Bueno para datos de negocio con tendencia, estacionalidades y festivos.

### Machine Learning supervisado

Convertimos la serie en tabla:

- lags;
- medias moviles;
- dia de semana;
- mes;
- temperatura;
- precio;
- festivos.

Luego usamos modelos como Random Forest, XGBoost o regresion regularizada.

## Validacion correcta

Nunca uses random train-test split si el problema es temporal.

Usa:

- train en pasado, test en futuro;
- walk-forward validation;
- rolling window;
- expanding window.

## Metricas

| Metrica | Interpretacion |
|---|---|
| MAE | error promedio absoluto |
| RMSE | penaliza mas errores grandes |
| MAPE | error porcentual, cuidado con valores cercanos a cero |
| Bias | si el modelo sobreestima o subestima sistematicamente |

## Pipeline practico

1. Ordenar por fecha.
2. Revisar frecuencia y datos faltantes.
3. Visualizar la serie.
4. Descomponer tendencia y estacionalidad.
5. Crear baseline.
6. Entrenar modelos.
7. Validar temporalmente.
8. Analizar residuos.
9. Reportar incertidumbre, no solo punto estimado.

## Preguntas para Siemens

- Cual es el horizonte de forecast: horas, dias, meses?
- El costo de sobreestimar y subestimar es igual?
- Hay variables externas disponibles: clima, calendario, precios, ocupacion?
- El modelo necesita explicabilidad o solo precision?
- Se requiere intervalo de prediccion?

