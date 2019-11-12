import unittest
import SimpleCalculator as cal
class TestCalculator(unittest.TestCase):
    def test_int_add(self):
        self.assertEqual(cal.add(1,43),44)
        
    def test_int_add_2(self):
        self.assertEqual(cal.add(-9,9),0)
    
    def test_float_add(self):
        self.assertEqual(cal.add(99.9,12),111.9)
        
    def test_int_minus(self):
        self.assertEqual(cal.minus(1,43),-42)
        
    def test_int_minus_2(self):
        self.assertEqual(cal.minus(-9,9),-18)

    def test_float_minus(self):
        self.assertEqual(cal.minus(99.9,12), 87.9)

if __name__ == '__main__':
    unittest.main()