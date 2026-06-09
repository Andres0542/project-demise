; ModuleID = "programa"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = constant [4 x i8] c"%d\0a\00"
define i32 @"main"()
{
entry:
  %"mod" = srem i32 2, 3
  %"a" = alloca i32
  store i32 %"mod", i32* %"a"
  %"a_val" = load i32, i32* %"a"
  %"fmt_ptr" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr", i32 %"a_val")
  ret i32 0
}
