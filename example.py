#!/usr/bin/env python

import agate
import agateremote

agateremote.patch()

table = agate.Table.from_url('TKTK')

print(table)
