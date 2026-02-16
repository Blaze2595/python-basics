# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select = [],types = [],has_headers = True,delimiter = ',',silence_errors = False):
    '''Parse a csv file into list of records'''

    with open(filename,'rt') as f:
        rows = csv.reader(f,delimiter=delimiter)
        headers = next(rows) if has_headers else []
        records = []
        index = []

        # Raise error if both has_headers = false and select is given
        if select and not has_headers:
            raise RuntimeError("Provide either Select or has_headers")

        # If Column selected then specific column index is picked out
        if select:
            for i,item in enumerate(headers):
                if item in select:
                    index.append(i)
        else:
            index = [x for x in range(len(headers))]
        
        # If types not specified, all the column values are converted to string
        types = form_types_object(headers) if not types and has_headers else types
        
        
        for i,line in enumerate(rows):
            try:
                if not line:
                    continue
                
                if has_headers:
                    record = {}
                    for x,y in enumerate(index):
                        record.update({headers[y]:types[x](line[y])})
                    
                    records.append(record)
                else:
                    record = []
                    for x,item in enumerate(line):
                        types = form_types_object(line) if not types else types
                        record.append(types[x](item))
                    
                    records.append(tuple(record))
                    
            except ValueError as ex:
                if not silence_errors:
                    print(f'Row {i+1} : Could not convert {line}')
                    print(f'Reason : {ex}')
    
    return records

def form_types_object(item):
    types = [str]
    types = types * len(item)
    return types