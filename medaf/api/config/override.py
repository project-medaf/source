'''

medaf/api/config/override.py

Copyright (c) 2022, Project MEDAF.
Licensed in MIT License.
This file is part of MEDAF.

This is responsible for overriding default configurations.

'''

from medaf.internal.config.get import RCConfig

class RCConfig:

    '''Override default RC configurations.'''

    def __init__(self):

        self.__config = {
            'Project-Layout': {
                'Root-Path':'.',
                'Apps-Path':'apps',
                'Configs-Path':'configs',
                'Tests-Path':'tests'
            },
            'Installed-Apps': {},
            'Debug-Mode': True
        }

    def modify(self, key: str, value: any):

        '''Modify default configurations.'''

        self.__config[key] = value

    def load(self):

        '''Load the configuration.'''

        RCConfig.load(self.__config)
