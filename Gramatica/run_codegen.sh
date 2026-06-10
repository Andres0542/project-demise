#!/bin/bash
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON="${ROOT}/venv/bin/python"
ARCHIVO="${1:-ejemplos/test_mapa_codegen.dmse}"
SALIDA="${2:-salida.ll}"
cd "$(dirname "$0")"
"$PYTHON" main.py "$ARCHIVO" "$SALIDA"
