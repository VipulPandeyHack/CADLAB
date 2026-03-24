class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()

for i in range(1, 11):
    stack.push(i)

reversed_items = []

while not stack.is_empty():
    reversed_items.append(stack.pop())

expression = "((a+b)*(c+d))"
balance_stack = Stack()
balanced = True

for ch in expression:
    if ch == "(":
        balance_stack.push(ch)
    elif ch == ")":
        if balance_stack.is_empty():
            balanced = False
            break
        balance_stack.pop()

if not balance_stack.is_empty():
    balanced = False

numbers = [5, 2, 9, 1, 7]
sort_stack = Stack()

for num in numbers:
    while not sort_stack.is_empty() and sort_stack.peek() > num:
        stack.push(sort_stack.pop())
    sort_stack.push(num)
    while not stack.is_empty():
        sort_stack.push(stack.pop())

sorted_result = []

while not sort_stack.is_empty():
    sorted_result.append(sort_stack.pop())

print(reversed_items)
print(balanced)
print(sorted_result)