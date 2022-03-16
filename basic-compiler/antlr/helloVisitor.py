# Generated from c:\Users\Ricardo\Desktop\ANTLR\basic-compiler\antlr\hello.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .helloParser import helloParser
else:
    from helloParser import helloParser

# This class defines a complete generic visitor for a parse tree produced by helloParser.

class helloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by helloParser#program.
    def visitProgram(self, ctx:helloParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#add.
    def visitAdd(self, ctx:helloParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#number.
    def visitNumber(self, ctx:helloParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#endline.
    def visitEndline(self, ctx:helloParser.EndlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#string.
    def visitString(self, ctx:helloParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#lessthan.
    def visitLessthan(self, ctx:helloParser.LessthanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#greaterthan.
    def visitGreaterthan(self, ctx:helloParser.GreaterthanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#divide.
    def visitDivide(self, ctx:helloParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#multiply.
    def visitMultiply(self, ctx:helloParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#substract.
    def visitSubstract(self, ctx:helloParser.SubstractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#assign.
    def visitAssign(self, ctx:helloParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#declare.
    def visitDeclare(self, ctx:helloParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#if.
    def visitIf(self, ctx:helloParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#ifelse.
    def visitIfelse(self, ctx:helloParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by helloParser#print.
    def visitPrint(self, ctx:helloParser.PrintContext):
        return self.visitChildren(ctx)



del helloParser