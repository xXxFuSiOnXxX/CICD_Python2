import unittest
import main


class SimpleTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.calculator('32', '+', '32'), 64)
        self.assertEqual(main.calculator('-32', '+', '32'), 0)
        self.assertEqual(main.calculator('-32', '+', '-32'), -64)
        self.assertEqual(main.calculator('0', '+', '0'), 0)

    def test_subtract(self):
        self.assertEqual(main.calculator('64', '-', '32'), 32)
        self.assertEqual(main.calculator('-32', '-', '32'), -64)
        self.assertEqual(main.calculator('-32', '-', '-32'), 0)
        self.assertEqual(main.calculator('32', '-', '32'), 0)
        self.assertEqual(main.calculator('0', '-', '0'), 0)

    def test_multiply(self):
        self.assertEqual(main.calculator('32', '*', '32'), 1024)
        self.assertEqual(main.calculator('-32', '*', '32'), -1024)
        self.assertEqual(main.calculator('-32', '*', '-32'), 1024)
        self.assertEqual(main.calculator('32', '*', '-32'), -1024)
        self.assertEqual(main.calculator('0', '*', '0'), 0)
        self.assertEqual(main.calculator('32', '*', '0'), 0)
        self.assertEqual(main.calculator('0', '*', '32'), 0)

    def test_divide(self):
        self.assertEqual(main.calculator('32', '/', '32'), 1)
        self.assertEqual(main.calculator('-32', '/', '32'), -1)
        self.assertEqual(main.calculator('-32', '/', '-32'), 1)
        self.assertEqual(main.calculator('32', '/', '-32'), -1)
        self.assertEqual(main.calculator('0', '/', '32'), 0)
        self.assertEqual(main.calculator('5', '/', '2'), 2.5)

        with self.assertRaises(ValueError):
            main.calculator('0', '/', '0')
            main.calculator('32', '/', '0')


if __name__ == '__main__':
    unittest.main()