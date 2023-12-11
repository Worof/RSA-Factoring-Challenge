#!/usr/bin/env python3
import sys
import math

def find_prime_factors(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            other_factor = n // i
            if is_prime(i) and is_prime(other_factor):
                return i, other_factor
    return None

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def main(file_path):
    with open(file_path, 'r') as file:
        n = int(file.read().strip())
        factors = find_prime_factors(n)
        if factors:
            print(f"{n}={factors[0]}*{factors[1]}")
        else:
            print(f"No prime factors found for {n}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <file>")
    else:
        main(sys.argv[1])
