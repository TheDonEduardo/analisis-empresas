# RKLB — Valoración (analista-de-valoracion)

**Fecha:** 2026-11-27 · **Modo:** encadenado (contrato confirmado) · **Cálculos:** `2026-11-27-dcf.py` (importes en $M)

## Paso 0 — Datos

| Dato | Valor | Periodo | Fuente |
| :--- | :--- | :--- | :--- |
| Precio | $47,02 (cierre 25-nov-2026); $50,46 en la sesión del 27-nov | — | IBKR |
| Acciones | 639,2M (30-sep-2026); 632,0M (4-nov, sin contar 7,45M pignoradas) | — | 10-Q Q3 (vía resumen) |
| Capitalización | ≈ $30.055M | — | Cálculo |
| Ventas | Q3 2026 $267,8M (+73 %); guía Q4 $270-290M; 2026e ≈ $1.000M (aprox.) | — | Comunicado Q3 |
| EBIT / beneficio neto | EBITDA ajustado del Q3 −$18M; pérdida neta del Q3 −$79,7M; BPA `no disponible` | Q3 2026 | Comunicado Q3 |
| OCF | Q3 +$7,2M | — | Call Q3 |
| Capex / SBC | `no disponible` | — | — |
| Deuda | Convertibles 2029: $1,3M. Préstamo puente de Iridium de $3.600M (se dispone al cierre) | — | 10-Q / 8-K |
| Caja + valores | $4.704M ($4.448M + $256M) | 30-sep-2026 | 10-Q Q3 |
| Consenso BPA | `no disponible` | — | — |

**Clasificación:** Sin beneficios.

## Paso 1 — DCF inverso

**No aplicable** (FCF negativo). Referencia por ventas: capitalización / ventas 2026e ≈ 30x.

## Paso 2 — DCF directo (contrato)

Supuestos: Año 0 = 2026e ($1.000M), incluye Iridium desde mediados de 2027; senda geométrica de ventas; quema explícita y rampa de margen; WACC 9 %; g 2,5 %.
Puente: `EV + (caja 4.704 − efectivo de Iridium 3.150 − deuda neta de Iridium 1.700) = EV − 146`.

| Escenario | Prob. | Ventas A5 / A10 | Margen FCFF | Quema | VP flujos | VP valor terminal | EV | Equity | Acciones | **Valor/acción** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Pesimista | 40 % | $2.000M / $3.000M | 5 % | −375 × 4 | −$830M | $999M | $169M | −$277M | 850M | **$0,00** (suelo) |
| Base | 40 % | $3.500M / $7.000M | 15 % | −400 × 2 | $1.915M | $6.994M (VT 16.558) | $8.909M | $8.763M | 760M | **$11,53** |
| Optimista | 20 % | $5.000M / $11.000M | 22 % | −500 | $5.563M | $16.120M (VT 38.162) | $21.683M | $21.537M | 720M | **$29,91** |

**Valor esperado ponderado** = 0,40 × 0 + 0,40 × 11,53 + 0,20 × 29,91 = 0 + 4,61 + 5,98 = **$10,59**

**Sensibilidad (base):**

| WACC \ g | 2 % | 2,5 % | 3 % |
| :--- | :--- | :--- | :--- |
| 8 % | 13,43 | 14,48 | 15,74 |
| 9 % | 10,83 | **11,53** | 12,35 |
| 10 % | 8,91 | 9,40 | 9,96 |

> **Nota:** el precio ($47) implica un EV de ≈ $30.000M, unas 4,3 veces el VP del valor terminal del escenario optimista. El mercado descuenta un resultado muy superior al contrato: o bien ventas a 10 años de más de $20.000M, o bien una valoración por "opcionalidad espacial" que el DCF no recoge. Con WACC 11 %: Base $7,80 / Opt $20,80.

## Paso 3 — Múltiplos (EV/Ventas)

Comparables (Firefly, Intuitive Machines, Planet, AST SpaceMobile, Iridium): múltiplos `no disponible` en esta sesión. RKLB: EV/Ventas 2026e ≈ 30x (sin Iridium). Media sectorial a 5 años: `no disponible`.

## Paso 4 — PEG

No aplicable (BPA negativo).

## Paso 5 — Calidad y riesgos

| Métrica | Dato |
| :--- | :--- |
| ROIC | No aplicable (pérdidas) |
| Deuda neta / EBITDA | Hoy caja neta de ≈ $4.700M; tras Iridium, deuda bruta ≈ $5.300M (puente + Iridium) frente a un EBITDA combinado de ≈ $480M → ≈ 1x neto (con la caja) |
| Márgenes | Margen bruto non-GAAP: 41,9 % → 38,4 % |
| Dilución | +17,6 % en 2026; ≈ +9 % adicional por Iridium (estimación) |
| Partidas no recurrentes | Costes de la operación de Iridium |
| Concentración | Gobierno de EE. UU. y defensa (`no disponible` %) |

## Paso 6 — Conclusión

1. **Rango de valor:** $0 — **$11,53** — $29,91. El precio ($47,02) está **por encima del optimista**. **Valor esperado ponderado: $10,59.**
2. **Margen de seguridad (base):** (11,53 − 47,02) / 11,53 = **−307,8 %**. Frente al valor ponderado: −344 %.
3. **Veredicto: sobrevalorada** frente al contrato. Confianza **baja**: el resultado depende por completo de supuestos de largo plazo (Neutron e Iridium) y el mercado valora RKLB con métricas de "líder espacial" que un DCF conservador no captura. Aun así, el precio exige que el escenario optimista se supere con creces.
4. **Dato de invalidación:** un primer vuelo de Neutron con éxito en 2027 y una cadencia de 10 o más vuelos en 2028, junto con la confirmación de ventas a 10 años por encima de $15.000M. Eso haría el contrato demasiado conservador.
5. **Contexto competitivo y de mercado:**

   Rocket Lab es el segundo lanzador de EE. UU. por cadencia, detrás de SpaceX, y fabricante de satélites y componentes. Neutron competirá con Falcon 9 y con nuevos entrantes (Firefly, Relativity). La compra de Iridium ($8.000M, cierre previsto a mediados de 2027) la convierte en operador de comunicaciones satelitales.

   La acción ha caído un 68,9 % desde el máximo de $151, con el retraso de Neutron a 2027 anunciado en los resultados del 9-nov-2026 y emisiones vía ATM (+17,6 % de acciones en 2026).
6. **Aviso:** análisis formativo; no constituye recomendación de inversión. El momento de entrada se decide con análisis técnico y gestión del riesgo.

## Fuentes

- https://www.sec.gov/Archives/edgar/data/0001819994/000181999426000073/rklb-11092026ex991.htm
- https://www.sec.gov/Archives/edgar/data/0001819994/000181999426000074/rklb-20260930.htm
- https://www.cnbc.com/2026/06/29/rocket-lab-buys-iridium.html
- https://seekingalpha.com/pr/20397311
