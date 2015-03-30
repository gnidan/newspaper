import logging

from newspaper.ast import ast

logger = logging.getLogger(__name__)

class Node(ast.Node):
    pass

#
# Word-Level Nodes
#
class Word(Node):
    word = ast.Field(str, unicode)

class Punctuation(Node):
    mark = ast.Field(str, unicode)
    align = ast.Field("left", "right", "no_align")


#
# Inline Nodes
#

class Text(Node):
    nodes = ast.List(Word, Punctuation, nested=True)

class Sentence(Text):
    pass


#
# Block-Level Nodes
#
class Block(Node):
    text = ast.Field(Text)

class Header(Block):
    pass

class Paragraph(Block):
    pass


#
# Top-Level Node
#
class Document(Node):
    blocks = ast.List(Block)

