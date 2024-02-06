T = int(input())
for i in range(T):
  money = int(input())
  quarter = money // 25
  money = money % 25
  
  dime = money // 10
  money = money % 10
  
  nickel = money // 5
  money = money % 5
  
  print(quarter, dime, nickel, money)
  
  
  #124 = 25*4 + 10*2+ 5*0 + 1*4