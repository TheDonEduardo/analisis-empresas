# META — Valoración (analista-de-valoracion)

**Fecha:** 2026-11-27 · **Modo:** encadenado (contrato confirmado) · **Cálculos:** `2026-11-27-dcf.py`

## Paso 0 — Datos

| Dato | Valor | Periodo | Fuente |
| :--- | :--- | :--- | :--- |
| Precio | $609,89 (cierre 25-nov-2026); $625,49 en la sesión del 27-nov | — | IBKR |
| Acciones diluidas | 2.573M | Q3 2026 | Comunicado Q3 |
| Capitalización | $1.569,2B | — | Cálculo |
| Ventas | 2025: $200,97B; Q3 2026: $64,6B (+26 %); guía Q4: $73-76B; 2026e ≈ $249B (aprox.) | — | Comunicados |
| Beneficio neto / BPA | Q3: $9,86B / $3,83 (sin el cargo legal: $7,40); 9M 2026: BPA $20,44; 2025: BPA $23,49 | — | Comunicados |
| OCF | Q3 2026: $32,79B | — | Comunicado Q3 |
| Capex (incl. principal de arrendamientos financieros) | Q3: $34,91B; 2025: $72,22B; guía 2026: $135-145B | — | Comunicados |
| FCF | Q3: −$2,12B; 2025: $43,59B | — | Comunicados |
| SBC | `no disponible` | — | — |
| Deuda a largo plazo | $80,92B | 30-sep-2026 | Comunicado Q3 |
| Caja + valores | $82,45B (más $12,5B de preferentes cobradas en oct-26 y $25B de acciones vendidas a plazo, por liquidar) | — | Comunicado Q3 / 8-K |
| Intereses / tasa impositiva | `no disponible` | — | — |
| Consenso BPA 1-2 años | `no disponible` | — | — |

**Clasificación:** Crecimiento con beneficios.

## Paso 1 — DCF inverso

El FCF TTM es próximo a cero por el Capex, así que se usa el **FCF de 2025 ($43,59B, antes de SBC por falta de dato)** frente a la capitalización: **g implícito = 13,4 % anual** durante 10 años.

Referencias: ventas +22 % (2025) y +26 % (Q3 2026). Expectativa **razonable**, siempre que el FCF vuelva a niveles de 2025 o superiores, lo que exige que el Capex se modere.

## Paso 2 — DCF directo (contrato)

Supuestos: Año 0 = 2026e ($249B); quema en los primeros años según el contrato; rampa del margen FCFF hasta el objetivo en el Año 5; WACC 9 %; g 2,5 %.
Puente: `EV + caja 82,45 + preferentes 12,5 + acciones a plazo 25,0 − deuda 80,9 − litigios − garantía de valor residual`. Las acciones de las preferentes y de la venta a plazo ya están incluidas en el número de acciones del contrato.

| Escenario | Prob. | Ventas A5 / A10 | Margen FCFF | Quema | VP flujos | VP valor terminal | EV | Ajustes | Equity | Acciones | **Valor/acción** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Pesimista | 25 % | $330B / $400B | 15 % | −25, −15 | $169,8B | $399,7B | $569,5B | −45 | $563,5B | 2.750M | **$204,92** |
| Base | 50 % | $430B / $600B | 22 % | −10 | $431,1B | $879,3B | $1.310,3B | −15 | $1.334,4B | 2.650M | **$503,55** |
| Optimista | 25 % | $520B / $800B | 28 % | 0 | $763,7B | $1.492,1B | $2.255,8B | −5 | $2.289,9B | 2.550M | **$897,99** |

Ejemplo de auditoría (base, Año 5): $430B × 22 % = $94,6B → VP = $61,5B. VT = 600 × 0,22 × 1,025 / 0,065 = $2.081,5B → VP = $879,3B.

**Valor esperado ponderado** = 0,25 × 204,92 + 0,50 × 503,55 + 0,25 × 897,99 = 51,23 + 251,78 + 224,50 = **$527,50**

