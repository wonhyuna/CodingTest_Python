n, m = map(int, input().split())
x, y, direction = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
arr = []

for i in range(n):
  arr.append(list(map(int, input().split())))
  
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_count = 0
arr[x][y] = 1

while True:
  # 1, 2 진행
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if arr[nx][ny] == 1:
    turn_count += 1
  else:
    x = nx
    y = ny
    count += 1
    arr[x][y] = 1
    turn_count = 0
  
  # 3 진행
  if turn_count == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    turn_count = 0
    
    if arr[nx][ny] == 1:
      break
    else:
      x = nx
      y = ny
  
print(count)
