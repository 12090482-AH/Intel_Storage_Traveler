# Intel_Storage_Traveler

CCG 3PE storage section performance testing tool for PCL publication. 

This tool is designed to evaluate the performance of NVMe SSDs by conducting file transfer tests.
It allows users to test file transfers within a single SSD (domestic travel = internal file transfer) and between two SSDs (interstate travel = external file transfer).
The tool is intended for use in PCL publications to ensure consistent and reliable performance metrics.

## Features
Automatic Test File Creation: Generates a test file of a specified size (default 50GB) if it doesn't already exist.
Flexible Testing Options: Users can choose to run only domestic travel tests, only interstate travel tests, or both.
Detailed Timing Information: Measures and reports the time taken for each file transfer operation.
Command-Line Interface: Easily specify test parameters and options via command-line arguments.

## Requirements
Python 3.10
Sufficient disk space for creating large test files
Permissions to read from and write to the specified SSD paths
