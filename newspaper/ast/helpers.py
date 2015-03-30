import logging

from newspaper.ast.node import *

logger = logging.getLogger(__name__)

def sentence(s=""):
    words = s.split(' ')

    return Sentence([Word(w) for w in words])
