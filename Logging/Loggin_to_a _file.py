

import logging
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
logging.info('So should this')
logging.debug('This message should go to the log file')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

getattr(logging, loglevel.upper())