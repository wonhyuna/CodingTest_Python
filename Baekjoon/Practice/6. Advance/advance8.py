total = 0 #학점의 총합
result = 0 #학점*과목평점의 합
rating = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

for i in range(20):
  s, p, g = input().split()
  p = float(p)
  if g != 'P':
    total += p
    result += p * grade[rating.index(g)]

print('%.6f'%(result/total))