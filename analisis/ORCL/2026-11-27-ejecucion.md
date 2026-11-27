# ORCL — Plan de ejecución (gestor-de-ejecucion)

**Fecha:** 2026-11-27 · **Datos:** barras diarias de IBKR (250 sesiones, `2026-11-27-barras-ibkr.json`) · **Cálculos:** `scripts/tecnico.py`

## Paso 0 — Fotografía técnica

| Indicador | Valor actual | Lectura rápida |
| :--- | :--- | :--- |
| Precio | $103,88 (cierre 25-nov); $108,68 en la sesión del 27-nov | Rebote desde mínimos |
| Rango 52 semanas | Máximo $250,25 / mínimo $99,34 (25-nov) | −58,5 % desde máximos |
| EMA 21 | $118,05 (−12,0 %) | Precio por debajo |
| SMA 50 | $130,11 (−20,2 %); hace 20 sesiones: $142,11 | Cae con fuerza |
| SMA 150 / SMA 200 | $151,88 / $152,44 (−31,6 % / −31,9 %); ambas descendentes | Tendencia bajista |
| ATR(14) | $8,52 (8,2 %) | Volatilidad extrema |
| RSI(14) | 37,7 | Débil |
| Volumen | Media de 5 días 21,8M frente a 20,9M de media en 50 días | Sin capitulación clara |
| Short Float / Days to Cover | `no disponible` | — |
| Próximos resultados | Q2 FY27: 9-14 dic-2026 (sin confirmar) | **Menos de 14 días: riesgo binario de hueco** |

## Paso 1 — Fase y niveles

**Fase 4 (Bajista).** Máximos y mínimos decrecientes desde septiembre ($250); todas las medias caen; nuevo mínimo anual el 25-nov.

Volumen: sin pico de capitulación; la distribución sigue constante. La fuerza relativa es muy negativa (−58 % frente a un mercado lateral). El interés corto es `no disponible`.

| Tipo de nivel | Precio / Zona | Relevancia técnica |
| :--- | :--- | :--- |
| Soporte inmediato | $99,3-100 | Mínimo anual del 25-nov y cifra redonda |
| Soporte estructural | `no disponible` por debajo de $99 (precios de 2023-24 sin datos en esta sesión); valor ponderado del DCF en $88 | — |
| Resistencia inmediata | $112-118,7 | Máximo del 23-nov ($118,70) y EMA 21 ($118,05) |
| Pivote de confirmación | $130,80 | Máximo del 13-nov y SMA 50 ($130,1) |

## Paso 2 — Escenarios

| Escenario | Condición exacta de activación | Zona de entrada | Stop | Distancia al stop |
| :--- | :--- | :--- | :--- | :--- |
| A. Recuperación del pivote (solo después de resultados) | Cierre > $130,80 con volumen > 31M (1,5x la media), después del Q2 FY27 | $130,8-136 | $112,00 | 14,4 % |
| B. Base después de resultados | Tras el Q2, mínimo creciente sobre $99 y cierre semanal > $118,70 | $115-119 (tramo reducido) | $98,00 | ≈ 15 % |
| C. Espera (vigente) | Fase 4 y resultados en menos de 14 días | Sin entrada | — | — |

## Paso 3 — Sizing

**Perfil:** Especulativo / Binario (FCF negativo, apalancamiento, dilución y contraparte única).

| Parámetro de riesgo | Propuesta concreta | Justificación |
| :--- | :--- | :--- |
| Peso máximo en cartera | **3 %** | Rango especulativo (2-4 %) |
| Riesgo máximo por operación | 0,5 % del capital | Con un stop del 14,4 %, el tamaño máximo es 0,5 / 14,4 ≈ 3,5 %, limitado al 3 % |
| Tramos | 50 % en el escenario A o B y 50 % al recuperar la SMA 200 (≈ $152) | Prohibido promediar a la baja |
| Salida | Stop a punto muerto a +1,5R; después, stop dinámico bajo la EMA 21 | — |

## Paso 4 — Encaje en la cartera del usuario (27-nov-2026)

- Posición: 30 acciones, ≈ 2.890 € (**14,0 %** de la cartera), precio medio ≈ $133,8 (−20,95 %).
- **Sobreponderación de 4,7 veces** el peso máximo especulativo (3 %), con resultados en menos de 14 días. Un hueco del −15/−20 % en los resultados restaría ≈ 2-3 % a la cartera.
- Correlación: ORCL comparte riesgo con NVDA (OpenAI es cliente y deudor de las dos) y con MSFT, META, AVGO y CRDO (85,7 % de la cartera en IA).
- **Stop de tesis frente a stop técnico:** el DCF sitúa el valor base ($83) y el ponderado ($88) por debajo del precio, y el gráfico está en Fase 4. No hay argumento ni fundamental ni técnico para mantener el 14 %. Opciones de gestión del riesgo:
  1. Reducir hacia el 3-4 % (≈ 6-9 acciones) antes de los resultados, aprovechando rebotes hacia $112-118.
  2. Mantener con salida total si cierra por debajo de $99, sabiendo que un hueco puede saltarse el stop.

  Nunca añadir hasta que se active el escenario A o B.

## Paso 5 — Veredicto

**No operable técnicamente ahora (Fase 4 / sin base).**

Alertas:
1. **Activación:** cierre > $130,80 con volumen > 31M (después de resultados).
2. **Invalidación:** cierre < $99 (rotura del mínimo anual).
3. **Calendario:** resultados del Q2 FY27, 9-14 dic-2026 (confirmar en investor.oracle.com); cualquier acción de S&P o Moody's sobre el rating.

Plan estrictamente formativo; no constituye recomendación de inversión personalizada.

## Paso 6 — Registro

- Google Sheets, fila 5: ORCL registrada. Las fórmulas F, J y N quedan intactas: precio $103,88, margen −24,63 %, distancia al stop 14,37 %.
- Respaldo local: `seguimiento/Seguimiento Análisis de Acciones.xlsx`.
