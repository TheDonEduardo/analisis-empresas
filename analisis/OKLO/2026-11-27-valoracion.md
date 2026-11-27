# OKLO — Valoración (analista-de-valoracion)

**Fecha:** 2026-11-27 · **Modo:** encadenado (contrato de `2026-11-27-tesis.md`, confirmado) · **Cálculos:** `2026-11-27-dcf.py` (importes en $M)

## Paso 0 — Datos

| Dato | Valor | Periodo | Fuente |
| :--- | :--- | :--- | :--- |
| Precio | $19,47 (cierre 25-nov-2026); $20,50 en la sesión del 27-nov | — | IBKR |
| Acciones | 195,29M (4-nov-2026) | — | 10-Q Q3 2026 (vía resumen) |
| Capitalización | ≈ $3.802M (a $19,47) | — | Cálculo |
| Ventas | Q3 2026 $1,86M; TTM `no disponible` | — | Resultados Q3 |
| EBIT | Q3: gastos operativos $84,3M; EBIT ≈ −$82M (−$71M con la plusvalía de $11,4M) | Q3 2026 | Resultados Q3 |
| Beneficio neto / BPA | Q3 −$41,7M (incluye intereses de la caja); BPA `no disponible` | — | Resultados Q3 |
| OCF | 9M 2026 −$48,7M (s, dato dudoso) | — | Resumen del 10-Q |
| Capex | `no disponible` | — | — |
| SBC | `no disponible` | — | — |
| Deuda | Sin deuda material identificada | — | — |
| Caja + valores negociables | **$3.131M** (caja $1.550M + corrientes $952M + no corrientes $629M); restringida $81,9M (excluida) | 30-sep-2026 | 10-Q Q3 |
| Caja por acción | $16,03 | — | Cálculo |
| Consenso BPA | `no disponible` | — | — |

**Clasificación:** Sin beneficios.

## Paso 1 — DCF inverso

**No aplicable.** Ventas mínimas y FCF negativo: el modelo no converge. EV implícito = 3.802 − 3.131 ≈ **$671M**, que es lo que el mercado paga por la opción nuclear.

## Paso 2 — DCF directo (contrato)

Supuestos: ventas con rampa lineal hasta el Año 5 y geométrica hasta el Año 10; quema explícita según el contrato; WACC 9 % (ver sensibilidad y nota del 12 %); g 2,5 %; sin valor terminal en el pesimista (margen negativo).
Puente: `EV + caja 3.131 − deuda 0`.

| Escenario | Prob. | Ventas A5 / A10 | Quema | VP flujos | VP valor terminal | EV | Equity | Acciones | **Valor/acción** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Pesimista | 50 % | $0 / $50M | −350/año × 10 = −$3.500M | −$2.246M | $0 | −$2.246M | $885M | 320M | **$2,77** |
| Base | 50 → 35 % | $150M / $1.500M | −500 × 5 = −$2.500M; luego 5 %, 10 %, 15 % | −$1.712M | $1.499M (VT 3.548) | −$213M | $2.918M | 250M | **$11,67** |
| Optimista | 15 % | $600M / $4.000M | −500 × 4 = −$2.000M; luego 10 % → 25 % | −$390M | $6.661M (VT 15.769) | $6.271M | $9.402M | 225M | **$41,79** |

Ejemplo de auditoría (base): VT = 1.500 × 0,15 × 1,025 / 0,065 = $3.548M → VP = 3.548 / 1,09^10 = $1.499M. Equity = −1.712 + 1.499 + 3.131 = $2.918M → / 250M = $11,67.

**Valor esperado ponderado** = 0,50 × 2,77 + 0,35 × 11,67 + 0,15 × 41,79 = 1,39 + 4,08 + 6,27 = **$11,74**

**Sensibilidad (base, $/acción):**

| WACC \ g | 2 % | 2,5 % | 3 % |
| :--- | :--- | :--- | :--- |
| 8 % | 12,64 | 13,32 | 14,14 |
| 9 % | 11,22 | **11,67** | 12,20 |
| 10 % | 10,23 | 10,54 | 10,91 |

