import unittest
import numpy as np
from control.ctrlutil import *

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.mag = np.array([1, 10, 100, 2, 0.1, 0.01])
        self.db = np.array([0, 20, 40, 6.0205999, -20, -40])

    def check_unwrap_array(self, angle, period=None):
        if period is None:
            angle_mod = angle % (2 * np.pi)
            angle_unwrap = unwrap(angle_mod)
        else:
            angle_mod = angle % period
            angle_unwrap = unwrap(angle_mod, period)
        np.testing.assert_array_almost_equal(angle_unwrap, angle)

    def test_unwrap_increasing(self):
        angle = np.linspace(0, 20, 50)
        self.check_unwrap_array(angle)

    def test_unwrap_decreasing(self):
        angle = np.linspace(0, -20, 50)
        self.check_unwrap_array(angle)

    def test_unwrap_inc_degrees(self):
        angle = np.linspace(0, 720, 50)
        self.check_unwrap_array(angle, 360)

    def test_unwrap_dec_degrees(self):
        angle = np.linspace(0, -720, 50)
        self.check_unwrap_array(angle, 360)

    def test_unwrap_large_skips(self):
        angle = np.array([0., 4 * np.pi, -2 * np.pi])
        np.testing.assert_array_almost_equal(unwrap(angle), [0., 0., 0.])

    def test_unwrap_list(self):
        angle = [0, 2.2, 5.4, -0.4]
        angle_unwrapped = [0, 0.2, 0.4, 0.6]
        np.testing.assert_array_almost_equal(unwrap(angle, 1.0), angle_unwrapped)


def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestUtils)

if __name__ == "__main__":
    unittest.main()
