N, B = input().split()
N = ''.join(reversed(N))
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#1010 -> 2**0 * 0 + 2**1 * 1 + 2**2 * 0 + 2**3 * 1
result = 0
for i in range(len(N)):
  ind = number.index(N[i])
  result += (int(B)**i)*ind
print(result)

# for i, n in enumerate(배열):
# i는 인덱스, n은 값