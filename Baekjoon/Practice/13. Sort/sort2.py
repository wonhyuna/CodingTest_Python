arr = []
for i in range(5):
  arr.append(int(input()))

arr = sorted(arr)

print(int(sum(arr)/len(arr)))
print(arr[2])