#!/usr/bin/env python

import agate

import agateremote

url = 'https://raw.githubusercontent.com/onyxfish/agate/master/examples/test.csv'
table = agate.Table.from_url(url)

print(table)

url = 'https://raw.githubusercontent.com/onyxfish/agate/master/examples/test.json'
table = agate.Table.from_url(url, callback=agate.Table.from_json)

print(table)

# import agateexcel
#
# url = 'https://github.com/onyxfish/agate-excel/raw/master/examples/test.xls'
# table = agate.Table.from_url(url, callback=agate.Table.from_xls, binary=True)
#
# print(table)
