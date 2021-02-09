import math
#This program sums the numbers with multiples 3 and 5

# For example, the numbers with multiples till 10 are 3 5 6 9. The sum is 32


def Multiples(a,b):
    arr=[]
    summ=0
    for i in range(a,b+1):
        if(i%3==0 or i%5 == 0):
            summ +=i
            arr.append(i)            
        else:
            continue
    print("The elements are:{}".format(arr))
    return summ
    
    
a=int(input("Enter the lower bound:"))
b=int(input("Enter the upper bound:"))
sum1 = Multiples(a,b)
print("The sum is: {}".format(sum1))