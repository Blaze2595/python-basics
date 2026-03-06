def typedproperty(name, expectedType):
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)
    
    @prop.setter
    def prop(self, value):
        if not isinstance(value, expectedType):
            raise TypeError(f'Expected {expectedType}')
        setattr(self, private_name, value)
    
    return prop