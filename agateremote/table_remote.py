#!/usr/bin/env python

"""
This module contains the Remote extension to :class:`Table <agate.table.Table>`.
"""

import agate
import requests
import six

class TableRemote(object):
    @classmethod
    def from_url(cls, url, callback=agate.Table.from_csv, binary=False, **kwargs):
        """
        Download a remote file and pass it to a :class:`.Table` parser.

        :param url:
            URL to a file to load.
        :param callback:
            The method to invoke to create the table. Typically either
            :meth:`agate.Table.from_csv` or :meth:`agate.Table.from_json`, but
            it could also be a method provided by an extension.
        :param binary:
            If :code:`True` the downloaded data will be processed as a string,
            otherwise it will be treated as binary data. (e.g. for Excel files)
        """
        r = requests.get(url)

        if binary:
            content = six.BytesIO(r.content)
        else:
            if six.PY2:
                content = six.StringIO(r.content)
            else:
                content = six.StringIO(r.text)

        return callback(content, **kwargs)
