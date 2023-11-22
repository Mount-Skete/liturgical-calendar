import unittest
from datetime import datetime

from data import Feast, Feasts, FeastType, FeastRank, Hymns


class FeastsTestCase(unittest.TestCase):
    feast1 = Feast(title='F1',
                   julian=datetime(2023, 1, 1),
                   gregorian=datetime(2023, 1, 14),
                   type=FeastType.GREAT,
                   rank=FeastRank.GREAT_DOXOLOGY,
                   hymns=Hymns())
    feast2 = Feast(title='F2',
                   julian=datetime(2023, 2, 1),
                   gregorian=datetime(2023, 2, 14),
                   type=FeastType.GREAT,
                   rank=FeastRank.GREAT_DOXOLOGY,
                   hymns=Hymns())

    def test_feasts_list_len(self):
        feasts = Feasts()
        feasts.append(self.feast1)
        feasts.append(self.feast2)

        actual = len(feasts)

        self.assertEqual(actual, 2)

    def test_feasts_get_item(self):
        feasts = Feasts()
        feasts.append(self.feast1)
        feasts.append(self.feast2)

        actual = feasts[1]

        self.assertEqual(actual.title, 'F2')

    def test_concat_len(self):
        feasts = Feasts()
        feasts.append(self.feast1)

        feasts += [self.feast2]

        self.assertEqual(len(feasts), 2)

    def test_for_date(self):
        feasts = Feasts()
        feasts.append(self.feast1)
        feasts.append(self.feast2)

        actual = feasts.for_date(datetime(2023, 1, 14))

        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0].title, 'F1')

    def test_init_params(self):
        feasts = Feasts(feasts=[self.feast1, self.feast2])

        self.assertEqual(len(feasts), 2)
        self.assertEqual(feasts[1].title, 'F2')


if __name__ == '__main__':
    unittest.main()
