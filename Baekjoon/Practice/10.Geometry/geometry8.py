li = sorted(map(int, input().split()))
if (sum(li)-max(li) > max(li)):
  print(sum(li))
else:
  print(sum(li)-max(li)+sum(li)-max(li)-1)