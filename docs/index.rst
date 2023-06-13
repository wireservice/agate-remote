======================
agate-remote |release|
======================

.. include:: ../README.rst

Install
=======

To install:

.. code-block:: bash

    pip install agate-remote

For details on development or supported platforms see the `agate documentation <https://agate.readthedocs.org>`_.

Usage
=====

agate-remote uses a monkey patching pattern to add read support for remote files to all :class:`agate.Table <agate.table.Table>` instances.

.. code-block:: python

    import agate
    import agateremote

Importing agate-remote adds methods to :class:`agate.Table <agate.table.Table>`.

.. code-block:: python

    table = agate.Table.from_url('https://raw.githubusercontent.com/onyxfish/agate/master/examples/test.csv')
    print(table)

agate-remote also let's you create an :class:`Archive`, which is a reference to a group of tables with a known path structure.

.. code-block:: python

    archive = agateremote.Archive('https://github.com/vincentarelbundock/Rdatasets/raw/master/csv/')

    table = archive.get_table('sandwich/PublicSchools.csv')
    print(table)

===
API
===

.. autofunction:: agateremote.table_remote.from_url

.. autoclass:: agateremote.archive.Archive
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
