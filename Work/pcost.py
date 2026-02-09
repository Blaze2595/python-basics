# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    content = []
    total_cost = 0

    try:
        f = open(filename)
        rows = csv.reader(f)
        header = next(rows)
    except FileNotFoundError:
        print('File not found. Try again')


    try:
        for s in rows:
            share = int(s[1])
            cost = float(s[2])
            total_cost = total_cost + (share * cost)
    except ValueError:
        print('Invalid Operation : ',s)
    
    return total_cost