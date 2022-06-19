'''

medaf/internal/config/default.py

Copyright (c) 2022, Anokidev.
Licensed in MIT License.
This file is part of MADAF.

This is responsible for parsing CLI commands.

'''

class DefaultConfig:

    '''Stores default configuration.'''

    rc_config = {
        'Project-Layout': {
            'Root-Path':'.',
            'Apps-Path':'apps',
            'Configs-Path':'configs',
            'Tests-Path':'tests'
        },
        'Installed-Apps': {}
    }
