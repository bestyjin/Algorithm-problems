import sys
x = int(sys.stdin.readline())
answer=0
while x!=0:
  if x%2==1:
    answer+=1
  x//=2
print(answer)
  