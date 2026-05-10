import sys
from antlr4 import CommonTokenStream, FileStream
from gen.DemiseLexer import DemiseLexer
from gen.DemiseParser import DemiseParser
from semantic.semantic_visitor import SemanticVisitor

def main():
    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding='utf-8')
    lexer  = DemiseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DemiseParser(stream)
    tree   = parser.program()      # regla inicial
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print('Errores sintácticos encontrados. Abortando.')
        return
        
    visitor = SemanticVisitor()
    visitor.visit(tree) # iniciar analisis semantico
    
    # -- reporte errores semanticos
    if visitor.errors:
        print('\n=== ERRORES SEMÁNTICOS ===')
        for e in visitor.errors:
            print(' ', e)
    else:
        print('Análisis semántico: OK')
    
    #warns = visitor.symtab.unused_warnings()
    #if warns:
        #print('\n=== ADVERTENCIAS ===')
        #for w in warns:
            #print(' ', w)

# ejecutar main
main()
