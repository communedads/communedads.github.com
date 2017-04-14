import feedparser as fp
from itertools import takewhile
import time

latest = fp.parse("http://feeds.soundcloud.com/users/soundcloud:users:239382065/sounds.rss")["entries"][0]

pdata = latest.published_parsed
soundcloud_id = latest.links[1].href \
                    .split("/")[4] \
                    .split("-")[0]

output = """---
layout: post
title: """ + latest["title"] + """
date: """ + time.strftime("%Y-%m-%d",pdata) + """
categories: episodes
comments: true
---
""" + latest["description"] + """

<iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/""" + soundcloud_id + """&amp;color=ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false"></iframe>"""

print output

