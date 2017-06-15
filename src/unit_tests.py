import unittest
import sol1

class TestAggregations(unittest.TestCase):
    """Tests data taken from the pivoted water_points dataset"""
    def abanyeri_water_points(self):
        """Verify the number of waterpoints"""
        data = calculate('https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json')
        
        abanyeri = data['communities']['Abanyeri']
        assertEqual(abanyeri['total'], 4)
        assertEqual(abanyeri['functional'], 4)
        assertEqual(abanyeri['non_functional'], 0)

if __name__ == '__main__':
    unittest.main()
