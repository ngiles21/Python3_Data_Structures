class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self._level = 0
      self.left_child = None
      self.right_child = None
      self.parent = None
    
        
      
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None
    self._height = 0
    

    
    
  def _insert(self, node, cur_node):
    if node.value < cur_node.value:  #left side
        if cur_node.left_child == None:
            cur_node.left_child = node
            cur_node.left_child.parent = cur_node # set parent
            node._level =  node._level + 1
        else:
            node._level =  node._level + 1
            self._insert(node, cur_node.left_child)
    elif node.value > cur_node.value:  #right side
        if cur_node.right_child == None:
            node._level =  node._level + 1
            cur_node.right_child = node
            cur_node.right_child.parent = cur_node # set parent
        else:
            node._level =  node._level + 1
            self._insert(node, cur_node.right_child)
    else:  #if neither greater than or less than it has to be already in table
        raise ValueError
    if self._height < node._level:
        self._height = node._level

  
    
    # TODO complete initialization

  def insert_element(self, value):
    
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    
    new_data = Binary_Search_Tree.__BST_Node(value)   #creating new node
    head_root = self.__root   #copy varible
    level = new_data._level
    if head_root == None: #base case
      head_root = new_data
      head_root._level = 1
    else:
        self.__insert(head_root, new_data)  #recursive case
       
    
   
  def _search(self, value, node):
    if value == node.value:
      return node
    elif value < node.value and node.left_child != None:
      return self._search(value,node.left_child)
    elif value>cur_node.value and node.right_child!=None:
      return self._search(value,node.right_child)
    
    else:  #if neither greater than or less than it has to be already in table
       raise ValueError
       
  def _min_value_node(cur):
    current = cur
    while current.left_child!=None:
        current=current.left_child
        return current
       # returns the number of children 
  def _num_children(parent):
    num_children=0
    if parent.left_child!=None: 
        num_children+=1
    if parent.right_child!=None: 
        num_children+=1
    return num_children
    
   
  def __remove(self, value):
    remove_node = self._search(value, self.__root)  #finds node to remove
    node_parent = remove_node.parent
    node_children = _num_children(remove_node)
#node has no children
    if node_children==0:
        if node_parent!=None:

            if node_parent.left_child == remove_node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None
        else:
            self.__root = None
#node has a single child
    if node_children == 1:
        if remove_node.left_child != None:
            child = remove_node.left_child
        else:
            child = remove_node.right_child
        if node_parent != None:
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child
        else:
            self.root = child
        child.parent = node_parent
# node has two children
    if node_children == 2:
        new_root = min_value_node(node.right_child)
        node.value = new_root.value
        self.__remove(new_root.value)
        
  def remove_element(self, value):
    return self.__remove(value)
     # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.  
  def _In_order(root, inorder):
    if root != None:
      if root._left != None:
        left = _In_order(root._left, inorder)
        return left
      else:
        inorder = inorder + ", " + ' ' +str(root.value) 
      if root._right != None:
        right = _In_order(root._right, inorder)
        return right
           
                
    return "[" + inorder + ' ' + ']'
    
  def in_order(self):
    root = self.__root
    inorder = ' '
    if self.__root == None:
      order = '[' + ' ' + ']'
      return order
    else:
      return self._In_order(root, inorder)
        
    
   

    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
     # TODO replace pass with your implementation
  def _pre_order(root, preorder):
    if root != None:
      preorder = preorder + ", " + ' ' +str(root.value) 
    if root._left != None:
      left = _pre_order(root._left, inorder)
      return left
    if root._right != None:
      right = _pre_order(root._right, inorder)
      return right
           
                
    return "[" + inorder + ' ' + ']'
  def pre_order(self):
    root = self.__root
    preorder = ' '
    if self.__root == None:
      order = '[' + ' ' + ']'
      return order
    else:
      inorder = inorder + str(self.__root.value)
      return self._In_order(root, inorder)
        
    
    
    
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.

  def _post_order(root, postorder):
  
    if root._left != None:
      left = _post_order(root._left, inorder)
      return left
    if root._right != None:
      right = _post_order(root._right, inorder)
      return right
    if root != None:
      postorder = postorder + ", " + ' ' +str(root.value) 
           
                
    return "[" + inorder + ' ' + ']'

  def post_order(self):
     root = self.__root
    postorder = ' '
    if self.__root == None:
      order = '[' + ' ' + ']'
      return order
    else:
      postorder = postorder + str(self.__root.value)
      return self._post_order(root, postorder)
        
  
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    pass # TODO replace pass with your implementation

  def get_height(self):
    return self._height

  def __str__(self):
    return str(self.in_order())

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.

