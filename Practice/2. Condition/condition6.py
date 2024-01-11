H, M = map(int, input().split())
T = int(input())

total = H * 60 + M
total = total + T

if(total > 1439):
  total = total - 1440

print(int(total/60), int(total%60))