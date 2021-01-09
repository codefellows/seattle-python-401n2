def count_common_nodes(head1, head2): 
    current1 = head1 
    current2 = head2 
    count = 0
  
    while current1: 
        while current2: 
  
            if (current1.value == current2.value): 
                count = count + 1
  
            current2 = current2.next
          
        current1 = current1.next
        current2 = head2 
      
    return count 