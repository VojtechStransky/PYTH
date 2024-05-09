import script as f
import unittest
import numpy as np


class TestClass(unittest.TestCase):
    def test_euler(self):
        with self.assertRaises(Exception) as context:
            f.euler(np.array([0, 0, 0, 0]), -3)

        self.assertTrue("h is not valid" in str(context.exception))

        self.assertTrue(
            np.array_equal(f.euler(np.array([0, 0, 0, 0]), 1), np.array([0, 0, 0, 0]))
        )

    def test_leapfrog(self):
        with self.assertRaises(Exception) as context:
            f.leapfrog(np.array([0, 0, 0, 0]), np.array([0, 0, 0, 0]), -3)

        self.assertTrue("h is not valid" in str(context.exception))

    def test_bulirsch_stoer(self):
        with self.assertRaises(Exception) as context:
            f.bulirsch_stoer(np.array([0, 0, 0, 0]), np.array([0, 0, 0, 0]), -3)

        self.assertTrue("h is not valid" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
