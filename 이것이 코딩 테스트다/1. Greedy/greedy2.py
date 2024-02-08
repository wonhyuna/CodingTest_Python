n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[-1]
second = arr[-2]

result = second * (m%k) + first * (m-m%k)
print(result)