

#this application calculates the sum of digits of any base with power
# for example, 2^5 = 32, 3 + 2 = 5

a = float(input("Enter the base of the number:"))
b = float(input("Enter the power of the number:"))
c = a**b
summ=0

print("The {} in {} is: {}".format(a,b,c))

while(c>0):
    dig=c%10
    summ=summ+dig
    c=c//10
print("The total sum of digits is:",summ)
    