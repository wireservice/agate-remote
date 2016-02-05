=====================
agate-remote |release|
=====================

.. include:: ../README.rst

Install
=======

To install:

.. code-block:: bash

    pip install agateremote

For details on development or supported platforms see the `agate documentation <http://agate.readthedocs.org>`_.

Usage
=====

agate-remote uses a monkey patching pattern to add read for xls and xlsx files support to all :class:`agate.Table <agate.table.Table>` instances.

.. code-block:: python

  import agate
  import agateremote

  agateremote.patch()

Calling :func:`.patch` attaches all the methods of :class:`.TableRemote` to :class:`agate.Table <agate.table.Table>`.

.. code-block:: python

  table = agate.Table.from_url('TKTK')
  print(table)

===
API
===

.. autofunction:: agateremote.patch

.. autoclass:: agateremote.table_remote.TableRemote
    :members:

Authors
=======

.. include:: ../AUTHORS.rst

Changelog
=========

.. include:: ../CHANGELOG.rst

License
=======

.. include:: ../COPYING

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
