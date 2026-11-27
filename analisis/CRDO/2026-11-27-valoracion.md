# CRDO — Valoración (analista-de-valoracion)

**Fecha:** 2026-11-27 · **Modo:** encadenado (contrato confirmado) · **Cálculos:** `2026-11-27-dcf.py` (importes en $M)

## Paso 0 — Datos

| Dato | Valor | Periodo | Fuente |
| :--- | :--- | :--- | :--- |
| Precio | $106,80 (cierre 25-nov-2026); $112,07 en la sesión del 27-nov | — | IBKR |
| Acciones diluidas | ≈ 188M (implícitas en 472,3 / 2,51) | FY26 | Cálculo; dato exacto `no disponible` |
| Capitalización | ≈ $20.078M | — | Cálculo |
| Ventas | FY26 $1.335M (+206 %); Q1 FY27 $479,0M; guía Q2 $525-535M; FY27e ≥ $2.470M (> +85 %) | — | Comunicados |
| Beneficio neto | FY26 GAAP $472,3M; non-GAAP $662M | FY26 | 10-K / comunicado |
| BPA diluido | FY26 $2,51 | FY26 | 10-K |
| OCF / Capex / FCF | `no disponible` | — | — |
| SBC | `no disponible` (diferencia GAAP / non-GAAP ≈ $190M en FY26) | — | — |
| Deuda | $0 identificada | — | — |
| Caja + inversiones a corto plazo | ≈ $1.400M | Fin de FY26 | Comunicado FY26 |
| Consenso BPA | `no disponible` | — | — |

**Clasificación:** Crecimiento con beneficios.

## Paso 1 — DCF inverso

FCF `no disponible`, así que se usa como proxy el beneficio neto GAAP de FY26 ($472,3M) frente a la capitalización: **g implícito = 15,6 % anual** durante 10 años. Referencias: ventas +206 % (FY26) y guía de > +85 % (FY27). Expectativa **conservadora** si el crecimiento actual se sostiene unos años; razonable si se tiene en cuenta el riesgo de concentración.

## Paso 2 — DCF directo (contrato)

Supuestos: Año 0 = FY27e ($2.500M); margen FCFF inicial del 25 % (supuesto propio: beneficio neto del 35 % menos SBC y Capex) que converge al objetivo en el Año 5; WACC 9 %; g 2,5 %. Puente: `EV + caja 1.400`.

| Escenario | Prob. | Ventas A5 / A10 | Margen FCFF | VP flujos | VP valor terminal | EV | Equity | Acciones | **Valor/acción** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Pesimista | 30 % | $2.500M / $3.000M | 15 % | $2.933M | $2.997M | $5.931M | $7.331M | 205M | **$35,76** |
| Base | 45 % | $5.500M / $9.000M | 25 % | $8.530M | $14.987M (VT 35.481) | $23.517M | $24.917M | 198M | **$125,84** |
| Optimista | 25 % | $8.000M / $14.000M | 30 % | $14.037M | $27.977M (VT 66.231) | $42.013M | $43.413M | 195M | **$222,63** |

Ejemplo de auditoría (base, Año 5): $5.500M × 25 % = $1.375M → VP = $894M. VT = 9.000 × 0,25 × 1,025 / 0,065 = $35.481M → VP = $14.987M.

**Valor esperado ponderado** = 0,30 × 35,76 + 0,45 × 125,84 + 0,25 × 222,63 = 10,73 + 56,63 + 55,66 = **$123,02**

**Sensibilidad (base):**

| WACC \ g | 2 % | 2,5 % | 3 % |
| :--- | :--- | :--- | :--- |
| 8 % | 142,01 | 150,62 | 160,96 |
| 9 % | 120,10 | **125,84** | 132,55 |
| 10 % | 103,80 | 107,82 | 112,41 |

## Paso 3 — Múltiplos (PER)

| Comparable | Por qué encaja | PER adelantado |
| :--- | :--- | :--- |
| Marvell | Conectividad y DSP óptico | ≈ 23,2x |
| Broadcom | SerDes y redes | ≈ 15,5x (FY27) |
| AMD | Semis de centros de datos | ≈ 31,3x |
| Astera Labs | Retimers y conectividad de IA, rival directo | `no disponible` |
| **Mediana** | — | **≈ 23,2x** |
| CRDO | — | PER histórico ≈ 42,5x (106,80 / 2,51 FY26); adelantado `no disponible` |
| Media sectorial a 5 años | — | `no disponible` |

## Paso 4 — PEG

`no disponible` (sin consenso de BPA a 3-5 años). Referencia: con un crecimiento de ventas de > 85 % en FY27, el PER histórico de 42,5x implica un PEG implícito inferior a 0,5.

## Paso 5 — Calidad y riesgos

| Métrica | Dato |
| :--- | :--- |
| ROIC | `no disponible` (beneficio neto de $472M sin deuda y con poco Capex indica un ROIC alto) |
| Deuda neta / EBITDA | Caja neta de ≈ $1.400M |
| Márgenes | Bruto non-GAAP: guía del 67-69 %; neto GAAP FY26 del 35 % |
| Dilución | SBC alto y PSU "ambicioso" del CEO; acciones ≈ 188M |
| Partidas no recurrentes | `no disponible` |
| Concentración | **Mayor cliente: 33 % de las ventas del Q1 FY27** |

## Paso 6 — Conclusión

1. **Rango de valor:** $35,76 — **$125,84** — $222,63. El precio ($106,80) está por debajo del base. **Valor esperado ponderado: $123,02.**
2. **Margen de seguridad (base):** (125,84 − 106,80) / 125,84 = **+15,1 %**. Frente al valor ponderado: +13,2 %.
3. **Veredicto: infravalorada** (margen moderado, justo en el límite del 15 %). Confianza **media-baja**: FCF, SBC y acciones exactas `no disponible`; un cliente concentra el 33 % de las ventas; y los resultados del 1-dic pueden mover el precio más de un 20 % (ATR del 14,7 %).
4. **Dato de invalidación:** la guía del Q3 FY27 el 1-dic-2026. Si confirma un FY27 > +85 % con margen bruto ≥ 67 %, el valor tiende al base u optimista. Si es plana o hay pérdida de cuota en el cliente principal, tiende al pesimista ($36).
5. **Contexto competitivo y de mercado:**

   Credo lidera los cables eléctricos activos (AEC) para racks de IA de los hiperescaladores y amplía su negocio de óptica (> $600M en FY27 según la guía). Compite con Marvell, Broadcom y Astera Labs, y con la posible adopción de óptica co-empaquetada (CPO).

   La acción ha caído un 65,4 % desde el máximo de $308,67 con tres desplomes en noviembre de 2026 ligados a ventas generalizadas del sector (5-nov −18 %, 20-nov −14 %, 25-nov −10 %), sin noticias propias de la compañía.
6. **Aviso:** análisis formativo; no constituye recomendación de inversión. El momento de entrada se decide con análisis técnico y gestión del riesgo.

## Fuentes

- https://investors.credosemi.com/news-events/news/news-details/2026/Credo-Technology-Group-Holding-Ltd-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Financial-Results/default.aspx
- https://www.tradingview.com/news/tradingview:e47517dc5d142:0-credo-technology-group-holding-ltd-fy-2026-revenue-1-34b-eps-2-51-10-k-summary/
- https://www.sec.gov/Archives/edgar/data/0001807794/000162828026059795/credoq12027ex-991.htm
- https://s205.q4cdn.com/511065572/files/doc_news/Credo-Schedules-Second-Quarter-Fiscal-Year-2027-Financial-Results-Conference-Call-2026.pdf
