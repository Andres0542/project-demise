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

    # ── spriteDeclaration ─────────────────────────────────────────────────────
    # Regla: SPRITE SPRITE_TYPE ARROW STRING_LITERAL
    # SPRITE_TYPE es un token léxico: 'wall' | 'floor' | 'sky'

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

    # ── filter ────────────────────────────────────────────────────────────────
    # Regla: FILTER LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN
    # IDENTIFIER[0] = nombre del filtro, IDENTIFIER[1] = target ('floor' | 'ceiling')
    # El target se valida semánticamente porque 'ceiling' no es SPRITE_TYPE pero
    # sí es un target válido de filter según la gramática de referencia.

    def visitFilter(self, ctx: DemiseParser.FilterContext):
        filter_name = ctx.FILTER_TYPE().getText()  # token ID, no IDENTIFIER
        target      = ctx.SPRITE_TYPE().getText()  # token ID, no IDENT
    	#filter_name = ctx.ID(0).getText()
	    #target = ctx.ID(1).getText()
        #identifiers = ctx.ID()
        #filter_name = identifiers[0].getText()
        #target      = identifiers[1].getText()
        line = ctx.start.line

        try:
            self.symtab.declare_filter(filter_name, target, line)
            print(f"✅ Filtro registrado: '{filter_name}' sobre '{target}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── npcDeclaration ────────────────────────────────────────────────────────
    # Regla: NPC ID ARROW STRING_LITERAL
    # Usa ID (no IDENTIFIER) según el .g4.

    def visitNpcDeclaration(self, ctx: DemiseParser.NpcDeclarationContext):
        name = ctx.ID().getText()           # token ID, no IDENTIFIER
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
            print(f"Música registrada: '{path}'")
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
                f"Mapa registrado: "
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
            print(f"Iluminación registrada: {value}")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── uiDeclaration ─────────────────────────────────────────────────────────
    # Regla: UI ARROW STRING_LITERAL
    # IMPORTANTE: la regla en el .g4 se llama 'uiDeclaration' (minúscula),
    # por lo tanto ANTLR genera visitUiDeclaration (no visitUIDeclaration).

    def visitUiDeclaration(self, ctx: DemiseParser.UiDeclarationContext):
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_ui(path, line)
            print(f"UI registrada: '{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── npcPositioning ────────────────────────────────────────────────────────
    # Regla: ID ARROW LPAREN INTEGER COMMA INTEGER RPAREN
    # Usa ID (no IDENTIFIER) según el .g4.

    def visitNpcPositioning(self, ctx: DemiseParser.NpcPositioningContext):
        name = ctx.ID().getText()           # token ID, no IDENTIFIER
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

    # ── weaponDeclaration ─────────────────────────────────────────────────────
    # Regla: WEAPON ID ARROW STRING_LITERAL
    # Usa ID (no IDENTIFIER) según el .g4.

    def visitWeaponDeclaration(self, ctx: DemiseParser.WeaponDeclarationContext):
        name = ctx.ID().getText()           # token ID, no IDENTIFIER
        path = self._strip(ctx.STRING_LITERAL().getText())
        line = ctx.start.line

        try:
            self.symtab.declare_weapon(name, path, line)
            print(f"Arma registrada: '{name}' | path='{path}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── weaponLogic ───────────────────────────────────────────────────────────
    # Regla: ID ARROW WEAPON_LOGIC
    # El comportamiento viene del token WEAPON_LOGIC (no IDENTIFIER):
    # 'chainsaw' | 'fist' | 'pistol' | 'shotgun' | 'chaingun' |
    # 'rocket_launcher' | 'energy_rifle' | 'BFG6000'
    # Nota: el lexer garantiza que WEAPON_LOGIC solo matchea esas cadenas,
    # pero se valida igual en el SymbolTable por robustez.

    def visitWeaponLogic(self, ctx: DemiseParser.WeaponLogicContext):
        weapon_name = ctx.ID().getText()            # token ID
        behavior    = ctx.WEAPON_LOGIC().getText()  # token WEAPON_LOGIC
        line = ctx.start.line

        try:
            self.symtab.declare_weapon_behavior(weapon_name, behavior, line)
            print(f"Comportamiento de arma: '{weapon_name}' → '{behavior}'")
        except SemanticError as e:
            self._error(e)

        return self.visitChildren(ctx)

    # ── testCommand ───────────────────────────────────────────────────────────
    # Regla: FLOORCASTING_TEST | RAYCASTING_TEST | RAYCASTING_MAZE_TEST
    # REFLEXING_FLOOR no existe en el .g4 actual, se elimina.

    def visitTestCommand(self, ctx: DemiseParser.TestCommandContext):
        if ctx.FLOORCASTING_TEST():
            print("Ejecutando test de floorcasting")
            # Floorcasting().main()
        elif ctx.RAYCASTING_TEST():
            print("Ejecutando test de raycasting")
        elif ctx.RAYCASTING_MAZE_TEST():
            print("Ejecutando test de laberinto con raycasting")

        return self.visitChildren(ctx)

    # ── Reporte final ─────────────────────────────────────────────────────────

    def report(self):
        """Imprime un resumen del análisis semántico al finalizar."""
        print("\n" + "=" * 50)
        if not self.errors:
            print("Análisis semántico completado sin errores.")
        else:
            print(f"❌ Análisis semántico completado con {len(self.errors)} error(es):")
            for e in self.errors:
                print(f"   • {e}")
        print("=" * 50)
