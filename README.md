# Intel_Storage_Traveler
CCG 3PE storage team's main performance testing tool for PCL publication. 

This tool is designed to evaluate the performance of storages (primarily NVMe SSDs) by conducting file transfer tests.
It allows users to test file transfers within a single storage (domestic travel = internal file transfer) and between two storages (interstate travel = external file transfer).
Moreover, although it is not the real-world file transfer senario, this tool also provides the sequential transfer test which is basically testing sequential I/O performance by writing to and reading from a file on a parimary storage using 1MB buffer.

CCG 3PE storage team has recently introduced a GUI version of this script for all users especially for external customers. However, we still encourage internal users to utilize the script version, as it allows for local automation tailored to your specific needs.

If user wants to utilize the GUI version, simply build the execution file using the provided batch file. Just make sure to have python3.1x and all required python packages as mentioned in the requirement section.

The tool is intended for use in PCL publications to ensure consistent and reliable performance metrics.

## Features
Automatic Test File Creation: Generates a test file of a specified size (default 50GB) if it doesn't already exist.

Detailed Timing Information: Measures and reports the time taken for each file transfer operation and sequential I/O operations.

Command-Line Interface: Easily specify test parameters and options via command-line arguments. This will enable end users to utilize the batch/bash shell scripting.

GUI version with a standalone capability: Built using CustomTkinter for a user-friendly experience. Standalone (pyinstaller) execution build is also ready for the users.

## Requirements
Python 3.10 or newer.

Sufficient disk space for creating large test files.

Permissions to read from and write to the specified SSD paths.

pyinstaller package -> pip install pyinstaller

CustomTkinter package -> pip install customtkinter

Pillow (PIL) package -> pip install pillow

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

## GUI version
Primary SSD Path: Directory path for the primary SSD.

Secondary SSD Path: Directory path for the secondary SSD (required for external tests).

File Size: Size of the test file in GB.

Test Type: Type of test to perform (internal, external, sequential, or all).

Cycles: Number of times to repeat the test.

Log File: Path to the log file for storing test results.

Terminal Output: Displays real-time test progress and results.

**To create the standalone version, simply run the build.bat file or execute this python command on the same directory where Intel_Storage_Traveler_GUI.py file is at. -> pyinstaller --onefile --name "Intel Storage Traveler" --add-data "intel_logo.png;." --icon "Intel_SSD_NVMe_icon.ico" Intel_Storage_Traveler_GUI.py

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! 

Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## Contact

Please let me know if you have any questions, my contact info: <alexander.han@intel.com>
