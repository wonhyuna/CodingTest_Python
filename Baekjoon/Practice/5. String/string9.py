a, b = input().split()

x = int(a[len(a)::-1])
y = int(b[::-1])

if x > y:
  print(x)
else:
  print(y)