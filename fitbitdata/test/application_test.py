# -*- coding: utf-8 -*-
"""
    fitbitdata.test.app_test
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Unit testing app module

    :copyright: (c) 2015 by Saeed Abdullah.

"""

import unittest

from fitbitdata import app

class AppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = fitbitdata.app.test_client()
