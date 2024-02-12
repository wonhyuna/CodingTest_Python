n = int(input())
route = list(input().split())
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ["L", "R", "U", "D"]

for i in route:
  for j in range(len(move)):
    if i == move[j]:
      x += dx[j]
      y += dy[j]
    
    if x == 0:
      x += 1
    elif x == n+1:
      x -= 1
    elif y == 0:
      y += 1
    elif y == n+1:
      y -= 1

print(x, y)