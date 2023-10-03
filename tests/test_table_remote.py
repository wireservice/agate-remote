import agate

import agateremote  # noqa: F401


class TestRemote(agate.AgateTestCase):
    def setUp(self):
        self.rows = (
            (1, 'a', True, '11/4/2015', '11/4/2015 12:22 PM', '4:15'),
            (2, '👍', False, '11/5/2015', '11/4/2015 12:45 PM', '6:18'),
            (None, 'b', None, None, None, None)
        )

        self.column_names = [
            'number', 'text', 'boolean', 'date', 'datetime', 'timedelta'
        ]

        self.column_types = [
            agate.Number(),
            agate.Text(),
            agate.Boolean(),
            agate.Date(),
            agate.DateTime(),
            agate.TimeDelta()
        ]

        self.table = agate.Table(self.rows, self.column_names, self.column_types)

    def test_from_url_csv(self):
        url = 'https://raw.githubusercontent.com/onyxfish/agate/master/examples/test.csv'
        table = agate.Table.from_url(url)

        self.assertColumnNames(table, self.table.column_names)
        self.assertColumnTypes(table, [agate.Number, agate.Text, agate.Boolean,
                               agate.Date, agate.DateTime, agate.TimeDelta])

        self.assertRows(table, self.table.rows)

    def test_from_url_json(self):
        url = 'https://raw.githubusercontent.com/onyxfish/agate/master/examples/test.json'
        table = agate.Table.from_url(url, callback=agate.Table.from_json)

        self.assertColumnNames(table, self.table.column_names)
        self.assertColumnTypes(table, [agate.Number, agate.Text, agate.Boolean,
                               agate.Date, agate.DateTime, agate.TimeDelta])

        self.assertRows(table, self.table.rows)

    def test_from_url_json_keyed(self):
        url = 'https://raw.githubusercontent.com/onyxfish/agate/master/examples/test_key.json'
        table = agate.Table.from_url(url, callback=agate.Table.from_json, key='data')

        self.assertColumnNames(table, self.table.column_names)
        self.assertColumnTypes(table, [agate.Number, agate.Text, agate.Boolean,
                               agate.Date, agate.DateTime, agate.TimeDelta])

        self.assertRows(table, self.table.rows)
