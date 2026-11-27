# AVGO — Valoración (analista-de-valoracion)

**Fecha:** 2026-11-27 · **Modo:** encadenado (contrato de `2026-11-27-tesis.md`, confirmado) · **Cálculos:** `2026-11-27-dcf.py`

## Paso 0 — Datos

| Dato | Valor | Periodo | Fuente |
| :--- | :--- | :--- | :--- |
| Precio | $300,86 (cierre 25-nov-2026); $313,25 en la sesión del 27-nov | — | IBKR |
| Acciones diluidas | 4.888M | Q1 FY26 (Q3 `no disponible`) | 10-Q Q1 FY26 |
| Capitalización | $1.470,6B | — | Cálculo |
| Ventas | FY25 $63,9B; Q1 FY26 $19,31B; Q2 $22,19B; Q3 $29,6B; guía Q4 $34,8B → FY26e $105,9B | — | Comunicados |
| Beneficio operativo (EBIT) | `no disponible` (Q4: margen operativo non-GAAP ≈ 66 % de guía) | — | — |
| Beneficio neto GAAP | FY25 $23,1B; Q1 FY26 $7,35B; Q2 $9,31B; Q3 `no disponible` | — | Comunicados |
| BPA | Consenso FY27 ≈ $19,41; Hock Tan: "más de $30" en FY28 | — | TIKR |
| OCF | 9M FY26 $32,95B; FY25 $27,5B | — | 10-Q Q3 / comunicado FY25 |
| Capex | Q1 $0,25B; Q2 $0,23B; Q3 $0,5B | — | Comunicados |
| FCF | Q1 $8,01B (41 %); Q2 $10,26B (46 %); Q3 $13,7B (46 %); FY25 $26,9B | — | Comunicados |
| SBC | Q1 FY26 $2,18B; 9M ≈ $6,29B (s) | — | 10-Q / comunicado |
| Deuda total | $66,1B | Q1 FY26 (Q3 `no disponible`) | 10-Q Q1 FY26 |
| Caja | $24,0B | Q3 FY26 | Comunicado Q3 |
| Intereses / tasa impositiva | `no disponible` / `no disponible` | — | — |

**Clasificación:** Crecimiento con beneficios.

## Paso 1 — DCF inverso

Faltan intereses y tasa impositiva, así que se usa la alternativa de **FCF al accionista frente a capitalización**.

`FCF base ≈ OCF Q4 FY25 7,67 (aprox.; capex de ese trimestre omitido) + FCF Q1-Q3 FY26 (8,01 + 10,26 + 13,70) − SBC anualizado 8,4 = $31,24B`

Resolviendo para igualar los $1.470,6B → **g implícito = 17,0 % anual** durante 10 años.

| Referencia | Crecimiento |
| :--- | :--- |
| Implícito en el precio | 17,0 % |
| Ventas FY24 → FY25 | +24 % |
| Ventas FY25 → FY26e | +66 % ($63,9B → $105,9B) |
| BPA FY25 → FY27 (consenso) | ≈ 69 % anual ($6,82 → $19,41) |

**Expectativa del mercado: razonable** (exige mantener un crecimiento alto durante 10 años; inferior al ritmo actual).

## Paso 2 — DCF directo (contrato)

Supuestos: Año 0 = FY26e ($105,9B); senda geométrica de ventas; margen FCFF que parte del 39 % (FCF 46 % menos ≈ 7 % de SBC) y converge al objetivo en el Año 5; WACC 9 %; g 2,5 %.
Puente: `EV + caja 24,0 − deuda 66,1 − pérdida esperada por garantías`.

| Escenario | Prob. | Ventas A5 / A10 | Margen FCFF | VP flujos | VP valor terminal | EV | Equity | Acciones | **Valor/acción** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Pesimista | 25 % | $150B / $170B | 28 % | $277,7B | $317,1B (VT 750,6) | $594,8B | $517,7B (−35) | 5.100M | **$101,50** |
| Base | 50 % | $260B / $340B | 36 % | $538,4B | $815,3B (VT 1.930,2) | $1.353,7B | $1.303,6B (−8) | 4.900M | **$266,04** |
| Optimista | 25 % | $350B / $480B | 40 % | $764,9B | $1.278,9B (VT 3.027,7) | $2.043,8B | $2.001,7B | 4.750M | **$421,41** |

Ejemplo de auditoría (base, Año 5): $260B × 36 % = $93,6B → VP = 93,6 / 1,09^5 = $60,8B. VT = 340 × 0,36 × 1,025 / 0,065 = $1.930,2B → VP = $815,3B.

**Valor esperado ponderado** = 0,25 × 101,50 + 0,50 × 266,04 + 0,25 × 421,41 = 25,38 + 133,02 + 105,35 = **$263,75**

**Sensibilidad (base, $/acción):**

