import unittest

# Импортируем функции из вашего модуля
from app import rgb_to_cmyk, cmyk_to_rgb, rgb_to_hsl, hsl_to_rgb

class TestColorConversion(unittest.TestCase):

    def test_rgb_to_cmyk(self):
        self.assertEqual(rgb_to_cmyk(255, 0, 0), (0, 255, 255, 0))  # Red
        self.assertEqual(rgb_to_cmyk(0, 255, 0), (255, 0, 255, 0))  # Green
        self.assertEqual(rgb_to_cmyk(0, 0, 255), (255, 255, 0, 0))  # Blue
        self.assertEqual(rgb_to_cmyk(0, 0, 0), (0, 0, 0, 255))      # Black
        self.assertEqual(rgb_to_cmyk(255, 255, 255), (0, 0, 0, 0))  # White

    def test_cmyk_to_rgb(self):
        self.assertEqual(cmyk_to_rgb(0, 255, 255, 0), (255, 0, 0))  # Red
        self.assertEqual(cmyk_to_rgb(255, 0, 255, 0), (0, 255, 0))  # Green
        self.assertEqual(cmyk_to_rgb(255, 255, 0, 0), (0, 0, 255))  # Blue
        self.assertEqual(cmyk_to_rgb(0, 0, 0, 255), (0, 0, 0))      # Black
        self.assertEqual(cmyk_to_rgb(0, 0, 0, 0), (255, 255, 255))  # White

    def test_rgb_to_hsl(self):
        self.assertEqual(rgb_to_hsl(255, 0, 0), (0, 100, 50))      # Red
        self.assertEqual(rgb_to_hsl(0, 255, 0), (120, 100, 50))    # Green
        self.assertEqual(rgb_to_hsl(0, 0, 255), (240, 100, 50))    # Blue
        self.assertEqual(rgb_to_hsl(0, 0, 0), (0, 0, 0))            # Black
        self.assertEqual(rgb_to_hsl(255, 255, 255), (0, 0, 100))    # White

    def test_hsl_to_rgb(self):
        self.assertEqual(hsl_to_rgb(0, 100, 50), (255, 0, 0))      # Red
        self.assertEqual(hsl_to_rgb(120, 100, 50), (0, 255, 0))    # Green
        self.assertEqual(hsl_to_rgb(240, 100, 50), (0, 0, 255))    # Blue
        self.assertEqual(hsl_to_rgb(0, 0, 0), (0, 0, 0))            # Black
        self.assertEqual(hsl_to_rgb(0, 0, 100), (255, 255, 255))    # White

if __name__ == '__main__':
    unittest.main()
