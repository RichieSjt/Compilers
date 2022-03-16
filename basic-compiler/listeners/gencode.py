from antlr.helloListener import helloListener
from antlr.helloParser import helloParser

class GenCode(helloListener):
    def __init__(self):
        self.stack = []

    def enterProgram(self, ctx:helloParser.ProgramContext):
        print('.main\n')

    def exitProgram(self, ctx:helloParser.ProgramContext):
        print('\nli $v0 10 \nsyscall')

    def exitAdd(self, ctx:helloParser.AddContext):
        print('Add')

    def exitNumber(self, ctx:helloParser.NumberContext):
        print(f'$t0 {ctx.Number().getText()}')

    def exitString(self, ctx:helloParser.StringContext):
        print(f'String {ctx.String().getText()}')

    def exitLessthan(self, ctx:helloParser.LessthanContext):
        print('Less than')

    def exitGreaterthan(self, ctx:helloParser.GreaterthanContext):
        print('Greater than')

    def exitDivide(self, ctx:helloParser.DivideContext):
        print('Divide')

    def exitMultiply(self, ctx:helloParser.MultiplyContext):
        print('Multiply')

    def exitSubstract(self, ctx:helloParser.SubstractContext):
        print('Substract')

    def exitAssign(self, ctx:helloParser.AssignContext):
        print(f'sw $t0 {ctx.Variable().getText()}')

    def exitDeclare(self, ctx:helloParser.DeclareContext):
        print('Declare')

    def enterIf(self, ctx:helloParser.IfContext):
        print('\nIf')

    def enterIfelse(self, ctx:helloParser.IfelseContext):
        print('\nIf else')

    def exitPrint(self, ctx:helloParser.PrintContext):
        print('li $v0 1 \nsyscall')
