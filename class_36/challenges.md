## Challenge #1 (20 Min)

Write a function to determine if a sentence is a panagram.  A panagram is a sentence or expression using every letter of the alphabet at least once.  Return 'True' or 'False"

> The quick brown fox jumps over the lazy sleeping dog.
> Five quacking Zephyrs jolt my wax bed.

An 'A' or an 'a' will count as 1.

You CANNOT use the string library

```python
  
def ispangram(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in inpus_string.lower():
            return False
  
    return True
```

## Chalenge #2 (40 Min)

Given a LL and an int, delete all nodes where the node value is >= the given int. 

(ll, 18)

[2] -> [19] -> [1] -> [12] -> [23] -> None
would return a ll of
[2]-> [1] -> [12] -> None

(ll, 2)

[2] -> [19] -> [1] -> [12] -> [23] -> None
would return a ll of
[1] -> None

(ll, 10)

[11] -> [5] -> None
would return a ll of
[5] -> None

(ll, 2)

[11] -> [5] -> None
would return a ll of
None


```python
def delete_over(ll, num):

    at_head_node = True
    current = ll.head 

    while at_head_node and ll.head:
        if not ll.head.next and ll.head.value >= num:
            ll.head = None
            return ll
        elif ll.head.value > num:
            ll.head = current.next
        else:
            at_head_node = False
    
    while current.next:
        previous = current 
        current = current.next 
        if current.value >= num:
            previous.next = current.next
    return ll       
```

## Challenge #3 (40 Min)

Write a function that takes a binary tree as an argument, as well as some integer. Check if there exists a leaf whose path weight equals the given integer. If there does, return True. Otherwise, return False.

```text
             [5]
        [4]        [7]  
     [2]       [9]     [4]
   [10][9]   [11][12] [21][23]
```       

```python
def leaf_has_weight(root, target, weight_so_far=0):

    if not root:
      return False

    my_weight = weight_so_far + root.value

    if not root.left and not root.right:
        return target == my_weight

    return (leaf_has_weight(root.left, target, my_weight) or 
            leaf_has_weight(root.right, target, my_weight))
```