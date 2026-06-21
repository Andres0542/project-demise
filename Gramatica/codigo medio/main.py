import sys
from antlr4 import CommonTokenStream, FileStream
from gen.DemiseLexer import DemiseLexer
from gen.DemiseParser import DemiseParser
from semantic.semantic_visitor import SemanticVisitor
from codegen.code_gen_visitor import CodeGenVisitor


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
    generador.visit(tree)
    
    # 3. Cierras la función main
    generador.finalizar()

    # 4. Emites el código guardándolo en un archivo .c
    codigo = generador.emitir("salida.c")
    print(codigo)


if __name__ == "__main__":
    main()
