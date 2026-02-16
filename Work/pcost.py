# pcost.py
#
# Exercise 1.27
import report
import stock

def portfolio_cost(filename):
    total_cost = 0

    portfolio = report.read_portfolio(filename)

    try:
        for i,items in enumerate(portfolio):
            share = int(items.Shares)
            cost = float(items.Price)
            total_cost += (share * cost)
    except ValueError:
        print(f'Row No : {i} Invalid Operation : ',items)
    
    return total_cost

def main(argv):
    if(len(argv) != 2):
        raise SystemExit('Usage: %s portfoliofile' % argv[0])
    filename = argv[1]
    print(f'The Total Cost is : {portfolio_cost(filename)}')


if __name__ == '__main__':
    import sys
    main(sys.argv)