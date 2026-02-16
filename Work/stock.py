class Stock:
    def __init__(self, name, shares, price):
        self.Name = name
        self.Shares = shares
        self.Price = price
    
    def cost(self):
        return self.Shares * self.Price
    
    def sell(self, share):
        self.Shares -= share