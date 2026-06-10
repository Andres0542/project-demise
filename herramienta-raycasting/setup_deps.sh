#!/bin/bash
set -e

PACKAGES=(
  clang llvm
  freeglut3-dev
  libsdl2-dev
  libsdl2-mixer-dev
  libgl1-mesa-dev
)

install_packages() {
  sudo apt-get install -y --no-install-recommends "${PACKAGES[@]}"
}

echo "Instalando dependencias (sin actualizar repositorios)..."
if install_packages; then
  echo "Dependencias instaladas. Ejecuta: ./comandos.sh"
  exit 0
fi

echo ""
echo "La instalación directa falló. Intentando apt-get update..."
if ! sudo apt-get update; then
  echo ""
  echo "⚠️  apt-get update falló (repositorios rotos en tu sistema)."
  echo "    Suele ser por: cloud.r-project.org (zara-cran40) o downloads.cursor.com."
  echo ""
  echo "    Arregla temporalmente con uno de estos:"
  echo "      sudo sed -i '/zara-cran40/d' /etc/apt/sources.list /etc/apt/sources.list.d/*.list 2>/dev/null"
  echo "      sudo rm /etc/apt/sources.list.d/cursor*.list 2>/dev/null"
  echo "    Luego vuelve a ejecutar: ./setup_deps.sh"
  echo ""
  echo "    O instala manualmente:"
  echo "      sudo apt-get install -y clang llvm freeglut3-dev libsdl2-dev libsdl2-mixer-dev libgl1-mesa-dev"
  exit 1
fi

install_packages
echo "Dependencias instaladas. Ejecuta: ./comandos.sh"
