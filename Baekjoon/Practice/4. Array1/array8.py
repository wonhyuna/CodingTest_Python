n_list = []
for i in range(10):
  n = int(input())
  if n % 42 not in n_list:
    n_list.append(n%42)
    
print(len(n_list))
  