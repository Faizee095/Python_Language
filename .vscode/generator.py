#Fibonacci Series

def Fibonacci(n):
    a=0
    b=1

    while a<n:
        yield a
        a,b=b,a+b

print('Enter the limit upto which you want the series')
z=int(input())
f=Fibonacci(z)
print(f)

for i in f:
    print (i)
    
