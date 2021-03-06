
# *Configuration server example -

# import logging
# import logging.config
# import time
# import os

# # read initial config file
# logging.config.fileConfig('logging.conf')

# # create and start listener on port 9999
# t = logging.config.listen(9999)
# t.start()

# logger = logging.getLogger('simpleExample')

# try:
#     # loop through logging calls to see the difference
#     # new configurations make, until Ctrl+C is pressed
#     while True:
#         logger.debug('debug message')
#         logger.info('info message')
#         logger.warning('warn message')
#         logger.error('error message')
#         logger.critical('critical message')
#         time.sleep(5)
# except KeyboardInterrupt:
#     # cleanup
#     logging.config.stopListening()
#     t.join()

# -------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/env python

import socket, sys, struct

with open(sys.argv[0], 'rb') as f:
    data_to_send = f.read()

HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting...')
breakpoint()
s.connect((HOST, PORT))
print('sending config...')
s.send(struct.pack('>L', len(data_to_send)))
s.send(data_to_send)
s.close()
print('complete')