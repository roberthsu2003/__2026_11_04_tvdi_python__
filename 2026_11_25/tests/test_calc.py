import unittest

from calc import divide


class TestDivide(unittest.TestCase):
    """測試 divide 函式的各項行為。"""

    def test_divide_positive_integers(self) -> None:
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_float_result(self) -> None:
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_negative_numbers(self) -> None:
        self.assertEqual(divide(-9, 3), -3.0)

    def test_divide_zero_numerator(self) -> None:
        self.assertEqual(divide(0, 5), 0.0)

    def test_divide_by_zero_raises_value_error(self) -> None:
        for divisor in (0, 0.0):
            with self.subTest(divisor=divisor):
                with self.assertRaises(ValueError) as ctx:
                    divide(10, divisor)
                self.assertEqual(str(ctx.exception), "除數不可為零")


if __name__ == "__main__":
    unittest.main()
