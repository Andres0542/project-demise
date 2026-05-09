import os
from .errors import (
    SemanticError,
    ResourceNotFoundError,
    DuplicateSpriteError,
    DuplicatePathError,
    DuplicateNPCError,
    DuplicateWeaponError,
    DuplicateMusicError,
    DuplicateMapError,
    DuplicateUIError,
    DuplicateLightningError,
    LightningRangeError,
    MapCoordError,
    MapNotDeclaredError,
    NPCNotDeclaredError,
    WeaponNotDeclaredError,
    InvalidWeaponBehaviorError,
)

# Comportamientos de arma válidos según gramatica.txt
VALID_WEAPON_BEHAVIORS = {
    "chainsaw", "fists", "pistol", "shotgun",
    "chaingun", "rocket_launcher", "energy_rifle", "BFG6000",
}

# Tipos de sprite válidos según la gramática
VALID_SPRITE_TYPES = {"wall", "floor", "ceiling", "sky"}


class SymbolTable:
    def __init__(self):
        # sprites: { tipo_sprite -> {"path": str, "line": int} }
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

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _check_file_exists(self, path: str, line: int):
        """Lanza ResourceNotFoundError si el archivo no existe en disco."""
        if not os.path.exists(path):
            raise ResourceNotFoundError(path, line)

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
            raise DuplicatePathError(path, line)

    # ── Sprites ───────────────────────────────────────────────────────────────

    def declare_sprite(self, sprite_type: str, path: str, line: int):
        """Registra un sprite de entorno (wall, floor, ceiling, sky)."""
        if sprite_type in self.sprites:
            raise DuplicateSpriteError(sprite_type, line)
        self._check_file_exists(path, line)
        self._check_path_unique(path, line)
        self.sprites[sprite_type] = {"path": path, "line": line}

    # ── Filtros ───────────────────────────────────────────────────────────────

    def declare_filter(self, filter_name: str, target: str, line: int):
        """Registra un filtro visual sobre floor o ceiling."""
        self.filters.append({"filter": filter_name, "target": target, "line": line})

    # ── NPCs ──────────────────────────────────────────────────────────────────

    def declare_npc(self, name: str, path: str, line: int):
        """Registra un NPC y su sprite."""
        if name in self.npcs:
            raise DuplicateNPCError(name, line)
        self._check_file_exists(path, line)
        self._check_path_unique(path, line)
        self.npcs[name] = {"path": path, "line": line}

    # ── Música ────────────────────────────────────────────────────────────────

    def declare_music(self, path: str, line: int):
        """Registra la pista de música del nivel."""
        if self.music is not None:
            raise DuplicateMusicError(line)
        self._check_file_exists(path, line)
        self.music = {"path": path, "line": line}

    # ── Mapa ──────────────────────────────────────────────────────────────────

    def declare_map(self, grid: list[list[int]], line: int):
        """Registra la matriz del mapa del nivel."""
        if self.map_grid is not None:
            raise DuplicateMapError(line)
        self.map_grid = grid
        self.map_line = line

    # ── Iluminación ───────────────────────────────────────────────────────────

    def declare_lightning(self, value: int, line: int):
        """Registra el nivel de iluminación (0–100)."""
        if self.lightning is not None:
            raise DuplicateLightningError(line)
        if not (0 <= value <= 100):
            raise LightningRangeError(value, line)
        self.lightning = value

    # ── UI ────────────────────────────────────────────────────────────────────

    def declare_ui(self, path: str, line: int):
        """Registra la imagen de HUD del nivel."""
        if self.ui is not None:
            raise DuplicateUIError(line)
        self._check_file_exists(path, line)
        self.ui = {"path": path, "line": line}

    # ── Posicionamiento de NPCs ───────────────────────────────────────────────

    def declare_npc_position(self, name: str, col: int, row: int, line: int):
        """
        Registra la posición de un NPC en la matriz.
        Valida que:
          - El mapa ya fue declarado.
          - El NPC fue declarado previamente.
          - Las coordenadas están dentro de los límites del mapa.
        """
        if self.map_grid is None:
            raise MapNotDeclaredError(line)
        if name not in self.npcs:
            raise NPCNotDeclaredError(name, line)

        num_rows = len(self.map_grid)
        num_cols = len(self.map_grid[0]) if num_rows > 0 else 0

        # (col, row) → acceso map_grid[row][col]
        if not (0 <= row < num_rows and 0 <= col < num_cols):
            raise MapCoordError(name, col, row, line)

        self.npc_positions[name] = {"col": col, "row": row, "line": line}

    # ── Armas ─────────────────────────────────────────────────────────────────

    def declare_weapon(self, name: str, path: str, line: int):
        """Registra un arma y su sprite."""
        if name in self.weapons:
            raise DuplicateWeaponError(name, line)
        self._check_file_exists(path, line)
        self._check_path_unique(path, line)
        self.weapons[name] = {"path": path, "line": line}

    def declare_weapon_behavior(self, weapon_name: str, behavior: str, line: int):
        """
        Asigna un comportamiento predefinido a un arma.
        Valida que:
          - El arma fue declarada previamente.
          - El comportamiento es uno de los válidos.
        """
        if weapon_name not in self.weapons:
            raise WeaponNotDeclaredError(weapon_name, line)
        if behavior not in VALID_WEAPON_BEHAVIORS:
            raise InvalidWeaponBehaviorError(behavior, line)
        self.weapon_behaviors[weapon_name] = {"behavior": behavior, "line": line}
