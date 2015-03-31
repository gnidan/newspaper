import logging

from newspaper import ast

logger = logging.getLogger(__name__)

def make_word(letters, lpunct=None, rpunct=None):
    return ast.Word(letters)

def make_punctuation(mark):
    return ast.Punctuation(mark=mark)

def make_chunk(lmarks, word, rmarks):
    left = []
    right = []

    for mark in lmarks:
        left.append(ast.Punctuation(mark=mark, align='right'))

    for mark in rmarks:
        left.append(ast.Punctuation(mark=mark, align='left'))

    return left + [word] + right

def make_line(chunks):
    nodes = [node for chunk in chunks for node in chunk]
    return ast.Text(nodes)

def make_paragraph(lines):
    text = ast.Text.join(lines)

    return ast.Paragraph(text)

def make_header(lines, level):
    text = ast.Text.join(lines)

    return ast.Header(text, level=level)

def make_document(blocks):
    return ast.Document(blocks)
