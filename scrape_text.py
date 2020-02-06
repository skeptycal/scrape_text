#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# scrape.py
import json
import os
import sys
from datetime import datetime
from typing import Any, Dict, List

# * per https://www.crummy.com/software/BeautifulSoup/bs4/doc/
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

# https://medium.com/better-programming/so-i-wrote-a-py-web-scraper-that-sends-me-scpt-text-messages-about-job-postings-34ffef9a1128
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

sch = BlockingScheduler()
CWD: str = os.getcwd()
SCRIPT_PATH: str = CWD + "/sentMessage.scpt"
url: str = ''
script_text: str = ''
default_cell_number: str = ''
current_number: str = ''


class Contact_List:
    def __init__(self):
        self.contacts = []

    def __repr__(self):
        return json.dumps(self)

    def add_contact(self, name="-", phonenumber="-", address="-"):
        new_contact = Contact(name, phonenumber, address)
        self.contacts.append(new_contact)
        return new_contact

    def save_to_file(self):
        with open("contact_list.json", 'w') as f:
            f.write(str(self.contacts))


class Contact:
    def __init__(self, name="-", phonenumber="-", address="-"):
        self.name = name
        self.phonenumber = phonenumber
        self.address = address

    def __repr__(self):
        return json.dumps({"name": self.name, "phonenumber": self.phonenumber, "address": self.address})


def test_contacts():

    contact_list = Contact_List()

    ted = contact_list.add_contact("Ted", "+000000000", "Somewhere")
    joe = contact_list.add_contact("Joe", "+555555555", "Somewhere Else")

    contact_list.save_to_file()

    with open('list.txt') as p:
        p = json.load(p)
        print(p)


def get_default_cell_number() -> str:
    """ Get contacts from file. """
    # TODO make this actually get contacts ... like, a dict of them ...
    default_cell_number = 'xxxxxxxxxx'
    return default_cell_number


def get_url_content(url: str) -> bytes:
    """ Return bytes containing contents from the given url. """
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return b''


def soup_match(url: str,
               tag_name: str,
               attrs_pass: Dict[Any, Any],
               parser_pass: str = DEFAULT_PARSER) -> List[Any]:
    """ Find matching tags from url. """
    html = get_url_content(url)
    soup = BeautifulSoup(html, features=DEFAULT_PARSER)
    return soup.findAll(name=tag_name, attrs=attrs_pass)


def send_text(cell_number: str, message: str, Verbose: bool = False) -> int:
    """ Return status of {message} sent to {cell_number}
            (Verbose - give CLI feedback if True """
    script_text = "osascript {} {} '{}'".format(SCRIPT_PATH,
                                                cell_number, message)
    try:
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


def main():

    url = 'https://www.indeed.com/jobs?q=web%20developer&l=Denver%2C%20CO&vjk=0c0f7c56b3d79b4c'
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


if __name__ == "__main__":
    # print('Default Parser: ', DEFAULT_PARSER) # test
    TEST_STATUS: bool = False
    default_cell_number = '13616488216'
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
        # main()
