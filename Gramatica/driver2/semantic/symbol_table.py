from .errors import SemanticError 
import os
class Symbol:
    def __init__(self, name, path, scope, line):
        self.name = name    # El identificador (ej. "Player")
        self.path = path    # La ruta del recurso (ej. "res://player.png")
        self.scope = scope
        self.line = line
        self.used = False   # Para el reporte de variables no usadas
    
class SymbolTable:
    def __init__(self):
        self._table = {}
        self._scope_stack = ['global']
        # Diccionario para registrar sprites: { nombre_sprite: path }
        self.sprites = {} 

    def declare_sprite(self, name: str, path: str, line: int):
        # Validación 1: Nombre duplicado
        if name in self.sprites:
            raise SemanticError(f"El sprite '{name}' ya ha sido declarado.", line)
        
        if not os.path.exists(path):
            raise SemanticError(f"Error de Recurso: El archivo en '{path}' no existe.", line)

        # Validación 2: Path duplicado (Opcional, pero recomendado)
        if path in [s['path'] for s in self.sprites.values()]:
            raise SemanticError(f"La ruta '{path}' ya está en uso por otro sprite.", line)

        # Registro
        self.sprites[name] = {
            "path": path,
            "line": line
        }