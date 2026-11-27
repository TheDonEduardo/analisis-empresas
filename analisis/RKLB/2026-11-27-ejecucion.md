# RKLB — Plan de ejecución (gestor-de-ejecucion)

**Fecha:** 2026-11-27 · **Datos:** barras diarias de IBKR · **Cálculos:** `scripts/tecnico.py`

## Paso 0 — Fotografía técnica

| Indicador | Valor actual | Lectura rápida |
| :--- | :--- | :--- |
| Precio | $47,02 (cierre 25-nov); $50,46 en la sesión del 27-nov | Rebote |
| Rango 52 semanas | Máximo $151,00 / mínimo $39,99 | −68,9 % desde máximos |
| EMA 21 | $53,96 (−12,9 %) | Precio por debajo |
| SMA 50 / 150 / 200 | $60,40 / $79,31 / $77,33 (−22 % / −41 % / −39 %), todas cayendo | Bajista |
| ATR(14) | $5,17 (**11,0 %**) | Volatilidad extrema |
| RSI(14) | 39,8 | Débil |
| Volumen | Media de 5 días 12,5M frente a 13,4M de media en 50 días | Neutro |
| Short Float | `no disponible` | — |
| Próximos resultados | Q4 2026 ≈ finales de feb-2027 (`no disponible`) | Más de 14 días |

## Paso 1 — Fase y niveles

**Fase 4 (Bajista).** Máximos y mínimos decrecientes desde $151 (julio). El rebote del 9-nov ($68,26) fracasó y el precio marcó un nuevo mínimo de $42,12 el 25-nov.

| Tipo de nivel | Precio / Zona | Relevancia técnica |
| :--- | :--- | :--- |
| Soporte inmediato | $42-45 | Mínimos del 19-nov ($43,89) y del 25-nov ($42,12) |
| Soporte estructural | $40 | Mínimo de 52 semanas ($39,99, nov-2025) |
| Resistencia inmediata | $50,5-54 | EMA 21 ($53,96) y máximos de noviembre |
| Pivote de confirmación | $64 | Máximo del rebote de noviembre ($63,77-68,26) y SMA 50 ($60,4) |

## Paso 2 — Escenarios

| Escenario | Condición exacta de activación | Zona de entrada | Stop | Distancia al stop |
| :--- | :--- | :--- | :--- | :--- |
| A. Recuperación del pivote | Cierre > $64 con volumen > 20M (1,5x la media) | $64-68 | $52 | 18,8 % |
| B. Doble suelo en $40 | Mantener $40-42 con volumen decreciente y cierre semanal > $54 | $54-56 (tramo reducido) | $41 | ≈ 24 % |
| C. Espera (vigente) | Fase 4 sin base | Sin entrada | — | — |

## Paso 3 — Sizing

**Perfil:** Especulativo / Binario (Neutron sin volar, compra apalancada, dilución).

| Parámetro de riesgo | Propuesta concreta | Justificación |
| :--- | :--- | :--- |
| Peso máximo | **2 %** | Especulativo con ATR del 11 % |
| Riesgo por operación | 0,5 % del capital | Con un stop del 18,8 %: 0,5 / 18,8 ≈ 2,7 %, limitado al 2 % |
| Tramos | 50 % en el escenario A o B y 50 % tras el primer vuelo con éxito de Neutron | Prohibido promediar a la baja |
| Salida | Stop a punto muerto a +1,5R | — |

## Paso 4 — Encaje en la cartera del usuario

- Posición: 43 acciones, ≈ 1.893 € (**9,1 %**), precio medio ≈ $79,3 (−39,07 %).
- **Sobreponderación de 4,5 veces** el peso máximo (2 %). Es la segunda posición especulativa junto a OKLO (5,2 %): un 14,3 % de la cartera en apuestas binarias.
- **Stop de tesis frente a stop técnico:** el DCF del contrato ($11,53 base; $29,91 optimista) queda muy por debajo del precio, y el gráfico está en Fase 4. Opciones de gestión del riesgo:
  1. Reducir hacia el 2-3 % (≈ 10-14 acciones) en rebotes a $50-54.
  2. Mantener como opción de largo plazo con salida si cierra por debajo de $40 (rotura del mínimo de 52 semanas).

  No añadir.

## Paso 5 — Veredicto

**No operable técnicamente ahora (Fase 4 / sin base).**

Alertas:
1. **Activación:** cierre > $64 con volumen > 20M.
2. **Invalidación:** cierre < $42 (aviso) y < $40 (ruptura).
3. **Calendario:** resultados del Q4 2026 (≈ feb-2027), noticias de Neutron (fecha del primer vuelo) y aprobaciones regulatorias de Iridium.

Plan estrictamente formativo; no constituye recomendación de inversión personalizada.

## Paso 6 — Registro

Google Sheets, fila 9 (precio $47,02, margen −307,81 %, distancia al stop 18,75 %, modelo Claude) y `seguimiento/Seguimiento Análisis de Acciones.xlsx`.
