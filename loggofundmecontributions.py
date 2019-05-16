#!python3-32

### https://pastebin.com/cLXz8mws

"""
The purpose of this script is to scrape gofund me for a list of the donors, their contribution,
and a profile picture if any is available
"""

import requests
import argparse
from parsedatetime import Calendar
from datetime import datetime
from bs4 import BeautifulSoup

URL = "https://www.gofundme.com/mvc.php?route=donate/pagingDonationsFoundation&url={}&idx={}&type=recent"
Calendar()

def parse_time(time):
    cal = Calendar()
    time, foo = cal.parse(time)
    time = datetime(*time[:6])
    return time.isoformat()
 
def parse(out, index):
    """
    Return a dict of the values
    """
    parsed = BeautifulSoup(out, 'html.parser')
    supporters = parsed.findAll("div", {"class":"supporter js-donation-content "})
    for supporter in supporters:
        data_id = supporter.attrs['data-id']
        name = supporter.findAll("div", {"class":"supporter-name"})[0].getText()
        amount = supporter.findAll("div", {"class":"supporter-amount"})[0].getText()
        time = parse_time(supporter.findAll("div", {"class":"supporter-time"})[0].getText())
        try:
            thumbnail = supporter.find("img").get("src")
        except AttributeError:
            # No Picture
            thumbnail = ""
        try:
            print("{},{},{},{},{}".format(data_id, name, amount, time, thumbnail).encode("utf-8") ,flush=True)
        except:
            print(index)

def main(campaign):
    index = 0
    while True:
        out = requests.get(URL.format(campaign, index))
        if out.status_code == 200:
            parse(out.text, index)
            index += 10
        else:
            break

if __name__ in "__main__":
    parser = argparse.ArgumentParser(description='Scrapes gofundme donors and values to a sqlite3 databases')
    parser.add_argument('-c', '--campaign',
                        help='Campaign name',
                        required=False,
                        default='TheTrumpWall')
    args = parser.parse_args()
    main(args.campaign)