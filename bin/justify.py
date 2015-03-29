#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2012 g. nicholas d'andrea <nick@gnidan.org>

import sys
from random import seed, random
from math import ceil
from StringIO import StringIO

ALLEY=4

class Word:
  def __init__(self, cargo=None, next=None):
    self.car = cargo
    self.cdr = next

  def is_space(self):
    return self.car[0] == ' '

  def __iter__(self):
    c = self
    while c is not None:
      word = c
      c = c.cdr
      yield word

  def __len__(self):
    acc = 0
    for w in self:
      acc += len(w.car)
    return acc

  def __str__(self):
    words = []
    for w in self:
      words.append(w.car)
    return ''.join(words)


def mklist(string):
  l = None
  for word in reversed(string.split()):
    l = Word(' ', l)
    l = Word(word, l)
  return l


def split_lines(l, cols):
  lines = []

  # we keep track of each line as we build it: keeping track of the start of
  # the line, and the end as we add to it.
  tail = l
  line = tail

  l = l.cdr
  acc = len(tail.car)
  for w in l:
    # based on line length, either cut and skip to the next line, or append
    # to the current.
    #
    # some funkiness here in the if condition to avoid having lines end in
    # spaces
    if w.is_space() and w.cdr and acc + len(w.car) + len(w.cdr.car) > cols \
        or acc + len(w.car) > cols:
      if w.is_space():
        acc += len(w.car)
        continue

      lines.append(line)
      line = w
      tail = w
      acc = len(tail.car)
    else:
      tail.cdr = w
      tail = tail.cdr
      tail.cdr = None
      acc += len(w.car)
  lines.append(line)

  return lines


def justify(lines, cols):
  for line in lines:
    to_add = cols - len(line)

    # don't add spaces if it's gonna be too many
    if to_add > cols / 4:
      continue

    for i in range(to_add):
      seen = 0.
      choice = None
      for w in line:
        if w.is_space():
          seen += 1.

          if random() < 1 / seen:
            choice = w
      choice.car += ' '


def page_footer(page=0, pages=0):
  page_footer = StringIO()
  page_number = '-- ' + str(page + 1) + " / " + str(pages) + ' --'
  page_footer.write('\n')
  page_footer.write(' ' * ((page_width - len(page_number)) / 2))
  page_footer.write(page_number)
  page_footer.write(' ' * ((page_width - len(page_number)) / 2))
  page_footer.write('\n\n')
  return page_footer.getvalue()


if __name__ == '__main__':
  seed()
  from optparse import OptionParser

  parser = OptionParser()
  parser.add_option('-f', '--filename', dest="filename", type="string",
      help="Filename to read", default=None, metavar="FILE")
  parser.add_option('-w', '--width', dest="width", type="int",
      help="Width of each line", default=80)
  parser.add_option('-c', '--cols', dest="cols", type="int",
      help="Number of columns", default=2)
  parser.add_option('-H', '--height', dest="page_height", type="int",
      help="Height of each page", default=24)

  (options, args) = parser.parse_args()

  cols = options.cols
  page_height = options.page_height
  page_width = options.width

  col_space = page_width / cols
  if cols > 1:
    col_width = col_space - ALLEY / 2
  else:
    col_width = col_space

  if options.filename is not None:
    with open(options.filename, 'r') as f:
      text = f.read()
  else:
    text = sys.stdin.read()

  paragraphs = text.split('\n\n')

  p_lines = []
  for p in paragraphs:
    l = mklist(p)
    if l is None:
      continue

    lines = split_lines(l, col_width)
    justify(lines, col_width)

    p_lines += lines
    p_lines += ['']

  height = int(ceil(1. * len(p_lines) / cols))

  fake_page_footer = page_footer()
  text_height = page_height - fake_page_footer.count('\n') - 1

  pages = int(ceil(1. * height / text_height))

  for page in range(pages):

    for row in range(text_height):
      for col in range(cols):
        index = page * text_height * cols + text_height * col + row
        if index < len(p_lines):
          line = str(p_lines[index])
          padding = col_space - len(line)

          if col != 0:
            sys.stdout.write(' ' * (ALLEY / 2))

          sys.stdout.write(line)

          if col != cols - 1:
            sys.stdout.write(' ' * padding)
      sys.stdout.write('\n')

    sys.stdout.write(page_footer(page, pages))
