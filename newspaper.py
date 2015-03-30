import logging

logger = logging.getLogger(__name__)

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


from newspaper.parse import parser

s = parser("hi there\nhow is it going\ni hope it is going quite well\n\n").paragraph()

logger.debug(str(s))
