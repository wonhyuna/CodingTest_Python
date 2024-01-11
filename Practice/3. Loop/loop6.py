import sys
#문자열 저장 -> .rstrip()

T = int(sys.stdin.readline())

for i in range(0, T):
  A, B = map(int, sys.stdin.readline().split())
  print(A+B)