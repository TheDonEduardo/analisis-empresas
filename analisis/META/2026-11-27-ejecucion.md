# META — Plan de ejecución (gestor-de-ejecucion)

**Fecha:** 2026-11-27 · **Datos:** barras diarias de IBKR · **Cálculos:** `scripts/tecnico.py`

## Paso 0 — Fotografía técnica

| Indicador | Valor actual | Lectura rápida |
| :--- | :--- | :--- |
| Precio | $609,89 (cierre 25-nov); $625,49 en la sesión del 27-nov | Rebote |
| Rango 52 semanas | Máximo $779,82 / mínimo $520,26 | −21,8 % desde máximos |
| EMA 21 | $620,58 (−1,7 %) | Muy cerca |
| SMA 50 | $672,42 (−9,3 %) | Girando a la baja |
| SMA 150 / 200 | $626,80 / $627,53 (−2,7 % / −2,8 %); la SMA 200 baja levemente (hace 20 sesiones: $632,14) | Planas o cayendo |
| ATR(14) | $25,35 (4,2 %) | Volatilidad moderada |
| RSI(14) | 45,7 | Neutral |
| Volumen | Media de 5 días 11,0M frente a 13,3M de media en 50 días | Sin presión |
| Short Float | `no disponible` | — |
| Próximos resultados | Finales de ene-2027 (`no disponible` exacto) | Más de 14 días |

## Paso 1 — Fase y niveles

**Fase 3 (Techo / Distribución).** Subida hasta $779,82 en septiembre y vuelta por debajo de las SMA 150/200, que se aplanan. Rango amplio de $520-780 durante todo 2026.

Volumen sin distribución agresiva. La fuerza relativa ha sido negativa desde septiembre.

| Tipo de nivel | Precio / Zona | Relevancia técnica |
| :--- | :--- | :--- |
| Soporte inmediato | $558-568 | Mínimos del 20-nov ($558,68) y del 25-nov ($567,75) |
| Soporte estructural | $520-525 | Mínimos de 52 semanas (marzo y agosto) |
| Resistencia inmediata | $627-648 | SMA 150/200 y máximos de mediados de noviembre ($648,45) |
| Pivote de confirmación | $650 | Recuperación del cluster de medias y de los máximos de noviembre |

## Paso 2 — Escenarios

| Escenario | Condición exacta de activación | Zona de entrada | Stop | Distancia al stop |
| :--- | :--- | :--- | :--- | :--- |
| A. Recuperación del pivote | Cierre > $650 con volumen > 20M (1,5x la media) | $650-670 | $610 | 6,2 % |
| B. Pullback a soporte | Prueba de $558-570 con vela de giro y volumen menor | $565-580 | $518 | ≈ 9 % |
| C. Espera (vigente) | Precio entre $570 y $650 sin gatillo | Sin entrada | — | — |

## Paso 3 — Sizing

**Perfil:** Crecimiento estructural (negocio de calidad; Capex y litigios elevan el riesgo).

| Parámetro de riesgo | Propuesta concreta | Justificación |
| :--- | :--- | :--- |
| Peso máximo | **8 %** | Extremo superior del rango de crecimiento (5-8 %) por la calidad del negocio publicitario |
| Riesgo por operación | 0,75 % del capital | Con un stop del 6,2 %, el tamaño máximo sería 12 %; limitado al 8 % |
| Tramos | 50 % en el escenario A o B y 50 % al confirmar por encima de la SMA 50 | Prohibido promediar a la baja |
| Salida | Stop a punto muerto a +1,5R; después, stop dinámico bajo la EMA 21 | — |

## Paso 4 — Encaje en la cartera del usuario

- Posición: 6 acciones, ≈ 3.345 € (**16,2 %**), precio medio ≈ $623 (−1,7 %).
- **Sobreponderación de 2 veces** el peso máximo (8 %). Junto con MSFT (21,6 %), concentra el 37,8 % de la cartera en dos megacaps de IA y publicidad o nube.
- **Stop de tesis frente a stop técnico:** la tesis es sólida, y el precio está un 21 % por encima del base del contrato, pero dentro de la sensibilidad (con WACC 8 % = $612). Opciones de gestión del riesgo:
  1. Reducir hacia el 8-10 % (≈ 3-4 acciones) en un rebote a la zona $640-650.
  2. Mantener las 6 con salida si cierra por debajo de $558 (rotura del soporte de noviembre).

  No añadir: la posición ya supera el máximo.

## Paso 5 — Veredicto

**En lista de vigilancia (esperar gatillo).** Fase 3, no Fase 4.

Alertas:
1. **Activación:** cierre > $650 con volumen > 20M.
2. **Soporte crítico:** cierre < $558 (aviso) y < $520 (ruptura estructural: Fase 4).
3. **Calendario:** resultados del Q4 2026 y guía de Capex de 2027 (finales de ene-2027); apelación de Nuevo México; juicios juveniles.

Plan estrictamente formativo; no constituye recomendación de inversión personalizada.

## Paso 6 — Registro

Google Sheets, fila 8 (precio $609,89, margen −21,12 %, distancia al stop 6,15 %) y `seguimiento/Seguimiento Análisis de Acciones.xlsx`.
