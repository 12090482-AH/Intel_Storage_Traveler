import os
import sys
import shutil
import time
import logging
import subprocess
import concurrent.futures
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import threading

def resource_path(relative_path):
    """This is for the standalone build purpose"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def setup_logging(log_file='test_log.log'):
    """Set up logging configuration."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def create_test_file(file_path, size_gb=50):
    """Create a test file of the specified size in GB."""
    message = f"Creating a test file of size {size_gb}GB at {file_path}..."
    print_to_terminal(message)
    logging.info(message)
    with open(file_path, 'wb') as f:
        f.seek(size_gb * 1024 * 1024 * 1024 - 1)
        f.write(b'\0')
    message = "Test file created successfully.\n"
    print_to_terminal(message)
    logging.info(message)

def begin_travel(source, destination):
    """Transfer a file from source to destination and measure the time taken."""
    try:
        start_time = time.time()
        shutil.copy2(source, destination)
        end_time = time.time()
        return end_time - start_time
    except Exception as e:
        message = f"Error during file transfer from {source} to {destination}: {e}\n"
        print_to_terminal(message)
        logging.error(message)
        return None

def train_travel(file_path, size_gb, cycles=1, queue_depth=4):
    """Test sequential R/W speed using Python with concurrent operations to simulate higher queue depth."""
    buffer_size = 1024 * 1024  # 1 MB buffer
    total_size = size_gb * 1024 * 1024 * 1024  # Convert GB to bytes

    message = "Starting sequential R/W test...\n"
    print_to_terminal(message)
    logging.info(message)

    total_suite_time = 0

    for cycle in range(cycles):
        message = f"Cycle {cycle + 1} of {cycles}"
        print_to_terminal(message)
        logging.info(message)

        start_suite_time = time.time()

        # Read Operation
        message = f"Testing sequential read speed for {size_gb}GB file..."
        print_to_terminal(message)
        logging.info(message)

        with concurrent.futures.ThreadPoolExecutor(max_workers=queue_depth) as executor:
            futures = {executor.submit(read_from_file, file_path, buffer_size, total_size // queue_depth): i for i in range(queue_depth)}
            for future in concurrent.futures.as_completed(futures):
                index = futures[future]
                read_time = future.result()
                message = f"Cycle {cycle + 1}, Concurrent read {index + 1} completed in {read_time:.2f} seconds."
                print_to_terminal(message)
                logging.info(message)

        # Write Operation
        message = f"Testing sequential write speed for {size_gb}GB file..."
        print_to_terminal(message)
        logging.info(message)

        with concurrent.futures.ThreadPoolExecutor(max_workers=queue_depth) as executor:
            futures = {executor.submit(write_to_file, file_path, buffer_size, total_size // queue_depth): i for i in range(queue_depth)}
            for future in concurrent.futures.as_completed(futures):
                index = futures[future]
                write_time = future.result()
                message = f"Cycle {cycle + 1}, Concurrent write {index + 1} completed in {write_time:.2f} seconds."
                print_to_terminal(message)
                logging.info(message)

        end_suite_time = time.time()
        cycle_time = end_suite_time - start_suite_time
        total_suite_time += cycle_time

        message = f"Cycle {cycle + 1} completed in {cycle_time:.2f} seconds.\n"
        print_to_terminal(message)
        logging.info(message)

    message = f"Total time for {cycles} sequential R/W cycles: {total_suite_time:.2f} seconds."
    print_to_terminal(message)
    logging.info(message)

def write_to_file(file_path, buffer_size, size):
    """Write data to a file and return the time taken."""
    start_time = time.time()
    with open(file_path, 'wb') as f:
        written = 0
        while written < size:
            f.write(b'\0' * buffer_size)
            written += buffer_size
    end_time = time.time()
    return end_time - start_time

def read_from_file(file_path, buffer_size, size):
    """Read data from a file and return the time taken."""
    start_time = time.time()
    with open(file_path, 'rb') as f:
        read = 0
        while read < size:
            f.read(buffer_size)
            read += buffer_size
    end_time = time.time()
    return end_time - start_time

def print_to_terminal(message):
    """Print message to the text widget terminal."""
    terminal_text.configure(state='normal')
    terminal_text.insert(ctk.END, message + '\n')
    terminal_text.configure(state='disabled')
    terminal_text.see(ctk.END)

def domestic_travel(file_path, primary_ssd_path, cycles=1):
    """Test transferring a file within the primary SSD."""
    message = "Starting internal file transfer test...\n"
    print_to_terminal(message)
    logging.info(message)
    total_suite_time = 0

    for cycle in range(cycles):
        message = f"Cycle {cycle + 1} of {cycles}"
        print_to_terminal(message)
        logging.info(message)
        start_suite_time = time.time()

        destination_path = os.path.join(primary_ssd_path, 'internal_test_copy')
        transfer_time = begin_travel(file_path, destination_path)
        
        if transfer_time is not None:
            message = f"Internal file transfer completed in {transfer_time:.2f} seconds."
            print_to_terminal(message)
            logging.info(message)
            os.remove(destination_path)
        else:
            message = "\nInternal file transfer failed."
            print_to_terminal(message)
            logging.warning(message)

        end_suite_time = time.time()
        cycle_time = end_suite_time - start_suite_time
        total_suite_time += cycle_time
        message = f"Cycle {cycle + 1} completed in {cycle_time:.2f} seconds.\n"
        print_to_terminal(message)
        logging.info(message)

    message = f"Total time for {cycles} internal file transfer cycles: {total_suite_time:.2f} seconds."
    print_to_terminal(message)
    logging.info(message)

def interstate_travel(file_path, primary_ssd_path, secondary_ssd_path, cycles=1):
    """Test transferring a file from primary to secondary SSD and back."""
    message = "Starting external file transfer test...\n"
    print_to_terminal(message)
    logging.info(message)
    total_suite_time = 0

    for cycle in range(cycles):
        message = f"Cycle {cycle + 1} of {cycles}"
        print_to_terminal(message)
        logging.info(message)
        start_suite_time = time.time()

        # Transfer from primary to secondary
        destination_path = os.path.join(secondary_ssd_path, 'external_test_copy')
        transfer_time_to_secondary = begin_travel(file_path, destination_path)
        
        if transfer_time_to_secondary is not None:
            message = f"Transfer to secondary storage completed in {transfer_time_to_secondary:.2f} seconds."
            print_to_terminal(message)
            logging.info(message)
            
            # Transfer back from secondary to primary
            return_path = os.path.join(primary_ssd_path, 'external_test_return_copy')
            transfer_time_to_primary = begin_travel(destination_path, return_path)
            
            if transfer_time_to_primary is not None:
                message = f"Transfer back to primary storage completed in {transfer_time_to_primary:.2f} seconds."
                print_to_terminal(message)
                logging.info(message)
                os.remove(return_path)
            else:
                message = "\nTransfer back to primary SSD failed."
                print_to_terminal(message)
                logging.warning(message)
            
            os.remove(destination_path)
        else:
            message = "\nTransfer to secondary storage failed."
            print_to_terminal(message)
            logging.warning(message)

        end_suite_time = time.time()
        cycle_time = end_suite_time - start_suite_time
        total_suite_time += cycle_time
        message = f"Cycle {cycle + 1} completed in {cycle_time:.2f} seconds.\n"
        print_to_terminal(message)
        logging.info(message)

    message = f"Total time for {cycles} external file transfer cycles: {total_suite_time:.2f} seconds."
    print_to_terminal(message)
    logging.info(message)

def run_tests(primary_ssd_path, secondary_ssd_path, file_size, test_type, cycles, log_file, queue_depth):
    setup_logging(log_file)
    test_file_path = os.path.join(primary_ssd_path, 'test_file')

    # Ensure primary path is valid
    if not os.path.exists(primary_ssd_path):
        message = f"Primary SSD path does not exist: {primary_ssd_path}"
        print_to_terminal(message)
        logging.error(message)
        return

    # Ensure secondary path is valid if needed
    if test_type in ['external', 'all'] and not secondary_ssd_path:
        message = "Secondary SSD path is required for external test."
        print_to_terminal(message)
        logging.error(message)
        return

    if secondary_ssd_path and not os.path.exists(secondary_ssd_path):
        message = f"Secondary SSD path does not exist: {secondary_ssd_path}"
        print_to_terminal(message)
        logging.error(message)
        return

    # Create the test file if it doesn't exist
    if not os.path.exists(test_file_path):
        create_test_file(test_file_path, file_size)

    # Run the specified tests
    if test_type in ['internal', 'all']:
        domestic_travel(test_file_path, primary_ssd_path, cycles)
    if test_type in ['external', 'all']:
        interstate_travel(test_file_path, primary_ssd_path, secondary_ssd_path, cycles)
    if test_type in ['sequential', 'all']:
        train_travel(test_file_path, file_size, cycles, queue_depth)

    # Delete the test file after all tests are done
    if os.path.exists(test_file_path):
        os.remove(test_file_path)
        message = "\n***All Tests Completed***\n"
        print_to_terminal(message)
        logging.info(message)

def select_primary_ssd():
    path = filedialog.askdirectory(title="Select Primary SSD Path")
    primary_ssd_path.set(path)

def select_secondary_ssd():
    path = filedialog.askdirectory(title="Select Secondary SSD Path")
    secondary_ssd_path.set(path)

def start_test():
    try:
        # Run tests in a separate thread to keep the GUI responsive
        threading.Thread(target=run_tests, args=(
            primary_ssd_path.get(),
            secondary_ssd_path.get(),
            int(file_size.get()),
            test_type.get(),
            int(cycles.get()),
            log_file.get(),
            int(queue_depth.get())  # Pass the queue depth
        )).start()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Intel NVMe SSD Performance Testing Tool")

primary_ssd_path = ctk.StringVar()
secondary_ssd_path = ctk.StringVar()
file_size = ctk.StringVar(value="50")
test_type = ctk.StringVar(value="all")
cycles = ctk.StringVar(value="1")
log_file = ctk.StringVar(value="test_log.log")
queue_depth = ctk.StringVar(value="32")

# Load and display the Intel logo
logo_image = Image.open(resource_path("intel_logo.png"))
logo_image = logo_image.resize((100, 50), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ctk.CTkLabel(root, image=logo_photo, text="")
logo_label.grid(row=0, column=0, pady=10, padx=0)

# Configure labels and entries
ctk.CTkLabel(root, text="Primary SSD Path:").grid(row=1, column=0, sticky=ctk.W, padx=10, pady=5)
ctk.CTkEntry(root, textvariable=primary_ssd_path, width=400).grid(row=1, column=1, padx=10, pady=5)
ctk.CTkButton(root, text="Browse", command=select_primary_ssd).grid(row=1, column=2, padx=10, pady=5)

ctk.CTkLabel(root, text="Secondary SSD Path:").grid(row=2, column=0, sticky=ctk.W, padx=10, pady=5)
ctk.CTkEntry(root, textvariable=secondary_ssd_path, width=400).grid(row=2, column=1, padx=10, pady=5)
ctk.CTkButton(root, text="Browse", command=select_secondary_ssd).grid(row=2, column=2, padx=10, pady=5)

ctk.CTkLabel(root, text="File Size (GB):").grid(row=3, column=0, sticky=ctk.W, padx=10, pady=5)
ctk.CTkEntry(root, textvariable=file_size).grid(row=3, column=1, sticky=ctk.W, padx=10, pady=5)

ctk.CTkLabel(root, text="Test Type:").grid(row=4, column=0, sticky=ctk.W, padx=10, pady=5)
ctk.CTkOptionMenu(root, variable=test_type, values=["internal", "external", "sequential", "all"]).grid(row=4, column=1, sticky=ctk.W, padx=10, pady=5)

ctk.CTkLabel(root, text="Cycles:").grid(row=5, column=0, sticky=ctk.W, padx=10, pady=5)
ctk.CTkEntry(root, textvariable=cycles).grid(row=5, column=1, sticky=ctk.W, padx=10, pady=5)

ctk.CTkLabel(root, text="Queue Depth:").grid(row=6, column=0, sticky=ctk.W, padx=10, pady=5)
ctk.CTkEntry(root, textvariable=queue_depth).grid(row=6, column=1, sticky=ctk.W, padx=10, pady=5)

ctk.CTkLabel(root, text="Log File:").grid(row=7, column=0, sticky=ctk.W, padx=10, pady=5)
ctk.CTkEntry(root, textvariable=log_file).grid(row=7, column=1, sticky=ctk.W, padx=10, pady=5)

# Terminal for test output
terminal_text = ctk.CTkTextbox(root, width=400, height=150, state='disabled')
terminal_text.place(relx=0.7, rely=0.4, anchor='n')

ctk.CTkButton(root, text="Start Test", command=start_test).grid(row=8, column=1, pady=20)

root.mainloop()
