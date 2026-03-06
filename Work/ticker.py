from follow import follow
import csv
from report import read_portfolio
from follow import follow
from tableformat import create_formatter, print_table

def select_column(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func,val in zip(types,row)]

def make_dict(rows,columns):
    for row in rows:
        yield {name:value for value,name in zip(row,columns)}

def filter_stocks(rows, names):
    rows = (row for row in rows if row['name'] in names)

def ticker(portfile, logfile, format = 'table'):
    portfolio = read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_stocks(rows,portfolio)
    formatter = create_formatter(format)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_column(rows, [0,1,4])
    rows = convert_types(rows,[str, float, float])
    rows = make_dict(rows, ['name','price','change'])
    return rows

if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)

