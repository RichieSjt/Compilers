# Generated from c:\Users\Ricardo\Desktop\ANTLR\basic-compiler\antlr\hello.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("@\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\3\5\3\22\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\7\3)\n\3\f\3\16\3,\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4>\n\4\3\4\2\3")
        buf.write("\4\5\2\4\6\2\2\2I\2\t\3\2\2\2\4\21\3\2\2\2\6=\3\2\2\2")
        buf.write("\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13")
        buf.write("\f\3\2\2\2\f\3\3\2\2\2\r\16\b\3\1\2\16\22\7\17\2\2\17")
        buf.write("\22\7\20\2\2\20\22\7\22\2\2\21\r\3\2\2\2\21\17\3\2\2\2")
        buf.write("\21\20\3\2\2\2\22*\3\2\2\2\23\24\f\f\2\2\24\25\7\3\2\2")
        buf.write("\25)\5\4\3\r\26\27\f\13\2\2\27\30\7\4\2\2\30)\5\4\3\f")
        buf.write("\31\32\f\n\2\2\32\33\7\5\2\2\33)\5\4\3\13\34\35\f\t\2")
        buf.write("\2\35\36\7\6\2\2\36)\5\4\3\n\37 \f\b\2\2 !\7\7\2\2!)\5")
        buf.write("\4\3\t\"#\f\7\2\2#$\7\b\2\2$)\5\4\3\b%&\f\6\2\2&\'\7\t")
        buf.write("\2\2\')\5\4\3\7(\23\3\2\2\2(\26\3\2\2\2(\31\3\2\2\2(\34")
        buf.write("\3\2\2\2(\37\3\2\2\2(\"\3\2\2\2(%\3\2\2\2),\3\2\2\2*(")
        buf.write("\3\2\2\2*+\3\2\2\2+\5\3\2\2\2,*\3\2\2\2-.\7\n\2\2.>\7")
        buf.write("\21\2\2/\60\5\4\3\2\60\61\7\13\2\2\61\62\5\6\4\2\62>\3")
        buf.write("\2\2\2\63\64\5\4\3\2\64\65\7\13\2\2\65\66\5\6\4\2\66\67")
        buf.write("\7\f\2\2\678\5\6\4\28>\3\2\2\29:\7\r\2\2:;\5\4\3\2;<\7")
        buf.write("\16\2\2<>\3\2\2\2=-\3\2\2\2=/\3\2\2\2=\63\3\2\2\2=9\3")
        buf.write("\2\2\2>\7\3\2\2\2\7\13\21(*=")
        return buf.getvalue()


class helloParser ( Parser ):

    grammarFileName = "hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'<'", 
                     "'>'", "'var'", "'?'", "':'", "'print('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Number", "String", "Var", "Endline", 
                      "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    Number=13
    String=14
    Var=15
    Endline=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(helloParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(helloParser.ExpressionContext,i)


        def getRuleIndex(self):
            return helloParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = helloParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.expression(0)
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << helloParser.Number) | (1 << helloParser.String) | (1 << helloParser.Endline))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return helloParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(helloParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(helloParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(helloParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class EndlineContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Endline(self):
            return self.getToken(helloParser.Endline, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndline" ):
                listener.enterEndline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndline" ):
                listener.exitEndline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndline" ):
                return visitor.visitEndline(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def String(self):
            return self.getToken(helloParser.String, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class LessthanContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(helloParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(helloParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessthan" ):
                listener.enterLessthan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessthan" ):
                listener.exitLessthan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessthan" ):
                return visitor.visitLessthan(self)
            else:
                return visitor.visitChildren(self)


    class GreaterthanContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(helloParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(helloParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterthan" ):
                listener.enterGreaterthan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterthan" ):
                listener.exitGreaterthan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterthan" ):
                return visitor.visitGreaterthan(self)
            else:
                return visitor.visitChildren(self)


    class DivideContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(helloParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(helloParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide" ):
                listener.enterDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide" ):
                listener.exitDivide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide" ):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(helloParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(helloParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)


    class SubstractContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(helloParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(helloParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstract" ):
                listener.enterSubstract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstract" ):
                listener.exitSubstract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubstract" ):
                return visitor.visitSubstract(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(helloParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(helloParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = helloParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [helloParser.Number]:
                localctx = helloParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 12
                self.match(helloParser.Number)
                pass
            elif token in [helloParser.String]:
                localctx = helloParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(helloParser.String)
                pass
            elif token in [helloParser.Endline]:
                localctx = helloParser.EndlineContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(helloParser.Endline)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = helloParser.AssignContext(self, helloParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 17
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 18
                        self.match(helloParser.T__0)
                        self.state = 19
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = helloParser.AddContext(self, helloParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 20
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 21
                        self.match(helloParser.T__1)
                        self.state = 22
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = helloParser.SubstractContext(self, helloParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 23
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 24
                        self.match(helloParser.T__2)
                        self.state = 25
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = helloParser.MultiplyContext(self, helloParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 26
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 27
                        self.match(helloParser.T__3)
                        self.state = 28
                        self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = helloParser.DivideContext(self, helloParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 29
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 30
                        self.match(helloParser.T__4)
                        self.state = 31
                        self.expression(7)
                        pass

                    elif la_ == 6:
                        localctx = helloParser.LessthanContext(self, helloParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 32
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 33
                        self.match(helloParser.T__5)
                        self.state = 34
                        self.expression(6)
                        pass

                    elif la_ == 7:
                        localctx = helloParser.GreaterthanContext(self, helloParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        self.match(helloParser.T__6)
                        self.state = 37
                        self.expression(5)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return helloParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(helloParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class DeclareContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Var(self):
            return self.getToken(helloParser.Var, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare" ):
                listener.enterDeclare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare" ):
                listener.exitDeclare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(helloParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(helloParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class IfelseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a helloParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(helloParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(helloParser.StatementContext)
            else:
                return self.getTypedRuleContext(helloParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfelse" ):
                listener.enterIfelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfelse" ):
                listener.exitIfelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = helloParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = helloParser.DeclareContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(helloParser.T__7)
                self.state = 44
                self.match(helloParser.Var)
                pass

            elif la_ == 2:
                localctx = helloParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.expression(0)
                self.state = 46
                self.match(helloParser.T__8)
                self.state = 47
                self.statement()
                pass

            elif la_ == 3:
                localctx = helloParser.IfelseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.expression(0)
                self.state = 50
                self.match(helloParser.T__8)
                self.state = 51
                self.statement()
                self.state = 52
                self.match(helloParser.T__9)
                self.state = 53
                self.statement()
                pass

            elif la_ == 4:
                localctx = helloParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.match(helloParser.T__10)
                self.state = 56
                self.expression(0)
                self.state = 57
                self.match(helloParser.T__11)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         




