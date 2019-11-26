import unittest


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_something(self):
        assert 1 == 1

    def test_something2(self):
        assert 12 == 12

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()