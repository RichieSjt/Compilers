# Generated from c:\Users\Ricardo\Desktop\Github\Compilers\basic-compiler\antlr\hello.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\6\16I\n\16\r\16\16\16J\3\17")
        buf.write("\6\17N\n\17\r\17\16\17O\3\20\6\20S\n\20\r\20\16\20T\3")
        buf.write("\21\6\21X\n\21\r\21\16\21Y\3\21\3\21\2\2\22\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22\3\2\6\3\2\62;\5\2\62;C\\c|\4\2C\\c|\5")
        buf.write("\2\13\f\17\17\"\"\2`\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+")
        buf.write("\3\2\2\2\r-\3\2\2\2\17/\3\2\2\2\21\63\3\2\2\2\23\65\3")
        buf.write("\2\2\2\259\3\2\2\2\27;\3\2\2\2\31@\3\2\2\2\33H\3\2\2\2")
        buf.write("\35M\3\2\2\2\37R\3\2\2\2!W\3\2\2\2#$\7-\2\2$\4\3\2\2\2")
        buf.write("%&\7/\2\2&\6\3\2\2\2\'(\7,\2\2(\b\3\2\2\2)*\7\61\2\2*")
        buf.write("\n\3\2\2\2+,\7>\2\2,\f\3\2\2\2-.\7@\2\2.\16\3\2\2\2/\60")
        buf.write("\7k\2\2\60\61\7p\2\2\61\62\7v\2\2\62\20\3\2\2\2\63\64")
        buf.write("\7?\2\2\64\22\3\2\2\2\65\66\7k\2\2\66\67\7h\2\2\678\7")
        buf.write("*\2\28\24\3\2\2\29:\7+\2\2:\26\3\2\2\2;<\7g\2\2<=\7n\2")
        buf.write("\2=>\7u\2\2>?\7g\2\2?\30\3\2\2\2@A\7r\2\2AB\7t\2\2BC\7")
        buf.write("k\2\2CD\7p\2\2DE\7v\2\2EF\7*\2\2F\32\3\2\2\2GI\t\2\2\2")
        buf.write("HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\34\3\2\2\2L")
        buf.write("N\t\3\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\36")
        buf.write("\3\2\2\2QS\t\4\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2")
        buf.write("\2\2U \3\2\2\2VX\t\5\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2")
        buf.write("YZ\3\2\2\2Z[\3\2\2\2[\\\b\21\2\2\\\"\3\2\2\2\7\2JOTY\3")
        buf.write("\b\2\2")
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
    Variable = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'int'", "'='", "'if('", 
            "')'", "'else'", "'print('" ]

    symbolicNames = [ "<INVALID>",
            "Number", "String", "Variable", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "Number", "String", 
                  "Variable", "WS" ]

    grammarFileName = "hello.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


