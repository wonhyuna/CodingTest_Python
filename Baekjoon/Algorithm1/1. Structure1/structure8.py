import sys
N = int(sys.stdin.readline())
arr = []

for i in range(N):
  command = sys.stdin.readline().split()
  if command[0] == "push_front":
    arr.insert(0, command[1])
    
  elif command[0] == "push_back":
    arr.append(command[1])
    
  elif command[0] == "pop_front":
    if len(arr) == 0:
      print(-1)
    else:
      print(arr[0])
      arr.pop(0)
      
  elif command[0] == "pop_back":
    if len(arr) == 0:
      print(-1)
    else:
      print(arr[-1])
      arr.pop(-1)
      
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
      print(arr[0])
      
  elif command[0] == "back":
    if len(arr) == 0:
      print(-1)
    else:
      print(arr[-1])