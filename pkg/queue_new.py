# class Queue:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if self.items:
#             return self.items.pop(0)
#         return None

#     def peek(self):
#         return self.items[0] if self.items else None

#     def size(self):
#         return len(self.items)

# class Queue:
#     def __init__(self):
#         self.items = []

#     # Adds an item to the tail of the queue (index 0 of list)
#     def push(self, item):
#         self.items.insert(0, item)

#     # Removes and returns an item from the head of the queue (last index of list)
#     def pop(self):
#         if self.items:
#             return self.items.pop()
#         return None

#     # Returns an item from the head of the queue
#     def peek(self):
#         return self.items[-1] if self.items else None

#     # Returns the number of items in the queue
#     def size(self):
#         return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"

