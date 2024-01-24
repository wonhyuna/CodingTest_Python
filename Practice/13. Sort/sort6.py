num = input()
arr = []

arr = list(num)
arr.sort(reverse=True)

for i in arr:
  print(i, end='')