class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head=None, values=None):
        self.head = head

    def __repr__(self):
        output = ''

        current = self.head

        while current:
            output += f'[{current.value}],'
            current = current.next
        ret

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head

        while current:

            if current.value == value:
                return True
            current = current.next

        return False

    def append(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            return
        current = self.head

        while current.next:
            current = current.next
        current.next = node

    def insert_before(self, value, new_value):
        current = self.head
        if current and current.value == value:
            self.head = Node(new_value, self.head)
            return

        while current and current.next:
            if current.next.value == value:
                node = Node(new_value, current.next)
                current.next = node
                return

        return f'{value} not in list'

    def insert_after(self, value, new_value):
        current = self.head

        while current:
            if current.value == value:
                node = Node(new_value, current.next)
                current.next = node
                return

            current = current.next

        return f'{value} not in list'

    def kth_from_end(self, k):
        leader = self.head
        follower = None
        paces_behind = 0

        while leader:
            leader = leader.next

            if follower:
                follower = follower.next
            elif paces_behind == k:
                follower = self.head
            else:
                paces_behind += 1

        if not follower:
            raise TargetError("k is out of range")

        return follower.value
