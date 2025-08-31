#to find cube using both functions
def cube(num):
    return num ** 3
num=int(input("Enter a number: "))
print(f"The cube of {num} using function is {cube(num)}")
cub=lambda num: num ** 3
print(f"The cube of {num} using lambda function is {cub(num)}")