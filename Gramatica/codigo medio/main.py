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

    visitor = SemanticVisitor()
    visitor.visit(tree)

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Errores sintácticos encontrados. Abortando.")
        return

    generador = CodeGenVisitor()
    try:
        triple, layout = inicializar_llvm()
        generador.module.triple = triple or "x86_64-pc-linux-gnu"
        generador.module.data_layout = layout
    except Exception as e:
        print(f"Advertencia: No se pudo auto-detectar el target nativo ({e}). Generando IR genérico.")

    generador.visit(tree)
    generador.finalizar()

    codigo = generador.emitir("salida.ll")
    print(codigo)


if __name__ == "__main__":
    main()
