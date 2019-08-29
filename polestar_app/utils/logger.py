import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s : %(asctime)s: %(message)s')

class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)


log = Logger().logger