# ------------------------------------------------------------
# yacc.py
#
# parser for newspaper source files
# ------------------------------------------------------------
import ply.yacc as yacc

import pdb
from lex import tokens

def p_document(p):
  'document : block_list'
  pdb.set_trace()
  p[0] = p[1]
  print 1

def p_blocklist(p):
  '''block_list : block block_list
                | '''
  pdb.set_trace()
  if len(p) == 3:
    p[0] = p[2].insert(0, p[1])
  elif len(p) == 1:
    p[0] = []
  print 2

def p_block(p):
  '''block : header NEWLINE
           | paragraph NEWLINE'''
  pdb.set_trace()
  p[0] = p[1]
  print 3

def p_header(p):
  'header : line HEADER'
  pdb.set_trace()
  p[0] = p[1]
  print 5

def p_paragraph(p):
  '''paragraph : 
               | line paragraph'''
  pdb.set_trace()
  if len(p) == 3:
    p[0] = p[2].insert(0, p[1])
  elif len(p) == 1:
    p[0] = []
  print 6

def p_line(p):
  '''line : NEWLINE
          | WORD line'''
  pdb.set_trace()
  p[0] = p[1]
  if len(p) == 3:
    if isinstance(p[2], str):
      p[2] = []

    p[0] = p[2].insert(0, p[1])
  elif len(p) == 1:
    p[0] = []
  print 7

def p_error(p):
  print "Syntax error in input!"

import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s")
log = logging.getLogger()

parser = yacc.yacc(debug=True,debuglog=log)

data = '''
Header
======

This is a paragraph

This is another paragraph
with multiple lines in it.
The quick brown fox jumps over
the lazy dog.

'''

result = parser.parse(data)
print result
