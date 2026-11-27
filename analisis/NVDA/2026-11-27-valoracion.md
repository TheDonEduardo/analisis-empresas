# NVDA — Valoración (analista-de-valoracion)

**Fecha:** 2026-11-27 · **Modo:** encadenado (contrato de inputs de `2026-11-27-tesis.md`, confirmado por el usuario) · **Cálculos:** `2026-11-27-dcf.py`

> La red de esta sesión bloquea sec.gov y nvidia.com: los datos proceden de búsquedas que citan los comunicados y 10-Q/10-K. (s) = fuente secundaria.

## Paso 0 — Datos

| Dato | Valor | Periodo | Fuente |
| :--- | :--- | :--- | :--- |
| Precio actual | $149,30 | Cierre 25-nov-2026 (26-nov festivo) | stockanalysis / heygotrade |
| Acciones diluidas | 24.190M | Q3 FY27 (media ponderada) | 8-K Q3 FY27 (s) |
| Capitalización | $3.611,6B | 149,30 × 24,19B | Cálculo |
| Ventas TTM | $361,7B | Q4 FY26 68,1 + Q1 81,6 + Q2 96,2 + Q3 115,8 | Comunicados de NVIDIA |
| EBIT | 9M FY27: $194,8B (53,5 + 63,7 + 77,5); Q4 FY26 `no disponible` | Q1-Q3 FY27 | Comunicados Q2/Q3 FY27 |
| Beneficio neto TTM | $226,3B (42,96 + 58,32 + 59,69 + 65,3) | TTM a oct-26 | Comunicados |
| BPA diluido | Q3 $2,70; Q2 $2,46; FY26 $4,90; TTM `no disponible` | — | Comunicados |
| OCF TTM | $158,9B (FY26 102,7 − 9M FY26 66,5 + 9M FY27 122,7) | TTM | 10-K FY26 + 8-K Q3 (s) |
| Capex | 9M FY27: $9,0B (OCF 122,7 − FCF 113,7); Q4 FY26 `no disponible` | 9M FY27 | 8-K Q3 (s) |
| SBC | FY26: $6,4B; TTM `no disponible` | FY26 | 10-K FY26 |
| Deuda total | `no disponible` | — | — |
| Caja + valores negociables | $53,5B (s) | 25-oct-2026 | Análisis del 10-Q Q3 |
| Gasto por intereses / tasa impositiva | `no disponible` / `no disponible` | — | — |
| Consenso BPA | FY28 ≈ $16,2-16,6; FY29 ≈ $21,8 | Nov-2026 | Yahoo Finance / 24/7 Wall St. (s) |
| Guía | Q4 FY27 $130B ±3 %; FY28 ≈ +75 % de ventas | 17-nov-2026 | Call Q3 FY27 |

**Clasificación:** Crecimiento con beneficios.

## Paso 1 — DCF inverso

Faltan intereses y tasa impositiva, así que se usa la alternativa: **FCF al accionista frente a capitalización** (NVIDIA tiene caja neta y la deuda es inmaterial frente a $3,6T).

`FCF base = OCF TTM 158,86 − Capex 9,0 (solo 9M; infraestima el capex) − SBC 6,39 (FY26) = $143,47B`

Resolviendo `Σ FCF₀(1+g)^t/1,09^t (t=1..10) + [FCF₁₀ × 1,025 / (0,09 − 0,025)] / 1,09^10 = $3.611,6B` → **g implícito = 8,7 % anual** (8,5 % frente a un EV sin deuda de $3.558,1B).

| Referencia | Crecimiento |
| :--- | :--- |
| Implícito en el precio (10 años) | 8,7 % |
| Ventas históricas a 5 años (FY21 $16,7B → FY26 $215,9B) | ≈ 67 % anual |
| Consenso BPA FY27 → FY29 ($9,66 → $21,8) | ≈ 50 % anual |
| Guía de ventas FY28 | ≈ +75 % |

**Expectativa del mercado: conservadora.**

## Paso 2 — DCF directo con escenarios (contrato de la tesis)

