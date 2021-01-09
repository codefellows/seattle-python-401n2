def count_common_nodes(ll_1, ll_2): 
    current1 = ll_1.head
    current2 = ll_2.head 
    count = 0
  
    while current1: 
        while current2: 
  
            if (current1.value == current2.value): 
                count = count + 1
  
            current2 = current2.next
          
        current1 = current1.next
        current2 = ll_2.head 
      
    return count 