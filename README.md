# Aether-Cracker

A simple Python tool to crack Gmail passwords using a drag-and-drop wordlist.

## Features

- Drag and drop wordlist file for easy usage.
- Supports multiple encodings for wordlist files.
- Handles connection retries and delays to avoid rate limiting.

## Requirements

- Python 3.6 or higher
- PyQt5
- smtplib (included in Python's standard library)
- Download a worldlist. Ex: rockyou.txt

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Zviqz/Aether-Cracker.git

## Example 
```sh
python AetherGmailCracker.py

Drag and drop your wordlist file into the window. Enter the target Gmail address when prompted:

```sh
Enter the target Gmail address: target@gmail.com

The tool will start trying passwords from the wordlist and print the progress:

```sh
Trying password1...
Trying password2...
Password found: correctpassword

