n=int(input("Enter a number: "))
def calc_factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial
print(calc_factorial(n))