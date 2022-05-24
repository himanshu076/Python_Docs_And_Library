from ast import Store
import logging
from socket import AI_V4MAPPED
from django.apps import apps

from requests import session
from yaml import add_multi_representer

logging.basicConfig(filemname='example.log', encoding='utf-8', level='logging.DEBUG')
logging.debug('This message should go to the log file')
logging.info('So Should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')






