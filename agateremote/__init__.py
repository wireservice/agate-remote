#!/usr/bin/env python

from agateremote.archive import Archive

def patch():
    """
    Patch the features of this library onto agate's core
    :class:`Table <agate.table.Table>` and
    :class:`TableSet <agate.tableset.TableSet>`.
    """
    import agate
    from agateremote.table_remote import TableRemote

    agate.Table.monkeypatch(TableRemote)
