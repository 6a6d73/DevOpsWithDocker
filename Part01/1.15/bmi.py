#!/bin/env python3

from sys import argv

if len(argv) != 3:
    print("This program accepts two (and only two) arguments: Weight & Height")
    print("If so inclined, can include a '.' for decimal")
    exit()

try:
    weight=float(argv[1])
    height=float(argv[2])
except ValueError:
    print('Only the following 11 characters are allowed:\n. 0 1 2 3 4 5 6 7 8 9')
    exit()

bmi=round((weight/(height/100)**2),1)
if bmi < 18.5:
    print(f"Underweight: {bmi}")
elif bmi < 25:
    print(f"Optimal weight: {bmi}")
elif bmi < 30:
    print(f"Overweight: {bmi}")
else:
    print(f"Obese: {bmi}")