#! /usr/bin/env python

import time
import unittest

import logging; logger = logging.getLogger("underworlds.testing.basic_server_interaction")
logging.basicConfig(level=logging.DEBUG)

import underworlds
import underworlds.server
from underworlds.types import Node


class TestSingleUser(unittest.TestCase):

    def setUp(self):
        self.server = underworlds.server.start()

        self.ctx = underworlds.Context("unittest - basic server interaction")


    def test_uptime(self):

        uptime = self.ctx.uptime()
        self.assertEqual(type(uptime), float)
        self.assertGreater(1,uptime)

        time.sleep(1)
        uptime = self.ctx.uptime()
        self.assertGreaterEqual(uptime,1)
        self.assertGreater(2, uptime)

    def tearDown(self):
        self.ctx.close()
        self.server.stop(0).wait()

def test_suite():
     suite = unittest.TestLoader().loadTestsFromTestCase(TestSingleUser)
     return suite


if __name__ == '__main__':
    unittest.main()
