"""Scraper
Do What I Tell You!
"Useful Screen Scraper for macOS"
https://www.github.com/scraper

# *#########################################################################* #
Scraper uses *Requests* and *Beautiful Soup* to parse html and send text
messages and alerts based on preset conditions. These conditions include:

    * Document Changes
    * Content Parse Results
    * Timer Intervals
    * Calendar Requests
    * Direct Request from user
    * Text File Scripts

Scraper requires Python 3.6+ and works best with lxml(speed) or
html5lib(accuracy) installed. Requires macOS to send texts.

# *#########################################################################* #
Beautiful Soup
Elixir and Tonic
"The Screen-Scraper's Friend"
http://www.crummy.com/software/BeautifulSoup/
Copyright (c) 2004-2019 Leonard Richardson
MIT License

Beautiful Soup uses a pluggable XML or HTML parser to parse a
(possibly invalid) document into a tree representation. Beautiful Soup
provides methods and Pythonic idioms that make it easy to navigate,
search, and modify the parse tree.

For more than you ever wanted to know about Beautiful Soup, see the
documentation:
http://www.crummy.com/software/BeautifulSoup/bs4/doc/

"""
# *#########################################################################* #

__author__ = "Michael Treanor (skeptycal@gmail.com)"
__version__ = "0.3.0"
__copyright__ = "Copyright (c) 2019 Michael Treanor"
# Use of this source code is governed by the MIT license.
__license__ = "MIT"

__all__ = ['Scraper']

# import re
# import traceback
# import warnings
# *#########################################################################* #
import os
import sys
from datetime import datetime
from typing import Any, Dict, List
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup

# *#########################################################################* #
# * DEFAULT_PARSER is set to the best choice for html parser based on:
# *      speed (lxml) > accuracy (html5lib) > built-in (html.parser)
# * If you need absolutely valid HTML5, use <html5lib>
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# do not use python's built in html parser before python 3.2.2
DEFAULT_PARSER: str = ''
try:  # use <lxml> for speed (HTML and/or XML) (VERY fast)
    import lxml
    DEFAULT_PARSER = 'lxml'
except:
    try:  # use <html5lib> to match browser closely (VERY slow)
        import html5lib
        DEFAULT_PARSER = 'html5lib'
    except:  # Python's built-in html parser
        DEFAULT_PARSER = 'html.parser'

# <lxml> is the ONLY supported XML parser
DEFAULT_XML: str = ''
try:
    import lxml
    DEFAULT_XML = 'lxml-xml'
except:
    pass
# *#########################################################################* #
