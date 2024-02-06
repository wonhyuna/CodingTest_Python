white = [[0 for i in range(100)] for j in range(100)]
count = 0

N = int(input())


for i in range(N):
  x, y = list(map(int, input().split()))
  
  for x_idx in range(x, x+10):
    for y_idx in range(y, y+10):
      white[x_idx][y_idx] = 1
  
for i in white:
  count += i.count(1)

print(count)
  