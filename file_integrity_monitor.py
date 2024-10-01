import hashlib
import os
import time
import logging

# Setup logging to record file changes
logging.basicConfig(filename='file_integrity.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def calculate_checksum(file_path):
    """Calculate the SHA-256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read file in chunks to avoid using too much memory
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None

def monitor_files(file_paths, interval=10):
    """Monitor a list of files for changes."""
    previous_checksums = {}

    # Initialize previous_checksums dictionary
    for file_path in file_paths:
        checksum = calculate_checksum(file_path)
        if checksum:
            previous_checksums[file_path] = checksum

    while True:
        for file_path in file_paths:
            current_checksum = calculate_checksum(file_path)
            if not current_checksum:
                continue  # Skip if file not found

            if previous_checksums[file_path] != current_checksum:
                logging.warning(f"File modified: {file_path}")
                print(f"Warning: File modified: {file_path}")
                previous_checksums[file_path] = current_checksum

        time.sleep(interval)

if __name__ == "__main__":
    # Files to monitor (add full file paths here)
    files_to_monitor = [
        "/path/to/your/important/file1.txt",
        "/path/to/your/important/file2.txt"
    ]

    # Set monitoring interval (in seconds)
    monitor_interval = 10

    monitor_files(files_to_monitor, monitor_interval)
