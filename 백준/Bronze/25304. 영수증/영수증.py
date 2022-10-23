import sys
sum = int(sys.stdin.readline())
n = int(sys.stdin.readline())
real_sum = 0
for i in range(n):
  price,amount = map(int,sys.stdin.readline().split())
  real_sum += price*amount

if real_sum == sum:
  print("Yes")
else:
  print("No")
