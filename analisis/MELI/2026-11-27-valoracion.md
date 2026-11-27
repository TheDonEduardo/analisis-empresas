# MELI — Valoración (analista-de-valoracion)

**Fecha:** 2026-11-27 · **Modo:** encadenado (contrato de `2026-11-27-tesis.md`, validado por el usuario) · **Cálculos:** `2026-11-27-dcf.py` (importes en $M) · **Estado:** Vigilancia (no está en cartera)

## Paso 0 — Datos

| Dato | Valor | Periodo | Fuente |
| :--- | :--- | :--- | :--- |
| Precio | $1.532,00 | 27-nov-2026 | IBKR |
| Acciones diluidas | ≈ 51M | TTM | Resumen de terceros (s) |
| Capitalización | ≈ $78.132M | — | Cálculo |
| Ventas | 2025 $28.900M (+39 %); Q3 2026 $10.750M (+45 %); 2026e ≈ $40.000M | — | Comunicados |
| EBIT | 2025 $3.200M (11,1 %); Q3 2026 $676M (6,3 %) | — | Comunicados |
| Beneficio neto | 2025 $2.000M (6,9 %); Q3 2026 $448M (4,2 %) | — | Comunicados |
| BPA | Q3 2026 ajustado $8,83 | — | Comunicado Q3 |
| OCF / Capex / FCF | `no disponible` | — | — |
| SBC | `no disponible` | — | — |
| Deuda | ≈ $13.200M sin arrendamientos / $16.150M con arrendamientos (s); deuda neta ≈ $8.030M (s) | 30-sep-2026 | Resúmenes de terceros |
| Caja | Disponible $4.162M; con la restringida, $18.721M (incluye $12.430M de garantías del Banco Central de Brasil) | 30-sep-2026 | 10-Q Q3 |
| Intereses / tasa impositiva | `no disponible` | — | — |
| Consenso BPA | 2026 ≈ $39,44 (Chartmill, 14-nov-2026); 2027 ≈ $61,26 (StockAnalysis, sin fecha) | — | (s) |

**Clasificación:** Crecimiento con beneficios. Con un componente financiero relevante (Mercado Pago), pero no es un banco puro, así que se aplica el DCF.

## Paso 1 — DCF inverso

FCF `no disponible` (además, el crecimiento de la cartera de crédito distorsiona el FCF). Como proxy se usa el beneficio neto de 2025 ($2.000M) frente a la capitalización: **g implícito = 14,5 % anual** durante 10 años. Referencias: ventas +39 % (2025) y +45 % (Q3 2026); consenso de BPA 2026 → 2027 ≈ +55 %. Expectativa **conservadora**.

## Paso 2 — DCF directo (contrato)

Supuestos: Año 0 = 2026e ($40.000M); margen FCFF inicial del 4 % (supuesto propio: el crecimiento del crédito absorbe caja) que converge al objetivo en el Año 5; WACC 9 %; g 2,5 %.
Puente: `EV − deuda neta 8.030 − ajuste extra`. Los $12.430M restringidos no se suman.

| Escenario | Prob. | Ventas A5 / A10 | Margen FCFF | VP flujos | VP valor terminal | EV | Equity | Acciones | **Valor/acción** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Pesimista | 25 % | $65.000M / $85.000M | 5 % | $19.106M | $28.310M (VT 67.019) | $47.416M | $37.386M (−2.000) | 51,5M | **$725,94** |
| Base | 50 % | $90.000M / $150.000M | 9 % | $45.693M | $89.925M (VT 212.885) | $135.618M | $127.588M | 50,5M | **$2.526,49** |
| Optimista | 25 % | $110.000M / $200.000M | 12 % | $73.803M | $159.866M (VT 378.462) | $233.669M | $225.639M | 49,5M | **$4.558,37** |

Ejemplo de auditoría (base, Año 5): $90.000M × 9 % = $8.100M → VP = 8.100 / 1,09^5 = $5.264M. VT = 150.000 × 0,09 × 1,025 / 0,065 = $212.885M → VP = $89.925M.

**Valor esperado ponderado** = 0,25 × 725,94 + 0,50 × 2.526,49 + 0,25 × 4.558,37 = 181,49 + 1.263,25 + 1.139,59 = **$2.584,32**

**Sensibilidad (base):**

| WACC \ g | 2 % | 2,5 % | 3 % |
| :--- | :--- | :--- | :--- |
| 8 % | 2.904,41 | 3.107,03 | 3.350,18 |
| 9 % | 2.391,23 | **2.526,49** | 2.684,29 |
| 10 % | 2.010,25 | 2.104,72 | 2.212,70 |

