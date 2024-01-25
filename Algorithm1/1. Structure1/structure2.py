import sys
T = int(sys.stdin.readline())

for i in range(T):
  sentence = sys.stdin.readline().split()
  for j in sentence:
    print(j[::-1], end=' ')
  print("")