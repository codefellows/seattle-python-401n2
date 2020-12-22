class Node:

  def __init__(self, value, next= None):
    self.value = value
    self.next = next


class LinkedList:

  def __init__(self, head= None):
    self.head = head

  def __str__(self):
    # { a } -> { b } -> { c } -> NULL"

    output = ''
    current = self.head

    while current is not None:
      output += f'{{ {current.value} }} -> '
      current = current.next
    return output + 'None'

  def insert(self, value):
    node = Node(value)

    if self.head is not None:
      node.next = self.head
    
    self.head = node

  def includes(self, value):
    current = self.head
    
    while current is not None:
      if current.value == value:
        return True
      current = current.next
    
    return False

if __name__ == "__main__":
    new_node = Node(1)
    new_linked = LinkedList()
    # print(new_linked)

    new_linked1 = LinkedList(new_node)
    new_linked1.insert(2)
    # print(new_linked1.includes(2))
    # print(new_linked1.includes(4))
    print(new_linked1)



    