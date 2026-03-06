from typedproperty import typedproperty

class Stock:
    
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    # __slots__ = ('name','_shares','price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, share):
        self.shares -= share

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'