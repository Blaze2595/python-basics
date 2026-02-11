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
        for i,s in enumerate(rows):
            record = dict(zip(header,s))
            share = int(record['shares'])
            cost = float(record['price'])
            total_cost += (share * cost)
    except ValueError:
        print(f'Row No : {i} Invalid Operation : ',s)
    
    return total_cost