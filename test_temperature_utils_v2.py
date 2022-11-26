import unittest
import temperature_utils_v2


class TemperatureUtilsTestV2(unittest.TestCase):

    def test_convert_to_celsius(self):
        test_cases = [
            (32, 0),
            (68, 20),
            (100, 37.78),
            (104, 40)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_celsius(temp_in))

    def test_convert_to_fahrenheit(self):
        test_cases = [
            (-17.7778, 0),
            (0, 32),
            (100, 212)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_fahrenheit(temp_in))

    def test_convert_c_to_kelvin(self):
        test_cases = [
            (-17.7778, 255.3722),
            (0, 273.15),
            (100, 373.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_c_to_kelvin(temp_in))

    def test_convert_f_to_kelvin(self):
        test_cases = [
            (32, 273.15),
            (68, 293.15),
            (100, 310.928),
            (104, 313.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_f_to_kelvin(temp_in))

    def test_temperature_tuple(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 0.0), (68, 20.0), (100, 37.78), (104, 40.0))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "f")
        self.assertEqual(expected, actual)

    def test_temperature_tuple2(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 273.15), (68, 293.15), (100, 310.928), (104, 313.1))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "fk")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 0.0), (0, 32.0), (100, 212.0))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "c")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple2(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 255.3722), (0, 273.15), (100, 373.15))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "ck")
        self.assertEqual(expected, actual)

    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils_v2.temperature_tuple(temps_input, "a"))
