'''

medaf/core/cli/help.py

Copyright (c) 2022, Anokidev.
Licensed in MIT License.
This file is part of MADAF.

This is responsible for providing the help message..

'''


helper: str = """MADAF help:

FORMAT: madaf [commands] [subcommands] [app_name(For app and depen command)] [args]

madaf app | madaf -a
Manage your apps using this command.

    - madaf new [app_name] --config=[config]
    This command will create a new app that is specified by the [app_name]. If [config] set to 'false', it
    will prevent the CLU from creating a configuration folder.

    - madaf run [app_name] --debug=[debug]
    This command will run an app that is specified by the [app_name]. Any [debug] value will override the
    debug value in the apps configuration.

    - madaf app remove [app_name]
    This command will remove an app that is specified by the [app_name]. Note that installed apps config
    is not updated.

madaf depen | madaf -d
Manage your dependencies using this command.

    - madaf depen install [app_name] --global=[global]
      This command will install [app_name]'s dependency on a local directory called 'medaf_modules'.
      That is located in './apps/[app_name]/medaf_modules'. However, you can use the --global argument
      to install the dependency globally. WARNING: It is recommended to use Python virtual-env if you
      want to use the --global argument.

    - madaf depen remove [app_name] --global=[global]
      This command is the opposite of 'madaf depen install'.

madaf help | madaf -h | madaf --help
Shows the help message.

madaf version | madaf -version | madaf--version
Shows the version of MADAF."""
