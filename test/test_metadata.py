import unittest

import configurator as pkg


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertIsNotNone(pkg.__metadata_version__, "Metadata Version is None")
        self.assertIsNotNone(pkg.__title__, "Package Name is None")
        self.assertIsNotNone(pkg.__version__, "Package Version is None")
        self.assertIsNotNone(pkg.__summary__, "Package Summary is None")
        self.assertIsNotNone(pkg.__author__, "Package Author is None")
        self.assertIsNotNone(pkg.__maintainer__, "Package Maintainer is None")
        self.assertIsNotNone(pkg.__license__, "Package License is None")
        self.assertIsNotNone(pkg.__url__, "Package URL is None")
        self.assertIsNotNone(pkg.__download_url__, "Package Download URL is None")
        self.assertIsNotNone(pkg.__project_urls__, "Package Version is None")
        self.assertIsNotNone(pkg.__copyright__, "Package Version is None")
        self.assertIsNotNone(pkg.__data_dir__, "Package Version is None")


if __name__ == "__main__":
    unittest.main()
