# ------------------------------------------------------------
# yacc.py
#
# parser for newspaper source files
# ------------------------------------------------------------
import ply.yacc as yacc

from lex import tokens

import ast
import formatter


def p_document(p):
  'document : block_list'
  p[0] = ast.Document(p[1])

def p_blocklist(p):
  '''block_list : block block_list
                | '''
  if len(p) == 3:
    p[2].insert(0, p[1])
    p[0] = p[2]
  elif len(p) == 1:
    p[0] = []

def p_block_header(p):
  '''block : word_list NEWLINE header blank'''
  p[0] = ast.Header( p[1] )

def p_block_paragraph(p):
  '''block : paragraph blank'''
  p[0] = p[1]

def p_block_blank(p):
  '''block : blank'''

def p_line(p):
  '''line : word_list NEWLINE'''
  p[0] = ast.Line(p[1])

def p_header(p):
  '''header : HEADER NEWLINE'''

def p_blank(p):
  '''blank : NEWLINE'''

def p_paragraph(p):
  '''paragraph : line_list'''
  p[0] = ast.Paragraph(p[1])

def p_linelist(p):
  '''line_list : line line_list
          | line'''
  if len(p) == 3:
    p[2].insert(0, p[1])
    p[0] = p[2]
  else:
    p[0] = [ p[1] ]

def p_wordlist(p):
  '''word_list : word_list WORD
        | WORD'''
  if len(p) == 3:
    p[1].append(p[2])
    p[0] = p[1]
  else:
    p[0] = [ p[1] ]

def p_error(p):
  print "Syntax error: Unexpected %s on line %d" \
    % (p.type, p.lineno)


parser = yacc.yacc()

data ='''
Let me tell you a story
=======================

This is a paragraph. Hello!

Another paragraph. This time
with more than one line.

'''

ast = parser.parse(data)
f = formatter.Formatter(ast)

f.format()
