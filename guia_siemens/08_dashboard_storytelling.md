# 08 Dashboards y storytelling analitico

## Objetivo

Un dashboard no debe ser una galeria de graficas. Debe ayudar a tomar decisiones.

## Estructura recomendada

1. Resumen ejecutivo.
2. KPIs principales.
3. Tendencias y drivers.
4. Escenarios.
5. Riesgos.
6. Supuestos y limitaciones.

## KPIs para energia

- demanda promedio;
- demanda pico;
- costo esperado;
- percentil 95 de costo;
- probabilidad de exceder capacidad;
- emisiones estimadas;
- ahorro potencial;
- downtime esperado;
- energia no servida.

## Visualizaciones utiles

- Line chart para series temporales.
- Fan chart para intervalos de forecast.
- Histograma para resultados Monte Carlo.
- Boxplot para comparar escenarios.
- Heatmap para demanda por hora y dia.
- Tornado chart para sensibilidad.
- Scatter risk-return para portafolios.

## Storytelling de incertidumbre

Una buena narrativa:

```text
1. Que observamos.
2. Que creemos que lo explica.
3. Que puede pasar.
4. Que tan riesgoso es.
5. Que decision recomendamos.
6. Que supuestos deben monitorearse.
```

## Plantilla de conclusion ejecutiva

```text
Bajo el escenario base, estimamos [resultado central].
El principal driver es [variable].
El riesgo relevante aparece en [percentil/escenario].
La recomendacion es [accion].
Esta conclusion depende de [supuestos].
```

## Errores comunes

- Mostrar demasiadas graficas.
- No explicar unidades.
- Ocultar incertidumbre.
- Usar colores sin significado.
- No distinguir historico, forecast y escenario.
- No indicar fecha de actualizacion.
- Hacer dashboards bonitos pero no accionables.

## Regla practica

Si alguien no puede responder "que decision tomo con esto?" despues de ver el dashboard, el dashboard todavia no esta terminado.

