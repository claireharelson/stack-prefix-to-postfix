# This module is used to process command line arguments and launch the program

from pathlib import Path
import argparse

import charels1_lab1

# Create the parser
arg_parser = argparse.ArgumentParser()

# Add an argument to the parser
arg_parser.add_argument("input_file", type=str, help="Input File Pathname")
arg_parser.add_argument("output_file", type=str, help="Output File Pathname")

# Parse the argument
args = arg_parser.parse_args()

# pathlib.Path
in_path = Path(args.input_file)
out_path = Path(args.output_file)

# Raises error if the input file's path or name is incorrect
try:
    with in_path.open('r') as input_file, out_path.open('w') as output_file:
        charels1_lab1.process_files(input_file, output_file)
except FileNotFoundError:
    print(f'FILE NAME "{in_path}" NOT FOUND. CHECK INPUT FILE NAME OR PATH.')
