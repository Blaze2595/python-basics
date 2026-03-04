# pcost.py
#
# Exercise 1.27
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)    
    return portfolio.total_cost

def main(argv):
    if(len(argv) != 2):
        raise SystemExit('Usage: %s portfoliofile' % argv[0])
    filename = argv[1]
    print(f'The Total Cost is : {portfolio_cost(filename)}')


if __name__ == '__main__':
    import sys
    main(sys.argv)