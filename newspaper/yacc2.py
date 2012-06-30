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
  '''block : line header blank
           | paragraph blank'''
  pdb.set_trace()
  p[0] = p[1]
  print 3

def p_header(p):
  'header : HEADER NEWLINE'
  pdb.set_trace()
  p[0] = p[1]
  print 5

def p_paragraph(p):
  '''paragraph : paragraph line
               | line'''
  pdb.set_trace()
  if len(p) == 3:
    p[0] = p[2].append( p[1] )
  elif len(p) == 2:
    p[0] = [ p[1] ]
  print 6

def p_line(p):
  '''line : WORD line
          | WORD NEWLINE'''
  pdb.set_trace()
  p[0] = p[1]
  if isinstance(p[2], str) and p[2]=='\n':
    p[0] = [ p[1] ]
  else:
    p[0] = p2.insert(0, p[1])
  print 7

def p_blank(p):
  '''blank : NEWLINE'''
  pdb.set_trace()
  p[0] = ''
  print 8

def p_error(p):
  print "ERROR"
  pdb.set_trace()

import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s")
log = logging.getLogger()

parser = yacc.yacc(debug=True,debuglog=log)

data = '''This is a paragraph
This is another paragraph
with multiple lines in it.
The quick brown fox jumps over
the lazy dog.

'''

result = parser.parse(data)
print result
