def find_node_recursive(root,key):
     
    if root is None or root.val == key:
        return root
 
    if root.val < key:
        return find_node_recursive(root.right,key)
   
    return find_node_recursive(root.left,key)
 
