while(1):
  n = int(input())
  n_list = []
  if n == -1:
    break
  for i in range(1, n):
      if (n % i == 0):
        n_list.append(i)
        
  if sum(n_list) == n:
    print(f"{n} =", end = "")
    for i in range(len(n_list)-1):
      print(f" {n_list[i]} +", end="")
    print(f" {n_list[-1]}")
    # print(n, " = ", " + ".join(str(i) for i in n_list), sep="")
  else:
    print(f"{n} is NOT perfect.")