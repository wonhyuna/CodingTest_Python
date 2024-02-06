import sys
T = sys.stdin.readline()
for i in range(int(T)):
  A, B = map(int, sys.stdin.readline().split())
  print("Case #{}: {} + {} = {}".format(i+1, A, B, A+B))