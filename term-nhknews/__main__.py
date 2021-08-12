# -*- coding: utf-8 -*-
"""
main script

"""
import json
from typing import (
    Final,
    Dict
)
import argparse
import feedparser
from util import inves_app_path
from color import *


def main():
    datapath: str = inves_app_path() + "/urldata.json"
    with open(datapath, 'r') as dataFile:
        URLDATA: Final[Dict[str, str]] = json.load(dataFile)

    parser = argparse.ArgumentParser(
            description="If you use this app, \
            you can know easily social situation on command line!!"
    )

    parser.add_argument('-t', '--type', default="main",
                        help="You can choose the news type which you want.\
                        can choose 'main', 'society', 'chemotherapy', 'politics',\
                        'economy', 'international', 'sports', 'culture', 'live'."
                        )

    args = parser.parse_args()

    feed = feedparser.parse(URLDATA[args.type])
    print(feed["feed"]["title"] + ' ' + \
            '[' + args.type + ']' + ' ' + feed["feed"]["updated"])
    for entry in feed.entries:
        print(entry.title + '\n' )#+ entry.summary + '\n' + entry.link)