**Sensibilidad (base):**

| WACC \ g | 2 % | 2,5 % | 3 % |
| :--- | :--- | :--- | :--- |
| 8 % | 574,43 | 612,19 | 657,49 |
| 9 % | 478,34 | **503,55** | 532,95 |
| 10 % | 406,93 | 424,53 | 444,65 |

> **Nota:** el margen FCFF base del contrato (22 %) está por debajo del histórico de Meta antes del ciclo de IA (2025: 43,59 / 200,97 ≈ 21,7 % después del Capex de 2025; ≈ 30 %+ antes). Con WACC 8 % y g 2,5 %, el base ($612) iguala el precio actual: la valoración es muy sensible a la tasa.

## Paso 3 — Múltiplos

PER adelantado de META y de los comparables (Alphabet ≈ 26,1x; Microsoft ≈ 26x; Amazon ≈ 26,9x; Snap / Pinterest `no disponible`): consenso de BPA de Meta para 2027 `no disponible`. Referencia con BPA anualizado sin el cargo legal (≈ $7,40 × 4 ≈ $29,6): PER ≈ 20,6x frente a una mediana de comparables de ≈ 26x. Media sectorial a 5 años: `no disponible`.

## Paso 4 — PEG

`no disponible` (sin consenso de crecimiento del BPA verificado).

## Paso 5 — Calidad y riesgos

| Métrica | Dato |
| :--- | :--- |
| ROIC | `no disponible` |
| Deuda neta / EBITDA | Caja neta ≈ $1,5B antes de la ampliación (82,45 − 80,92); ≈ $39B después de cobrar las preferentes y la venta a plazo |
| Márgenes | FCF/ventas: 21,7 % (2025) → negativo en el Q3 2026 |
| Dilución | Primera ampliación: ≈ +1,6 % (40M acciones) más preferentes (≈ 20M en 2029). Recompras suspendidas |
| Partidas no recurrentes | Cargo legal de $9,89B en el Q3 2026; cargo fiscal en 2025 |
| Concentración | Sin cliente dominante |

## Paso 6 — Conclusión

1. **Rango de valor:** $204,92 — **$503,55** — $897,99. El precio ($609,89) está por encima del base. **Valor esperado ponderado: $527,50.**
2. **Margen de seguridad (base):** (503,55 − 609,89) / 503,55 = **−21,1 %**. Frente al valor ponderado: −15,6 %.
3. **Veredicto: sobrevalorada** (moderadamente) frente al contrato. Confianza **media**: el negocio está verificado, pero el valor depende de cuándo y cuánto se modere el Capex; SBC y consenso `no disponible`; con WACC 8 % estaría en valor razonable.
4. **Dato de invalidación:** la guía de Capex de 2027 (finales de ene-2027). Si es ≤ $150B con ventas creciendo al 20 % o más, el FCF vuelve a ≈ 25 % y el valor tiende al optimista. Si es de ≈ $250B, el pesimista gana peso.
5. **Contexto competitivo y de mercado:**

   Meta domina la publicidad social con más de 3.000M de usuarios diarios y compite por la atención con TikTok, YouTube y los asistentes de IA. Lanzó Muse (más de 10M de cuentas según la call del Q3 2026) y concentra su inversión en Meta Superintelligence Labs.

   En oct-2026 hizo su primera ampliación de capital ($37.500M entre acciones y preferentes) y suspendió las recompras. El 21-oct-2026 recibió una condena de $25B en Nuevo México. La acción ha caído un 21,8 % desde el máximo de $779,82.
6. **Aviso:** análisis formativo; no constituye recomendación de inversión. El momento de entrada se decide con análisis técnico y gestión del riesgo.

## Fuentes

- https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-09302026xexhibit991.htm
- https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/
- https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Pricing-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx
- https://www.abqjournal.com/news/judge-orders-meta-pay-25-billion-to-new-mexico-for-violations-of-state-law/3146756
