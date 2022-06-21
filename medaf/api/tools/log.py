'''

medaf/api/logging.py

Copyright (c) 2022, Anokidev.
Licensed in MIT License.
This file is part of medaf.

This is responsible for parsing CLI commands.

'''

import logging

from medaf.api.config.get import GetRCConfig

class Log:

    '''
        Log stuff, you know.
    '''

    def __init__(self, name: str) -> None:

        config = GetRCConfig()
        debug = config.get('Debug-Mode')
        self.__name: str = name

        if debug is True:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(message)s', force=True)
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(message)s', force=True)

    # GRAND LOG.

    def grand_debug(self, message: str) -> None:
        '''Log debug message.'''
        logging.debug(f"[{self.__name}] ==> {message}")

    def grand_info(self, message: str) -> None:
        '''Log info message.'''
        logging.info(f"[{self.__name}] ==> {message}")

    def grand_warning(self, message: str) -> None:
        '''Log warning message.'''
        logging.warning(f"[{self.__name}] ==> {message}")

    def grand_error(self, message: str) -> None:
        '''Log error message.'''
        logging.error(f"[{self.__name}] ==> {message}")

    def grand_critical(self, message: str) -> None:
        '''Log critical message.'''
        logging.critical(f"[{self.__name}] ==> {message}")

    # PARENT LOG.

    def parent_debug(self, message: str) -> None:
        '''Log debug message.'''
        logging.debug(f"                 --> {message}")

    def parent_info(self, message: str) -> None:
        '''Log info message.'''
        logging.info(f"                 --> {message}")

    def parent_warning(self, message: str) -> None:
        '''Log warning message.'''
        logging.warning(f"                 --> {message}")

    def parent_error(self, message: str) -> None:
        '''Log error message.'''
        logging.error(f"                 --> {message}")

    def parent_critical(self, message: str) -> None:
        '''Log critical message.'''
        logging.critical(f"                 --> {message}")

    # CHILD LOG.

    def child_debug(self, message: str) -> None:
        '''Log debug message.'''
        logging.debug(f"                   > {message}")

    def child_info(self, message: str) -> None:
        '''Log info message.'''
        logging.info(f"                   > {message}")

    def child_warning(self, message: str) -> None:
        '''Log warning message.'''
        logging.warning(f"                   > {message}")

    def child_error(self, message: str) -> None:
        '''Log error message.'''
        logging.error(f"                   > {message}")

    def child_critical(self, message: str) -> None:
        '''Log critical message.'''
        logging.critical(f"                   > {message}")
