# NVDA — Plan de ejecución (gestor-de-ejecucion)

**Fecha:** 2026-11-27 · **Cadena:** paso 3 de 3 · **Datos:** barras diarias de IBKR (250 sesiones hasta el 25-nov-2026), cálculos en `2026-11-27-tecnico.py`

## Paso 0 — Fotografía técnica

| Indicador | Valor actual | Lectura rápida |
| :--- | :--- | :--- |
| Precio | $149,30 (cierre 25-nov-2026); $155,26 en la sesión del 27-nov (IBKR, en tiempo real) | Rebote débil tras la caída |
| Rango 52 semanas | Máximo $243,37 / mínimo $124,51 (20-nov-2026) | −38,7 % desde máximos |
| EMA 21 | $170,82 (−12,6 %) | Precio por debajo |
| SMA 50 | $203,65 (−26,7 %); hace 20 sesiones: $222,07 | Cae con fuerza |
| SMA 150 | $208,95 (−28,5 %) | Precio por debajo |
| SMA 200 | $202,87 (−26,4 %); hace 20 sesiones: $204,14 | Empieza a girar a la baja |
| ATR(14) | $13,34 (8,9 % del precio) | Volatilidad extrema (> 8 %) |
| RSI(14) | 37,5 | Débil, sin sobreventa |
| Volumen | Media de 5 días: 313,4M frente a 120,2M de media en 50 días (2,6x) | Volumen de capitulación y de evento |
| Short Float / Days to Cover | ≈ 1,05 % (StatMuse, sin fecha) / 1-2,5 días (fuentes contradictorias) | Interés corto bajo; datos no actualizados |
| Próximos resultados | Q4 FY27 ≈ 24-feb-2027 (estimado, sin confirmar) | Faltan más de 14 días: sin riesgo binario inmediato |

## Paso 1 — Fase y niveles

**Fase 4 (Bajista).** Máximos y mínimos decrecientes desde $243 (octubre); el precio está por debajo de todas las medias; la SMA 50 cae con fuerza y la SMA 200 empieza a girar.

Dinámica: el volumen de capitulación del 20-nov (441M, mínimo $124,51) fue seguido de una vela de +31,5 % el 23-nov (readmisión de Huang, 462M). La continuación posterior fracasó (−5,9 % y −3,9 %), lo que indica distribución en los rebotes. La fuerza relativa frente al mercado es negativa. El interés corto es bajo (≈ 1 %), así que no hay combustible para un short squeeze: los rebotes dependen de noticias.

| Tipo de nivel | Precio / Zona | Relevancia técnica |
| :--- | :--- | :--- |
| Soporte inmediato | $141-146 | Mínimos del 25-nov ($141,17) y del 19-nov ($145,71) |
| Soporte estructural | $124,5 | Mínimo de capitulación del 20-nov; valoración pesimista en $72 |
| Resistencia inmediata | $165-171,5 | Cierre y máximo del 23-nov, confluencia con la EMA 21 ($170,8) |
| Pivote de confirmación | $171,50 (primera señal) y $203-204 (SMA 200/50, fin de Fase 4) | Cierre por encima con volumen > 1,5x la media |

## Paso 2 — Escenarios sin FOMO

| Escenario | Condición exacta de activación | Zona de entrada | Stop | Distancia al stop |
| :--- | :--- | :--- | :--- | :--- |
| A. Recuperación del pivote (principal) | Cierre diario > $171,50 con volumen > 180M (1,5x la media de 50 días), mantenido 2 sesiones | $171,5-178 (máximo aceptable: $180) | $150,00 | 12,5 % (desde $171,5) |
| B. Doble suelo / base semanal | Nueva prueba de la zona $125-135 con volumen menor que el del 20-nov, seguida de un cierre semanal > $150 | $145-150 (solo un tramo inicial reducido) | $119,00 | ≈ 18 % (desde $145) |
| C. Espera (vigente hoy) | Precio entre $124,5 y $171,5 sin estructura, o cierre < $124,5 | Sin entrada | — | — |

Reglas aplicadas: Fase 4, así que no se compra en caída libre. El ATR del 8,9 % obliga a stops amplios y a compensarlo con un tamaño menor. Los resultados quedan a más de 14 días.

## Paso 3 — Sizing

**Perfil:** Crecimiento estructural (negocio de calidad, penalizado por el riesgo de gobernanza y por la volatilidad).

| Parámetro de riesgo | Propuesta concreta | Justificación |
| :--- | :--- | :--- |
| Peso máximo en cartera | 5 % | Extremo inferior del rango de crecimiento (5-8 %) por la investigación sobre el CEO, los $118B en garantías y un ATR del 8,9 % |
| Riesgo máximo por operación | 0,75 % del capital | Activo volátil. Con un stop del 12,5 %: 0,75 / 12,5 = 6 % del capital, limitado al 5 % (riesgo efectivo ≈ 0,63 %) |
| Política de tramos | 50 % al activarse el escenario A; 50 % al recuperar la SMA 200 (≈ $203) con volumen o en un pullback que respete $171,5 | Prohibido promediar a la baja mientras siga en Fase 4 |
| Gestión de salida | Stop a punto muerto a +1,5R (≈ $203, confluencia con la SMA 200/50); después, stop dinámico bajo la EMA 21 | Proteger beneficios en un activo con ATR alto |

## Paso 4 — Encaje en cartera

No hay datos de cartera en esta conversación. Antes de lanzar una orden, comprueba:
1. **Exposición acumulada a semiconductores e IA.** El repositorio `alpha-portfolio-bot` lista una cartera con AVGO 18 %, NVDA 6 %, MSFT 10 %, GOOGL 12 % y META 7 %. Si esa es tu cartera real, ya tienes más del 50 % en la temática IA y una posición en NVDA (en ese caso, cambia el estado a `En cartera`).
2. **Qué posición saldría** si tu cartera tiene un cupo cerrado de 10 posiciones.

## Paso 5 — Veredicto

**No operable técnicamente ahora (Fase 4 / sin base).** Valoración atractiva (margen del 21 % frente al escenario base), pero sin estructura técnica.

Alertas a programar:
1. **Activación:** cierre diario > $171,50 con volumen > 180M.
2. **Invalidación / soporte:** cierre < $141 (aviso) y < $124,50 (ruptura estructural: no operar).
3. **Calendario:** 8-ene-2027 (plazo de la demanda colectiva) y ≈ 24-feb-2027 (resultados del Q4 FY27; confirmar la fecha en investor.nvidia.com).

Plan estrictamente formativo; no constituye recomendación de inversión personalizada.

## Paso 6 — Registro

- Google Sheets `Seguimiento Análisis de Acciones`, fila 4: NVDA registrada (A-E, G-I, K-M, O-Q). Las fórmulas F, J y N quedan intactas: muestran precio $149,30, margen 21,44 % y distancia al stop 12,54 %.
- Respaldo local: `seguimiento/Seguimiento Análisis de Acciones.xlsx`.
