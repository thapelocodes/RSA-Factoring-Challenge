#!/usr/bin/python
import sys

def fact(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    infile = sys.argv[1]

    try:
        with open(infile, 'r') as f:
            numbers = f.read().splitlines()
        
        for num in numbers:
            num = int(num)
            factor1, factor2 = fact(num)
            print(f"{num}={factor1}*{factor2}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == "__main__":
    main()
