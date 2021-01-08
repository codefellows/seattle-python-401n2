# ll1: [1] -> [3] -> [5]
#       |   /  |  /   |
# ll2: [2] -> [4] -> [6] - > [8]
#                     ^
# ll1: 1 -> 2 -> 3 -> 4 -> 5 -> 6


def merge_list(ll1, ll2):

    current_ll1 = ll1.head
    current_ll2 = ll2.head

    while current_ll1 and current_ll2:  # 5 6

        ll1_next = current_ll1.next  # None
        ll2_next = current_ll2.next  # 8

        current_ll1.next = current_ll2  # 6

        # do a check for ll1_next if none break or return
        if not ll1_next:  #
            break

        current_ll2.next = ll1_next

        # current_ll1, current_ll2 = ll1_next, ll2_next
        current_ll1 = ll1_next  #
        current_ll2 = ll2_next  #

    return ll1

   # if not ll1.head or ll2.head:
    #     return ll1 or ll2
    # validate that both lists have nodes
