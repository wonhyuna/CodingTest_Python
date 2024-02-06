import sys
T = int(sys.stdin.readline())
for i in range(T):
  ps = list(sys.stdin.readline().rstrip())
  for j in range(len(ps)):
    if ps[j] == "(":
      for k in range(j+1, len(ps)):
        if ps[k] == ")":
          ps[k] = "*"
          ps[j] = "*"
          break
  if ps.count("*") == len(ps):
    print("YES")
  else:
    print("NO")