#!python3-32
## Double check we're running the right python
## import platform
## print(platform.python_branch(), platform.python_compiler())

import requests
from bs4 import BeautifulSoup
import datetime

import os
import sys

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

goFundMeURL = r"http://www.gofundme.com/TheTrumpWall"

page = requests.get(goFundMeURL)
soup = BeautifulSoup(page.text, 'html.parser')

currentFunds = soup.select("h2.goal > strong")
currentFunds = currentFunds[0].text # there are two html elements with the funds, we only need 1

time = datetime.datetime.now()
time = time.strftime("%Y-%m-%d %H:%M:%S")

text = '"' + currentFunds + '", ' + time

print(text)

#with open(get_script_path() + "/log.txt", "a") as file:
#	file.write(text + "\n")
