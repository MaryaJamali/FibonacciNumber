# Fibonacci:A string of numbers that are created by calculating the sum of the previous two numbers.Except(1,0)
# Formula: n={0,1,1,2,3,4,5,....}   F1=F2=1   n>2    Fn=F(n-1)+F(n-2)

# print number Fibonacci
def fibonacci(n):
    # DANGER..... this code(line 7, 8) shows all the information of the code in execution
    # import pdb
    # pdb.set_trace()
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


def main():
    n = int(input("Enter length of fibonacci sequence: "))
    print("Result is: ")
    for i in range(1, n+1):
        print(fibonacci(i), end=",")


main()
