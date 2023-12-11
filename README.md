# Factorization Script

## Overview
This Python script is designed to factorize numbers into a product of two smaller numbers. Given a file containing natural numbers, each on a new line, the script reads these numbers and finds two factors for each number, such that their product equals the original number.

## Requirements
- Python 3.x
- A text file containing natural numbers, one per line.

## Usage
To use the script, run it from the command line with the file containing the numbers as an argument:


Where `<file>` is the path to the file containing the natural numbers to factor.

## Script Functionality
- The script reads the input file line by line, processing each number.
- For each number, it attempts to find a pair of smaller numbers whose product equals the original number.
- The factorization is printed to the console in the format `n=p*q`, where `n` is the original number, and `p` and `q` are its factors.
