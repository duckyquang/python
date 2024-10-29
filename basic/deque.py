import collections
from collections import deque

qList = collections.deque([1, 2, 3])
print(f"This is the base list: {qList}")

qList.append(4)
print(f"This is the list after 4 is appended to the right: {qList}")

qList.appendleft(0)
print(f"This is the list after 0 is appended to the left: {qList}")

qList.pop()
print(f"This is the list after the last-to-right element is popped: {qList}")

qList.popleft()
print(f"This is the list after the last-to-left element is popped: {qList}")

advancedList = collections.deque([1, 2, 3, 3, 4, 2, 4])

index = advancedList.index(2, 1, 3)
print(f"This is the index of 3: {index}")
