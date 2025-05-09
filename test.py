import unittest
from main import is_standard, is_special, is_rejected

class TestPackageClassification(unittest.TestCase):

    def test_standard_package(self):
        pkg = {"width": 10, "height": 10, "length": 10, "mass": 5}
        self.assertTrue(is_standard(pkg))
        self.assertFalse(is_special(pkg))
        self.assertFalse(is_rejected(pkg))

    def test_special_by_mass(self):
        pkg = {"width": 10, "height": 10, "length": 10, "mass": 25}
        self.assertFalse(is_standard(pkg))
        self.assertTrue(is_special(pkg))
        self.assertFalse(is_rejected(pkg))

    def test_special_by_volume(self):
        pkg = {"width": 200, "height": 200, "length": 30, "mass": 5}
        self.assertFalse(is_standard(pkg))
        self.assertTrue(is_special(pkg))
        self.assertFalse(is_rejected(pkg))

    def test_rejected_package(self):
        pkg = {"width": 200, "height": 200, "length": 30, "mass": 30}
        self.assertFalse(is_standard(pkg))
        self.assertTrue(is_special(pkg))
        self.assertTrue(is_rejected(pkg))

    def test_edge_case_on_limits(self):
        pkg = {"width": 100, "height": 100, "length": 100, "mass": 20}
        self.assertFalse(is_standard(pkg))
        self.assertTrue(is_special(pkg))
        self.assertTrue(is_rejected(pkg))

if __name__ == '__main__':
    unittest.main()
