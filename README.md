# project-demise
Raycasting tech simplified even more for Python users to use!!! Only your perturbated imagination is the limit

# 🎮 Demise — Lenguaje de Configuración de Niveles

**Demise** es un lenguaje de dominio específico (DSL) diseñado para configurar niveles de un videojuego tipo *raycasting* (estilo Doom/Wolfenstein). Permite declarar recursos visuales, mapas, enemigos, armas, música e iluminación mediante una sintaxis simple y legible.

La gramática está definida en ANTLR4 (`Demise.g4`) y su análisis semántico es implementado en Python.

---

## 📋 Tabla de contenidos

- [Estructura general](#estructura-general)
- [Declaraciones](#declaraciones)
  - [sprite](#sprite)
  - [filter](#filter)
  - [npc](#npc)
  - [music](#music)
  - [map](#map)
  - [lightning](#lightning)
  - [UI](#ui)
  - [npcPositioning](#npcpositioning)
  - [weapon](#weapon)
  - [weaponLogic](#weaponlogic)
  - [testCommand](#testcommand)
- [Comentarios](#comentarios)
- [Tokens y tipos de datos](#tokens-y-tipos-de-datos)
- [Reglas semánticas](#reglas-semánticas)
- [Advertencias](#advertencias)
- [Ejemplo completo](#ejemplo-completo)

---

## Estructura general

Un programa Demise es una secuencia de **declaraciones** (`statement`) en cualquier orden, terminada por el fin de archivo. No hay una estructura de bloques obligatoria ni un orden forzado entre declaraciones (salvo las dependencias semánticas indicadas más abajo).

```
programa
  └── statement*
        ├── spriteDeclaration
        ├── filter
        ├── npcDeclaration
        ├── musicDeclaration
        ├── mapDeclaration
        ├── lightningDeclaration
        ├── uiDeclaration
        ├── npcPositioning
        ├── weaponDeclaration
        ├── weaponLogic
        ├── testCommand
        └── comentario
```

---

## Declaraciones

### `sprite`

Declara la textura que se usará para un tipo de superficie del entorno. Se aplica automáticamente durante el renderizado.

```
sprite <tipo> -> '<ruta>'
```

**Tipos válidos:** `wall` · `floor` · `sky`

```
sprite wall  -> 'wall.jpg'
sprite floor -> 'floor.jpg'
sprite sky   -> 'sky.jpg'
```

**Reglas semánticas:**
- El archivo referenciado debe existir en disco.
- Cada tipo (`wall`, `floor`, `sky`) solo puede declararse **una vez**.
- La ruta no puede estar en uso por otro símbolo.

---

### `filter`

Aplica un filtro visual (efecto de color o post-proceso) sobre una superficie del entorno.

```
filter(<nombre_filtro>, <target>)
```

**Targets válidos:** `floor` · `ceiling`

```
filter(hotline,    ceiling)
filter(bloody_moon, ceiling)
filter(green_waste, floor)
```

**Reglas semánticas:**
- El `<target>` debe ser `floor` o `ceiling`. Cualquier otro valor genera un error.
- Se pueden declarar múltiples filtros sobre el mismo target.

---

### `npc`

Declara un enemigo y la ruta al sprite que lo representa.

```
npc <nombre> -> '<ruta>'
```

```
npc imp       -> 'Imp.jpg'
npc Cacodemon -> 'Cacodemon.jpg'
npc Leo       -> 'Leo.jpg'
```

**Reglas semánticas:**
- El archivo referenciado debe existir en disco.
- El nombre de cada NPC debe ser **único**.
- La ruta no puede estar en uso por otro símbolo.

---

### `music`

Declara la pista de música de fondo del nivel. Sonará en loop infinito.

```
music -> '<ruta>'
```

```
music -> 'Numb.mp3'
```

**Reglas semánticas:**
- El archivo referenciado debe existir en disco.
- Solo puede declararse **una vez** por nivel.

---

### `map`

Define la matriz del mapa del nivel. Cada fila va entre corchetes `[...]` y el mapa termina con `;`.

```
map ->
[fila_0]
[fila_1]
...
[fila_N];
```

**Valores de celda:**

| Valor | Significado |
|-------|-------------|
| `0` | Espacio transitable (el jugador puede moverse aquí) |
| `1` | Pared (bloquea el movimiento y se renderiza con el sprite `wall`) |
| `2` | Salida del nivel |

```
map ->
[1 1 1 1 1 1 1 1 1 1]
[1 0 0 0 0 0 0 0 0 1]
[1 0 0 0 0 0 0 0 0 1]
[1 0 0 0 2 0 0 0 0 1]
[1 0 0 0 0 0 0 0 0 1]
[1 1 1 1 1 1 1 1 1 1];
```

> ⚠️ El punto y coma final `;` es **obligatorio**. Su ausencia genera un error sintáctico.

**Reglas semánticas:**
- Solo puede declararse **un mapa** por nivel.
- El mapa debe ser declarado **antes** de posicionar NPCs.

---

### `lightning`

Define el nivel de iluminación global del nivel.

```
lightning -> <valor>
```

```
lightning -> 50
```

**Rango válido:** `0` (oscuridad total) a `100` (iluminación máxima).

**Reglas semánticas:**
- El valor debe estar en el rango `[0, 100]`. Valores fuera de rango generan error.
- Solo puede declararse **una vez** por nivel.

---

### `UI`

Declara la imagen de la interfaz de usuario (HUD) que se superpondrá en pantalla durante el juego.

```
UI -> '<ruta>'
```

```
UI -> 'DoomUI.png'
```

**Reglas semánticas:**
- El archivo referenciado debe existir en disco.
- Solo puede declararse **una vez** por nivel.

---

### `npcPositioning`

Coloca un NPC previamente declarado en una posición específica del mapa.

```
<nombre_npc> -> (<col>, <fila>)
```

```
imp       -> (3, 3)
Cacodemon -> (2, 2)
```

**Reglas semánticas:**
- El **mapa debe haber sido declarado** antes de posicionar cualquier NPC.
- El NPC referenciado debe haber sido declarado previamente con `npc`.
- Las coordenadas `(col, fila)` deben estar dentro de los límites de la matriz del mapa. El acceso interno es `mapa[fila][col]`.

---

### `weapon`

Declara un arma y la ruta al sprite que la representa.

```
weapon <nombre> -> '<ruta>'
```

```
weapon shotgun -> 'Shotgun.png'
weapon BFG6000 -> 'BFG6000.png'
```

**Reglas semánticas:**
- El archivo referenciado debe existir en disco.
- El nombre de cada arma debe ser **único**.
- La ruta no puede estar en uso por otro símbolo.

---

### `weaponLogic`

Asigna un comportamiento de disparo predefinido a un arma declarada.

```
<nombre_arma> -> <comportamiento>
```

```
shotgun -> shotgun
BFG6000 -> BFG6000
```

**Comportamientos válidos:**

| Token | Descripción |
|-------|-------------|
| `chainsaw` | Motosierra (cuerpo a cuerpo) |
| `fist` | Puños (cuerpo a cuerpo) |
| `pistol` | Pistola estándar |
| `shotgun` | Escopeta |
| `chaingun` | Ametralladora |
| `rocket_launcher` | Lanzacohetes |
| `energy_rifle` | Rifle de energía |
| `BFG6000` | BFG 9000 |

**Reglas semánticas:**
- El arma referenciada debe haber sido declarada previamente con `weapon`.
- El comportamiento debe ser uno de los listados arriba. Cualquier otro valor genera un error.

---

### `testCommand`

Ejecuta un modo de prueba predefinido del motor de renderizado. Útil durante el desarrollo.

```
floorcasting_test
raycasting_test
raycasting_maze_test
```

| Comando | Descripción |
|---------|-------------|
| `floorcasting_test` | Prueba del renderizado de suelo y techo |
| `raycasting_test` | Prueba básica del motor de raycasting |
| `raycasting_maze_test` | Prueba del raycasting con un laberinto predefinido |

No requieren argumentos ni generan errores semánticos.

---

## Comentarios

Los comentarios son de una sola línea y comienzan con `//`. Pueden aparecer en cualquier lugar del programa.

```
// Esto es un comentario
sprite wall -> 'wall.jpg'   // Comentario al final de línea
```

---

## Tokens y tipos de datos

| Token | Formato | Ejemplo |
|-------|---------|---------|
| `STRING_LITERAL` | Texto entre comillas simples | `'wall.jpg'` |
| `INTEGER` | Número entero positivo | `50`, `0`, `100` |
| `ID` | Letra o `_`, seguido de letras, dígitos o `_` | `imp`, `BFG6000`, `my_npc` |
| `SPRITE_TYPE` | Palabra clave fija | `wall`, `floor`, `sky` |
| `WEAPON_LOGIC` | Palabra clave fija | `shotgun`, `BFG6000`, ... |
| `ARROW` | Símbolo de asignación | `->` |

> Los espacios y tabulaciones (`\t`, ` `) son ignorados por el lexer. Los saltos de línea son reconocidos como token `ESPACIO` pero no afectan la semántica.

---

## Reglas semánticas

Resumen de todas las validaciones aplicadas durante el análisis semántico:

| Regla | Error lanzado |
|-------|---------------|
| Sprite de mismo tipo declarado más de una vez | `DuplicateSpriteError` |
| Ruta de archivo usada por más de un símbolo | `DuplicatePathError` |
| Archivo referenciado no existe en disco | `ResourceNotFoundError` |
| NPC declarado más de una vez con el mismo nombre | `DuplicateNPCError` |
| Arma declarada más de una vez con el mismo nombre | `DuplicateWeaponError` |
| `music` declarada más de una vez | `DuplicateMusicError` |
| `map` declarado más de una vez | `DuplicateMapError` |
| `UI` declarada más de una vez | `DuplicateUIError` |
| `lightning` declarado más de una vez | `DuplicateLightningError` |
| Valor de `lightning` fuera de `[0, 100]` | `LightningRangeError` |
| NPC posicionado antes de declarar el mapa | `MapNotDeclaredError` |
| NPC posicionado sin haber sido declarado | `NPCNotDeclaredError` |
| Coordenadas de NPC fuera de los límites del mapa | `MapCoordError` |
| `weaponLogic` aplicado a un arma no declarada | `WeaponNotDeclaredError` |
| Comportamiento de arma no reconocido | `InvalidWeaponBehaviorError` |
| Target de `filter` distinto de `floor` o `ceiling` | `InvalidFilterTargetError` |

---

## Advertencias

Las advertencias no detienen la compilación pero indican posibles inconsistencias en el nivel:

| Situación | Advertencia |
|-----------|-------------|
| NPC declarado pero sin posición en el mapa | `"El NPC 'X' fue declarado pero nunca posicionado en el mapa."` |
| Arma declarada sin `weaponLogic` asignado | `"El arma 'X' fue declarada pero no tiene un comportamiento asignado."` |

---

## Ejemplo completo

```
// === Texturas de entorno ===
sprite wall  -> 'wall.jpg'
sprite floor -> 'floor.jpg'
sprite sky   -> 'sky.jpg'

// === Filtros visuales ===
filter(hotline,    ceiling)
filter(green_waste, floor)

// === Enemigos ===
npc imp       -> 'Imp.jpg'
npc Cacodemon -> 'Cacodemon.jpg'

// === Música ===
music -> 'Numb.mp3'

// === Mapa del nivel ===
map ->
[1 1 1 1 1 1 1 1 1 1]
[1 0 0 0 0 0 0 0 0 1]
[1 0 0 0 0 0 0 0 0 1]
[1 0 0 0 0 0 0 0 0 1]
[1 0 0 0 2 0 0 0 0 1]
[1 0 0 0 0 0 0 0 0 1]
[1 0 0 0 0 0 0 0 0 1]
[1 0 0 0 0 0 0 0 0 1]
[1 0 0 0 0 0 0 0 0 1];

// === Iluminación ===
lightning -> 50

// === HUD ===
UI -> 'DoomUI.png'

// === Posicionamiento de enemigos ===
imp       -> (3, 3)
Cacodemon -> (2, 2)

// === Armas ===
weapon shotgun -> 'Shotgun.png'
weapon BFG6000 -> 'BFG6000.png'

shotgun -> shotgun
BFG6000 -> BFG6000

// === Test de motor ===
raycasting_test
```
