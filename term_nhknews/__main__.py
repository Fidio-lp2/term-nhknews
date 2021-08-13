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
    with open(datapath, 'r') as data_file:
        URL_DATA: Final[Dict[str, str]] = json.load(data_file)

    parser = argparse.ArgumentParser(
            description="If you use this app, \
            you can know easily social situation on command line!!"
    )

    parser.add_argument('-t', '--type', default="main",
                        help="You can choose the news type which you want.\
                        can choose 'main', 'society', 'chemotherapy', \
                        'politics', 'economy', 'international', \
                        'sports', 'culture', 'live'."
                        )
    parser.add_argument('-n', "--number", default=7,
                        help="You can set the number of news \
                        that you want know.")

    args = parser.parse_args()

    parse_data = feedparser.parse(URL_DATA[args.type])
    feed = parse_data["feed"]
    entries = parse_data["entries"]

    news_num: str = str(args.number) \
        if args.number <= len(entries) else str(len(entries))

    print(blue("-*- " + feed["title"]) + ' ' + \
        cyan(feed["updated"][:-6]) + ' ' + \
        cyan('[' + news_num + '/' + \
        str(len(entries)) + ']' + " -*-"))
    i: int = 0
    for entry in entries:
        print(magenta('▸ ') + white(str(entry.title)))
        print(green(entry.summary))
        print(yellow(entry.link))
        i += 1
        if int(args.number) > i:
            print()
        if int(args.number) <= i:
            break
