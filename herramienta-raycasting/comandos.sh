clang -S -emit-llvm main.c -o intermedio.ll
clang intermedio.ll -lGL -lGLU -lglut -lm -lSDL2 -lSDL2_mixer -o a.out

