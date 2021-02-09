


# This application calculates the largest polyndrome number made from 
# product of 3-digits number

n=0

for x in range(999, 100, -1):
    for y in range(x, 100, -1):
        a = x * y
        if a > n:
            s = str(x * y)
            if s == s[::-1]:
                n = x * y


print("The largest palindrome number is:{}".format(n))