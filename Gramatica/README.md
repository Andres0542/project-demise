# Demise Engine

## 🎮 Menu Grafico Interactivo

Ejecuta el driver con menu grafico profesional:

```bash
py -3.13 driver.py
```

### Opciones del Menu
- **RayCasting** - Renderizado 3D basico
- **FloorCasting** - Renderizado de pisos
- **MAZE** - Laberinto 3D
- **Cambiar Resolucion** - Ajustar tamaño de ventana
- **Cambiar FOV** - Campo de vision
- **FPS Cap** - Limite de frames

## 🚀 Ejecucion Directa
Para ejecutar con archivo de configuracion:

```bash
py -3.13 driver.py <config_file>
```

### Ejemplos
```bash
# Floorcasting
py -3.13 driver.py ../Ejemplo-1 (Floorcasting)/Ejemplo1.txt

# Raycasting
py -3.13 driver.py ../Ejemplo-2 (RayCasting)/Ejercicio1.txt

# Maze
py -3.13 driver.py ../Ejemplo-2 (RayCasting)/Ejercicio2.txt
```

## 🎨 Caracteristicas

- **Menu grafico**
- **Configuraciones** de resolucion, FOV y FPS
- **Python 3.13** con dependencias automaticas
- **Renderizado 3D** con pygame y numba

## 📖 Vista General de Gramatica

### Elementos de nuestra Syntax

#### 1. Declaracion de Sprites
```
sprite floor -> 'floor.png'
sprite ceiling -> 'ceiling.png'
sprite wall -> 'wall.png'
sprite skybox -> 'skybox.jpg'
```

#### 2. Declaracion de Filtros
```
filter(hotline, ceiling)
filter(blur, floor)
```

#### 3. Comandos de Prueba
```
floorcasting_test
raycasting_test
raycasting_maze_test
reflexing_floor
```

**Version:** 1.1 
