# Generated from c:\Users\Ricardo\Desktop\Github\Compilers\basic-compiler\antlr\hello.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .helloParser import helloParser
else:
    from helloParser import helloParser

# This class defines a complete listener for a parse tree produced by helloParser.
class helloListener(ParseTreeListener):

    # Enter a parse tree produced by helloParser#program.
    def enterProgram(self, ctx:helloParser.ProgramContext):
        pass

    # Exit a parse tree produced by helloParser#program.
    def exitProgram(self, ctx:helloParser.ProgramContext):
        pass


    # Enter a parse tree produced by helloParser#add.
    def enterAdd(self, ctx:helloParser.AddContext):
        pass

    # Exit a parse tree produced by helloParser#add.
    def exitAdd(self, ctx:helloParser.AddContext):
        pass


    # Enter a parse tree produced by helloParser#number.
    def enterNumber(self, ctx:helloParser.NumberContext):
        pass

    # Exit a parse tree produced by helloParser#number.
    def exitNumber(self, ctx:helloParser.NumberContext):
        pass


    # Enter a parse tree produced by helloParser#string.
    def enterString(self, ctx:helloParser.StringContext):
        pass

    # Exit a parse tree produced by helloParser#string.
    def exitString(self, ctx:helloParser.StringContext):
        pass


    # Enter a parse tree produced by helloParser#lessthan.
    def enterLessthan(self, ctx:helloParser.LessthanContext):
        pass

    # Exit a parse tree produced by helloParser#lessthan.
    def exitLessthan(self, ctx:helloParser.LessthanContext):
        pass


    # Enter a parse tree produced by helloParser#greaterthan.
    def enterGreaterthan(self, ctx:helloParser.GreaterthanContext):
        pass

    # Exit a parse tree produced by helloParser#greaterthan.
    def exitGreaterthan(self, ctx:helloParser.GreaterthanContext):
        pass


    # Enter a parse tree produced by helloParser#divide.
    def enterDivide(self, ctx:helloParser.DivideContext):
        pass

    # Exit a parse tree produced by helloParser#divide.
    def exitDivide(self, ctx:helloParser.DivideContext):
        pass


    # Enter a parse tree produced by helloParser#multiply.
    def enterMultiply(self, ctx:helloParser.MultiplyContext):
        pass

    # Exit a parse tree produced by helloParser#multiply.
    def exitMultiply(self, ctx:helloParser.MultiplyContext):
        pass


    # Enter a parse tree produced by helloParser#substract.
    def enterSubstract(self, ctx:helloParser.SubstractContext):
        pass

    # Exit a parse tree produced by helloParser#substract.
    def exitSubstract(self, ctx:helloParser.SubstractContext):
        pass


    # Enter a parse tree produced by helloParser#declare.
    def enterDeclare(self, ctx:helloParser.DeclareContext):
        pass

    # Exit a parse tree produced by helloParser#declare.
    def exitDeclare(self, ctx:helloParser.DeclareContext):
        pass


    # Enter a parse tree produced by helloParser#assign.
    def enterAssign(self, ctx:helloParser.AssignContext):
        pass

    # Exit a parse tree produced by helloParser#assign.
    def exitAssign(self, ctx:helloParser.AssignContext):
        pass


    # Enter a parse tree produced by helloParser#if.
    def enterIf(self, ctx:helloParser.IfContext):
        pass

    # Exit a parse tree produced by helloParser#if.
    def exitIf(self, ctx:helloParser.IfContext):
        pass


    # Enter a parse tree produced by helloParser#ifelse.
    def enterIfelse(self, ctx:helloParser.IfelseContext):
        pass

    # Exit a parse tree produced by helloParser#ifelse.
    def exitIfelse(self, ctx:helloParser.IfelseContext):
        pass


    # Enter a parse tree produced by helloParser#print.
    def enterPrint(self, ctx:helloParser.PrintContext):
        pass

    # Exit a parse tree produced by helloParser#print.
    def exitPrint(self, ctx:helloParser.PrintContext):
        pass



del helloParser