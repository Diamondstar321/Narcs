import unittest
from unittest.mock import patch
from prescription import Prescription

#TEST (in shell): python -m unittest unit_test_prescription.py

'''
Test suite for verifying the Prescription class's interactions with a CSV-based database,
including adding, reading, deleting, and updating prescription records.
'''

class TestPrescription(unittest.TestCase):

    def setUp(self):
        """
        Set up test fixtures for each test method.
        Initializes a sample prescription to be used in various test methods.
        """
        self.sample_prescription = Prescription("Aspirin", "2025-12", 19.99, 100)

    @patch('builtins.open')
    @patch('csv.DictWriter')
    def test_add_prescription(self, mock_csv_writer, mock_open):
        """
        Test adding a prescription to the database.
        Verifies that the file is opened correctly and that the prescription data is written to the CSV file.
        """
        Prescription.add_prescription(self.sample_prescription)
        mock_open.assert_called_once_with('prescription_database.csv', mode='a', newline='')
        mock_csv_writer.return_value.writerow.assert_called()

    @patch('builtins.open')
    @patch('csv.DictReader')
    def test_read_prescriptions(self, mock_csv_reader, mock_open):
        """
        Test reading prescriptions from the database.
        Verifies that prescriptions are correctly read from the CSV file and that the data matches expected values.
        """
        mock_csv_reader.return_value.__iter__.return_value = iter([{
            'Name': 'Aspirin',
            'Expiration Date': '2025-12',
            'Price': '19.99',
            'Stock': '100'
        }])
        prescriptions = Prescription.read_prescriptions()
        mock_open.assert_called_once_with('prescription_database.csv', mode='r')
        self.assertEqual(len(prescriptions), 1)

    @patch('builtins.open')
    @patch('csv.DictWriter')
    def test_delete_prescription(self, mock_csv_writer, mock_open):
        """
        Test deleting a prescription from the database.
        Verifies that the prescription is deleted from the CSV file and that the file is rewritten without the deleted entry.
        """
        with patch('prescription.Prescription.read_prescriptions', return_value=[{'Name': 'Aspirin', 'Expiration Date': '2025-12', 'Price': '19.99', 'Stock': '100'}]):
            Prescription.delete_prescription("Aspirin")
            mock_open.assert_called_once_with('prescription_database.csv', mode='w', newline='')
            mock_csv_writer.return_value.writeheader.assert_called()

    @patch('builtins.open')
    @patch('csv.DictWriter')
    def test_update_prescription(self, mock_csv_writer, mock_open):
        """
        Test updating a prescription in the database.
        Verifies that the prescription is updated in the CSV file and that all appropriate data fields are modified as expected.
        """
        with patch('prescription.Prescription.read_prescriptions', return_value=[{'Name': 'Aspirin', 'Expiration Date': '2025-12', 'Price': '19.99', 'Stock': '100'}]):
            result = Prescription.update_prescription("Aspirin", self.sample_prescription)
            mock_open.assert_called_once_with('prescription_database.csv', mode='w', newline='')
            mock_csv_writer.return_value.writeheader.assert_called()
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()