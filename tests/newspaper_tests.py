from nose.tools import *
import logging

import newspaper

logger = logging.getLogger(__name__)

def setup():
    logger.info("setup")

def teardown():
    logger.info("teardown")

def test_basic():
    logger.info("test")
