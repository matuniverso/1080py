
# ? The prime factors of 13195 are 5, 7, 13 and 29.
# ? What is the largest prime factor of the number 600851475143 ?

import math

result = 0
n = 600851475143

for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        result = i
        n /= i

print(result)
