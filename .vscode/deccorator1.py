
def addition(func):
    def perform(a,b):
        print ('Sum of '+ str(a) +' and ' + str(b) + ' = '  )
        returned= func(a,b)
        print('got the value from sum function()')
        return returned

    return perform


@addition
def sum(a,b):
    c = a + b
    return c


print(sum(5,7))



