N = int(input())
cnt = 0

for i in range(N):
  error = 0
  word = input()
  for index in range(len(word)-1):
    if word[index] != word[index+1]:
      new_word = word[index+1:]
      if word[index] in new_word:
        error+=1
  if error == 0:
    cnt+=1
print(cnt)      