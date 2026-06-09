import sys
from antlr4 import CommonTokenStream, FileStream
from gen.DemiseLexer import DemiseLexer
from gen.DemiseParser import DemiseParser
from semantic.semantic_visitor import SemanticVisitor
from codegen.code_gen_visitor import CodeGenVisitor
# === NUEVO: Importar bindings de llvmlite ===
from llvmlite import binding

def main():

    def inicializar_llvm():
        """Inicializa los componentes nativos y obtiene el triple y data layout."""
        binding.initialize()
        binding.initialize_native_target()
        binding.initialize_native_asmprinter()

        # Obtener el triple de la máquina actual (ej. x86_64-pc-linux-gnu)
        target_triple = binding.get_process_triple()
    
        # Obtener el layout de datos correspondiente a esa arquitectura
        target = binding.Target.from_triple(target_triple)
        target_machine = target.create_target_machine()
        data_layout = str(target_machine.target_data)
    
        return target_triple, data_layout

    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding='utf-8')
    lexer  = DemiseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DemiseParser(stream)
    tree   = parser.program()      # regla inicial
    visitor = SemanticVisitor()
    visitor.visit(tree) # iniciar analisis semantico

    if parser.getNumberOfSyntaxErrors() > 0:
        print('Errores sintácticos encontrados. Abortando.')
        return
    
    generador = CodeGenVisitor()
    # --- NUEVA SECCIÓN DE CONFIGURACIÓN ---
    try:
        triple, layout = inicializar_llvm()
        generador.module.triple = "x86_64-pc-linux-gnu"#triple
        generador.module.data_layout = layout
    except Exception as e:
        print(f"Advertencia: No se pudo auto-detectar el target nativo ({e}). Generando IR genérico.")
    # --------------------------------------

    generador.visit(tree)
    generador.finalizar()

    codigo = generador.emitir("salida.ll")
    print(codigo)
    # -- reporte errores semanticos
    #if visitor.errors:
        #print('\n=== ERRORES SEMÁNTICOS ===')
        #for e in visitor.errors:
            #print(' ', e)
    #else:
        #print('Análisis semántico: OK')
    
    #warns = visitor.symtab.unused_warnings()
    #if warns:
        #print('\n=== ADVERTENCIAS ===')
        #for w in warns:
            #print(' ', w)

if __name__ == "__main__":
    main()