> **Nota:** para una empresa nuclear sin ingresos, una tasa del 12 % es más realista: Pes $3,60 / Base $9,17 / Opt $26,94 (valor ponderado $9,05). **Veto contable:** la caja ($3.131M) cubre la quema base ($2.500M) sin más dilución, pero no el Capex de construcción a escala comercial (`no disponible`).

## Paso 3 — Múltiplos

Clasificación "sin beneficios", así que tocaría P/S. Con unas ventas anualizadas de ≈ $7M, el P/S (≈ 540x) no tiene significado. Comparables (NuScale, NANO Nuclear, Centrus, X-Energy privada): múltiplos `no disponible` en esta sesión. Métrica alternativa: **precio / caja por acción = 19,47 / 16,03 = 1,21x**. Media sectorial a 5 años: `no disponible`.

## Paso 4 — PEG

No aplicable (BPA negativo).

## Paso 5 — Calidad y riesgos

| Métrica | Dato |
| :--- | :--- |
| ROIC | No aplicable (sin ingresos) |
| Deuda neta / EBITDA | Caja neta de $3.131M; EBITDA negativo |
| Márgenes | Gastos operativos del Q3 $84,3M frente a ventas de $1,86M |
| Dilución | +21,7 % en 2026 (160,5M → 195,3M acciones) |
| Partidas no recurrentes | Plusvalía de $11,4M en el Q3; los intereses de la caja reducen la pérdida neta |
| Concentración | Pipeline dominado por Meta (prepago), Switch (no vinculante) y Equinix (LOI) |

## Paso 6 — Conclusión

1. **Rango de valor:** Pesimista $2,77 — Base $11,67 — Optimista $41,79. El precio ($19,47) está entre el base y el optimista. **Valor esperado ponderado: $11,74.**
2. **Margen de seguridad (base):** (11,67 − 19,47) / 11,67 = **−66,8 %**. Frente al valor ponderado: −65,8 %.
3. **Veredicto: sobrevalorada** frente al contrato de la tesis. Confianza **baja**: es una opción binaria (licencia de la NRC), las hipótesis de ventas no tienen respaldo contractual, y el Capex y el SBC no están disponibles. El suelo de caja ($16,03 por acción) explica por qué el mercado paga más que el base: descuenta una probabilidad optimista mayor que el 15 % del contrato.
4. **Dato de invalidación:** la presentación y aceptación de la solicitud de licencia (COLA) de Aurora por la NRC, junto con un PPA vinculante firmado (Meta o Switch). Ambas cosas moverían las probabilidades hacia el escenario base u optimista.
5. **Contexto competitivo y de mercado:**

   Oklo compite en reactores modulares avanzados (SMR) con NuScale, X-Energy, Kairos y TerraPower por la demanda eléctrica de los centros de datos de IA. Su reactor de pruebas Groves alcanzó la criticidad el 5-ago-2026, pero Aurora sigue en fase de pre-solicitud ante la NRC.

   La acción ha caído un 83 % desde el máximo de $115,72 y marcó un mínimo de $17,28 el 25-nov-2026, cerca de su caja por acción ($16,03). La financiación vía ATM (dos programas de $1.000M en 2026) ha sostenido la caja a costa de diluir un 22 %.
6. **Aviso:** análisis formativo; no constituye recomendación de inversión. El momento de entrada se decide con análisis técnico y gestión del riesgo.

## Fuentes

- https://www.sec.gov/Archives/edgar/data/0001849056/000162828026071319/oklo-20260930.htm
- https://www.minichart.com.sg/2026/11/06/oklo-q3-2026-41-7m-net-loss-3-13b-liquidity-as-pre-commercial-nuclear-firm-builds-cash/
- https://www.tikr.com/blog/oklo-stock-heres-why-investors-need-to-look-at-its-26-share-count-jump
