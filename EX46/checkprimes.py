import calc

mydata = [501, 207, 249, 67, 83, 14597, 839]
result = []
for num in mydata:
    result.append((num, calc.isprime(num)))

print result
