#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

t = urllib2.urlopen('http://www.gmasson.com.br/').read()

# TAG
tags = t.split('<a')[1:]
tags = [ tag.split('</a>')[0].split('>',1)[1] for tag in tags ]

for i in tags:
    print i
