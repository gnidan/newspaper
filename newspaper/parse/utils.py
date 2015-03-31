import logging

from newspaper import ast

logger = logging.getLogger(__name__)

def make_word(letters):
    return ast.Word(letters)

def make_line(words):
    return ast.Text(words)

def make_paragraph(lines):
    text = ast.Text.join(lines)

    return ast.Paragraph(text)

def make_header(lines, level):
    text = ast.Text.join(lines)

    return ast.Header(text, level=level)

def make_document(blocks):
    return ast.Document(blocks)
