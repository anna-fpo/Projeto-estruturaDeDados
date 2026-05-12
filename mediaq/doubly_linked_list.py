class Node:
    def __init__(self, track):
        self.track = track
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.size = 0

    def add(self, track):
        new_node = Node(track)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.cursor = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1


    def current(self):
        if self.cursor:
            return self.cursor.track
        return None

    def move_next(self):
        if self.cursor and self.cursor.next:
            self.cursor = self.cursor.next

        return self.current()

    def move_prev(self):
        if self.cursor and self.cursor.prev:
            self.cursor = self.cursor.prev

        return self.current()

    def __len__(self):
        return self.size