Supuestos comunes: Año 0 = FY27e ($423,6B = 81,6 + 96,2 + 115,8 + 130 de guía); las ventas siguen una senda geométrica hasta Año 5 y Año 10; el margen FCFF parte del 36 % (FCF/ventas del Q3 37,8 % menos ≈ 1,5 pp de SBC; supuesto propio) y converge linealmente al objetivo en el Año 5; WACC 9 %; g 2,5 %.
Puente: `(EV + caja 53,5 + inversiones de capital 99 × % − pérdida esperada por garantías − deuda [no disponible]) / acciones diluidas proyectadas`.

| Escenario | Prob. | Ventas A5 / A10 | Margen FCFF | VP flujos 1-10 | VP valor terminal | EV | Ajustes | Equity | Acciones | **Valor/acción** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Pesimista | 25 % | $380B / $450B | 30 % | $823,8B | $899,2B (VT 2.128,8) | $1.723,0B | +53,5 +39,6 −60 | $1.756,1B | 24.500M | **$71,68** |
| Base | 50 % | $700B / $950B | 40 % | $1.694,1B | $2.531,2B (VT 5.992,3) | $4.225,3B | +53,5 +69,3 −15 | $4.333,1B | 22.800M | **$190,05** |
| Optimista | 25 % | $950B / $1.400B | 46 % | $2.513,5B | $4.289,7B (VT 10.155,4) | $6.803,3B | +53,5 +99,0 −0 | $6.955,8B | 21.500M | **$323,53** |

Ejemplo de auditoría (base, Año 5): ventas $700B × 40 % = FCFF $280,0B → VP = 280,0 / 1,09^5 = $182,0B. VT = 950 × 0,40 × 1,025 / 0,065 = $5.992,3B → VP = 5.992,3 / 1,09^10 = $2.531,2B.

**Valor esperado ponderado** = 0,25 × 71,68 + 0,50 × 190,05 + 0,25 × 323,53 = 17,92 + 95,03 + 80,88 = **$193,82**

**Sensibilidad (escenario base, $/acción):**

| WACC \ g | 2 % | 2,5 % | 3 % |
| :--- | :--- | :--- | :--- |
| 8 % | 214 | 227 | 242 |
| 9 % | 182 | **190** | 200 |
| 10 % | 157 | 163 | 170 |

> **⚠️ Veto contable (alerta):** la guía de la directiva (FY28 ≈ +75 %, ≈ $741B) y el consenso de ventas FY28 (≈ $709B) ya superan las ventas Año 5 del escenario base ($700B). El contrato asume implícitamente un pico cíclico en FY28 seguido de estancamiento. Se mantiene el contrato confirmado por el usuario, pero como referencia, con el Año 1 anclado a la guía: Pes $80,41 / Base $199,90 / Opt $334,17. La valoración es, por diseño, conservadora frente a la guía.

## Paso 3 — Múltiplos frente a comparables

| Comparable | Por qué encaja | PER adelantado | EV/EBITDA |
| :--- | :--- | :--- | :--- |
| AMD | Rival directo en GPU de centro de datos | 31,3x | 72,8x |
| Broadcom (AVGO) | ASIC a medida (TPU) y redes de IA | 17,9x | 23,1x |
| Marvell (MRVL) | ASIC y conectividad para centros de datos | 23,2x | 53,7x |
| TSMC (TSM) | Fabricante de todos los chips de IA; tamaño comparable ($1,9T) | `no disponible` (≈21x trailing) | 15,6x |
| **Mediana** | — | **23,2x** | **38,4x** |
| NVDA | — | ≈ 9,1x (149,30 / 16,4) | ≈ 20x (s) |
| Media del sector a 5 años | — | `no disponible` | `no disponible` |

Fuentes: investinglive (nov-26) para el PER; multiples.vc (oct-26) para el EV/EBITDA. Los datos varían mucho entre proveedores. NVDA cotiza con un fuerte descuento frente a la mediana de sus comparables pese a crecer más.

## Paso 4 — PEG (solo indicador)

| Empresa | PER adelantado | Crecimiento BPA 3-5 años | PEG |
| :--- | :--- | :--- | :--- |
| NVDA | 9,1x | ≈ 50 % (FY27 → FY29, 2 años) | ≈ 0,18 |
| AMD / AVGO / MRVL / TSM | ver Paso 3 | `no disponible` | `no disponible` |

## Paso 5 — Calidad y riesgos

