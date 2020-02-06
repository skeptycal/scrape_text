#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# # scrape.py
import json
import os
import sys
from datetime import datetime
from typing import Any, Dict, List
from collections import Counter, deque

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# do not use python's built in html parser before python 3.2.2
# use <lxml> for speed (HTML and/or XML)
#   - <lxml> is the ONLY supported XML parser
# use <html5lib> to match browser closely
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
XML: bool = False
try:  # use <lxml> for speed (HTML and/or XML) (VERY fast)
    import lxml as parser
    DEFAULT_PARSER = 'lxml'
    XML = True
except:
    try:  # use <html5lib> to match browser closely (VERY slow)
        import html5lib as parser
        DEFAULT_PARSER = 'html5lib'
    except:  # Python's built-in html parser
        import html.parser as parser
        DEFAULT_PARSER = 'html.parser'

# *#########################################################################* #

sch = BlockingScheduler()
SCRIPT_PATH: str = os.getcwd() + "/sentMessage.scpt"
url: str = ''
script_text: str = ''
default_cell_number: str = ''
current_number: str = ''


class Contact_List(list):
    joe = Contact("Joe", "+555555555", "Somewhere Else")
    contact_list = Contact_List([ted, joe])
    contact_list.save_to_file()

    with open('list.txt') as p:
        p = json.load(p)
        print(p)


def get_default_cell_number() -> str:
    """ Get contacts from file. """
    # TODO make this actually get contacts ... like, a dict of them ...
    default_cell_number = 'xxxxxxxxxx'
    return default_cell_number


class WebPageSet(deque[WebPage]):
    DEFAULT_WEBPAGESET_SIZE = 2000  # maximum number of pages
    # TODO this should be 'maximum size' ... and check it's own size

    def __init__(self, iterable, maxlen, check_links=True, image_storage=''):
        if not maxlen or maxlen < 2:
            maxlen = cls.DEFAULT_WEBPAGESET_SIZE
        self.check_links = check_links
        self.store = True if image_storage else False
        self.image_storage = image_storage
        super().__init__(iterable, maxlen)

    def count(self):
        """ count tags, emails, ... whatever from the entire set """
        pass

    def common(self):
        """ find items that this pageset has in common. """
        pass

    def size_check(self):
        print(self.__sizeof__())


class WebPage(requests.Response):

    def __init__(self, url):
        super().__init__()
        self.url: str = url
        self.dirty: bool = true
        self.last_status: int = 0
        self.tags = {}
        self.auth: Tuple[str, str] = ('user', 'pass')
        # >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

    def get_url_content(self, url: str) -> str:
        """ Return decoded contents from <url> using default parameters. """
        self = requests.get(url)
        self.history.append()
        self.last_status = self.status_code
        if self.last_status == 200:
            return self.text
        else:
            return ''

    def tag_find(self,
                 tag_name: str,
                 attrs_pass: Dict[Any, Any],
                 parser_pass: str = DEFAULT_PARSER) -> List[Any]:
        """ Find matching tags from url. """
        soup = BeautifulSoup(self.text, features=DEFAULT_PARSER)
        return soup.findAll(name=tag_name, attrs=attrs_pass)

    def tag_list(self, tag_name: str):
        if self.dirty:
            self.tags = Counter(self.text)
        return self.tags

    def to_markdown():
        pass

    def to_json(self):
        return json.dumps(self.text)

    def stats(self):
        pass

    def soup(self):
        pass
        # return BeautifulSoup()


def send_text(cell_number: str, message: str, Verbose: bool = False) -> int:
    """ Return status of {message} sent to {cell_number}
            (Verbose - give CLI feedback if True """
    script_text = "osascript {} {} '{}'".format(SCRIPT_PATH,
                                                cell_number, message)
    try:
        print('send test: ', script_text)
        result = os.system(script_text)
    except:
        result = 42
    if Verbose:
        print('Sending this text to {}: {} '.format(cell_number, script_text))
        if result:
            print('Text Failed ...')
        else:
            print('Text Sent ...')
    return result


def main_test():

    url = 'https://www.indeed.com/jobs?q=python&l=Remote'
    matches = soup_match(url, tag_name='div', attrs_pass={'class': 'title'})
    print(type(matches))
    for match in matches:
        print(match.text.strip())

    for jobTitle in matches:
        if "Developer" in jobTitle.text:
            send_text(default_cell_number, 'jobTitle.text')
            break
        elif "Jr" in jobTitle.text:
            send_text(default_cell_number, 'jobTitle.text')
            break


def main():
    print('Default Parser: ', DEFAULT_PARSER)  # test
    TEST_STATUS: bool = False
    default_cell_number = '13616488261'
    current_cell_number = get_default_cell_number()
    if len(sys.argv) > 1:
        result = send_text(default_cell_number,
                           ' '.join(sys.argv[1:]), Verbose=TEST_STATUS)

    # test
    if test == True:
        test_cell_number = default_cell_number
        message_text = 'A python program just sent you a message ...'
        result = send_text(cell_number=test_cell_number,
                           message=message_text, Verbose=TEST_STATUS)
        print('Text result: ', result)


if __name__ == "__main__":
    main()
