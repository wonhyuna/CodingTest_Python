import sys
N = int(sys.stdin.readline())
arr = []

for i in range(N):
  command = sys.stdin.readline().split()
  
  if command[0] == "push":
    arr.insert(0, command[1])
    
  elif command[0] == "pop":
    if len(arr) == 0:
      print(-1)
    else:
      print(arr.pop())
      
  elif command[0] == "size":
    print(len(arr))
    
  elif command[0] == "empty":
    if len(arr) == 0:
      print(1)
    else: 
      print(0)
      
  elif command[0] == "front":
    if len(arr) == 0:
      print(-1)
    else:
      print(arr[len(arr)-1])
      
  elif command[0] == "back":
    if len(arr) == 0:
      print(-1)
    else:
      print(arr[0])