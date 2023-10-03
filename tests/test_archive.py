import agate

import agateremote


class TestArchive(agate.AgateTestCase):
    def setUp(self):
        self.archive = agateremote.Archive('https://github.com/vincentarelbundock/Rdatasets/raw/master/csv/')

    def test_get_table(self):
        table = self.archive.get_table('sandwich/PublicSchools.csv')

        self.assertColumnNames(table, ('rownames', 'Expenditure', 'Income'))
        self.assertColumnTypes(table, [agate.Text, agate.Number, agate.Number])
        self.assertEqual(len(table.rows), 51)
