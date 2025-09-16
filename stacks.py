from collections import deque

stack = deque()
stack.append(3)
stack.append(6)
stack.append(8)
stack.append(36)
stack.append(33)

def count(list):
    count = 0
    for item in list:
        count += 1
    return count


print(stack)
print(f"count: {count(stack)}")
print(count(stack))
# print(dir(stack))