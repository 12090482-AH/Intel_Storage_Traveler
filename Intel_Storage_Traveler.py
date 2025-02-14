import os
import shutil
import time
import argparse

def begin_travel(source, destination):
    """Transfer a file from source to destination and measure the time taken."""
    start_time = time.time()
    shutil.copy2(source, destination)
    end_time = time.time()
    return end_time - start_time

def domestic_travel(file_path, primary_ssd_path):
    """Test transferring a file within the primary SSD."""
    print("Starting domestic travel test...")
    start_suite_time = time.time()

    destination_path = os.path.join(primary_ssd_path, 'internal_test_copy')
    transfer_time = begin_travel(file_path, destination_path)
    print(f"Domestic travel completed in {transfer_time:.2f} seconds.")

    os.remove(destination_path)  # Clean up

    end_suite_time = time.time()
    total_suite_time = end_suite_time - start_suite_time
    print(f"Total time for domestic travel test suite: {total_suite_time:.2f} seconds.\n")

def interstate_travel(file_path, primary_ssd_path, secondary_ssd_path):
    """Test transferring a file from primary to secondary SSD and back."""
    print("Starting interstate travel test...")
    start_suite_time = time.time()

    # Transfer from primary to secondary
    destination_path = os.path.join(secondary_ssd_path, 'external_test_copy')
    transfer_time_to_secondary = begin_travel(file_path, destination_path)
    print(f"Transfer to secondary SSD completed in {transfer_time_to_secondary:.2f} seconds.")

    # Transfer back from secondary to primary
    return_path = os.path.join(primary_ssd_path, 'external_test_return_copy')
    transfer_time_to_primary = begin_travel(destination_path, return_path)
    print(f"Transfer back to primary SSD completed in {transfer_time_to_primary:.2f} seconds.")

    os.remove(destination_path)  # Clean up
    os.remove(return_path)  # Clean up

    end_suite_time = time.time()
    total_suite_time = end_suite_time - start_suite_time
    print(f"Total time for interstate travel test suite: {total_suite_time:.2f} seconds.\n")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="NVMe SSD File Transfer Test")
    parser.add_argument('test_file_path', type=str, help='Path to the test file')
    parser.add_argument('primary_ssd_path', type=str, help='Path to the primary SSD')
    parser.add_argument('secondary_ssd_path', type=str, help='Path to the secondary SSD')

    # Parse arguments
    args = parser.parse_args()

    # Run tests
    domestic_travel(args.test_file_path, args.primary_ssd_path)
    interstate_travel(args.test_file_path, args.primary_ssd_path, args.secondary_ssd_path)

if __name__ == "__main__":
    main()