| Métrica | Dato |
| :--- | :--- |
| ROIC frente al 8-10 % | `no disponible` (capital invertido no verificado; el beneficio neto TTM de $226B apunta a un ROIC muy superior al coste de capital) |
| Deuda neta / EBITDA | Caja neta (caja + valores $53,5B; deuda `no disponible`) |
| Márgenes | Bruto: 71,1 % (FY26) → 74,8 % (Q3 FY27) → guía 71-72 %. Operativo Q3: 66,9 % (77,5 / 115,8). FCF Q3: 37,8 % |
| Dilución anual | −1,2 % (recompras netas) |
| Partidas no recurrentes | Q1 FY27: beneficio neto ($58,3B) > EBIT ($53,5B), lo que indica ganancias en inversiones de capital. Riesgo inverso si se deterioran los $99B invertidos |
| Concentración de clientes | Q3: 14 %, 11 % y 11 %; cuentas a cobrar 18 % y 17 % |

## Paso 6 — Conclusión

1. **Rango de valor:** Pesimista $71,68 — Base $190,05 — Optimista $323,53. El precio ($149,30) está entre el pesimista y el base (34 % del recorrido). **Valor esperado ponderado: $193,82.**
2. **Margen de seguridad (base):** (190,05 − 149,30) / 190,05 = **21,4 %**. Frente al valor ponderado: (193,82 − 149,30) / 193,82 = 23,0 %.
3. **Veredicto: infravalorada.** Confianza **media**: deuda, intereses, tasa impositiva y SBC TTM `no disponible`; datos de fuentes secundarias; riesgo de gobernanza abierto; y alerta de veto contable (contrato conservador frente a la guía).
4. **Dato de invalidación:** un recorte agregado del Capex de los hiperescaladores para 2027-28 o unas ventas del Q4 FY27 por debajo de $126B (extremo inferior de la guía). Cualquiera de los dos movería las probabilidades hacia el escenario pesimista ($72).
5. **Contexto competitivo y de mercado:**

   NVIDIA mantiene una cuota estimada del 75-81 % del mercado de aceleradores, pero los ASIC (TPU de Google, con Anthropic y Meta como clientes) y AMD ganan terreno en inferencia. El mercado total crece más rápido de lo que NVIDIA pierde cuota, y la directiva habla de un backlog de la industria de la nube de $2,5T (declaración de la call del 17-nov-2026).

   La acción cayó desde $186,64 (6-nov) hasta $149,30 (25-nov) por la crisis de gobernanza: dimisión de Huang el 12-nov y readmisión el 23-nov (+31,5 % ese día), tras lo que perdió de nuevo un 9,5 % en dos sesiones. El mercado descuenta un crecimiento del FCF de solo el 8,7 % anual, lo que refleja escepticismo sobre la durabilidad del ciclo de Capex de IA más que sobre los resultados actuales.
6. **Aviso:** análisis formativo; no constituye recomendación de inversión. El momento de entrada se decide con análisis técnico y gestión del riesgo.

## Fuentes

- Precio: https://stockanalysis.com/stocks/nvda/history/ · https://www.heygotrade.com/en/news/nvidia-nvda-stock-news-november-26-2026/
- Resultados Q3 FY27: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27pr.htm · https://www.gurufocus.com/news/9205938/nvidia-corp-reports-q3-fiscal-2027-earnings-eps-of-270-and-revenue-of-1158-billion-exceed-estimates
- Resultados Q2 FY27: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/
- 10-K FY26: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- Flujos de caja Q3 (s): https://www.crowdfundedwealth.com/articles/nvidia-q3-fiscal-2027-results-8-k-what-the-filing-says
- Guía FY28 +75 %: https://seekingalpha.com/news/4673972-nvidia-projects-75-percent-fiscal-2028-revenue-growth-amid-leadership-transition · https://investinglive.com/stocks/nvidia-sees-75-revenue-growth-next-year-as-kress-points-to-2-5-trillion-backlog/
- Consenso: https://finance.yahoo.com/markets/stocks/articles/nvidia-price-prediction-wall-street-143044345.html · https://247wallst.com/investing/2026/11/08/why-nvidia-at-13-times-expected-earnings-still-isnt-cheap/
- Comparables: https://investinglive.com/stocks/nvidia-stock-plunges-8-6-but-amd-and-broadcom-rally-which-chip-stocks-are-worth-buying/ · https://multiples.vc/ai-chips-hardware-valuation-multiples
