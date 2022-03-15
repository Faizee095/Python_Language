# class Car:
#     speed = 0
#     started = False
#     def start(self):
#         self.started = True
#         print("Car started, let's ride!")
#     def increase_speed(self, delta):
#         if self.started:
#             self.speed = self.speed + delta
#             print('Vrooooom!')
#         else:
#             print("You need to start the car first")
#     def stop(self):
#         self.speed = 0
#         print('Halting')

#####################################################################################
# if __name__ == '__main__':
#     car1=Car()
#     car1.start()

# def decor1(func):
#     def inner():
#         print('inside decor1')
#         x = func()
#         return x * x
#     return inner
 
# def decor(func):
#     def inner():
#         print('inside decor')
#         x = func()
#         return 2 * x
#     return inner
 
# @decor1
# @decor
# def num():
#     return 10
 
# print(num())
##########################################################################################
def common(func):
    def inner(a,b):
        print('Performing Mathematical Operation')
        return func(a,b)

    return inner

@common
def add(a,b):
    print('Addtion')
    return a+b

@common
def sub(a,b):
    print('Subtraction')
    return a-b

@common
def mul(a,b):
    print('Multiplication')
    return a*b

@common
def modulus(a,b):
    print('Modulus')
    return a%b



print(add(5,5))
print(sub(5,5))
print(mul(5,5))
print(modulus(5,5))