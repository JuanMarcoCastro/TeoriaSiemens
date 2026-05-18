# Guia de estudio Siemens: Quant, Energy Analytics y Stochastic Modeling

Esta guia esta pensada para prepararte para un internship donde vas a mezclar data science, simulacion, energia y derivados financieros. La idea no es volverte matematico puro en unas semanas, sino darte criterio practico para modelar incertidumbre, validar resultados y comunicar decisiones.

## Objetivo principal

Aprender a convertir datos inciertos en escenarios utiles:

- Que probablemente va a pasar.
- Que podria pasar en casos extremos.
- Que tan confiable es el modelo.
- Que decision recomienda el analisis.
- Que supuestos pueden romper la conclusion.

## Mapa mental del rol

Tu trabajo vive en la interseccion de cuatro areas:

1. Data Science: limpiar datos, analizar patrones, probar hipotesis y visualizar.
2. Forecasting: estimar demanda, precios, consumo, carga y comportamiento futuro.
3. Modelos estocasticos: simular futuros posibles, fallas, shocks y distribuciones.
4. Finanzas cuantitativas: opciones, riesgo, volatilidad, portafolios y cobertura.

## Preguntas que debes poder responder

- Como se comporta historicamente esta variable?
- Hay tendencia, estacionalidad, anomalías o cambios estructurales?
- Que variables explican mejor la demanda, el costo o el riesgo?
- Como valido un modelo si los datos estan ordenados en el tiempo?
- Como genero escenarios futuros razonables?
- Como mido riesgo: percentiles, VaR, expected shortfall, costo esperado?
- Como comparo un metodo cerrado como Black-Scholes contra Monte Carlo?
- Como comunico incertidumbre sin sonar ambiguo?

## Ruta recomendada

1. Fundamentos estadisticos.
2. Series de tiempo y forecasting.
3. Procesos estocasticos.
4. Monte Carlo.
5. Opciones y Black-Scholes.
6. Portafolios y riesgo.
7. Analitica energetica.
8. Dashboards y storytelling.

## Archivos de esta guia

- `01_probabilidad_estadistica.md`: probabilidad, inferencia, testing y regresion.
- `02_series_de_tiempo.md`: ARIMA, SARIMA, validacion temporal y forecasting.
- `03_modelos_estocasticos.md`: Markov, Brownian motion, GBM y simulacion.
- `04_monte_carlo.md`: pipeline practico, variance reduction y analisis de escenarios.
- `05_opciones_black_scholes.md`: calls, puts, pricing, Greeks y limitaciones.
- `06_portafolios_markowitz.md`: retorno, riesgo, frontera eficiente y Sharpe ratio.
- `07_energia_resiliencia.md`: demanda, electrificacion, centros de datos y riesgo energetico.
- `08_dashboard_storytelling.md`: como convertir modelos en decisiones ejecutivas.
- `09_plan_8_semanas.md`: calendario de estudio con entregables.

## Proyectos base

- `proyectos/01_forecast_energia`: simulacion de datos energeticos y forecasting.
- `proyectos/02_monte_carlo_opciones`: Black-Scholes vs Monte Carlo.
- `proyectos/03_markowitz_portafolio`: optimizacion de portafolio.
- `proyectos/04_riesgo_energetico`: simulacion de demanda, fallas y costos.

## Como estudiar

Para cada modulo:

1. Lee la intuicion.
2. Aprende las formulas minimas.
3. Corre o adapta el proyecto.
4. Escribe tres conclusiones ejecutivas.
5. Documenta supuestos y limitaciones.

La habilidad clave no es solo calcular. Es saber decir: "bajo estos supuestos, el resultado esperado es X, pero el riesgo relevante esta en Y".

