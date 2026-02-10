# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    total_cost = []

    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in rows:
            d = {}
            d['name'] = line[0]
            d['shares'] = int(line[1])
            d['cost'] = float(line[2])
            total_cost.append(d)
    
    return total_cost

def read_prices(filename):
    values = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for line in rows:
            if(len(line) > 0):
                values[str(line[0])] = float(line[1])

    return values