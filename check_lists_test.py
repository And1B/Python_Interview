from Methods import generate_data, check_differences, read_data
import unittest
import os.path

class Testing(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.filenameSpecified = 'SpecifiedList.txt'
        self.filenameMeasured = 'MeasuredList.txt'
        generate_data('SpecifiedList.txt')
        generate_data('MeasuredList.txt')
        check_differences(read_data(self.filenameMeasured), read_data(self.filenameSpecified))

    def test_measured_list(self):
        self.assertTrue(os.path.isfile(self.filenameMeasured), 'List of Measured Items not found')

    def test_specified_list(self):
        self.assertTrue(os.path.isfile(self.filenameSpecified), 'List of Specified Items not found')

    def test_list_equality(self):
        self.assertCountEqual( read_data('SpecifiedList.txt'), read_data('MeasuredList.txt'))


if __name__ == '__main__':
    unittest.main()
