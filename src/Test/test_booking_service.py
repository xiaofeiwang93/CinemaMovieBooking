import os
import csv
import pytest
from Services.DbService import DbService

# Define a temporary test CSV file path
test_csv_file = 'test_database.csv'

@pytest.fixture
def cleanup_csv_file():
    # Delete the test CSV file if it exists
    if os.path.exists(test_csv_file):
        os.remove(test_csv_file)

def test_create_csv_file(cleanup_csv_file):
    # Define column names for testing
    column_names = ['ID', 'Name', 'Age']

    # Call the function with the test CSV file and column names
    DbService.create_csv_file(test_csv_file, column_names)

    # Check if the file exists
    assert os.path.exists(test_csv_file)

    # Check if the file is not empty
    assert os.path.getsize(test_csv_file) > 0

    # Read the content of the file and check the header
    with open(test_csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)

    assert header == column_names

def test_get_next_id_empty_file(cleanup_csv_file):
    # Create an empty test CSV file
    with open(test_csv_file, mode="w", newline=""):
        pass

    # Call the function with the test CSV file
    next_id = DbService.get_next_id(test_csv_file)

    # Check if the function returns 1 for an empty file
    assert next_id == 1

def test_get_next_id_non_empty_file(cleanup_csv_file):
    # Create a test CSV file with existing IDs
    with open(test_csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['id'])
        writer.writerow(['1'])
        writer.writerow(['3'])
        writer.writerow(['2'])

    # Call the function with the test CSV file
    next_id = DbService.get_next_id(test_csv_file)

    # Check if the function returns the correct next ID (4 in this case)
    assert next_id == 4


def test_read_all_records(cleanup_csv_file):
    # Create a test CSV file with sample records
    sample_records = [
        {'id': '1', 'name': 'Alice', 'age': '30'},
        {'id': '2', 'name': 'Bob', 'age': '25'},
        {'id': '3', 'name': 'Charlie', 'age': '35'},
    ]

    with open(test_csv_file, mode="w", newline="") as file:
        fieldnames = list(sample_records[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sample_records)

    # Call the function to read all records from the test CSV file
    records = DbService.read_all_records(test_csv_file)

    # Check if the function returns the expected records
    assert records == sample_records

if __name__ == "__main__":
    pytest.main([__file__])
