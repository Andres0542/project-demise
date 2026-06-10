#!/bin/bash
set -e
LLI="${LLI:-$(command -v lli || command -v lli-16)}"
if [ -z "$LLI" ]; then
  echo "lli no encontrado. Ejecuta: ./setup_deps.sh"
  exit 1
fi
"$LLI" -load=libGL.so -load=libGLU.so -load=libglut.so -load=libSDL2.so -load=libSDL2_mixer.so intermedio.ll
