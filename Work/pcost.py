# pcost.py
#
# Exercise 1.27
import report

def portfolio_cost(filename):
    total_cost = 0

    portfolio = report.read_portfolio(filename)

    try:
        for i,items in enumerate(portfolio):
            share = int(items['shares'])
            cost = float(items['price'])
            total_cost += (share * cost)
    except ValueError:
        print(f'Row No : {i} Invalid Operation : ',items)
    
    return total_cost

def main(argv):
    print(f'The Total Cost is : {portfolio_cost(argv[1])}')


if __name__ == '__main__':
    import sys

    main(sys.argv)