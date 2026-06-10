#!/bin/bash
set -e
CLANG="${CLANG:-$(command -v clang || command -v clang-16)}"
if [ -z "$CLANG" ]; then
  echo "clang no encontrado. Ejecuta: ./setup_deps.sh"
  exit 1
fi
"$CLANG" -S -emit-llvm main.c -o intermedio.ll
"$CLANG" intermedio.ll -lGL -lGLU -lglut -lm -lSDL2 -lSDL2_mixer -o a.out
