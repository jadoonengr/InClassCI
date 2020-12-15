import unittest
from mod1 import addition as md1


class TestAdd(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(md1(1,2),3)
        self.assertEqual(md1(1,5),6)
        self.assertEqual(md1(30,4),34)
        self.assertEqual(md1(65,36),101)
     
unittest.main()