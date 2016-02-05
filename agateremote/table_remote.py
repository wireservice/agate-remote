#!/usr/bin/env python

"""
This module contains the Remote extension to :class:`Table <agate.table.Table>`.
"""

import agate

class TableRemote(object):
    @classmethod
    def from_url(cls, url, **kwargs):
        """
        Download a remote file and pass it to a parser.

        :param url:
            Path to an XLS file to load or a file-like object for one.
        """
        #return agate.Table(rows, column_names)
        pass
