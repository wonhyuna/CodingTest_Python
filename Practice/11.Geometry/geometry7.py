while (1):
  a, b, c = map(int, input().split())
  
  if (a == b == c == 0):
    break
  
  if (sum((a, b, c))-max((a, b, c)) > max((a, b, c))):
    if(a==b==c):
      print("Equilateral")
    elif((a==b) or (b==c) or (c==a)):
      print("Isosceles")
    else:
      print("Scalene")
  else:
    print("Invalid")