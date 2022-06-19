'''

medaf/api/logging.py

Copyright (c) 2022, Anokidev.
Licensed in MIT License.
This file is part of MADAF.

This is responsible for parsing CLI commands.

'''

import logging

from madaf.api.config.get import GetAppConfig

class Log:

    '''
        Log stuff, you know.
    '''

    def __init__(self, name: str) -> None:

        config = GetAppConfig()
        debug = config.get['Debug-Mode']

        if debug is True:
            logging.basicConfig(level=logging.DEBUG,
                                format=f'[{name}][%(levelname)s] > %(message)s', force=True)
        else:
            logging.basicConfig(level=logging.INFO,
                                format=f'[{name}] [%(levelname)s] > %(message)s', force=True)

    def debug(self, message: str) -> None:
        '''Log debug message.'''
        logging.debug(message)

    def info(self, message: str) -> None:
        '''Log info message.'''
        logging.info(message)

    def warning(self, message: str) -> None:
        '''Log warning message.'''
        logging.warning(message)

    def error(self, message: str) -> None:
        '''Log error message.'''
        logging.error(message)

    def critical(self, message: str) -> None:
        '''Log critical message.'''
        logging.critical(message)
