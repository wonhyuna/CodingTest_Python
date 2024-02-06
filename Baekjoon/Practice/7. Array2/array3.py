table = [[" "]*15 for i in range(5)]

for i in range(5):
  s = list(input())
  for j in range(len(s)):
    table[i][j] = s[j]
    
for i in range(15):
  for j in range(5):
    if table[j][i] != " ":
      print(table[j][i], end='')
    else:
      continue