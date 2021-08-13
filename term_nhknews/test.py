# -*- encoding:utf-8 -*-

import feedparser
import pprint


RSS_URL = 'https://www.nhk.or.jp/rss/news/cat0.xml'

d = feedparser.parse(RSS_URL)
pprint.pprint(d)

print((d.get('feed')).get('subtitle'))
for entry in d.entries:
    print(entry.title, entry.link)
