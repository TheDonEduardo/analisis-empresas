# AVGO — Plan de ejecución (gestor-de-ejecucion)

**Fecha:** 2026-11-27 · **Datos:** barras diarias de IBKR (`2026-11-27-barras-ibkr.json`) · **Cálculos:** `scripts/tecnico.py`

## Paso 0 — Fotografía técnica

| Indicador | Valor actual | Lectura rápida |
| :--- | :--- | :--- |
| Precio | $300,86 (cierre 25-nov); $313,25 en la sesión del 27-nov | Rebote tras una mecha en $278 |
| Rango 52 semanas | Máximo $495,00 / mínimo $278,00 (25-nov) | −39,2 % desde máximos |
| EMA 21 | $327,67 (−8,2 %) | Precio por debajo |
| SMA 50 | $340,55 (−11,7 %); hace 20 sesiones: $353,91 | Cae |
| SMA 150 / SMA 200 | $376,49 (−20,1 %) / $367,31 (−18,1 %); la SMA 200 está plana (hace 20 sesiones: $367,79) | La de 200 se aplana |
| ATR(14) | $19,99 (6,6 %) | Volatilidad alta |
| RSI(14) | 40,7 | Débil |
| Volumen | Media de 5 días 22,0M frente a 14,4M de media en 50 días (1,5x) | Volumen alto en la caída |
| Short Float / Days to Cover | `no disponible` | — |
| Próximos resultados | **9-dic-2026 (confirmado)** | **Menos de 14 días: riesgo binario** |

## Paso 1 — Fase y niveles

**Fase 4 (Bajista).** Máximos decrecientes desde $495 (agosto); el precio está por debajo de todas las medias y la SMA 50 cae. Matiz: la SMA 200 se aplana y la zona $278-300 ha frenado tres caídas (mar-2026: $289,96; 3-nov: $289,76; 25-nov: mecha a $278 con cierre en $300,86). Es un posible inicio de base, pero sin confirmar.

Volumen alto en la caída del 20-nov (34,5M) y en la mecha del 25-nov: puede haber absorción. Fuerza relativa negativa. Interés corto `no disponible`.

| Tipo de nivel | Precio / Zona | Relevancia técnica |
| :--- | :--- | :--- |
| Soporte inmediato | $290-300 | Tres apoyos en 2026 |
| Soporte estructural | $278 | Mínimo de 52 semanas (mecha del 25-nov) |
| Resistencia inmediata | $324-334 | EMA 21 ($327,7) y máximos del 23-nov ($324,5) |
| Pivote de confirmación | $370 | Máximos del 9-nov y del 19-nov ($369,3-369,8) y SMA 200 ($367) |

## Paso 2 — Escenarios

| Escenario | Condición exacta de activación | Zona de entrada | Stop | Distancia al stop |
| :--- | :--- | :--- | :--- | :--- |
| A. Ruptura del pivote | Cierre > $370 con volumen > 21,6M (1,5x la media) | $370-385 (máximo aceptable: $390) | $324 | 12,4 % |
| B. Base confirmada después de resultados | Tras el 9-dic, la zona $278-300 se mantiene y hay un cierre semanal > $334 | $334-345 (tramo reducido) | $289 | ≈ 13,5 % |
| C. Espera (vigente) | Fase 4 y resultados en 12 días | Sin entrada | — | — |

ATR del 6,6 %: stops por fuera del ruido diario (≈ 2 ATR).

## Paso 3 — Sizing

**Perfil:** Crecimiento estructural (FCF excepcional, con riesgo de concentración y de garantías).

| Parámetro de riesgo | Propuesta concreta | Justificación |
| :--- | :--- | :--- |
| Peso máximo | **6 %** | Rango de crecimiento (5-8 %), penalizado por la concentración en un distribuidor del 50 % |
| Riesgo por operación | 0,75 % del capital | Con un stop del 12,4 %: 0,75 / 12,4 ≈ 6 % |
| Tramos | 50 % en el escenario A o B y 50 % en un pullback que respete el pivote | Prohibido promediar a la baja |
| Salida | Stop a punto muerto a +1,5R; después, stop dinámico bajo la EMA 21 | — |

## Paso 4 — Encaje en la cartera del usuario

- Posición: 10 acciones, ≈ 2.764 € (**13,4 %**), precio medio ≈ $370,6 (−18,1 %).
- **Sobreponderación de 2,2 veces** el peso máximo (6 %), con resultados el 9-dic.
- Correlación: comparte con NVDA y ORCL la exposición a Anthropic y OpenAI y al ciclo de Capex de IA.
- **Stop de tesis frente a stop técnico:** de las tres, es la tesis más sólida (caja real del 46 %), y el precio está cerca del valor razonable ($266-300), no muy por encima. Opciones de gestión del riesgo:
  1. Reducir hacia el 6-8 % (≈ 5 acciones), preferiblemente en rebotes a $324-334 antes de resultados.
  2. Mantener las 10 con salida total si cierra por debajo de $278, sabiendo que un hueco en resultados puede saltarse el stop.

  No añadir hasta que se active el escenario A o B.

## Paso 5 — Veredicto

**No operable técnicamente ahora (Fase 4 / sin base confirmada).**

Alertas:
1. **Activación:** cierre > $370 con volumen > 21,6M.
2. **Invalidación:** cierre < $290 (aviso) y < $278 (ruptura estructural).
3. **Calendario:** 9-dic-2026, después del cierre (resultados Q4 FY26 y guía de IA FY27).

Plan estrictamente formativo; no constituye recomendación de inversión personalizada.

## Paso 6 — Registro

- Google Sheets, fila 6: AVGO registrada. Las fórmulas F, J y N quedan intactas: precio $300,86, margen −13,09 %, distancia al stop 12,43 %.
- Respaldo local: `seguimiento/Seguimiento Análisis de Acciones.xlsx`.
