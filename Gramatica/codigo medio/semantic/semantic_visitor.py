from .symbol_table import SymbolTable
from .errors import SemanticError
from gen.DemiseVisitor import DemiseVisitor
from gen.DemiseParser import DemiseParser


class SemanticVisitor(DemiseVisitor):
    def __init__(self):
        self.symtab = SymbolTable()
        self.errors: list[SemanticError] = []

    # ── Helper ────────────────────────────────────────────────────────────────
    def _error(self, error: SemanticError):
        """Registra un error semántico y lo imprime."""
        self.errors.append(error)
        print(f"❌ {error}")

    def _strip(self, string_token: str) -> str:
        """Elimina las comillas simples de un STRING_LITERAL."""
        return string_token.strip("'")

    def visitSpriteDeclaration(self, ctx: DemiseParser.SpriteDeclarationContext):
        sprite_type = ctx.SPRITE_TYPE().getText()
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_sprite(sprite_type, path, line)
            print(f"Sprite registrado: tipo='{sprite_type}' | path='{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    def visitNpcDeclaration(self, ctx: DemiseParser.NpcDeclarationContext):
        name = ctx.ID().getText()           
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_npc(name, path, line)
            print(f"NPC registrado: '{name}' | path='{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    def visitMusicDeclaration(self, ctx: DemiseParser.MusicDeclarationContext):
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_music(path, line)
            print(f"Música registrada: '{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    def visitMapDeclaration(self, ctx: DemiseParser.MapDeclarationContext):
        line = ctx.start.line
        grid: list[list[int]] = []

        for row_ctx in ctx.mapRow():
            row = [int(tok.getText()) for tok in row_ctx.INTEGER()]
            grid.append(row)

        try:
            self.symtab.declare_map(grid, line)
            print(
                f"Mapa registrado: "
                f"{len(grid)} filas × {len(grid[0]) if grid else 0} columnas"
            )
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    def visitUiDeclaration(self, ctx: DemiseParser.UiDeclarationContext):
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_ui(path, line)
            print(f"UI registrada: '{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    def visitNpcPositioning(self, ctx: DemiseParser.NpcPositioningContext):
        name = ctx.ID().getText()           
        integers = ctx.INTEGER()
        col = int(integers[0].getText())
        row = int(integers[1].getText())
        line = ctx.start.line

        try:
            self.symtab.declare_npc_position(name, col, row, line)
            print(f"NPC '{name}' posicionado en ({col},{row})")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    def visitWeaponDeclaration(self, ctx: DemiseParser.WeaponDeclarationContext):
        name = ctx.ID().getText()           
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_weapon(name, path, line)
            print(f"Arma registrada: '{name}' | path='{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)


