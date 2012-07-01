from StringIO import StringIO

class ASTNode:
  def __init__(self, children):
    self.children = children

  def accept(self, visitor):
    preferred_visit = 'visit_' + self.__class__.__name__.lower()
    default = visitor.visit

    visit = getattr(visitor, preferred_visit, default)
    visit(self)

  def __str__(self):
    s = StringIO()
    s.write(self.__class__.__name__)
    s.write('\n')
    for child in self.children:
      for line in str(child).split('\n'):
        s.write("  " + line + '\n')
    return s.getvalue()

class Document(ASTNode):
  def __init__(self, blocks):
    self.children = blocks

class Block(ASTNode):
  def __init__(self, children):
    super(children)

class Header(Block):
  def __init__(self, words):
    self.children = words

  def __str__(self):
    s = StringIO()
    s.write(self.__class__.__name__)
    s.write('\n')
    s.write('  ' + ' '.join(self.children))
    return s.getvalue()

class Paragraph(Block):
  def __init__(self, lines):
    self.children = lines

class Line(ASTNode):
  def __init__(self, words):
    self.children = words

  def __str__(self):
    s = StringIO()
    s.write(self.__class__.__name__)
    s.write('\n')
    s.write('  ' + ' '.join(self.children))
    return s.getvalue()
