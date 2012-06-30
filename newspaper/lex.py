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
  t.type = 'NEWLINE'
  return t

def t_error(t):
  print "Illegal character '%s'" % t.value[0]
  t.lexer.skip(1)

lexer = lex.lex()

data ='''Header
=======

This is a paragraph. Hello!

Another paragraph. This time
with more than one line.

'''
if __name__ == '__main__':
  lexer.input(data)
  while True:
    tok = lexer.token()
    if not tok:
      break
    print tok

