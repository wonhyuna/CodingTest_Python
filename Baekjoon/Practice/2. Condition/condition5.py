H, M = map(int, input().split())

total = H * 60 + M
alarm = total - 45

if (alarm < 0):
  alarm = 1440 + alarm
  
print(int(alarm/60), int(alarm%60))