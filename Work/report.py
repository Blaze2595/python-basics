# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    values = []

    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i,line in enumerate(rows):
            record = dict(zip(headers,line))
            d = {}
            d['name'] = record['name']
            d['shares'] = int(record['shares'])
            d['cost'] = float(record['price'])
            values.append(d)
    
    return values

def read_prices(filename):
    values = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for line in rows:
            if(len(line) > 0):
                values[str(line[0])] = float(line[1])

    return values

def portfolio_report(portfoliofile, pricesfile):
    result = []

    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)
    result = get_profit_margin(portfolio,prices)
    print_report(result)
    return True

def get_profit_margin(portfolio,prices):
    result = []

    for item in portfolio:
        if(item['name'] in prices):
            name = item['name']
            shares = item['shares']
            price = float(prices[item['name']])
            change = price - float(item['cost'])
            t = (name,shares,price,change)

            result.append(t)
    
    return result

def print_report(report):
    headers = ('Names','Share','Price','Cost')
    line = ('__________','__________','__________','__________')

    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{line[0]:>10s} {line[1]:>10s} {line[2]:>10s} {line[3]:>10s}')
    
    for _name,_share,_price,_change in report:
        print(f'{_name:>10s} {_share:>10d} {f"${_price:.2f}":>10} {_change:>10.2f}')