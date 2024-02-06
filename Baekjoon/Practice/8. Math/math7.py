A, B, V = map(int, input().split())

x = (V - B) / (-B+A)

result = 0
if (x-int(x) > 0):
  result = 1

result += int(x)

print(result)