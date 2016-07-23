# class YourDict(dict):
#     def __setattr__(self,attr,value):
#         self[attr] = value

#     def __getattr__(self,attr):

import unittest
from assignment1 import YourDict

class TestMyModule(unittest.TestCase):

    def test_if_is_equal(self):
        test_dict = YourDict()
        test_dict['england'] = 1000
        self.assertEqual(test_dict.england,test_dict['england'])

    def test_if_is__not_equal(self):
        test_dict = YourDict()
        test_dict['germany'] = 2000
        self.assertNotEqual(test_dict.germay, test_dict['germany'])

if '__main__' == __name__:
    unittest.main()

