N, B = map(int, input().split())
alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = "" # 진수 변환
divide = 0 # 나머지 값
while (N >= B):
  divide = N % B
  N = N // B
  result += alpha[divide]
result += alpha[N]

result = result[::-1]
print(result)


# 10(N) -> 2진수(B)
# 10 / 2 = 5 ...0
# 5 / 2 = 2 ...1
# 2 / 2 ... 0
# 1