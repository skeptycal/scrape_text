# scrape.py
import os
from datetime import datetime
from typing import Any, Dict, List

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


def get_url_content(url: str) -> bytes:
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return b''


def soup_match(url: str, div: str, attrs: Dict[Any, Any]) -> List[Bea .element.Tag]:
    html = get_url_content(url)
    soup = BeautifulSoup(html, features=DEFAULT_PARSER)
    return soup.findAll(name='div', attrs={'class': 'title'})


def send_text(cell_number: str, message: str) -> int:
    script_text = "osascript {} {} '{}'".format(SCRIPT_PATH,
                                                cell_number, message)
    os.system(script_text)


def main():
    url = 'https://www.indeed.com/jobs?q=web%20developer&l=Denver%2C%20CO&vjk=0c0f7c56b3d79b4c'
    html = get_url_content(url)
    # response = requests.get(url)
    # html = response.content
    soup = BeautifulSoup(html, features="html.parser")
    matches = soup.findAll(name='div', attrs={'class': 'title'})
    print(type(matches))
    for match in matches:
        print(match.text.strip())

    for jobTitle in matches:
        if "Developer" in jobTitle.text:
            send_text = "osascript {} {} '{}' in {} ".format(SCRIPT_PATH,
                                                             cell_number, jobTitle.text, soup.name)
            print(send_text)
            os.system(send_text)
            break
        # elif "Jr" in jobTitle.text:
        #     os.system(
        #         "osascript sendMessage.scpt {} '{}' ".format(cell_number, message))
        #     break


if __name__ == "__main__":
    print(DEFAULT_PARSER)
    cell_number: str = '13616488216'
    message = 'A python program just sent you a message ...'
    # main()
