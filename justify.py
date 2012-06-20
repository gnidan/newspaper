#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2012 g. nicholas d'andrea <nick@gnidan.org>

import sys
from random import seed, random

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


if __name__ == '__main__':
  seed()
  from optparse import OptionParser

  parser = OptionParser()
  parser.add_option('-w', '--width', dest="width", type="int",
      help="Number of columns for each line", default=80)

  (options, args) = parser.parse_args()

  text = sys.stdin.read()

  l = mklist(text)

  lines = split_lines(l, options.width)
  justify(lines, options.width)

  for line in lines:
    print line