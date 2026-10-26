"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._stackList = []


    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        #append adds the value to the end of the list, aka the top, and pop interacts with the last/top item
        self._stackList.append(value)


    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # the list object itself will return true if not empty and false if it is empty, this allows a quick
        # check with an if statement that returns a string with a message instead of an error if empty
        if not self._stackList:
            return "pop(): List is empty"
        else:
            return self._stackList.pop()


    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # peek returns a string with a warning if the list is empty, and returns the top item/last item if the list is
        # not empty
        if not self._stackList:
            return "peek(): List is empty"
        else:
            return self._stackList[-1]


    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        if not self._stackList:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._queueList = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        #the append() method adds a value to the end/back of the deque, this means the first item added will remain
        # at the front
        self._queueList.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # this if will return a warning message if the deque is empty, otherwise popleft() will remove and return the
        # front item
        if not self._queueList:
            return "dequeue(): deque is empty"
        else:
            return self._queueList.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # if the deque is not empty then front returns index 0 of the deque, which is always the first item
        if not self._queueList:
            return "front(): deque is empty"
        else:
            return self._queueList[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        if not self._queueList:
            return True
        else:
            return False


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    print("Create a Stack object:")
    testStack = Stack()
    print("    testStack created from Stack() class...\n")

    print("Add at least 4 values to the stack:")
    testStack.push("list_item_1")
    testStack.push("list_item_2")
    testStack.push("list_item_3")
    testStack.push("list_item_4")
    print("    4 items added to testStack...\n")

    print("Demonstrate LIFO behavior:")
    print("    the last item in the list is:", testStack.peek())
    print("    pop() returns:", testStack.pop())
    print("    pop() returns:", testStack.pop())
    print("    pop() returns:", testStack.pop())
    print("    pop() returns:", testStack.pop())
    print("    ")

    print("Show what happens when pop() is used on an empty stack: ")
    testStack2 = Stack()
    print("    testStack2 created as an empty Stack()...")
    print("   ", testStack2.pop(), "\n")

    print("Show what happens when peek() is used on an empty stack:")
    print("   ", testStack2.peek(), "\n")

    print("verify a single-item stack becomes empty after removal:")
    testStack2.push("list2_item_1")
    print("    list2_item_1 added to testStack2...")
    print("    pop():", testStack2.pop())
    print("    is_empty() returns:", testStack2.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    print("Create a Queue object:")
    testQueue = Queue()
    print("    testQueue created from Queue() class...\n")

    print("Add at least 4 values to the queue:")
    testQueue.enqueue("queue_item_1")
    testQueue.enqueue("queue_item_2")
    testQueue.enqueue("queue_item_3")
    testQueue.enqueue("queue_item_4")
    print("    4 items added to testQueue...\n")

    print("demonstrate FIFO behavior:")
    print("    the first item in the queue is:", testQueue.front())
    print("    dequeue() returns:", testQueue.dequeue())
    print("    dequeue() returns:", testQueue.dequeue())
    print("    dequeue() returns:", testQueue.dequeue())
    print("    dequeue() returns:", testQueue.dequeue())
    print("    ")

    print("Show what happens when dequeue() is used on an empty queue:")
    testQueue2 = Queue()
    print("    testQueue2 created as an empty Queue...")
    print("   ", testQueue2.dequeue(), "\n")

    print("Show what happens when front() is used on an empty queue:")
    print("   ", testQueue2.front(), "\n")

    print("Verify a single-item queue becomes empty after removal:")
    testQueue2.enqueue("queue2_item_1")
    print("    value queue2_item_1 added to testQueue2")
    print("    dequeue() returns:", testQueue2.dequeue())
    print("    is_empty() returns:", testQueue2.is_empty())

if __name__ == "__main__":
    main()
