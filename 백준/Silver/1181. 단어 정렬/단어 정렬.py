import sys
n = int(sys.stdin.readline())
words=set()
for i in range(n):
  words.add(sys.stdin.readline().rstrip())
words=list(words)
words.sort()
words.sort(key=lambda x:len(x))
print("\n".join(words))
