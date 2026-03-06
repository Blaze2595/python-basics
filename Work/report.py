# report.py
#
# Exercise 2.4
from fileparse import parse_csv
import stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename,**opts):
    with open(filename) as lines:
        portfile = parse_csv(lines=lines,select=['name','shares','price'],
                             types=[str,int,float],has_headers=True,**opts)
    
    portfolio =  [stock.Stock(**d) for d in portfile]
    return Portfolio(portfolio)


def read_prices(filename):
    with open(filename) as lines:
        return parse_csv(lines=lines,types=[str,float],has_headers=False)


def portfolio_report(portfoliofile, pricesfile, format = 'table'):
    result = []

    formatter = tableformat.create_formatter(format)
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)
    result = get_profit_margin(portfolio,prices)

    print_report(result, formatter)


def get_profit_margin(portfolio,prices):
    result = []
    prices = dict(prices)

    for item in portfolio:
        if(item.name in prices):
            name = item.name
            shares = int(item.shares)
            price = float(prices[item.name])
            change = price - float(item.price)
            t = (name,shares,price,change)

            result.append(t)
    
    return result


def print_report(report, formatter):
    headers = ('Names','Share','Price','Change')
    line = ('__________','__________','__________','__________')

    # print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    # print(f'{line[0]:>10s} {line[1]:>10s} {line[2]:>10s} {line[3]:>10s}')
    
    # for _name,_share,_price,_change in report:
        # print(f'{_name:>10s} {_share:>10d} {f"${_price:.2f}":>10} {_change:>10.2f}')
    formatter.headings(['Name','Share','Price','Change'])
    for name, share, price, change in report:
        rowdata = [name, str(share), f'{price:0.2f}',f'{change:0.2f}']
        formatter.row(rowdata)


def main(argv):
    portfolio_report(argv[1],argv[2],argv[3])


if __name__ == '__main__':
    import sys

    main(sys.argv)