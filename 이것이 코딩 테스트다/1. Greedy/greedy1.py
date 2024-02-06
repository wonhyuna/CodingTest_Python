n = int(input())
count = 0

coins = [500, 100, 50, 10]

while n > 0:
  for i in coins:
    count += (n // i)
    n = n % i
    
print(count)
