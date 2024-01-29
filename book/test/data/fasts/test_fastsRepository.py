import os
import unittest

from data.fasts import FastsRepository


class FastsRepositoryTestCase(unittest.TestCase):
    FASTS_DATA_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'res',
        'fasts.xml'
    )

    repo: FastsRepository

    def setUp(self):
        self.repo = FastsRepository(2024, self.FASTS_DATA_PATH)

    def test_load_all(self):
        self.assertGreater(len(self.repo.types), 0)
        self.assertGreater(len(self.repo.fasts), 0)


if __name__ == '__main__':
    unittest.main()
