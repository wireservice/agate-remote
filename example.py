#!/usr/bin/env python

import agate
import agateremote

table = agate.Table.from_url('https://raw.githubusercontent.com/onyxfish/agate/master/examples/test.csv')

print(table)

table = agate.Table.from_url('https://raw.githubusercontent.com/onyxfish/agate/master/examples/test.json', callback=agate.Table.from_json)

print(table)

# import agateexcel
#
# agateexcel.patch()
#
# table = agate.Table.from_url('https://github.com/onyxfish/agate-excel/raw/master/examples/test.xls', callback=agate.Table.from_xls, binary=True)
#
# print(table)
