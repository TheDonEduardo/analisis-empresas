# analisis-empresas

Análisis fundamental y técnico de empresas. Creación de lista de observación y niveles para poder operarlas.

## Cómo se usa

Pide a Claude Code que analice una empresa y se ejecutarán, en orden, tres skills:

1. **`analista-de-tesis`** — tesis de inversión, auditoría forense (SEC), Red Team y contrato de inputs con probabilidades. Pausa para que confirmes los supuestos.
2. **`analista-de-valoracion`** — DCF inverso y directo, sensibilidad, múltiplos, PEG, calidad y riesgos → rango de valor y margen de seguridad.
3. **`gestor-de-ejecucion`** — fase de Weinstein, niveles, entrada sin FOMO, stop, sizing y veredicto operativo.

Ejemplo: `Analiza NVDA con la cadena completa: analista-de-tesis → analista-de-valoracion → gestor-de-ejecucion`.

## Estructura

```
.claude/
  agents/        explore (haiku, solo lectura) · implementer (sonnet) · code-improver
  skills/        analista-de-tesis · analista-de-valoracion · gestor-de-ejecucion
                 arena · trader-* (importadas de alpha-portfolio-bot)
  settings.json  plugins codex y ecc
analisis/<TICKER>/   informes en Markdown por fecha
seguimiento/         Seguimiento Análisis de Acciones.xlsx (respaldo local)
scripts/seguimiento.py   crear/actualizar la hoja local (1 ticker = 1 fila)
```

## Hoja de seguimiento

| Col | Campo | Origen |
| :-- | :-- | :-- |
| A | Ticker (formato GOOGLEFINANCE) | todas |
| B | Empresa | todas |
| C | Fecha Análisis | todas |
| D | Estado (`En cartera` / `Vigilancia` / `Descartada`) | todas |
| E | Veredicto Tesis | tesis |
| F | Precio Actual — **fórmula** | automática |
| G | Valor Base | valoración |
| H | Valor Pond. | valoración |
| I | Rango (Pes - Opt) | valoración |
| J | Margen Seg. (%) — **fórmula** | automática |
| K | Fase Weinstein | ejecución |
| L | Entrada / Pivote | ejecución |
| M | Stop Invalidación | ejecución |
| N | Dist. Stop (%) — **fórmula** | automática |
| O | Peso Máx. (%) | ejecución |
| P | Veredicto Operativo | ejecución |
| Q | Catalizador / Riesgo Clave | valoración / ejecución |

La hoja principal vive en Google Sheets (`Seguimiento Análisis de Acciones`). Para crearla, importa el `.xlsx` de `seguimiento/` en Google Drive y conviértelo a Hojas de cálculo de Google: la fórmula `GOOGLEFINANCE` de la columna F empezará a funcionar.

```bash
pip install -r requirements.txt
```

```bash
python scripts/seguimiento.py show
```

> Los análisis son formativos y no constituyen recomendación de inversión.
