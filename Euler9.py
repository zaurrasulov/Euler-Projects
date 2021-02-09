
#This application prints the Pythagorean triplet in which a+b+c=1000

import math
def Pythagorean_triplet(n):
  for b in range(n):
    for a in range(1, b):
        c = math.sqrt( a * a + b * b)
        if (c % 1 == 0 and a+b+c==1000):
            print(a, b, int(c))
            
Pythagorean_triplet(1000)