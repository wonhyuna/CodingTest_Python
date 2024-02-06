X = int(input())
N = int(input())

sum = 0
for i in range(0, N):
  A, B = map(int, input().split())
  sum += A * B

if(X == sum):
  print("Yes")
else:
  print("No")