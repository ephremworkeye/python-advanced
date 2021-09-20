from collections import deque

alist = deque([])
alist.append(5)
alist.append(4)
alist.appendleft(2)
alist.pop()
alist.popleft()
print(alist)