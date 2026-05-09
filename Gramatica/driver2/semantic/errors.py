#class SemanticError(Exception):
#    def __init__(self, message: str, line: int = 0):
#        super().__init__(f'[Error Semántico, línea {line}] {message}')
#        self.line = line
class SemanticError(Exception):
    def __init__(self, message, line):
        super().__init__(message)
        self.message = message  # Aquí definimos el atributo explícitamente
        self.line = line

    def __str__(self):
        return f"[Error Semántico, línea {self.line}] {self.message}"