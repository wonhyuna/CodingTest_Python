# 1 2 6  7  15
# 3 5  8  14 
# 4  9  13
# 10  12
# 11

n = int(input())
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    up = n
    down = line - n + 1
else:
    up = line - n + 1
    down = n

print(up,'/',down, sep="")