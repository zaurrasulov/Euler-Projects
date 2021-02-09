
# Fibonnaci series is a very important term in Maths. 

# The logic of writing the next element is:
# N = N-1 + N-2

# After finding the elements, the sum of all elements is found
# The sum of only even numbers is found
# The sum of only odd numbers is found

a = int (input("Enter the upper bound:"))
b = 1
c = 1


def fibon(a, b, c):
    arr=[b,c]
    summ=0
    sum1=0
    sum2=0
    for i in range(a):
        b,c=c, c+b
        arr.append(c)
        summ+=c
    for j in arr:
        if(j%2==0):
            sum1=sum1+j
        if(j%2==1):
            sum2=sum2+j
    print("The Fibonacci series is:\n{}".format(arr))
    print("The sum of elements is: {}".format(summ))
    print("The sum of even elements is:{}".format(sum1))
    print("The sum of odd elements is:{}".format(sum2))
        
fibon(a, b, c)