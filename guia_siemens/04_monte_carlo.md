# 04 Simulacion Monte Carlo

## Idea central

Monte Carlo usa aleatoriedad para resolver problemas donde el futuro es incierto o la formula exacta es dificil.

En vez de preguntar:

```text
cual sera el costo?
```

preguntas:

```text
como se distribuye el costo bajo miles de futuros posibles?
```

## Pipeline practico

1. Definir variables inciertas.
2. Asignar distribuciones.
3. Definir relaciones entre variables.
4. Simular muchos escenarios.
5. Calcular metricas por escenario.
6. Resumir la distribucion final.
7. Validar sensibilidad a supuestos.

## Ejemplo energetico

Variables:

- demanda diaria;
- precio por MWh;
- probabilidad de falla;
- duracion de outage;
- costo por energia no servida.

Metricas:

- costo esperado;
- percentil 95;
- probabilidad de exceder presupuesto;
- expected shortfall;
- escenarios de estres.

## Ejemplo de opciones

Para una call europea:

1. Simulas muchos precios finales S_T.
2. Calculas payoff:

```text
max(S_T - K, 0)
```

3. Promedias payoffs.
4. Descuentas a valor presente:

```text
precio = exp(-rT) * promedio(payoff)
```

## Analisis de resultados

No reportes solo promedio.

Reporta:

- media;
- mediana;
- desviacion estandar;
- percentil 5;
- percentil 95;
- probabilidad de perder dinero;
- peor 1% de escenarios;
- sensibilidad a supuestos.

## Variance reduction

Tecnicas para estimar mejor con menos simulaciones.

### Antithetic variates

Si usas un shock Z, tambien usas -Z. Reduce ruido en algunas simulaciones.

### Control variates

Usas una variable relacionada cuyo valor esperado conoces para corregir la estimacion.

### Importance sampling

Muestreas mas frecuentemente los escenarios raros que te importan.

## Buenas practicas

- Fija `random_seed` para reproducibilidad.
- Valida unidades.
- Usa distribuciones coherentes con el fenomeno.
- Revisa correlaciones entre variables.
- Separa supuestos, simulacion y visualizacion.
- Haz pruebas con pocos escenarios antes de correr miles.
- Explica por que elegiste cada distribucion.

## Errores comunes

- Asumir independencia cuando no existe.
- Usar normal para variables que no pueden ser negativas.
- Confundir escenario extremo con prediccion.
- Creer que mas simulaciones arreglan malos supuestos.
- No validar contra historia o criterio experto.

## Frase profesional

"El promedio es manejable, pero el percentil 95 excede el umbral operativo; la decision debe basarse en tolerancia al riesgo, no solo en costo esperado."

