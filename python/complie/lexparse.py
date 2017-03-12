from ply import lex
import sys

reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
  'void' : 'VOID',
    'char' : 'CHAR',
    'short' : 'SHORT',
    'int' : 'INT',
    'long' : 'LONG',
   'stuct' : 'STRUCT',
   'union' : 'UNION',
   'enum' : 'ENUM',
   'static' : 'STATIC',
   'extern' : 'EXTERN',
   'const' : 'CONST',
   'signed' : 'SIGNED',
   'unsigned' : 'UNSIGNED',
   'switch' : 'SWITCH',
   'case' : 'CASE',
   'default' : 'DEFAULT_',
   'do' : 'DO',
   'return' : 'RETURN',
   'break' : 'BREAK',
   'continue' : 'CONTINUE',
   'goto' : 'GOTO',
   'typedef' : 'TYPEDEF',
   'sizeof' : 'SIZEOF',
}

tokens = [
   'OPERATOR',
   'FLOAT',
   'INTEGER',
   'STRING',
   'INCLCUDE',
   'LINECOMMENT',
   'BLOCKCOMMENT',
   'CHARACHER',
   'IDENTIFIER',
   'LINE',
   'BRACHET',
   'SEMICOLON',
]+list(reserved.values())

def t_OPERATOR(t):
     r'[\+|\-|\*|\/|\>\=|\<\=|\*|\&|\?|\:|\!|\=\=|\!\=|\,|\=|\;]'
     return t

def t_IDENTIFIER(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'IDENTIFIER')
     return t

def t_FLOAT(t):
     r'[0-9]+\.[0-9]+'
     return t

def t_INTEGER(t):
     r'\d+'
     return t

def t_STRING(t):
     r'\"[^\"]*\"'
     return t

def t_INCLCUDE(t):
     r'\#include<[a-zA_Z\.]+>'
     return t

def t_LINECOMMENT(t):
     r'\\\\.*'
     return t

def t_BLOCKCOMMENT(t):
     r'\\\*[a-zA-Z ]+\*\\'
     return t

def t_CHARACHER(t):
     r"'\D'"
     return t

def t_BRACHET(t):
     r'[\(|\)|\[|\]|\{|\}]'
     return t

def t_SEMICOLON(t):
     r';'
     return t

def t_LINE(t):
     r'\n'
     return t

t_ignore = ' \t\r\n'

if __name__ == "__main__":
     print("lex start\n---------------------")
     srcname = "main.c"
     f=open(srcname,'r')
     srcstr=f.read(100000)
     print(srcstr)
     lexer=lex.lex()
     lexer.input(srcstr)
     print(reserved.values())
     print(reserved.get('if','IDENTIFIER'))
     for tok in lexer:
          print(tok)
     
     
