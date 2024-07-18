def my_function(parameeter,parameter2):
    print("welcome to calling function")
    print(parameeter+parameter2)


my_function(8,8)


def my_function1(param1=5, param2=5):
    print(param1 * param2)


my_function1(4,2)

def my_return_function(par1=4, par2=9):
    return (par1 * par2 )

print(my_return_function(4,2)+ 4 )


def hello_world_printer():
    return("hello world")


print(hello_world_printer())