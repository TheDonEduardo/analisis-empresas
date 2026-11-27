# CLAUDE.md — analisis-empresas

Repositorio para el **análisis fundamental y técnico de empresas cotizadas**, con una hoja de seguimiento que resume lo más importante de cada análisis (una fila por acción).

## Regla de delegación (obligatoria)

El agente principal **planifica y coordina; no ejecuta el trabajo de archivos él mismo**:

- **Toda lectura o búsqueda en el repositorio** (abrir archivos, buscar con patrones, revisar skills, análisis previos o la hoja de seguimiento) se delega en el subagente **`explore`** (`.claude/agents/explore.md`, modelo haiku, solo lectura).
- **Toda escritura de código o archivos** (crear/editar scripts, skills, informes, actualizar la hoja local, ejecutar tests) se delega en el subagente **`implementer`** (`.claude/agents/implementer.md`, modelo sonnet).
- El agente principal se limita a: entender la petición, planificar, lanzar los subagentes con instrucciones concretas, integrar sus resultados, hacer la investigación web de las skills de análisis y responder al usuario.
- Excepción: comandos git (commit/push) y lecturas triviales de la respuesta de un subagente.

## Cadena de análisis (en este orden)

| Orden | Skill | Qué entrega | Escribe en la hoja |
| :--- | :--- | :--- | :--- |
| 1 | `analista-de-tesis` | Tesis, auditoría forense, Red Team y **contrato de inputs** con probabilidades | No |
| 2 | `analista-de-valoracion` | Rango de valor (pes/base/opt), valor ponderado, margen de seguridad | `A–E`, `G–I`, `Q` |
| 3 | `gestor-de-ejecucion` | Fase Weinstein, niveles, entrada/stop, sizing, veredicto operativo | `A–E`, `G–I`, `K–M`, `O–Q` |

- Entre la skill 1 y la 2 hay una **pausa de control humano**: el usuario confirma o ajusta el contrato de inputs.
- Si la cadena completa se ejecuta en el mismo turno, el registro en la hoja se consolida una sola vez en `gestor-de-ejecucion`.
- `analista-de-valoracion` y `gestor-de-ejecucion` también funcionan de forma independiente.

## Hoja de seguimiento

- **Principal:** Google Sheets `Seguimiento Análisis de Acciones` (ID `1e1tnkq22SdkMAd8t6GS4-uAjSux77Gh7XwjgFuqmVHk`), pestaña `Seguimiento`. Leer/escribir con el conector Google Sheets (`get_values`, `update_values`) por rangos concretos de la fila del ticker, nunca tocando `F`, `J` y `N`.
- **Respaldo local versionado:** `seguimiento/Seguimiento Análisis de Acciones.xlsx`, gestionado **solo** con `scripts/seguimiento.py` (`init`, `upsert`, `show`).
- Reglas inviolables: 1 ticker = 1 fila (columna `A`); nunca sobrescribir las fórmulas `F` (Precio Actual), `J` (Margen Seg. %) y `N` (Dist. Stop %); no borrar valores existentes de `K–P` al actualizar datos fundamentales; usar exactamente los valores de los desplegables (`D`, `E`, `K`, `P`); rellenar `R` (Modelo / Fuente) con `Claude` (o `Consenso Claude + X`) y no tocar nunca `S` (Notas 2ª Opinión).

## Dónde guardar los informes

`analisis/<TICKER>/AAAA-MM-DD-<tesis|valoracion|ejecucion>.md` (ticker sin prefijo de mercado, p. ej. `analisis/NVDA/2026-11-27-tesis.md`).

## Otras skills disponibles

Importadas de `alpha-portfolio-bot`: `arena` y la familia `trader-*` (scanner, news, entry, exit, timemachine, budget, risk, broker, alerts, analyst, pelosi). Agente adicional: `code-improver` (revisión de código, solo lectura). Plugins habilitados en `.claude/settings.json`: `codex` (de `TheDonEduardo/codex-plugin-cc`) y `ecc`.

## Normas generales

- Idioma: español.
- Nunca inventar datos financieros: si no está verificado, `no disponible`.
- Los análisis son formativos y no constituyen recomendación de inversión.
- Nunca guardar claves de API ni tokens en el repositorio; usar variables de entorno.