> **Nota:** el valor terminal supone ≈ 66 % del EV base, y el riesgo país de LatAm justifica un WACC más alto: con un 10 %, el base baja a $2.104,72 (margen +27 %). Sigue por encima del precio.

## Paso 3 — Múltiplos (PER adelantado)

| Comparable | Por qué encaja | PER adelantado |
| :--- | :--- | :--- |
| Amazon | Comercio electrónico, logística y publicidad | ≈ 26,9x (sin fecha) |
| Sea Ltd (Shopee) | Rival directo en Brasil, con fintech | `no disponible` |
| Nu Holdings | Fintech LatAm, rival de Mercado Pago | `no disponible` |
| Coupang | Marketplace con logística propia | `no disponible` |
| **Mediana** | — | `no disponible` (solo 1 dato) |
| MELI | — | ≈ 38,8x (BPA 2026e $39,44); ≈ 25,0x (BPA 2027e $61,26) |
| Media sectorial a 5 años | — | `no disponible` |

## Paso 4 — PEG (indicador)

MELI: 25,0x (2027e) / ≈ 55 % de crecimiento del BPA 2026 → 2027 ≈ **0,45** (con consensos de fuentes y fechas dispares). Comparables: `no disponible`.

## Paso 5 — Calidad y riesgos

| Métrica | Dato |
| :--- | :--- |
| ROIC | `no disponible` |
| Deuda neta / EBITDA | ≈ 8.030 / EBITDA `no disponible`; ≈ 2,5x el EBIT de 2025 ($3.200M) |
| Márgenes | Operativo: 11,1 % (2025) → 6,3 % (Q3 2026); neto: 6,9 % → 4,2 % |
| Dilución | Acciones ≈ 51M, estables |
| Partidas no recurrentes | `no disponible` |
| Concentración | Sin cliente dominante. Crédito: cartera de $17.900M (+62 %), morosidad de 15-90 días ≈ 7,0 %, NIMAL 20,1 % |

## Paso 6 — Conclusión

1. **Rango de valor:** $725,94 — **$2.526,49** — $4.558,37. El precio ($1.532) está entre el pesimista y el base (45 % del recorrido). **Valor esperado ponderado: $2.584,32.**
2. **Margen de seguridad (base):** (2.526,49 − 1.532) / 2.526,49 = **+39,4 %**. Frente al valor ponderado: +40,7 %.
3. **Veredicto: infravalorada.** Confianza **media**: el crecimiento y la escala están verificados, pero FCF, SBC y acciones exactas `no disponible`; el valor terminal pesa mucho; y el riesgo de crédito en LatAm no ha pasado por una recesión a esta escala.
4. **Dato de invalidación:** morosidad de 15-90 días por encima del 9 % o margen operativo por debajo del 6 % durante dos trimestres seguidos. Cualquiera de los dos movería el valor hacia el pesimista ($726).
5. **Contexto competitivo y de mercado:**

   MercadoLibre es líder del comercio electrónico y la fintech en LatAm, pero en Brasil afronta a Shopee, Temu y Amazon, que la han llevado a bajar el umbral de envío gratis hasta R$19. Mercado Pago compite con Nubank y con la banca tradicional mientras su cartera de crédito crece un 62 %.

   La acción cotiza en $1.532, cerca del mínimo de 52 semanas ($1.333,54) y un 34,6 % por debajo del máximo ($2.342), tras un Q3 2026 con ventas +45 % pero un BPA ajustado de $8,83 por debajo de lo esperado y un margen operativo del 6,3 %.
6. **Aviso:** análisis formativo; no constituye recomendación de inversión. El momento de entrada se decide con análisis técnico y gestión del riesgo.

## Registro

Google Sheets, fila 17 (A-E, G-I, Q-R; Estado `Vigilancia`; Modelo `Claude`). Precio $1.532,92 y margen 39,33 % calculados por las fórmulas. Las columnas técnicas K-P quedan vacías hasta que se ejecute `gestor-de-ejecucion`.

## Fuentes

- https://www.sec.gov/Archives/edgar/data/0001099590/000109959026000027/meli-20260930xex991.htm
- https://www.sec.gov/Archives/edgar/data/0001099590/000109959026000029/meli-20260930.htm
- https://www.businesswire.com/news/home/20260224245400/en/MercadoLibre-Inc.-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results
- https://www.chartmill.com/stock/quote/MELI/estimates · https://stockanalysis.com/stocks/meli/forecast/
