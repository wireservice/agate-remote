#!/usr/bin/env python

"""
This module contains the Remote extension to :class:`Table <agate.table.Table>`.
"""

from tempfile import mkstemp

import agate
import requests

class TableRemote(object):
    @classmethod
    def from_url(cls, url, callback=agate.Table.from_csv, **kwargs):
        """
        Download a remote file and pass it to a parser.

        :param url:
            Path to an XLS file to load or a file-like object for one.
        """
        path = 'temp'

        r = requests.get(url)

        with open(path, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)

        return callback(path, **kwargs)
