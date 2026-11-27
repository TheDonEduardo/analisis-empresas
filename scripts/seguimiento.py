#!/usr/bin/env python3
"""Hoja de seguimiento local: "Seguimiento Análisis de Acciones.xlsx" (pestaña "Seguimiento").

Réplica en Excel de la hoja de Google Sheets que usan las skills
analista-de-valoracion y gestor-de-ejecucion. Sirve como respaldo versionado
en el repositorio y como plantilla para importar en Google Sheets.

Uso:
    # Crear (o regenerar vacía) la plantilla
    python scripts/seguimiento.py init [--force]

    # Insertar o actualizar la fila de un ticker (1 acción = 1 fila)
    python scripts/seguimiento.py upsert --ticker NASDAQ:NVDA --empresa "NVIDIA" \
        --estado Vigilancia --veredicto-tesis "Sólida y verificable" \
        --valor-base 165 --rango "$120 - $210" --catalizador "Resultados 2026-02-25"

    # Ver el contenido
    python scripts/seguimiento.py show

Reglas que aplica el script:
  * Nunca duplica tickers (columna A).
  * Nunca sobrescribe las fórmulas de F (Precio Actual), J (Margen Seg. %) y N (Dist. Stop %).
  * Solo actualiza las columnas que se pasan como argumento; el resto se conserva.
  * El Estado (D) de una fila existente se conserva salvo que se indique otro.
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "seguimiento" / "Seguimiento Análisis de Acciones.xlsx"
SHEET = "Seguimiento"
MAX_ROWS = 200  # filas preparadas con fórmulas y desplegables

COLUMNS = [
    ("A", "Ticker", 16),
    ("B", "Empresa", 26),
    ("C", "Fecha Análisis", 14),
    ("D", "Estado", 13),
    ("E", "Veredicto Tesis", 22),
    ("F", "Precio Actual", 13),
    ("G", "Valor Base", 12),
    ("H", "Valor Pond.", 12),
    ("I", "Rango (Pes - Opt)", 18),
    ("J", "Margen Seg. %", 13),
    ("K", "Fase Weinstein", 17),
    ("L", "Entrada / Pivote", 15),
    ("M", "Stop Invalidación", 16),
    ("N", "Dist. Stop %", 12),
    ("O", "Peso Máx. (%)", 13),
    ("P", "Veredicto Operativo", 20),
    ("Q", "Catalizador / Riesgo Clave", 50),
]

LISTS = {
    "D": ["En cartera", "Vigilancia", "Descartada"],
    "E": ["Sólida y verificable", "Especulativa asimétrica", "No invertible"],
    "K": ["Fase 1 (Base)", "Fase 2 (Alcista)", "Fase 3 (Techo)", "Fase 4 (Bajista)"],
    "P": ["Ejecutable ahora", "Lista de vigilancia", "No operable ahora"],
}

FORMULA_COLS = {"F", "J", "N"}


def formulas(r: int) -> dict[str, str]:
    # GOOGLEFINANCE solo funciona en Google Sheets; en Excel F queda vacía
    # (IFERROR) y puede rellenarse a mano o con el complemento de datos de Excel.
    return {
        "F": f'=IFERROR(GOOGLEFINANCE(A{r},"price"),"")',
        "J": f'=IF(AND(ISNUMBER(G{r}),ISNUMBER(F{r}),G{r}<>0),(G{r}-F{r})/G{r},"")',
        "N": f'=IF(AND(ISNUMBER(L{r}),ISNUMBER(M{r}),L{r}<>0),(L{r}-M{r})/L{r},"")',
    }


def init(force: bool = False) -> None:
    if XLSX.exists() and not force:
        print(f"Ya existe: {XLSX} (usa --force para regenerarla vacía)")
        return
    XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = SHEET

    head_fill = PatternFill("solid", fgColor="1F3864")
    for col, name, width in COLUMNS:
        c = ws[f"{col}1"]
        c.value = name
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = head_fill
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[col].width = width
    ws.row_dimensions[1].height = 30
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = f"A1:Q{MAX_ROWS + 1}"

    formula_fill = PatternFill("solid", fgColor="EDEDED")
    for r in range(2, MAX_ROWS + 2):
        for col, f in formulas(r).items():
            ws[f"{col}{r}"] = f
            ws[f"{col}{r}"].fill = formula_fill
        ws[f"J{r}"].number_format = "0.0%"
        ws[f"N{r}"].number_format = "0.0%"
        ws[f"O{r}"].number_format = "0.0%"
        for col in ("F", "G", "H", "L", "M"):
            ws[f"{col}{r}"].number_format = "#,##0.00"
        ws[f"C{r}"].number_format = "yyyy-mm-dd"

    for col, values in LISTS.items():
        dv = DataValidation(type="list", formula1='"' + ",".join(values) + '"', allow_blank=True)
        dv.error = "Usa uno de los valores del desplegable"
        dv.showErrorMessage = True
        ws.add_data_validation(dv)
        dv.add(f"{col}2:{col}{MAX_ROWS + 1}")

    rng = f"J2:J{MAX_ROWS + 1}"
    ws.conditional_formatting.add(rng, CellIsRule(operator="greaterThanOrEqual", formula=["0.2"],
                                                  fill=PatternFill("solid", fgColor="C6EFCE")))
    ws.conditional_formatting.add(rng, CellIsRule(operator="lessThan", formula=["0"],
                                                  fill=PatternFill("solid", fgColor="FFC7CE")))

    # Pestaña de leyenda
    lg = wb.create_sheet("Leyenda")
    lg["A1"], lg["B1"] = "Columna", "Contenido / quién la rellena"
    lg["A1"].font = lg["B1"].font = Font(bold=True)
    legend = [
        ("A Ticker", "Formato GOOGLEFINANCE (NASDAQ:NVDA, NYSE:META, BME:ITX). Clave única: 1 acción = 1 fila."),
        ("B-C", "Empresa y fecha del último análisis (AAAA-MM-DD)."),
        ("D Estado", "En cartera / Vigilancia / Descartada. Se conserva si ya existía."),
        ("E Veredicto Tesis", "analista-de-tesis (vía valoracion o ejecucion)."),
        ("F Precio Actual", "FÓRMULA (GOOGLEFINANCE). No sobrescribir."),
        ("G-I", "analista-de-valoracion: Valor Base, Valor Ponderado, Rango Pes-Opt."),
        ("J Margen Seg. %", "FÓRMULA (G-F)/G. No sobrescribir."),
        ("K-M, O-P", "gestor-de-ejecucion: Fase, Entrada, Stop, Peso Máx., Veredicto Operativo."),
        ("N Dist. Stop %", "FÓRMULA (L-M)/L. No sobrescribir."),
        ("Q", "Catalizador o riesgo clave en una línea."),
    ]
    for i, (a, b) in enumerate(legend, start=2):
        lg[f"A{i}"], lg[f"B{i}"] = a, b
    lg.column_dimensions["A"].width = 20
    lg.column_dimensions["B"].width = 90

    wb.save(XLSX)
    print(f"Creada: {XLSX}")


FIELD_TO_COL = {
    "empresa": "B", "estado": "D", "veredicto_tesis": "E", "valor_base": "G",
    "valor_pond": "H", "rango": "I", "fase": "K", "entrada": "L", "stop": "M",
    "peso_max": "O", "veredicto_operativo": "P", "catalizador": "Q",
}
NUMERIC = {"G", "H", "L", "M"}


def _peso(value: str) -> float:
    v = value.strip().replace(",", ".")
    if v.endswith("%"):
        return float(v[:-1]) / 100
    f = float(v)
    return f / 100 if f > 1 else f


def upsert(args: argparse.Namespace) -> None:
    if not XLSX.exists():
        init()
    wb = load_workbook(XLSX)
    ws = wb[SHEET]
    ticker = args.ticker.strip().upper()

    target, first_empty = None, None
    for r in range(2, ws.max_row + 2):
        val = ws[f"A{r}"].value
        if val and str(val).strip().upper() == ticker:
            target = r
            break
        if not val and first_empty is None:
            first_empty = r
    is_new = target is None
    r = target or first_empty or ws.max_row + 1

    ws[f"A{r}"] = ticker
    ws[f"C{r}"] = dt.date.today() if not args.fecha else dt.date.fromisoformat(args.fecha)
    for field, col in FIELD_TO_COL.items():
        value = getattr(args, field)
        if value is None:
            continue
        if col in LISTS and value not in LISTS[col]:
            sys.exit(f"Valor no válido para {col}: {value!r}. Opciones: {LISTS[col]}")
        if col in NUMERIC:
            value = float(str(value).replace(",", "."))
        elif col == "O":
            value = _peso(value)
        ws[f"{col}{r}"] = value
    if is_new and args.estado is None:
        ws[f"D{r}"] = "Vigilancia"
    # Garantiza que las fórmulas siguen en su sitio (filas más allá de MAX_ROWS)
    for col, f in formulas(r).items():
        if not ws[f"{col}{r}"].value:
            ws[f"{col}{r}"] = f

    wb.save(XLSX)
    print(f"{'Añadida' if is_new else 'Actualizada'} fila {r}: {ticker}")


def show() -> None:
    if not XLSX.exists():
        sys.exit("No existe la hoja. Ejecuta: python scripts/seguimiento.py init")
    ws = load_workbook(XLSX)[SHEET]
    for row in ws.iter_rows(min_row=1, values_only=True):
        if row[0] is None:
            continue
        print(" | ".join("" if v is None or (isinstance(v, str) and v.startswith("=")) else str(v) for v in row))


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    pi = sub.add_parser("init")
    pi.add_argument("--force", action="store_true")
    sub.add_parser("show")
    pu = sub.add_parser("upsert")
    pu.add_argument("--ticker", required=True)
    pu.add_argument("--fecha", help="AAAA-MM-DD (por defecto hoy)")
    for field in FIELD_TO_COL:
        pu.add_argument("--" + field.replace("_", "-"), dest=field)
    a = p.parse_args()
    if a.cmd == "init":
        init(a.force)
    elif a.cmd == "upsert":
        upsert(a)
    else:
        show()


if __name__ == "__main__":
    main()
