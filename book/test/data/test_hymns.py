import unittest

from data import Hymn, Hymns


class HymnsTestCase(unittest.TestCase):
    hymn1 = Hymn(title='T1', content='c1', echo=1)
    hymn2 = Hymn(title='T2', content='c2', echo=2)
    hymn3 = Hymn(title='T3', content='c3', echo=3)
    hymn4 = Hymn(title='T4', content='c4', echo=4)

    def test_hymns_list_len(self):
        hymns = Hymns()
        hymns.append(self.hymn1)
        hymns.append(self.hymn2)

        actual = len(hymns)

        self.assertEqual(actual, 2)

    def test_hymns_get_item(self):
        hymns = Hymns()
        hymns.append(self.hymn1)
        hymns.append(self.hymn2)

        actual = hymns[1]

        self.assertEqual(actual.title, 'T2')

    def test_concat_len(self):
        hymns = Hymns()
        hymns.append(self.hymn1)
        hymns.append(self.hymn2)

        hymns += [self.hymn3, self.hymn4]

        self.assertEqual(len(hymns), 4)
        self.assertEqual(hymns[3].title, 'T4')

    def test_init_params(self):
        hymns = Hymns(title='T', hymns=[self.hymn1, self.hymn2])

        self.assertEqual(len(hymns), 2)
        self.assertEqual(hymns[1].title, 'T2')


if __name__ == '__main__':
    unittest.main()
