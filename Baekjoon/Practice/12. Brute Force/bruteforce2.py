N = input()
count = 0

for i in range(int(N)):
  result = i
  str_i = str(i)
  result += sum((map(int, str(i))))
    
  if result == int(N):
    print(str_i)
    count += 1
    break
  
if count == 0:
  print("0")
#abc -> a+b+c+abc = N