import logging

from newspaper.ast import ast

logger = logging.getLogger(__name__)

#
# Word-Level Nodes
#
class Word(ast.Node):
    word = ast.Field(str, unicode)

class Punctuation(ast.Node):
    mark = ast.Field(str, unicode)
    align = ast.Field("left", "right", "no_align")


#
# Inline Nodes
#

class Text(ast.Node):
    nodes = ast.List(Word, Punctuation, nested=True)

class Sentence(Text):
    pass


#
# Block-Level Nodes
#
class Block(ast.Node):
    text = ast.Field(Text)

class Header(Block):
    pass

class Paragraph(Block):
    pass


#
# Top-Level Node
#
