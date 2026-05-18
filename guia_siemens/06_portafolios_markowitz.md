# 06 Portafolios y Markowitz

## Objetivo

Markowitz busca construir portafolios que balanceen retorno esperado y riesgo.

La idea central:

```text
no importa solo el riesgo de cada activo, sino como se mueven juntos.
```

## Retorno de portafolio

Si tienes pesos w y retornos esperados mu:

```text
E[R_p] = w' * mu
```

## Riesgo de portafolio

Con matriz de covarianza Sigma:

```text
Var(R_p) = w' * Sigma * w
```

La volatilidad es la raiz cuadrada de la varianza.

## Diversificacion

Si dos activos no estan perfectamente correlacionados, combinarlos puede reducir riesgo.

## Frontera eficiente

Conjunto de portafolios que ofrecen el mayor retorno esperado para cada nivel de riesgo, o el menor riesgo para cada nivel de retorno.

## Sharpe ratio

Mide retorno excedente por unidad de riesgo:

```text
Sharpe = (retorno_portafolio - tasa_libre_riesgo) / volatilidad
```

## Aplicacion practica

Pasos:

1. Obtener precios historicos.
2. Calcular retornos.
3. Estimar retorno esperado.
4. Estimar matriz de covarianza.
5. Simular u optimizar pesos.
6. Calcular retorno, volatilidad y Sharpe.
7. Visualizar frontera eficiente.

## Limitaciones

- Retornos esperados son dificiles de estimar.
- Covarianzas cambian en el tiempo.
- Sensible a outliers.
- Supone relaciones lineales.
- Puede generar pesos extremos.

Mejoras modernas:

- regularizacion de covarianza;
- constraints en pesos;
- risk parity;
- Black-Litterman;
- robust optimization;
- escenarios Monte Carlo.

## Relacion con energia

Aunque Markowitz viene de finanzas, la logica aplica a portafolios de riesgo:

- fuentes energeticas;
- contratos;
- proveedores;
- tecnologias;
- escenarios de demanda;
- estrategias de cobertura.

La pregunta cambia de "activos financieros" a "combinaciones de exposiciones".

## Frase profesional

"La optimizacion sugiere una combinacion atractiva, pero la recomendacion depende de la estabilidad de la matriz de covarianza y de restricciones reales del negocio."

