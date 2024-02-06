T = []
for i in range(3):
  x = int(input())
  T.append(x)

if (sum(T) == 180):
  if (T[0] == T[1] == T[2]):
    print("Equilateral")
  elif ((T[0] == T[1]) or (T[1] == T[2]) or (T[0] == T[2])):
    print("Isosceles")
  else:
    print("Scalene")
    
else: 
  print("Error")