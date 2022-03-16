from antlr.helloListener import helloListener
from antlr.helloParser import helloParser

class GenCode(helloListener):

    # Enter a parse tree produced by helloParser#program.
    def enterProgram(self, ctx:helloParser.ProgramContext):
        print('.text')

    # Exit a parse tree produced by helloParser#program.
    def exitProgram(self, ctx:helloParser.ProgramContext):
        print('Exit')

    # Exit a parse tree produced by helloParser#add.
    def exitAdd(self, ctx:helloParser.AddContext):
        print('Add')

    # Exit a parse tree produced by helloParser#number.
    def exitNumber(self, ctx:helloParser.NumberContext):
        print(f'uwu {ctx.Number().getText()}')

    # Exit a parse tree produced by helloParser#endline.
    def exitEndline(self, ctx:helloParser.EndlineContext):
        print('End line')

    # Exit a parse tree produced by helloParser#string.
    def exitString(self, ctx:helloParser.StringContext):
        print('String')

    # Exit a parse tree produced by helloParser#lessthan.
    def exitLessthan(self, ctx:helloParser.LessthanContext):
        print('Less than')

    # Exit a parse tree produced by helloParser#greaterthan.
    def exitGreaterthan(self, ctx:helloParser.GreaterthanContext):
        print('Greater than')

    # Exit a parse tree produced by helloParser#divide.
    def exitDivide(self, ctx:helloParser.DivideContext):
        print('Divide')

    # Exit a parse tree produced by helloParser#multiply.
    def exitMultiply(self, ctx:helloParser.MultiplyContext):
        print('Multiply')

    # Exit a parse tree produced by helloParser#substract.
    def exitSubstract(self, ctx:helloParser.SubstractContext):
        print('Substract')

    # Exit a parse tree produced by helloParser#assign.
    def exitAssign(self, ctx:helloParser.AssignContext):
        print('Assign')

    # Exit a parse tree produced by helloParser#declare.
    def exitDeclare(self, ctx:helloParser.DeclareContext):
        print('Declare')

    # Exit a parse tree produced by helloParser#if.
    def exitIf(self, ctx:helloParser.IfContext):
        print('If statement')

    # Exit a parse tree produced by helloParser#ifelse.
    def exitIfelse(self, ctx:helloParser.IfelseContext):
        print('If else statement')

    # Exit a parse tree produced by helloParser#print.
    def exitPrint(self, ctx:helloParser.PrintContext):
        print('Print')