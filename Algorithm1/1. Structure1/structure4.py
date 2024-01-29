import sys

n = int(sys.stdin.readline())
count = 1
stack = []
op = []
temp = True

for i in range(n):
  num = int(sys.stdin.readline())
  while count <= num:
    stack.append(count)
    op.append("+")
    count += 1
    
  if stack[-1] == num:
    stack.pop()
    op.append("-")
      
  else:
    temp = False
    break

if temp == False:
  print("NO")

else:
  for i in op:
    print(i)
    
  

