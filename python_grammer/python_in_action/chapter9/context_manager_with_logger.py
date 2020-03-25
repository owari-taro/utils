import logging
from contextlib import contextmanager

logger=logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler)

logger.setLevel(logging.INFO)




@contextmanager
def debug_context():
    level=logger.level
    try:
        logger.setLevel(logging.DEBUG)
        yield

    finally:
        #set back the level to initial 
        logger.setLevel(level)