N = int(input())
arr = list(map(int, input().split()))
arr_sort = sorted(list(set(arr)))

dic = {}
for i in range(len(arr_sort)):
  dic[arr_sort[i]] = i
  
for i in arr:
  print(dic[i], end = ' ')