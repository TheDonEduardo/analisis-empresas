# ORCL — Valoración (analista-de-valoracion)

**Fecha:** 2026-11-27 · **Modo:** encadenado (contrato de `2026-11-27-tesis.md`, confirmado por el usuario) · **Cálculos:** `2026-11-27-dcf.py`

## Paso 0 — Datos

| Dato | Valor | Periodo | Fuente |
| :--- | :--- | :--- | :--- |
| Precio | $103,88 (cierre 25-nov-2026); $108,68 en la sesión del 27-nov | — | IBKR |
| Acciones diluidas | ≈ 3.090M (≈ 3.000M implícitas en el Q1 [4,7 / 1,56] + ≈ 86M de la emisión de noviembre) | Q1 FY27 | Cálculo; dato exacto `no disponible` |
| Capitalización | ≈ $321B (a $103,88) | — | Cálculo |
| Ventas | FY26 $67,4B; Q1 FY27 $19,35B (+30 %) | FY26 / Q1 FY27 | Comunicados de Oracle |
| EBIT GAAP | FY26 $20,6B; Q1 FY27 $6,73B (frente a $4,28B) → TTM ≈ $23,05B | TTM | Comunicados |
| Beneficio neto | Q1 FY27 $4,7B; FY26 `no disponible` | — | Comunicado Q1 |
| BPA | Q1 GAAP $1,56; non-GAAP $1,92; guía FY27 non-GAAP ≈ $8,05-8,10 | — | Comunicado / call |
| OCF | FY26 $32,0B; Q1 FY27 ≈ $23B (incluye $11,4B de prepagos) | — | Comunicado / StorageNewsletter (s) |
| Capex | FY26 ≈ $55,7B (implícito); Q1 FY27 $28,5B; guía FY27 $90-95B | — | Yahoo / comunicado |
| FCF | FY26 −$23,7B; Q1 FY27 ≈ −$5,0 a −$5,4B | — | Comunicado / ERP Today |
| SBC | `no disponible` | — | — |
| Deuda total | ≈ $125B a 31-ago (s) + $10B en bonos (nov) ≈ $135B | — | Prensa |
| Preferentes convertibles obligatorias | $5B (Serie D, 6,5 %) | Feb-2026 | 424B5 |
| Caja + valores | $31,9B a 31-may-2026 (31-ago `no disponible`) | FY26 | 10-K (vía resumen) |
| Gasto por intereses | FY26 $4,6B; Q1 FY27 $1,43B (+55 %) | — | 10-K / 10-Q |
| Tasa impositiva efectiva | `no disponible` | — | — |
| Consenso BPA | FY27 ≈ $8,15-8,31; FY28 ≈ $11,06 | Nov-2026 | TIKR / Chartmill (s) |

**Clasificación:** Crecimiento con beneficios (BPA positivo), con FCF negativo por el Capex.

## Paso 1 — DCF inverso

**No aplicable.** El FCF base es negativo (FY26 −$23,7B), así que el modelo no converge. Se evalúa con el DCF por escenarios con quema explícita y con múltiplos.

## Paso 2 — DCF directo (contrato de la tesis)

Supuestos: Año 0 = FY27 ($90B); senda geométrica de ventas; quema explícita de FCFF en los primeros años según el contrato y después rampa hasta el margen objetivo; WACC 9 %; g 2,5 %. La quema que queda de FY27 se considera financiada con las emisiones de noviembre ($20B).
Puente: `EV + caja 31,9 − deuda 135 − preferentes 5 − ajuste extra`.

| Escenario | Prob. | Quema (A1-A4) | VP flujos | VP valor terminal | EV | Equity | Acciones | **Valor/acción** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Pesimista | 35 % | −50, −45, −35, −20 = −$150B | −$95,8B | $63,9B | −$31,9B | −$160,0B (incluye −$20B de garantías) | 3.800M | **$0,00** (suelo) |
| Base | 45 % | −45, −35 = −$80B; luego 6 %, 12 %, 18 % | $79,7B | $311,7B (VT 738,0) | $391,5B | $283,4B | 3.400M | **$83,35** |
| Optimista | 20 % | −45; luego 10 %, 17 %, 22 %, 25 % | $272,5B | $632,8B (VT 1.498,1) | $905,3B | $797,2B | 3.150M | **$253,07** |

Ejemplo de auditoría (base, Año 5): ventas $200B × 18 % = $36,0B → VP = 36,0 / 1,09^5 = $23,4B. VT = 260 × 0,18 × 1,025 / 0,065 = $738,0B → VP = $311,7B.

**Valor esperado ponderado** = 0,35 × 0 + 0,45 × 83,35 + 0,20 × 253,07 = 0 + 37,51 + 50,61 = **$88,12**

**Sensibilidad (base, $/acción):**

| WACC \ g | 2 % | 2,5 % | 3 % |
| :--- | :--- | :--- | :--- |
| 8 % | 102,68 | 113,11 | 125,63 |
| 9 % | 76,38 | **83,35** | 91,47 |
| 10 % | 56,90 | 61,77 | 67,33 |

