# ------------------------------------------------------------
# yacc.py
#
# parser for newspaper source files
# ------------------------------------------------------------
import ply.yacc as yacc

from lex import tokens

def p_document(p):
  'document : block_list'
  p[0] = p[1]

def p_blocklist(p):
  '''block_list : block block_list
                | '''
  if len(p) == 3:
    p[2].insert(0, p[1])
    p[0] = p[2]
  elif len(p) == 1:
    p[0] = []

def p_block(p):
  '''block : line header blank
        | paragraph blank
        | blank'''
  p[0] = p[1]

def p_line(p):
  '''line : word_list NEWLINE'''
  p[0] = p[1]

def p_header(p):
  '''header : HEADER NEWLINE'''
  p[0] = p[1]

def p_blank(p):
  '''blank : NEWLINE'''
  p[0] = p[1]

def p_paragraph(p):
  '''paragraph : line paragraph
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
  print "Syntax error in input!"


parser = yacc.yacc()


data ='''Header
=======

This is a paragraph. Hello!

Another paragraph. This time
with more than one line.

'''

result = parser.parse(data)
import pprint
pp = pprint.PrettyPrinter(indent=2)
print pp.pprint(result)
