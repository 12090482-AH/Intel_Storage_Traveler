import os
import shutil
import time
import argparse

def create_test_file(file_path, size_gb=50):
    """Create a test file of the specified size in GB."""
    print(f"Creating a test file of size {size_gb}GB at {file_path}...")
    with open(file_path, 'wb') as f:
        f.seek(size_gb * 1024 * 1024 * 1024 - 1)
        f.write(b'\0')
    print("Test file created successfully.")

def begin_travel(source, destination):
    """Transfer a file from source to destination and measure the time taken."""
    try:
        start_time = time.time()
        shutil.copy2(source, destination)
        end_time = time.time()
        return end_time - start_time
    except Exception as e:
        print(f"Error during file transfer from {source} to {destination}: {e}")
        return None

def domestic_travel(file_path, primary_ssd_path):
    """Test transferring a file within the primary SSD."""
    print("Starting internal file transfer test...")
    start_suite_time = time.time()

    destination_path = os.path.join(primary_ssd_path, 'internal_test_copy')
    transfer_time = begin_travel(file_path, destination_path)
    
    if transfer_time is not None:
        print(f"Internal file transfer completed in {transfer_time:.2f} seconds.")
        os.remove(destination_path)  # Clean up
    else:
        print("Internal file transfer failed.")

    end_suite_time = time.time()
    total_suite_time = end_suite_time - start_suite_time
    print(f"Total time for internal file transfer test suite: {total_suite_time:.2f} seconds.\n")

def interstate_travel(file_path, primary_ssd_path, secondary_ssd_path):
    """Test transferring a file from primary to secondary SSD and back."""
    print("Starting external file transfer test...")
    start_suite_time = time.time()

    # Transfer from primary to secondary
    destination_path = os.path.join(secondary_ssd_path, 'external_test_copy')
    transfer_time_to_secondary = begin_travel(file_path, destination_path)
    
    if transfer_time_to_secondary is not None:
        print(f"Transfer to secondary SSD completed in {transfer_time_to_secondary:.2f} seconds.")
        
        # Transfer back from secondary to primary
        return_path = os.path.join(primary_ssd_path, 'external_test_return_copy')
        transfer_time_to_primary = begin_travel(destination_path, return_path)
        
        if transfer_time_to_primary is not None:
            print(f"Transfer back to primary SSD completed in {transfer_time_to_primary:.2f} seconds.")
            os.remove(return_path)  # Clean up
        else:
            print("Transfer back to primary SSD failed.")
        
        os.remove(destination_path)  # Clean up
    else:
        print("Transfer to secondary SSD failed.")

    end_suite_time = time.time()
    total_suite_time = end_suite_time - start_suite_time
    print(f"Total time for interstate travel test suite: {total_suite_time:.2f} seconds.\n")

def main():
    parser = argparse.ArgumentParser(description="NVMe SSD File Transfer Test")
    parser.add_argument('primary_ssd_path', type=str, help='Path to the primary SSD')
    parser.add_argument('secondary_ssd_path', type=str, help='Path to the secondary SSD')
    parser.add_argument('--file-size', type=int, default=50, help='Size of the test file in GB (default: 50GB)')
    args = parser.parse_args()

    test_file_path = os.path.join(args.primary_ssd_path, 'test_file')

    # Ensure paths are valid
    if not os.path.exists(args.primary_ssd_path):
        print(f"Primary SSD path does not exist: {args.primary_ssd_path}")
        return
    if not os.path.exists(args.secondary_ssd_path):
        print(f"Secondary SSD path does not exist: {args.secondary_ssd_path}")
        return

    # Create the test file if it doesn't exist
    if not os.path.exists(test_file_path):
        create_test_file(test_file_path, args.file_size)

    domestic_travel(test_file_path, args.primary_ssd_path)
    interstate_travel(test_file_path, args.primary_ssd_path, args.secondary_ssd_path)

if __name__ == "__main__":
    main()
