from .symbol_table import SymbolTable
from .errors import SemanticError
from gen.DemiseVisitor import DemiseVisitor
from gen.DemiseParser import DemiseParser
from .Comportamiento.Floorcasting import Floorcasting


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

    # ── spriteDeclaration ─────────────────────────────────────────────────────
    # Regla: SPRITE SPRITE_TYPE ARROW STRING_LITERAL

    def visitSpriteDeclaration(self, ctx: DemiseParser.SpriteDeclarationContext):
        sprite_type = ctx.SPRITE_TYPE().getText()
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_sprite(sprite_type, path, line)
            print(f"✅ Sprite registrado: tipo='{sprite_type}' | path='{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── filter ────────────────────────────────────────────────────────────────
    # Regla: FILTER LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN
    # Nombre de regla en .g4: 'filter' → método visitFilter

    def visitFilter(self, ctx: DemiseParser.FilterContext):
        # Los dos IDENTIFIER son: [0] = nombre del filtro, [1] = superficie target
        identifiers = ctx.IDENTIFIER()
        filter_name = identifiers[0].getText()
        target      = identifiers[1].getText()
        line = ctx.start.line

        try:
            self.symtab.declare_filter(filter_name, target, line)
            print(f"✅ Filtro registrado: '{filter_name}' sobre '{target}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── npcDeclaration ────────────────────────────────────────────────────────
    # Regla: NPC IDENTIFIER ARROW STRING_LITERAL

    def visitNpcDeclaration(self, ctx: DemiseParser.NpcDeclarationContext):
        name = ctx.IDENTIFIER().getText()
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_npc(name, path, line)
            print(f"✅ NPC registrado: '{name}' | path='{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── musicDeclaration ──────────────────────────────────────────────────────
    # Regla: MUSIC ARROW STRING_LITERAL

    def visitMusicDeclaration(self, ctx: DemiseParser.MusicDeclarationContext):
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_music(path, line)
            print(f"✅ Música registrada: '{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── mapDeclaration ────────────────────────────────────────────────────────
    # Regla: MAP ARROW mapRow+ SEMICOLON
    # Subrregla mapRow: LBRACKET INTEGER+ RBRACKET

    def visitMapDeclaration(self, ctx: DemiseParser.MapDeclarationContext):
        line = ctx.start.line
        grid: list[list[int]] = []

        for row_ctx in ctx.mapRow():
            row = [int(tok.getText()) for tok in row_ctx.INTEGER()]
            grid.append(row)

        try:
            self.symtab.declare_map(grid, line)
            print(
                f"✅ Mapa registrado: "
                f"{len(grid)} filas × {len(grid[0]) if grid else 0} columnas"
            )
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── lightningDeclaration ──────────────────────────────────────────────────
    # Regla: LIGHTNING ARROW INTEGER

    def visitLightningDeclaration(self, ctx: DemiseParser.LightningDeclarationContext):
        value = int(ctx.INTEGER().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_lightning(value, line)
            print(f"✅ Iluminación registrada: {value}")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── UIDeclaration ─────────────────────────────────────────────────────────
    # Regla: UI ARROW STRING_LITERAL

    def visitUiDeclaration(self, ctx: DemiseParser.UiDeclarationContext):
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_ui(path, line)
            print(f"✅ UI registrada: '{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── npcPositioning ────────────────────────────────────────────────────────
    # Regla: IDENTIFIER ARROW LPAREN INTEGER COMMA INTEGER RPAREN

    def visitNpcPositioning(self, ctx: DemiseParser.NpcPositioningContext):
        name = ctx.IDENTIFIER().getText()
        integers = ctx.INTEGER()
        col = int(integers[0].getText())
        row = int(integers[1].getText())
        line = ctx.start.line

        try:
            self.symtab.declare_npc_position(name, col, row, line)
            print(f"✅ NPC '{name}' posicionado en ({col},{row})")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── weaponDeclaration ─────────────────────────────────────────────────────
    # Regla: WEAPON IDENTIFIER ARROW STRING_LITERAL

    def visitWeaponDeclaration(self, ctx: DemiseParser.WeaponDeclarationContext):
        name = ctx.IDENTIFIER().getText()
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_weapon(name, path, line)
            print(f"✅ Arma registrada: '{name}' | path='{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── weaponLogic ───────────────────────────────────────────────────────────
    # Regla: IDENTIFIER ARROW IDENTIFIER

    def visitWeaponLogic(self, ctx: DemiseParser.WeaponLogicContext):
        identifiers = ctx.IDENTIFIER()
        weapon_name = identifiers[0].getText()
        behavior    = identifiers[1].getText()
        line = ctx.start.line

        try:
            self.symtab.declare_weapon_behavior(weapon_name, behavior, line)
            print(f"✅ Comportamiento de arma: '{weapon_name}' → '{behavior}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── testCommand ───────────────────────────────────────────────────────────
    # Regla: FLOORCASTING_TEST | RAYCASTING_TEST | RAYCASTING_MAZE_TEST | REFLEXING_FLOOR

    def visitTestCommand(self, ctx: DemiseParser.TestCommandContext):
        if ctx.FLOORCASTING_TEST():
            print("🧪 Ejecutando floorcasting_test...")
            Floorcasting().main()
        elif ctx.RAYCASTING_TEST():
            print("🧪 Ejecutando raycasting_test...")
        elif ctx.RAYCASTING_MAZE_TEST():
            print("🧪 Ejecutando raycasting_maze_test...")
        elif ctx.REFLEXING_FLOOR():
            print("🧪 Ejecutando reflexing_floor...")

        return self.visitChildren(ctx)

    # ── Reporte final ─────────────────────────────────────────────────────────

    def report(self):
        """Imprime un resumen del análisis semántico al finalizar."""
        print("\n" + "=" * 50)
        if not self.errors:
            print("✅ Análisis semántico completado sin errores.")
        else:
            print(f"❌ Análisis semántico completado con {len(self.errors)} error(es):")
            for e in self.errors:
                print(f"   • {e}")
        print("=" * 50)
