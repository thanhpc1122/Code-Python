n = 123456
sum = 0
while n != 0:
    temp = n % 10
    sum += temp
    n //= 10

print(sum) 