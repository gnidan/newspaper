from nose.tools import *
from unittest import TestCase
import logging

from newspaper.ast.node import *
from newspaper.ast import helpers

logger = logging.getLogger(__name__)

class ASTTestCase(TestCase):
    def setup(self):
        logger.info("setup")

    def teardown(self):
        logger.info("teardown")

    def test_sentence(self):
        s = helpers.sentence("This sentence has five words")
        logger.debug(Word._fields)
        self.assertEquals(len(s.nodes), 5)
        self.assertEquals(s.nodes[0].word, "This")

