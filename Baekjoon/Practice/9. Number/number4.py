N = int(input())
n_list = list(map(int, input().split()))

result = 0
for i in range(N):
  sosu = 0
  for j in range(1, n_list[i]+1):
    if n_list[i] % j == 0:
      sosu += 1
  if sosu == 2:
    result += 1

print(result)