import ast

class Formatter:
  defaults = {
      'width': 80,
      'page-height': 60,
      'justify': 'left-right',
      'columns': 2,
      'header-colspan': 2,
      }

  def __init__(self, ast):
    self.ast = ast
    self.options = self.defaults

  def set_options(self, **opts):
    for k, v in opts:
      self.options[k] = v

  def format(self):
    self.ast.accept(self)

  def visit(self, node):
    ''' Generic visit() '''
    print "visiting node: ", node.__class__.__name__
    for child in node.children:
      if child is not None:
        child.accept(self)

  def visit_line(self, node):
    print node

  def visit_header(self, node):
    print node


class Block:
  def __init__(self, parent=None, **kwargs):
    pass

class Document(Block):
  def __init__(self, **kwargs):

class Page(Block):
  def __init__(self, **kwargs):
    super(**kwargs)
