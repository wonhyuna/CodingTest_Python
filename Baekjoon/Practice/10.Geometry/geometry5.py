N = int(input())

X = []
Y = []
for i in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)

w = max(X) - min(X)
h = max(Y) - min(Y)
print(w*h)