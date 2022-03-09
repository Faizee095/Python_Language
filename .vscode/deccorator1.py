
def addition(call):
    def perform(a,b):
        print ('Sum of '+ str(a) +' and ' + str(b) + ' = '  )
        return call(a,b)

    return perform


@addition
def sum(a,b):
    c = a + b
    return c


print(sum(5,7))



