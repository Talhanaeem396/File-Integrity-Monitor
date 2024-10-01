# File Integrity Monitor (FIM)

## Overview

The **File Integrity Monitor (FIM)** is a basic cybersecurity tool that monitors files for unauthorized changes by calculating and comparing their SHA-256 checksums. It helps in detecting file tampering or corruption, which is crucial for maintaining the security and integrity of important system or configuration files.

## Features

- **Checksum Calculation**: Uses SHA-256 to compute the checksum of monitored files.
- **Real-time Monitoring**: Continuously monitors specified files for any changes at a given interval.
- **Logging**: Logs any detected file changes into `file_integrity.log`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Talhanaeem396/File-Integrity-Monitor.git

2. Navigate to the project directory:
   ```bash
   cd file-integrity-monitor

3. Update the files_to_monitor list in file_integrity_monitor.py with the paths of the files you want to monitor.

## Usage
To start monitoring files, simply run the script:
   ```bash
   python file_integrity_monitor.py
