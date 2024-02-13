alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
num = ['1', '2', '3', '4', '5', '6', '7', '8']
steps = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]
result = 0

start = input()

index1 = alpha.index(start[0])
index2 = num.index(start[1])
for step in steps:
  x_result = index1 + step[0]
  y_result = index2 + step[1]
  
  if x_result >= 0 and x_result <= 7 and y_result >= 0 and y_result <= 7:
    result += 1

print(result)    