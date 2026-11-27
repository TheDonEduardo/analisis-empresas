# MELI — Plan de ejecución (gestor-de-ejecucion)

**Fecha:** 2026-11-27 · **Datos:** barras diarias de IBKR (`2026-11-27-barras-ibkr.json`, 251 sesiones hasta el 27-nov) · **Cálculos:** `scripts/tecnico.py` · **Estado:** Vigilancia (no está en cartera)

## Paso 0 — Fotografía técnica

| Indicador | Valor actual | Lectura rápida |
| :--- | :--- | :--- |
| Precio | $1.532,92 (cierre 27-nov-2026, sesión corta) | +4,5 % en el día con hueco alcista ($1.550 en la apertura) |
| Rango 52 semanas | Máximo $2.342 (ene-2026) / mínimo $1.333,54 (20-nov-2026) | −34,5 % desde máximos; +15 % desde el mínimo en 5 sesiones |
| EMA 21 | $1.521,10 (+0,8 %) | Recuperada por primera vez |
| SMA 50 | $1.679,39 (−8,7 %); hace 20 sesiones: $1.846,58 | Cae con fuerza |
| SMA 150 / 200 | $1.746,64 / $1.755,55 (−12,2 % / −12,7 %); ambas descendentes | Bajista |
| ATR(14) | $65,24 (4,3 %) | Volatilidad moderada |
| RSI(14) | 48,0 | Neutral, saliendo de la debilidad |
| Volumen | Media de 5 días 0,5M frente a 0,4M de media en 50 días | Algo de acumulación en el rebote |
| Short Float / Days to Cover | ≈ 1,5-2,0 % / ≈ 1-2 días (30-jun y 30-sep-2026, fuentes dispares) | Bajo: sin combustible de short squeeze |
| Próximos resultados | Q4 2026 ≈ finales de feb-2027 (`no disponible`) | Más de 14 días |

## Paso 1 — Fase y niveles

**Fase 4 (Bajista) con base incipiente.** Máximos decrecientes desde $2.342 (enero) y medias descendentes. Pero hay un doble suelo en $1.333-1.355 (20 y 23-nov), un rebote del +15 % y la EMA 21 recuperada. Aún no hay un mínimo creciente semanal confirmado.

Volumen: el hueco bajista del 5-nov (resultados del Q3; de $1.739,88 a $1.530,28) dejó un hueco sin cubrir entre $1.610 y $1.740. El rebote actual llega con volumen por encima de la media. Interés corto bajo (≈ 2 %).

| Tipo de nivel | Precio / Zona | Relevancia técnica |
| :--- | :--- | :--- |
| Soporte inmediato | $1.460-1.470 | Consolidación del 12-19 de noviembre |
| Soporte estructural | $1.333,5 | Mínimo de 52 semanas y doble suelo de noviembre; valor pesimista del DCF en $726 (lejos) |
| Resistencia inmediata | $1.555-1.610 | Máximo del 27-nov ($1.554,50) y borde inferior del hueco del 5-nov |
| Pivote de confirmación | $1.680 | SMA 50 ($1.679) y mitad del hueco bajista del 5-nov |

## Paso 2 — Escenarios

| Escenario | Condición exacta de activación | Zona de entrada | Stop | Distancia al stop |
| :--- | :--- | :--- | :--- | :--- |
| A. Recuperación del pivote (principal) | Cierre > $1.680 con volumen > 600K (1,5x la media) | $1.680-1.740 (máximo aceptable: $1.750) | $1.540 | 8,3 % |
| B. Pullback con mínimo creciente | Retroceso ordenado a $1.460-1.500 con volumen menor, mínimo por encima de $1.420 y cierre semanal > $1.530 | $1.470-1.510 (tramo reducido, 50 %) | $1.400 | ≈ 5,4 % (≈ 1,1 ATR; tamaño reducido) |
| C. Espera | Ni A ni B; o un cierre < $1.420 que reabre la Fase 4 | Sin entrada | — | — |

Anti-FOMO: no se compra el hueco alcista del 27-nov ($1.550) sin pullback ni ruptura del pivote.

## Paso 3 — Sizing

**Perfil:** Crecimiento estructural (rentable, con riesgo de crédito y divisas de LatAm).

| Parámetro de riesgo | Propuesta concreta | Justificación |
| :--- | :--- | :--- |
| Peso máximo | **5 %** (≈ 1.035 € sobre ≈ 20.694 €; menos de 1 acción a ≈ $1.533, así que haría falta comprar fracciones) | Extremo inferior del rango de crecimiento por el riesgo de crédito y de LatAm |
| Riesgo máximo por operación | 0,75 % del capital (≈ 155 €) | Con un stop del 8,3 %, el tamaño posible sería ≈ 9 %, limitado al 5 % (riesgo efectivo ≈ 0,4 %) |
| Tramos | 50 % en el escenario B (o A) y 50 % al confirmar el pivote de $1.680 o cerrar por encima de la SMA 200 (≈ $1.755) | Prohibido promediar a la baja por debajo de $1.420 |
| Salida | Stop a punto muerto a +1,5R (≈ $1.890 desde la entrada A); después, stop dinámico bajo la EMA 21 | El hueco de $1.610-1.740 se cubre en el camino |

## Paso 4 — Encaje en la cartera del usuario

- MELI **no está en cartera**. La cartera actual (≈ 20.694 €) tiene el 85,7 % en infraestructura de IA y el 14,3 % en especulativas.
- **Mejora la diversificación:** comercio electrónico y fintech en LatAm, con baja correlación directa con el ciclo de Capex de IA. Es, además, la mejor relación valor/calidad analizada (margen del +39 % frente al base).
- **Coste de oportunidad:** con todas las posiciones por encima de su peso máximo, entrar en MELI tiene más sentido **financiado con la reducción** de las posiciones priorizadas en el resumen de cartera (ORCL → RKLB → OKLO), no con dinero nuevo que aumente la exposición total.
- Verificaciones antes de la orden: (1) que el bróker permita comprar fracciones de acción; (2) el tipo de cambio EUR/USD y las comisiones sobre una orden pequeña.

## Paso 5 — Veredicto

**En lista de vigilancia (esperar gatillo).** Fase 4 con base incipiente (doble suelo y EMA 21 recuperada) y valoración muy atractiva. Falta el gatillo A o B.

Alertas:
1. **Activación:** cierre > $1.680 con volumen > 600K.
2. **Pullback y soporte:** precio en $1.460-1.500 (zona de B); cierre < $1.420 (B invalidado) y < $1.333 (ruptura estructural).
3. **Calendario:** resultados del Q4 2026 (≈ finales de feb-2027): morosidad de 15-90 días, NIMAL y margen operativo.

Plan estrictamente formativo; no constituye recomendación de inversión personalizada.

## Paso 6 — Registro

Google Sheets, fila 17: K-M, O-R actualizadas (Fase 4, entrada $1.680, stop $1.540, peso 5 %, Lista de vigilancia, Claude). Las fórmulas calculan una distancia al stop del 8,33 %. Respaldo en `seguimiento/Seguimiento Análisis de Acciones.xlsx`.
