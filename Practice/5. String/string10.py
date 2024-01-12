word = input()
tel = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0
for i in word:
  for j in tel:
    if i in j:
      result += (tel.index(j) + 3)

print(result)