> **⚠️ Veto contable:** la caja libre no cubre la quema sin más dilución y deuda (FY26: $43B de deuda y $5B de capital; FY27: $20B de ATM + $20B en noviembre). Con un rating BBB- y bonos al 7-8,65 %, un WACC del 10 % es defendible: el valor base bajaría a $61,77. Confianza penalizada.

## Paso 3 — Múltiplos (PER adelantado)

| Comparable | Por qué encaja | PER adelantado |
| :--- | :--- | :--- |
| Microsoft | Hiperescalador más software empresarial | ≈ 26x (TIKR, nov-26) |
| Amazon (AWS) | Hiperescalador líder | ≈ 26,9x (sin fecha) |
| Alphabet (GCP) | Hiperescalador con chips propios | ≈ 26,1x (sin fecha) |
| CoreWeave | Neocloud de GPU, el comparable más cercano a OCI-IA | ≈ 34,8x (sin fecha; dato dudoso) |
| **Mediana** | — | **≈ 26,5x** |
| ORCL | — | ≈ 9,4x ($103,88 / $11,06 FY28) |
| Media sectorial a 5 años | — | `no disponible` (media propia de ORCL a 5 años ≈ 21x, TIKR) |

El múltiplo sobre beneficios parece muy barato, pero el beneficio contable no refleja la quema de caja ni el riesgo de dilución y de deuda. El DCF sobre caja libre es la métrica relevante aquí.

## Paso 4 — PEG (indicador)

ORCL: 9,4x / crecimiento del BPA FY27 → FY28 (+35,7 %) ≈ **0,26**. Comparables: `no disponible`.

## Paso 5 — Calidad y riesgos

| Métrica | Dato |
| :--- | :--- |
| ROIC frente al 8-10 % | `no disponible`. Con FCF negativo y bonos al 7-8,65 %, el ROIC incremental de la IA está sin demostrar |
| Deuda neta / EBITDA | `no disponible` (EBITDA sin verificar). Deuda neta ≈ $103B frente a un EBIT TTM ≈ $23B → ≈ 4,5x el EBIT. Cobertura de intereses: EBIT / intereses ≈ 23,05 / 5,1 ≈ 4,5x |
| Márgenes | Operativo GAAP: 30,6 % (FY26) → 34,8 % (Q1 FY27). FCF: −35 % (FY26) |
| Dilución | ≈ +7-8 % en 2026 (ATM de 141M + ≈ 86M de noviembre), más ≈ 25M de las preferentes en 2029 |
| Partidas no recurrentes | El OCF del Q1 está inflado por $11,4B de prepagos de clientes |
| Concentración | OpenAI ≈ 40-50 % del RPO (estimación de S&P); Oracle no lo desglosa |

## Paso 6 — Conclusión

1. **Rango de valor:** Pesimista $0 — Base $83,35 — Optimista $253,07. El precio ($103,88) está por encima del base. **Valor esperado ponderado: $88,12.**
2. **Margen de seguridad (base):** (83,35 − 103,88) / 83,35 = **−24,6 %**. Frente al valor ponderado: −17,9 %.
3. **Veredicto: sobrevalorada** sobre caja libre. Confianza **baja**: dispersión extrema ($0-253), deuda, caja y acciones sin verificar en fuentes primarias, y veto contable activo. Los múltiplos sobre beneficio (9,4x) apuntan en sentido contrario.
4. **Dato de invalidación:** un FCF del Q2 FY27 menos negativo de lo guiado con el RPO estable, junto con una confirmación de la financiación de OpenAI. O, en sentido negativo, una rebaja del rating a bono basura.
5. **Contexto competitivo y de mercado:**

   Oracle compite con AWS, Azure y GCP, que financian su Capex con caja propia, y con neoclouds como CoreWeave. Su ventaja es la capacidad contratada (RPO de $664B), pero su desventaja es financiarla con deuda BBB- y con emisión de acciones. Microsoft no renovó en 2026 un contrato de capacidad de IA antigua (Bloomberg, 6-nov-2026).

   La acción ha caído un 58,5 % desde el máximo de $250,25 hasta un mínimo de $99,34 el 25-nov-2026. Ha emitido $10B en acciones a $116 (2-nov), por encima del precio actual. Los CDS de Oracle marcan máximos históricos, una señal de que el mercado de crédito está más preocupado que el de acciones.
6. **Aviso:** análisis formativo; no constituye recomendación de inversión. El momento de entrada se decide con análisis técnico y gestión del riesgo.

## Fuentes

- https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm
- https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/
- https://www.marketscreener.com/news/oracle-annual-report-for-fiscal-year-ending-may-31-2026-form-10-k-ce7f5cd3d088ff21
- https://www.tikr.com/blog/oracle-is-54-below-its-june-high-wall-street-still-sees-236
- https://www.chartmill.com/stock/quote/ORCL/estimates
- https://www.tikr.com/blog/big-techs-1-trillion-rally-bets-regulation-wont-touch-the-profits-of-the-tech-companies
