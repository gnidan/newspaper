# ------------------------------------------------------------
# lex.py
#
# tokenizer for newspaper source files
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'HEADER',
    'WORD',
    'NEWLINE',
)

t_HEADER      = r'\=+'
t_WORD        = r'[^\=\s]+'

t_ignore      = ' \t'

def t_newline(t):
  r'\n'
  t.lexer.lineno += 1

def t_error(t):
  print "Illegal character '%s'" % t.value[0]
  t.lexer.skip(1)

lexer = lex.lex()
