import sys
from collections import Counter
n = int(sys.stdin.readline())
num=[]
for i in range(n):
  num.append(int(sys.stdin.readline()))
num.sort()
print(round(sum(num)/n))
print(num[n//2])
num_c = Counter(num).most_common(2)
if len(num_c) > 1:
  if num_c[0][1] == num_c[1][1]:
    print(num_c[1][0])
  else:
    print(num_c[0][0])
else:
  print(num_c[0][0])
print(num[-1]-num[0])