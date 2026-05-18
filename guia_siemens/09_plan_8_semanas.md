# Plan de estudio de 8 semanas

## Semana 1: estadistica, probabilidad y Python numerico

Objetivo: reforzar los fundamentos que aparecen en casi todos los modelos.

Temas:

- Variables aleatorias.
- Esperanza, varianza, covarianza y correlacion.
- Distribuciones normal, lognormal, binomial, poisson y exponencial.
- Intervalos de confianza.
- p-values y pruebas de hipotesis.
- t-test, ANOVA y regresion lineal.

Entregable:

- Notebook con simulaciones de distribuciones.
- Mini reporte: diferencia entre correlacion, causalidad y significancia estadistica.

## Semana 2: series de tiempo clasicas

Objetivo: aprender a diagnosticar y modelar datos temporales.

Temas:

- Tendencia, estacionalidad y ruido.
- Estacionariedad.
- Autocorrelacion y partial autocorrelation.
- AR, MA, ARIMA y SARIMA.
- Train-test split temporal.

Entregable:

- Forecast simple de una serie energetica o simulada.
- Comparacion entre naive forecast, media movil y ARIMA.

## Semana 3: forecasting moderno y validacion

Objetivo: construir modelos utiles con variables externas.

Temas:

- Prophet.
- Regresion con features de calendario.
- XGBoost o Random Forest para forecasting supervisado.
- Walk-forward validation.
- MAE, RMSE, MAPE y bias.

Entregable:

- Modelo que use temperatura, calendario y rezagos para predecir demanda.

## Semana 4: procesos estocasticos

Objetivo: entender como evoluciona una variable aleatoria en el tiempo.

Temas:

- Cadenas de Markov.
- Matrices de transicion.
- Random walk.
- Brownian motion.
- Geometric Brownian Motion.

Entregable:

- Simulador de estados de demanda: baja, normal, alta, critica.
- Simulador de precios con GBM.

## Semana 5: Monte Carlo

Objetivo: generar y analizar miles de escenarios.

Temas:

- Muestreo aleatorio.
- Simulacion de paths.
- Percentiles y escenarios extremos.
- VaR.
- Antithetic variates y control variates.

Entregable:

- Simulacion de costos energeticos bajo incertidumbre de demanda y precio.

## Semana 6: opciones, Black-Scholes y Greeks

Objetivo: entender pricing de derivados con formula cerrada y simulacion.

Temas:

- Calls y puts.
- Intrinsic value y time value.
- Risk-neutral pricing.
- Black-Scholes.
- Delta, Gamma, Vega, Theta y Rho.
- Monte Carlo para opciones europeas.

Entregable:

- Comparar precio Black-Scholes vs Monte Carlo.
- Sensibilidad del precio ante volatilidad y tiempo.

## Semana 7: portafolios y riesgo

Objetivo: optimizar combinaciones de activos y medir exposicion.

Temas:

- Retorno esperado.
- Matriz de covarianza.
- Volatilidad de portafolio.
- Frontera eficiente.
- Sharpe ratio.
- VaR y expected shortfall.

Entregable:

- Frontera eficiente con activos simulados o reales.

## Semana 8: proyecto end-to-end

Objetivo: unir forecasting, simulacion, riesgo y comunicacion.

Proyecto sugerido:

"Evaluacion de riesgo energetico para una flotilla electrica o centro de datos".

Debe incluir:

- Limpieza o generacion de datos.
- EDA.
- Forecast de demanda.
- Simulacion Monte Carlo.
- Escenarios optimista, base y estres.
- KPIs.
- Recomendaciones.
- Limitaciones.

Entregable final:

- Notebook.
- Script reproducible.
- Resumen ejecutivo de una pagina.
- Dashboard o visualizaciones clave.

