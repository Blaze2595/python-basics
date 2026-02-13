# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select = [],types = []):
    '''Parse a csv file into list of records'''

    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        for line in rows:
            if not line:
                continue
            if(select and not types):
                records.append({name:value for name,value in zip(headers,line) if name in select})
            elif(select and types):
                records.append({name:func(value) for name,value,func in zip(headers,line,types) if name in select})
            elif(types and not select):
                records.append({name:func(value) for name,value,func in zip(headers,line,types)})
            else:
                records.append({name:value for name,value in zip(headers,line)})
    
    return records