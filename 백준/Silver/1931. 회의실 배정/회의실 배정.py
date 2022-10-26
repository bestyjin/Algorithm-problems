import sys
n=int(sys.stdin.readline())
ttable=[]
for i in range(n):
    ttable.append(tuple(map(int,sys.stdin.readline().split())))
ttable.sort(key= lambda x: (x[1], x[0]))

count=1
end_time = ttable[0][1]
for i in range(1,n):
  if ttable[i][0] >= end_time:
    count+=1
    end_time = ttable[i][1]
print(count)
  