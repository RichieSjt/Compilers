# Generated from c:\Users\Ricardo\Desktop\ANTLR\basic-compiler\antlr\hello.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\16\6\16F\n\16\r\16\16\16G\3\17\6\17K\n\17")
        buf.write("\r\17\16\17L\3\20\6\20P\n\20\r\20\16\20Q\3\21\3\21\3\22")
        buf.write("\6\22W\n\22\r\22\16\22X\3\22\3\22\2\2\23\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23\3\2\7\3\2\62;\5\2\62;C\\c|\4\2C\\c|\3\2")
        buf.write("\f\f\4\2\13\13\17\17\2_\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2")
        buf.write("\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21\63")
        buf.write("\3\2\2\2\23\67\3\2\2\2\259\3\2\2\2\27;\3\2\2\2\31B\3\2")
        buf.write("\2\2\33E\3\2\2\2\35J\3\2\2\2\37O\3\2\2\2!S\3\2\2\2#V\3")
        buf.write("\2\2\2%&\7?\2\2&\4\3\2\2\2\'(\7-\2\2(\6\3\2\2\2)*\7/\2")
        buf.write("\2*\b\3\2\2\2+,\7,\2\2,\n\3\2\2\2-.\7\61\2\2.\f\3\2\2")
        buf.write("\2/\60\7>\2\2\60\16\3\2\2\2\61\62\7@\2\2\62\20\3\2\2\2")
        buf.write("\63\64\7x\2\2\64\65\7c\2\2\65\66\7t\2\2\66\22\3\2\2\2")
        buf.write("\678\7A\2\28\24\3\2\2\29:\7<\2\2:\26\3\2\2\2;<\7r\2\2")
        buf.write("<=\7t\2\2=>\7k\2\2>?\7p\2\2?@\7v\2\2@A\7*\2\2A\30\3\2")
        buf.write("\2\2BC\7+\2\2C\32\3\2\2\2DF\t\2\2\2ED\3\2\2\2FG\3\2\2")
        buf.write("\2GE\3\2\2\2GH\3\2\2\2H\34\3\2\2\2IK\t\3\2\2JI\3\2\2\2")
        buf.write("KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\36\3\2\2\2NP\t\4\2\2O")
        buf.write("N\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2R \3\2\2\2ST\t")
        buf.write("\5\2\2T\"\3\2\2\2UW\t\6\2\2VU\3\2\2\2WX\3\2\2\2XV\3\2")
        buf.write("\2\2XY\3\2\2\2YZ\3\2\2\2Z[\b\22\2\2[$\3\2\2\2\7\2GLQX")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class helloLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    Number = 13
    String = 14
    Var = 15
    Endline = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'var'", "'?'", 
            "':'", "'print('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "Number", "String", "Var", "Endline", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "Number", "String", 
                  "Var", "Endline", "WS" ]

    grammarFileName = "hello.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


