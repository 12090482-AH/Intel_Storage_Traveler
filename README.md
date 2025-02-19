# Intel_Storage_Traveler

CCG 3PE storage section performance testing tool for PCL publication. 

This tool is designed to evaluate the performance of NVMe SSDs by conducting file transfer tests.
It allows users to test file transfers within a single SSD (domestic travel = internal file transfer) and between two SSDs (interstate travel = external file transfer).
The tool is intended for use in PCL publications to ensure consistent and reliable performance metrics.

## Features
Automatic Test File Creation: Generates a test file of a specified size (default 50GB) if it doesn't already exist.

Detailed Timing Information: Measures and reports the time taken for each file transfer operation and sequential I/O operations.

Command-Line Interface: Easily specify test parameters and options via command-line arguments. This will enable end users to utilize the batch/bash shell scripting.

## Requirements
Python 3.10
Sufficient disk space for creating large test files.
Permissions to read from and write to the specified SSD paths.
dd command available (for sequential tests on Linux/macOS).

## Installation
git clone https://github.com/12090482-AH/Intel_Storage_Traveler.git

## Usage
Run the tool using the following command:

py Intel_Storage_Traveler.py <primary_ssd_path> [--secondary_ssd_path <secondary_ssd_path>] [--file-size <size_in_gb>] [--test <test_type>] [--cycles <number_of_cycles>] [--log-file <log_file_path>]

### Arguments
<primary_ssd_path>: Path to the primary SSD.

### Options
--secondary_ssd_path <secondary_ssd_path>: Path to the secondary SSD (required for external test).

--file-size <size_in_gb>: Specify the size of the test file in gigabytes. Default is 50GB.

--test <test_type>: Specify which test to run. Options are internal, external, sequential, or all. Default is all.

--cycles <number_of_cycles>: Number of test cycles to run. Default is 1.

--log-file <log_file_path>: Path to the log file. Default is test_log.log.

### Examples
Run both tests with a 50GB test file:

py Intel_Storage_Traveler.py </path/to/primary/ssd"> --secondary_ssd_path <"/path/to/secondary/ssd">

Run only the internal file transfer test with a 20GB test file:

py Intel_Storage_Traveler.py </path/to/primary/ssd> --secondary_ssd_path </path/to/secondary/ssd> --file-size <20> --test <internal>

Run sequential read and write tests only:

py Intel_Storage_Traveler.py </path/to/primary/ssd> --test <sequential>

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! 

Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## Contact

Please let me know if you have any questions, my contact info: <alexander.han@intel.com>
