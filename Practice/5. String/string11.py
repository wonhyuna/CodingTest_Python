# import sys
# words = sys.stdin.readlines()

# for i in words:
#   print(i.rstrip())

while True:
  try:
    print(input())
  except EOFError:
    break