from Methods import generate_data, read_data, check_differences
import unittest
import os.path


class Testing(unittest.TestCase):

    def setUp(self):
        generate_data('MeasuredList.txt')
        generate_data('SpecifiedList.txt')
        #self.measured = read_data('MeasuredList.txt')
        #self.specified = read_data('SpecifiedList.txt')
        self.filenameMeasured = 'MeasuredList.txt'
        self.filenameSpecified = 'SpecifiedList.txt'

    def test_measured_list(self):
        self.assertTrue(os.path.isfile(self.filenameMeasured), 'List of Measured Items not found')

    def test_specified_list(self):
        self.assertTrue(os.path.isfile(self.filenameSpecified), 'List of Specified Items not found')

    def test_lists(self):
        self.assertCountEqual(read_data('MeasuredList.txt'), read_data('SpecifiedList.txt'))


if __name__ == '__main__':
    unittest.main()
