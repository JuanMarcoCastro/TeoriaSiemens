# Proyecto 01: Forecast energetico

Objetivo: simular una serie de demanda electrica con tendencia, estacionalidad, temperatura y ruido; despues construir baselines y un modelo de regresion con features temporales.

## Que practicas

- EDA de series de tiempo.
- Features de calendario.
- Lags.
- Train-test split temporal.
- MAE y RMSE.
- Comparacion contra baseline.
- Regresion ridge implementada con `numpy`.

## Como correr

Desde `guia_siemens`:

```bash
python proyectos/01_forecast_energia/forecast_energia.py
```

## Que observar

- Si el modelo mejora contra el naive forecast.
- En que periodos se equivoca mas.
- Si los errores tienen patron temporal.
