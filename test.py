# -*-coding: utf-8 -*-


import os
import smartconf
import unittest


class TestSmartConf(unittest.TestCase):
    def setUp(self):
        self.ini_file = 'test.ini'
        sc = smartconf.SmartConf()
        cfg = sc.cd
        cfg.section1 = dict()
        cfg.section1['option1'] = 'value1'
        cfg.section1['foo'] = 'bar'
        sc.save(self.ini_file)

    def test_load(self):
        sc = smartconf.SmartConf()
        r = sc.load(self.ini_file)
        self.assertEqual(r.section1.option1, 'value1')

    def test_add_section(self):
        sc = smartconf.SmartConf()
        r = sc.load(self.ini_file)

        r.newsection = dict()
        r.newsection['foo'] = 'bar'
        sc.save()

        r2 = sc.load(self.ini_file)
        self.assertDictEqual(r.newsection, r2.newsection)
        self.assertEqual('bar', r2.newsection.foo)

    def test_remove_option(self):
        option = 'foo'
        sc = smartconf.SmartConf()
        r = sc.load(self.ini_file)
        r.section1.pop(option, None)
        sc.save()

        r2 = sc.load(self.ini_file)
        self.assertNotIn(option, r2.section1)

    def test_remove_section(self):
        sc = smartconf.SmartConf()
        r = sc.load(self.ini_file)
        member = 'section1'
        r.pop(member, None)
        sc.save()

        r2 = sc.load(self.ini_file)
        self.assertNotIn(member, r2)

    def tearDown(self):
        if os.path.exists(self.ini_file):
            os.remove(self.ini_file)

if __name__ == '__main__':
    unittest.main()
