# CRDO — Plan de ejecución (gestor-de-ejecucion)

**Fecha:** 2026-11-27 · **Datos:** barras diarias de IBKR · **Cálculos:** `scripts/tecnico.py`

## Paso 0 — Fotografía técnica

| Indicador | Valor actual | Lectura rápida |
| :--- | :--- | :--- |
| Precio | $106,80 (cierre 25-nov); $112,07 en la sesión del 27-nov | Rebote tras una mecha en $93,28 |
| Rango 52 semanas | Máximo $308,67 / mínimo $86,48 (mar-2026) | −65,4 % desde máximos |
| EMA 21 | $130,64 (−18,3 %) | Precio por debajo |
| SMA 50 / 150 / 200 | $164,87 / $200,74 / $180,86 (−35 % / −47 % / −41 %); la SMA 50 cae con fuerza | Bajista |
| ATR(14) | $15,68 (**14,7 %**) | Volatilidad extrema |
| RSI(14) | 38,1 | Débil |
| Volumen | Media de 5 días 5,1M, igual que la media de 50 días | Neutro |
| Short Float | `no disponible` | — |
| Próximos resultados | **1-dic-2026 (confirmado, después del cierre; en 4 días)** | **Riesgo binario de hueco** |

## Paso 1 — Fase y niveles

**Fase 4 (Bajista).** Máximos y mínimos decrecientes desde $308,67 (julio); la SMA 50 cae con fuerza y el precio está por debajo de todas las medias.

Volumen estable, sin capitulación clara; la mecha a $93,28 del 25-nov fue absorbida (cierre en $106,80). Fuerza relativa muy negativa.

| Tipo de nivel | Precio / Zona | Relevancia técnica |
| :--- | :--- | :--- |
| Soporte inmediato | $93-98 | Mínimos del 20-nov ($97,92) y del 25-nov ($93,28) |
| Soporte estructural | $86,5 | Mínimo de 52 semanas (mar-2026) |
| Resistencia inmediata | $118-131 | Máximos del 23-nov ($126,72) y EMA 21 ($130,64) |
| Pivote de confirmación | $148 | Máximo del rebote del 13-nov ($148,19) |

## Paso 2 — Escenarios

| Escenario | Condición exacta de activación | Zona de entrada | Stop | Distancia al stop |
| :--- | :--- | :--- | :--- | :--- |
| A. Recuperación del pivote (después de resultados) | Cierre > $148 con volumen > 7,7M (1,5x la media) | $148-155 | $118 | 20,3 % |
| B. Base después de resultados | Tras el 1-dic, $93 aguanta y hay un cierre semanal > $126 | $126-132 (tramo reducido) | $92 | ≈ 27 % |
| C. Espera (vigente) | Fase 4 y resultados en 4 días | Sin entrada | — | — |

ATR del 14,7 % y resultados en menos de 14 días: no se activa capital antes del 1-dic.

## Paso 3 — Sizing

**Perfil:** Crecimiento estructural (rentable y sin deuda), penalizado por la concentración y por una volatilidad extrema.

| Parámetro de riesgo | Propuesta concreta | Justificación |
| :--- | :--- | :--- |
| Peso máximo | **4 %** | Por debajo del rango de crecimiento (5-8 %) por el ATR del 14,7 % y el cliente del 33 % |
| Riesgo por operación | 0,75 % del capital | Con un stop del 20,3 %: 0,75 / 20,3 ≈ 3,7 % |
| Tramos | 50 % en el escenario A o B y 50 % al recuperar la SMA 50 | Prohibido promediar a la baja |
| Salida | Stop a punto muerto a +1,5R | — |

## Paso 4 — Encaje en la cartera del usuario

- Posición: 15 acciones, ≈ 1.501 € (**7,3 %**), precio medio ≈ $119 (−7,73 %).
- **Sobreponderación de 1,8 veces** el peso máximo (4 %), con resultados en 4 días y un ATR del 14,7 %: un hueco del ±25 % movería la cartera ≈ ±1,8 %.
- Correlación con NVDA y AVGO (mismos hiperescaladores).
- **Stop de tesis frente a stop técnico:** de las ocho posiciones es, junto con NVDA, la única con margen de seguridad positivo frente al escenario base (+15 %). Opciones de gestión del riesgo:
  1. Reducir hacia el 4-5 % (≈ 8-10 acciones) antes del 1-dic para limitar el riesgo de hueco.
  2. Mantener las 15 aceptando el riesgo binario, con salida total si cierra por debajo de $86,5 (mínimo de 52 semanas).

  No añadir antes de resultados.

## Paso 5 — Veredicto

**No operable técnicamente ahora (Fase 4 / sin base).**

Alertas:
1. **Activación:** cierre > $148 con volumen > 7,7M.
2. **Invalidación:** cierre < $93 (aviso) y < $86,5 (ruptura estructural).
3. **Calendario:** 1-dic-2026, después del cierre (resultados del Q2 FY27 y guía del Q3).

Plan estrictamente formativo; no constituye recomendación de inversión personalizada.

## Paso 6 — Registro

Google Sheets, fila 10 (precio $106,80, margen +15,13 %, distancia al stop 20,27 %, modelo Claude) y `seguimiento/Seguimiento Análisis de Acciones.xlsx`.
