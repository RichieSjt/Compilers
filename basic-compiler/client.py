from antlr4 import *
from antlr.helloParser import helloParser
from antlr.helloLexer import helloLexer
from listeners.gencode import GenCode

import sys


def main():
    parser = helloParser(CommonTokenStream(helloLexer(FileStream("input.txt"))))
    tree = parser.program()

    gencode = GenCode()
    walker = ParseTreeWalker()
    walker.walk(gencode, tree)

if __name__ == '__main__':
    main()