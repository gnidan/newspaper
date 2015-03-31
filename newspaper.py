import logging

logger = logging.getLogger(__name__)

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


from newspaper.parse import parser

s = parser("hi there\n=====\n\nhi how are you\ni am quite well\n\n").document()

logger.debug(str(s))
