import sys
from antlr4 import CommonTokenStream, FileStream
from gen.DemiseLexer import DemiseLexer
from gen.DemiseParser import DemiseParser
from semantic.semantic_visitor import SemanticVisitor
from codegen.code_gen_visitor import CodeGenVisitor
from llvmlite import binding


def inicializar_llvm():
    target_triple = binding.get_process_triple()
    target = binding.Target.from_triple(target_triple)
    target_machine = target.create_target_machine()
    data_layout = str(target_machine.target_data)
    return target_triple, data_layout


def main():
    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding="utf-8")
    lexer = DemiseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DemiseParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Errores sintácticos encontrados. Abortando.")
        return

    visitor = SemanticVisitor()
    visitor.visit(tree)

    generador = CodeGenVisitor()
    try:
        triple, layout = inicializar_llvm()
        generador.module.triple = triple
        generador.module.data_layout = layout
    except Exception as e:
        print(f"Advertencia: No se pudo auto-detectar el target nativo ({e}). Generando IR genérico.")

    generador.visit(tree)
    generador.finalizar()

    salida = sys.argv[2] if len(sys.argv) > 2 else "salida.ll"
    codigo = generador.emitir(salida)
    print(f"\n=== LLVM IR generado en {salida} ===")
    print(codigo)


if __name__ == "__main__":
    main()
