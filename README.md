# This is Medaf.

Medaf is an open-source app framework that is based on the plugin-oriented architecture. You can use Medaf and some plugin suites to build mobile, desktop, nor web applications easily with some knowledge on Python.

## Installation:

1. PIP:

```bash
pip install medaf
```

For you source builders, you can build Medaf by cloning the repo, build the source, and the install it:

2. Build the source code on Mac OS, Linux, and other UNIX Operating System (Bash):

```bash
git clone https://www.github.com/project-medaf/src.git
cd src/script
./install-for-nix.sh
```

3. Build the source code on Windows (PowerShell):

```powershell
git clone https://www.github.com/project-medaf/src.git
cd src\script
.\install-for-win.sh
```

## Architecture:

Medaf is going to be plugin-based, meaning that each functionality is going to be provided by plugins. When creating a new project, you What kind of plugins? Well, this table is going to provide you with information that you need:

---
Type: ['Content', 'Middleware']
Description: ['This type of plugins are the one that are going to create response.', 'This type of plugins act as a middleware that can modify requests and responses.']
---

## License:

Medaf is open-source and is licensed in [MIT License](/LICENSE.md)

## Contributing:

See [CONTRIBUTING.md](/CONTRIBUTING.md).

## Code of Conduct:

See [CODE_OF_CONDUCT.md](/CODE_OF_CONDUCT.md).