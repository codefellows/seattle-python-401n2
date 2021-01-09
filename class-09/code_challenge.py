# Given 2 ll, return the count of duplicate values
# Algo
# def function count_common_nodes
#   current1 assigned to ll1 head
#   current2 assigned to ll2 head
#   set count to 0

# while current1 is not None
#    while current2 is not None
#       if (current1 == current2):  We want to look at values
#           count = count + 1
#       Move current2 to current2.next
#     increment current1 to current1.next
#     current2 to ll_2.head

# return count

def count_common_nodes(ll_1, ll_2):
    current1 = ll_1.head
    current2 = ll_2.head
    count = 0

    while current1:
        while current2:
            if current1.value == current2.value:
                count += 1
            current2 = current2.next
        current1 = current1.next
        current2 = ll_2.head

    return count

