
import unittest
import json
from unittest_data_provider import data_provider
from ddt import ddt, data, file_data, unpack
from pprint import pprint

@ddt
class TestItemId(unittest.TestCase):
    itemIds = lambda: (
        ( 'q42', ),
        ( 'Q42', ),
        ( 'Q1', ),
        ( 'Q1000', ),
        ( 'Q31337', ),
    )
        
    @file_data('bbb.json')
    def test_file_data_dict(self, value):
        
        pprint(value["from"])
        self.assertTrue(bool(value["succes"]))
        #self.assertEquals(15, value["nm"], "nie jest rowne")
       
    