N = int(input())
arr = []

for i in range(N):
  x = int(input())
  arr.append(x)
  
arr = sorted(arr)

for i in range(N):
  print(arr[i])