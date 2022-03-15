def dec1(func):
    def dec12():
        print('inside dec12')
        x=func()
      
        return x - 3
    return dec12

def dec2(func):
    def dec21():
        print('inside dec21')
        x= func()
        print(x)
        return x + 2
    return dec21


@dec1
@dec2
def test():
    return 10

print(test())