import sys
n = int(sys.stdin.readline())
stack=[]
start=1
answer = []
flag=True
for i in range(n):
  num = int(sys.stdin.readline())
  while start<=num:
    stack.append(start)
    answer.append("+")
    start+=1
  if stack[-1] == num:
    stack.pop()
    answer.append("-")
  else:
    print("NO")
    flag=False
    break
if flag:
  print('\n'.join(answer))