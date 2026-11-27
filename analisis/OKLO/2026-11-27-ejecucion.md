# OKLO — Plan de ejecución (gestor-de-ejecucion)

**Fecha:** 2026-11-27 · **Datos:** barras diarias de IBKR (`2026-11-27-barras-ibkr.json`) · **Cálculos:** `scripts/tecnico.py`

## Paso 0 — Fotografía técnica

| Indicador | Valor actual | Lectura rápida |
| :--- | :--- | :--- |
| Precio | $19,47 (cierre 25-nov); $20,50 en la sesión del 27-nov | Cerca de mínimos |
| Rango 52 semanas | Máximo $115,72 / mínimo $17,28 (25-nov) | −83,2 % desde máximos |
| EMA 21 | $23,26 (−16,3 %) | Precio por debajo |
| SMA 50 / 150 / 200 | $29,24 / $44,82 / $48,53 (−33 % / −57 % / −60 %), todas cayendo | Tendencia bajista extrema |
| ATR(14) | $2,22 (**11,4 %**) | Volatilidad extrema |
| RSI(14) | 33,8 | Débil, cerca de la sobreventa |
| Volumen | Media de 5 días 7,1M frente a 6,7M de media en 50 días | Sin capitulación |
| Short Float / Days to Cover | `no disponible` | — |
| Próximos resultados | Q4 2026 ≈ mar-2027 (`no disponible`) | Sin riesgo binario inmediato por resultados (sí por noticias de la NRC) |

## Paso 1 — Fase y niveles

**Fase 4 (Bajista).** Máximos y mínimos decrecientes desde enero; todas las medias caen.

Volumen sin capitulación clara. La dilución vía ATM añade oferta constante en los rebotes. Fuerza relativa muy negativa.

| Tipo de nivel | Precio / Zona | Relevancia técnica |
| :--- | :--- | :--- |
| Soporte inmediato | $17,28 | Mínimo de 52 semanas (25-nov) |
| Soporte estructural | ≈ $16 | Caja por acción ($16,03): un suelo fundamental que la quema erosiona ≈ $1,5-2,5 por año |
| Resistencia inmediata | $22,9-24,1 | EMA 21 ($23,26) y máximos de mediados de noviembre |
| Pivote de confirmación | $27,73 | Máximo del rebote del 9-nov |

## Paso 2 — Escenarios

| Escenario | Condición exacta de activación | Zona de entrada | Stop | Distancia al stop |
| :--- | :--- | :--- | :--- | :--- |
| A. Recuperación del pivote | Cierre > $27,73 con volumen > 10M (1,5x la media) | $27,7-29,5 | $22,00 | 20,7 % (≈ 2,5 ATR) |
| B. Base sobre la caja | Varias semanas sin perder $17,28, cierre semanal > $24,10 y una noticia de la NRC (aceptación de la COLA) | $23,5-24,5 | $17,00 | ≈ 29 % (tamaño mínimo) |
| C. Espera (vigente) | Fase 4 sin base | Sin entrada | — | — |

ATR > 8 %: stops amplios y tamaño muy reducido.

## Paso 3 — Sizing

**Perfil:** Especulativo / Binario.

| Parámetro de riesgo | Propuesta concreta | Justificación |
| :--- | :--- | :--- |
| Peso máximo | **2 %** | Extremo inferior del rango especulativo (2-4 %): binario regulatorio y ATR del 11 % |
| Riesgo por operación | 0,5 % del capital | Con un stop del 20,7 %: 0,5 / 20,7 ≈ 2,4 %, limitado al 2 % |
| Tramos | 50 % en el escenario A o B y 50 % tras la aceptación de la COLA | Prohibido promediar a la baja |
| Salida | Stop a punto muerto a +1,5R; vender parte si el precio se duplica | — |

## Paso 4 — Encaje en la cartera del usuario

- Posición: 59 acciones, ≈ 1.068 € (**5,2 %**), precio medio ≈ $38,0 (−47,74 %).
- **Sobreponderación de 2,6 veces** el peso máximo (2 %).
- Es la única posición fuera de la temática de semis y software de IA, pero depende del mismo motor: la demanda eléctrica de los centros de datos de IA.
- **Stop de tesis frente a stop técnico:** la caja (≈ $16 por acción) limita en parte la caída a corto plazo, pero el DCF del contrato ($11,67 base) y la Fase 4 no justifican el 5,2 %. Opciones de gestión del riesgo:
  1. Reducir hacia el 2-3 % (≈ 23-35 acciones) en rebotes a $23-24.
  2. Mantener como opción de lotería con salida total si cierra por debajo de $16 (rotura de la caja por acción).

  No añadir hasta que se active el escenario A o B.

## Paso 5 — Veredicto

**No operable técnicamente ahora (Fase 4 / sin base).**

Alertas:
1. **Activación:** cierre > $27,73 con volumen > 10M.
2. **Invalidación:** cierre < $17,28 (aviso) y < $16 (rotura de la caja por acción).
3. **Calendario y noticias:** presentación o aceptación de la COLA de Aurora (NRC), anuncios de ATM y resultados del Q4 2026 (≈ mar-2027).

Plan estrictamente formativo; no constituye recomendación de inversión personalizada.

## Paso 6 — Registro

- Google Sheets, fila 7: OKLO registrada. Las fórmulas F, J y N quedan intactas: precio $19,47, margen −66,84 %, distancia al stop 20,66 %.
- Respaldo local: `seguimiento/Seguimiento Análisis de Acciones.xlsx`.
