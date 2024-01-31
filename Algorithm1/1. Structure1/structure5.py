import sys
word = list(input())
cursor = len(word)

for i in range(int(sys.stdin.readline())):
  command = list(input().split())
  if command[0] == "P":
    word.insert(cursor, command[1])
    cursor += 1
  elif command[0] == "L":
    if cursor > 0:
      cursor -= 1
  elif command[0] == "D":
    if cursor < len(word):
      cursor += 1
  else:
    if cursor > 0:
      word.remove(word[cursor-1])
      
print(''.join(word))