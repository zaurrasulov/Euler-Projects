


# The factors of 10 are [1, 2, 5]
# The maximum prime factor of 10 is 5.

# The application below helps to find the prime largest prime factor of the each number


def Largest_Prime_Factor(n):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if (n % i == 0):
            prime_factor = i
            n /= i
        else:
            i += 1

    if (prime_factor < n):
         prime_factor = n

    return prime_factor
  
while(True):
    a=int(input("Input the number:"))
    b=Largest_Prime_Factor(a)
    print("The largest prime factor of {} is: {}".format(a,b))
    if(a=='q'):
        break