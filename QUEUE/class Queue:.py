class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def front(self):
        if len(self.items) == 0:
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Queue()

for i in range(1, 11):
    queue.enqueue(i)

processed = []

while not queue.is_empty():
    item = queue.dequeue()
    processed.append(item * 2)

task_queue = Queue()
task_queue.enqueue("task1")
task_queue.enqueue("task2")
task_queue.enqueue("task3")

completed_tasks = []

while not task_queue.is_empty():
    task = task_queue.dequeue()
    completed_tasks.append(task + "_done")

numbers = [5, 3, 8, 1, 2]
sorted_queue = Queue()

for num in numbers:
    sorted_queue.enqueue(num)

sorted_list = sorted(sorted_queue.items)

print(processed)
print(completed_tasks)
print(sorted_list)