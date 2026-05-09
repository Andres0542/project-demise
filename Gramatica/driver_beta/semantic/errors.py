class SemanticError(Exception):
    """Error semántico genérico con número de línea."""

    def __init__(self, message: str, line: int):
        super().__init__(message)
        self.message = message
        self.line = line

    def __str__(self):
        return f"[Error Semántico, línea {self.line}] {self.message}"


# ── Errores de recursos (archivo no encontrado) ────────────────────────────────

class ResourceNotFoundError(SemanticError):
    def __init__(self, path: str, line: int):
        super().__init__(f"El archivo '{path}' no existe.", line)


# ── Errores de redeclaración ───────────────────────────────────────────────────

class DuplicateSpriteError(SemanticError):
    def __init__(self, name: str, line: int):
        super().__init__(f"El sprite '{name}' ya fue declarado.", line)


class DuplicatePathError(SemanticError):
    def __init__(self, path: str, line: int):
        super().__init__(f"La ruta '{path}' ya está en uso por otro símbolo.", line)


class DuplicateNPCError(SemanticError):
    def __init__(self, name: str, line: int):
        super().__init__(f"El NPC '{name}' ya fue declarado.", line)


class DuplicateWeaponError(SemanticError):
    def __init__(self, name: str, line: int):
        super().__init__(f"El arma '{name}' ya fue declarada.", line)


class DuplicateMusicError(SemanticError):
    def __init__(self, line: int):
        super().__init__("Ya se declaró una pista de música para este nivel.", line)


class DuplicateMapError(SemanticError):
    def __init__(self, line: int):
        super().__init__("Ya se declaró un mapa para este nivel.", line)


class DuplicateUIError(SemanticError):
    def __init__(self, line: int):
        super().__init__("Ya se declaró una UI para este nivel.", line)


class DuplicateLightningError(SemanticError):
    def __init__(self, line: int):
        super().__init__("Ya se declaró un valor de iluminación para este nivel.", line)


# ── Errores de rango y valores ─────────────────────────────────────────────────

class LightningRangeError(SemanticError):
    def __init__(self, value: int, line: int):
        super().__init__(
            f"El valor de iluminación '{value}' está fuera de rango (0–100).", line
        )


class MapCoordError(SemanticError):
    def __init__(self, npc: str, col: int, row: int, line: int):
        super().__init__(
            f"La posición ({col},{row}) del NPC '{npc}' está fuera de los límites del mapa.",
            line,
        )


class MapNotDeclaredError(SemanticError):
    def __init__(self, line: int):
        super().__init__(
            "Se intentó posicionar un NPC pero el mapa aún no fue declarado.", line
        )


class NPCNotDeclaredError(SemanticError):
    def __init__(self, name: str, line: int):
        super().__init__(
            f"El NPC '{name}' no fue declarado antes de ser posicionado.", line
        )


class WeaponNotDeclaredError(SemanticError):
    def __init__(self, name: str, line: int):
        super().__init__(
            f"El arma '{name}' no fue declarada antes de asignarle un comportamiento.",
            line,
        )


class InvalidWeaponBehaviorError(SemanticError):
    VALID = {
        "chainsaw", "fists", "pistol", "shotgun",
        "chaingun", "rocket_launcher", "energy_rifle", "BFG6000",
    }

    def __init__(self, behavior: str, line: int):
        super().__init__(
            f"El comportamiento de arma '{behavior}' no es válido. "
            f"Valores aceptados: {', '.join(sorted(self.VALID))}.",
            line,
        )
