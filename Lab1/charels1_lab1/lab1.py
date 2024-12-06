# This script takes input and output files in to process
from sys import stderr
from time import time_ns
from typing import TextIO

from charels1_lab1.str_converter import Convert
from charels1_lab1.runtime_metrics import RuntimeMetric


def convert_string(value: str) -> (str, RuntimeMetric):
    """
    Converts a prefix string into a postfix string
    value: prefix string to convert
    return: metrics on algorithm performance
    """
    convert = Convert(value)
    start_time = time_ns()
    postfix_string = convert.converter()
    end_time = time_ns()
    metric = RuntimeMetric(len(value), end_time - start_time)
    return postfix_string, metric


def process_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    Reads prefix string values from an input file and writes them as postfix string values to an output file
    input_file: an opened text file set to read mode
    output_file: an opened text file set to write mode
    """
    total_conversions = 0
    metrics = []
    next_line = input_file.readline()

    while next_line is not None and next_line != "":
        try:
            value = str(next_line)
        except ValueError:
            print(f'Error parsing {next_line} for string', file=stderr)
            continue
        finally:
            next_line = input_file.readline()

        output_string, runtime_metric = convert_string(value)
        output_file.write(output_string)
        output_file.write('\n')
        metrics.append(runtime_metric)
        total_conversions += 1

    output_file.write("\n")
    for metric in metrics:
        output_file.write(f"Statement of size {metric.get_size()} took {metric.get_runtime()}ns "
                          f"to convert from prefix to postfix.\n")
