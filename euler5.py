
# ? 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# ? What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

result = 0

while True:
    result += 20
    for i in range(1, 20 + 1):
        if result % i != 0:
            break
    else:
        break

print(result)
