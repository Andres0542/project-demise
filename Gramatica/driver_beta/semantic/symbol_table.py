import os
from .errors import SemanticError
# Comportamientos de arma válidos según WEAPON_LOGIC en Demise.g4.
VALID_WEAPON_BEHAVIORS = {
    "chainsaw", "fist", "pistol", "shotgun",
    "chaingun", "rocket_launcher", "energy_rifle", "BFG6000",
}


VALID_SPRITE_TYPES = {"wall", "floor", "sky"}

VALID_FILTER_TARGETS = {"floor", "ceiling"}


class SymbolTable:
    def __init__(self):
        # sprites: { sprite_type -> {"path": str, "line": int} }
        self.sprites: dict[str, dict] = {}

        # filters: lista de {"filter": str, "target": str, "line": int}
        self.filters: list[dict] = []

        # npcs: { nombre_npc -> {"path": str, "line": int} }
        self.npcs: dict[str, dict] = {}

        # music: {"path": str, "line": int} | None
        self.music: dict | None = None

        # map_grid: lista de listas de int | None
        self.map_grid: list[list[int]] | None = None
        self.map_line: int = 0

        # lightning: int | None
        self.lightning: int | None = None

        # ui: {"path": str, "line": int} | None
        self.ui: dict | None = None

        # npc_positions: { nombre_npc -> {"col": int, "row": int, "line": int} }
        self.npc_positions: dict[str, dict] = {}

        # weapons: { nombre_arma -> {"path": str, "line": int} }
        self.weapons: dict[str, dict] = {}

        # weapon_behaviors: { nombre_arma -> {"behavior": str, "line": int} }
        self.weapon_behaviors: dict[str, dict] = {}

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _check_file_exists(self, path: str, line: int):
        """Lanza ResourceNotFoundError si el archivo no existe en disco."""
        if not os.path.exists(path):
            raise SemanticError(f"El archivod '{path}' no existe.", line) #Mod

    def _check_path_unique(self, path: str, line: int):
        """Lanza DuplicatePathError si la ruta ya está registrada en cualquier símbolo."""
        all_paths = (
            [s["path"] for s in self.sprites.values()]
            + [n["path"] for n in self.npcs.values()]
            + [w["path"] for w in self.weapons.values()]
            + ([self.music["path"]] if self.music else [])
            + ([self.ui["path"]] if self.ui else [])
        )
        if path in all_paths:
            raise SemanticError(f"La ruta '{path}' ya está en uso por otro símbolo.", line) #Mod

    # ── Sprites ───────────────────────────────────────────────────────────────
    # Regla: SPRITE SPRITE_TYPE ARROW STRING_LITERAL
    # SPRITE_TYPE en el lexer: 'wall' | 'floor' | 'sky'

    def declare_sprite(self, sprite_type: str, path: str, line: int):
        """Registra un sprite de entorno (wall, floor, sky)."""
        if sprite_type in self.sprites:
            raise SemanticError(f"El sprite '{sprite_type}' ya fue declarado.", line) #Mod
        self._check_file_exists(path, line)
        self._check_path_unique(path, line)
        self.sprites[sprite_type] = {"path": path, "line": line}

    # ── Filtros ───────────────────────────────────────────────────────────────
    # Regla: FILTER LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN
    # El segundo IDENTIFIER (target) debe ser 'floor' o 'ceiling' (validación semántica).

    def declare_filter(self, filter_name: str, target: str, line: int):
        """
        Registra un filtro visual.
        Valida que el target sea 'floor' o 'ceiling'.
        """
        if target not in VALID_FILTER_TARGETS:
            raise SemanticError(f"El target '{target}' no es válido para el filtro.", line) #Mod
        self.filters.append({"filter": filter_name, "target": target, "line": line})

    # ── NPCs ──────────────────────────────────────────────────────────────────
    # Regla: NPC ID ARROW STRING_LITERAL

    def declare_npc(self, name: str, path: str, line: int):
        """Registra un NPC y su sprite."""
        if name in self.npcs: 
            raise SemanticError(f"El NPC '{name}' ya fue declarado.", line) #Mod
        self._check_file_exists(path, line)
        self._check_path_unique(path, line)
        self.npcs[name] = {"path": path, "line": line}

    # ── Música ────────────────────────────────────────────────────────────────
    # Regla: MUSIC ARROW STRING_LITERAL

    def declare_music(self, path: str, line: int):
        """Registra la pista de música del nivel."""
        if self.music is not None:
            raise SemanticError("Ya se declaró una pista de música para este nivel.", line) #Mod
        self._check_file_exists(path, line)
        self.music = {"path": path, "line": line}

    # ── Mapa ──────────────────────────────────────────────────────────────────
    # Regla: MAP ARROW mapRow+ SEMICOLON

    def declare_map(self, grid: list[list[int]], line: int):
        """Registra la matriz del mapa del nivel."""
        if self.map_grid is not None:
            raise SemanticError("Ya se declaró un mapa para este nivel.", line) #Mod
        self.map_grid = grid
        self.map_line = line

    # ── Iluminación ───────────────────────────────────────────────────────────
    # Regla: LIGHTNING ARROW INTEGER

    def declare_lightning(self, value: int, line: int):
        """Registra el nivel de iluminación (0–100)."""
        if self.lightning is not None:
            raise SemanticError("Ya se declaró un valor de iluminación para este nivel.", line) #Mod
        if not (0 <= value <= 100):
            raise LightningRangeError(value, line) #Mod
        self.lightning = value

    # ── UI ────────────────────────────────────────────────────────────────────
    # Regla: UI ARROW STRING_LITERAL

    def declare_ui(self, path: str, line: int):
        """Registra la imagen de HUD del nivel."""
        if self.ui is not None:
            raise SemanticError("Ya se declaró una UI para este nivel.", line) #Mod
        self._check_file_exists(path, line)
        self.ui = {"path": path, "line": line}

    # ── Posicionamiento de NPCs ───────────────────────────────────────────────
    # Regla: ID ARROW LPAREN INTEGER COMMA INTEGER RPAREN

    def declare_npc_position(self, name: str, col: int, row: int, line: int):
        """
        Registra la posición de un NPC en la matriz.
        Valida que:
          - El mapa ya fue declarado.
          - El NPC fue declarado previamente.
          - Las coordenadas (col, row) están dentro de los límites del mapa.
        """
        if self.map_grid is None:
            raise SemanticError("Se intentó posicionar un NPC pero el mapa aún no fue declarado.", line) #Mod
        if name not in self.npcs:
            raise SemanticError(f"El NPC '{name}' no fue declarado antes de ser posicionado.", line) #Mod

        num_rows = len(self.map_grid)
        num_cols = len(self.map_grid[0]) if num_rows > 0 else 0

        # Acceso: map_grid[row][col]
        if not (0 <= row < num_rows and 0 <= col < num_cols):
            raise MapCoordError(name, col, row, line) #Mod

        self.npc_positions[name] = {"col": col, "row": row, "line": line}

    # ── Armas ─────────────────────────────────────────────────────────────────
    # Regla: WEAPON ID ARROW STRING_LITERAL

    def declare_weapon(self, name: str, path: str, line: int):
        """Registra un arma y su sprite."""
        if name in self.weapons:
            raise SemanticError(f"El arma '{name}' ya fue declarada.", line) #Mod
        self._check_file_exists(path, line)
        self._check_path_unique(path, line)
        self.weapons[name] = {"path": path, "line": line}

    # ── Comportamiento de armas ───────────────────────────────────────────────
    # Regla: ID ARROW WEAPON_LOGIC
    # WEAPON_LOGIC en el lexer: 'chainsaw' | 'fist' | 'pistol' | 'shotgun' |
    #                            'chaingun' | 'rocket_launcher' | 'energy_rifle' | 'BFG6000'

    def declare_weapon_behavior(self, weapon_name: str, behavior: str, line: int):
        """
        Asigna un comportamiento predefinido a un arma.
        Valida que:
          - El arma fue declarada previamente.
          - El comportamiento es uno de los válidos según WEAPON_LOGIC en el .g4.
        Nota: en el parser ANTLR el token WEAPON_LOGIC ya garantiza que el
        behavior sea válido léxicamente; esta validación actúa como segunda
        barrera para usos programáticos directos del SymbolTable.
        """
        if weapon_name not in self.weapons:
            raise SemanticError(f"El arma '{weapon_name}' no fue declarada antes de asignarle un comportamiento.", line) #Mod
        if behavior not in VALID_WEAPON_BEHAVIORS:
            raise SemanticError(f"El comportamiento de arma '{behavior}' no es válido. Valores aceptados: {', '.join(sorted(VALID_WEAPON_BEHAVIORS))}.", line) #Mod
        self.weapon_behaviors[weapon_name] = {"behavior": behavior, "line": line}
