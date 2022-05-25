import logging
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# numeric_level = getattr(logging, loglevel.upper())
# if not isinstance(numeric_level, int):
#     raise ValueError('Invalid log level: %s' % loglevel)
# logging.basicConfig(level=numeric_level)

# Removed log & add new
# The output will be the same as before, but the log file is no longer appended to, so the messages from earlier runs are lost.
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
# logging.debug('This message should go to the log file')


# ------------------------------------------------------------------------------------------------------------------------------
# Logging from multiple modules
# import mylib

# def main():
#     # breakpoint()
#     logging.basicConfig(filename='example.log', level=logging.INFO)
#     logging.info("Standard")
#     mylib.do_something()
#     logging.info("Finished")


# if __name__ == '__main__':
#     main()

# ----------------------------------------------------------------------------------------------------------------------------
# logging.warning('%s before you %s', 'Look', 'leap!')

# ------------------------------------------------------------------------------------------------------------------------------
# Changing the format of displayed messages
# To change the format which is used to display messages, you need to specify the format you want to use:

# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('Hi, Something-Something')


# ------------------------------------------------------------------------------------------------------------------------------
# Displaying the date/time in messages
# logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
# logging.warning('is when this event was logged.')

# ------------------------------------------------------------------------------------------------------------------------------
# If you need more control over the formatting of the date/time, provide a datefmt argument to basicConfig, as in this example:
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('is when this event was logged.')


# ------------------------------------------------------------------------------------------------------------------------------
# Configuring Logging -

# import logging

# # create logger
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)

# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # add formatter to ch
# ch.setFormatter(formatter)

# # add ch to logger
# logger.addHandler(ch)

# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

# ------------------------------------------------------------------------------------------------------------------------------

# import logging
# import logging.config

# logging.config.fileConfig('logging.conf')

# # create logger
# logger = logging.getLogger('simpleExample')

# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

# ------------------------------------------------------------------------------------------------------------------------------
import logging
logging.getLogger('foo').addHandler(logging.NullHandler())