| WACC \ g | 2 % | 2,5 % | 3 % |
| :--- | :--- | :--- | :--- |
| 8 % | 302,21 | 321,15 | 343,87 |
| 9 % | 253,40 | **266,04** | 280,79 |
| 10 % | 216,99 | 225,82 | 235,91 |

> **Nota (veto contable leve):** la guía de IA para FY27 ($115B) más el resto del negocio (≈ $45B) apunta a ≈ $160B en el Año 1, por encima de la senda del contrato ($126,7B). Con el Año 1 anclado en $160B: Pes $108,34 / Base $272,32 / Opt $427,00. El impacto es menor (+2 %), porque el contrato ya prevé que el margen se comprima.

## Paso 3 — Múltiplos (PER adelantado)

| Comparable | Por qué encaja | PER adelantado |
| :--- | :--- | :--- |
| NVIDIA | Líder en aceleradores de IA | ≈ 9,1x (FY28) |
| AMD | GPU y CPU para centros de datos | ≈ 31,3x |
| Marvell | ASIC a medida y conectividad, rival directo | ≈ 23,2x |
| TSMC | Fabricante de los XPU | `no disponible` |
| **Mediana** | — | **≈ 23,2x** |
| AVGO | — | ≈ 15,5x ($300,86 / $19,41 FY27); EV/EBITDA ≈ 23,1x (multiples.vc, oct-26) |
| Media sectorial a 5 años | — | `no disponible` (media propia a 3 años ≈ 30x, TIKR) |

## Paso 4 — PEG (indicador)

AVGO: 15,5x / ≈ 54,6 % (BPA FY27 → FY28: $19,41 → $30) ≈ **0,28**. Comparables: `no disponible`.

## Paso 5 — Calidad y riesgos

| Métrica | Dato |
| :--- | :--- |
| ROIC | `no disponible` (FCF de ≈ $40B frente a un Capex mínimo indica un ROIC operativo muy alto; el fondo de comercio de VMware lo diluye a nivel contable) |
| Deuda neta / EBITDA | (66,1 − 24,0) / 43,0 (EBITDA ajustado FY25) ≈ **0,98x**, y menor con el EBITDA TTM |
| Márgenes | FCF/ventas: 41 % → 46 % → 46 % (Q1-Q3 FY26). Bruto ≈ 75 % → guía ≈ 73 % (s), presionado por racks y memoria |
| Dilución | +1,1 % anual (4.836M → 4.888M) |
| Partidas no recurrentes | Amortización de intangibles de VMware (la diferencia GAAP / non-GAAP) |
| Concentración | **Un distribuidor = 50 %** de las ventas del Q3 FY26; 5 mayores clientes finales ≈ 55 % |

## Paso 6 — Conclusión

1. **Rango de valor:** Pesimista $101,50 — Base $266,04 — Optimista $421,41. El precio ($300,86) está algo por encima del base. **Valor esperado ponderado: $263,75.**
2. **Margen de seguridad (base):** (266,04 − 300,86) / 266,04 = **−13,1 %**. Frente al valor ponderado: −14,1 %.
3. **Veredicto: valor razonable** (cotiza con una prima moderada frente al escenario base; dentro de la banda de ±15 %). Confianza **media**: generación de caja verificada, pero deuda y acciones con datos del Q1, y riesgo de concentración y de garantías difícil de cuantificar.
4. **Dato de invalidación:** la guía de IA para FY27 en los resultados del 9-dic. Si confirma $115B o más, el valor tiende al optimista; si confirma el recorte de Google o baja de $100B, tiende al pesimista.
5. **Contexto competitivo y de mercado:**

   Broadcom domina los ASIC de IA a medida y las redes Ethernet de IA, con Google, Anthropic y OpenAI como pilares. MediaTek y los diseños internos de los clientes son la amenaza principal: el 20-nov-2026, Ming-Chi Kuo informó de un posible recorte de ≈ 20 % en los TPU 8i de Google, no confirmado.

   La acción cayó un 12,2 % el 20-nov (−$191B de capitalización) y marcó un mínimo de 52 semanas de $278 el 25-nov. Cotiza a ≈ 15,5x el BPA de FY27, por debajo de su media a 3 años (≈ 30x). El mercado descuenta riesgo de concentración y de financiación de clientes.
6. **Aviso:** análisis formativo; no constituye recomendación de inversión. El momento de entrada se decide con análisis técnico y gestión del riesgo.

## Fuentes

- https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000080/avgo-20260802.htm
- https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-first-quarter-fiscal-year-2026-financial
- https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-second-quarter-fiscal-year-2026-financial
- https://www.sec.gov/Archives/edgar/data/1730168/000173016826000016/avgo-20260201.htm
- https://www.tikr.com/blog/is-broadcom-a-momentum-stock-wearing-a-value-costume-its-december-9-report-will-tell
- https://multiples.vc/ai-chips-hardware-valuation-multiples
