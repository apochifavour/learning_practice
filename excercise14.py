"""from collections import deque

def reverse_first(queue, k):
    actual_k = min(k, len(queue))
    
    stack = []
    for _ in range(actual_k):
        stack.append(queue.popleft())
        
    while stack:
        queue.append(stack.pop())
        
    
    remaining = len(queue) - actual_k
    
    for _ in range(remaining):
        queue.append(queue.popleft())

    return queue

num = reverse_first(queue([10, 20, 30, 40, 50]), k=3)
print(num)
"""

#from collections import deque

def reverse_first(queue, k):
    if not queue or k <= 0:
        return queue
    k = min(k, len(queue))
    for _ in range(k):
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    for _ in range(len(queue) - k):
        queue.append(queue.popleft())
        
    return queue
num = reverse_first(queue([10, 20, 30, 40, 50]), k=3)
print(num)












"""
from collections import deque


def reverse_first(queue, k):
  stack = []
  for _ in range(k):
    stack.append(queue.popleft())
  while stack:
    queue.append(stack.pop())
  remaining = len(queue) - k
  for _ in range(remaining):
    queue.append(queue.popleft())

  return queue"""
