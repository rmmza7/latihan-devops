import unittest
from app import hitung_diskon

class TestApp(unittest.TestCase):
    def test_hitung_diskon_normal(self):
        self.assertEqual(hitung_diskon(100000, 10), 90000)

if __name__ == '__main__':
    unittest.main()
