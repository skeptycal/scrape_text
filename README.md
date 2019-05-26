# scraper version 0.3.0

[![Netlify Status](https://api.netlify.com/api/v1/badges/416b8ca3-82db-470f-9adf-a6d06264ca75/deploy-status)](https://app.netlify.com/sites/mystifying-keller-ab5658/deploys)  ![Azure DevOps builds](https://img.shields.io/azure-devops/build/skeptycal0275/skeptycal/1.svg?color=blue&label=Azure%20DevOps&style=popout) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask.svg?color=Yellow&label=Python&style=popout) ![Twitter Follow](https://img.shields.io/twitter/follow/skeptycal.svg?label=%40skeptycal&style=social) ![GitHub followers](https://img.shields.io/github/followers/skeptycal.svg?style=social)

Last update: 05-25-2019 | 01:38:26

---

### Scraper parses html and sends text messages and alerts based on preset conditions.

```bash

###############################################################################
# scraper : Scraper parses html and sends text messages and alerts based on preset conditions. (version 0.3.0)
#
# author    - Michael Treanor  <skeptycal@gmail.com>
# copyright - 2019 (c) Michael Treanor
# license   - MIT <https://opensource.org/licenses/MIT>
# github    - https://www.github.com/skeptycal
#
# Usage: scraper {init|reset|version|help}
#
#   Parameters:
#       [init, -i, --init]        -- install and initialize
#       [commit, -m] MESSAGE      -- git commit and push with MESSAGE
#       [reset, -r, --reset]      -- reset initial repo files (with backup)
#       [version, -v, --version]  -- display version information
#       [help, -h, --help]        -- display usage and information
#
###############################################################################


# Run this script if changes to the pre-commit or yaml configuration are added.

# Please make changes directly to the 'template' file:
#     <.pre\-commit-template.yaml>
# and run the script 'pc' to update the yaml to current versioning.

# Please do not make changes directly to the 'config' file. The 'config' file:
#     <.pre-commit-config.yaml>
#   is created and updated by the 'pc' script automatically in order to maintain
#   the correct, current versioning from git (master sha) so changes to the
#   commit file will be overwritten when updating.
###############################################################################


```

---

```bash
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── __init__.py
├── __pycache__
│   └── __init__.cpython-37.pyc
├── bak
│   ├── README.md.bak
│   ├── codecov.yml.bak
│   ├── pipfile.bak
│   ├── requirements.txt.bak
│   └── setup.py.bak
├── codecov.yml
├── contact_list.json
├── requirements.txt
├── scrape_text.py
├── scraper.json
├── scraper.py
├── sentMessage.scpt
└── setup.py

2 directories, 18 files
```
