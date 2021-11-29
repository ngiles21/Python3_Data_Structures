class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      self.val = val
      self.next = None
      self.previous = None
      
      
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation


  def __init__(self):
    self._header = Linked_List.__Node('header')
    self._header.next =  Linked_List.__Node('trailer')
    self._trailer = self._header.next
    self._trailer.previous = self._header
    self._header.previous = None
    self._trailer.next = None
    self.__size = 0
    
    
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation


  def __len__(self):
    return self.__size
    # return the number of value-containing nodes in 
    # this list.
    # TODO replace pass with your implementation
   

  def append_element(self, val):
    newest_1 = Linked_List.__Node(val)
    current_1 = self._trailer.previous
    newest_1.previous = current_1
    newest_1.next = self._trailer
    self._trailer.previous = newest_1
    current_1.next = newest_1
    self.__size += 1


    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
 

  def insert_element_at(self, val, index):
    if index > 0 and self.__size < index:
        raise IndexError('Out of bounds')
        
    elif (self.__size) < index or index < 0:
        raise IndexError('Out of bounds')
    if index == (self.__size):
        raise IndexError('Can not insert at end use append_element')
    current_i = self._trailer.previous
    i = 0
    newest = Linked_List.__Node(val)
    if  index > self.__size / 2:
        
        while i < (self.__size) - index:
            current_i = current_i.previous
            i += 1
    
   
    else:
        
        current_i = self._header
        while i < index:
          current_i = current_i.next
          i = i + 1


    newest.next = current_i.next
    current_i.next.previous = newest
    newest.previous = current_i
    current_i.next = newest
    self.__size += 1
    
     

    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    # TODO replace pass with your implementation
   

  def remove_element_at(self, index):
    if self.__size == 0:
        raise ValueError('List is empty')
    elif (self.__size-1) < index or index < 0:
        raise IndexError('Out of bounds')
    i = 0
    if  index > self.__size / 2:
        current = self._trailer.previous
        while i < (self.__size-1) - index:
                current = current.previous
                i += 1
    else:
    
        

        current = self._header.next
        i = 0
        while i < index:
          current = current.next
          i = i + 1
    removed = current.val

    current.previous.next = current.next
    current.next.previous = current.previous
    self.__size -= 1
    return removed


    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
   

  def get_element_at(self, index):
    if self.__size == 0:
        raise ValueError('List is empty')
    if (self.__size-1) < index or index < 0:
        raise IndexError('Out of bounds')
    i = 0
    if  index > self.__size / 2:
        current_2 = self._trailer.previous
        while i < (self.__size-1) - index:
                current_2 = current_2.previous
                i += 1
                
    else:
        
        current_2 = self._header.next
        while i < index:
          current_2 = current_2.next
          i = i + 1
    return current_2.val
    
  def rotate_left(self):
    if self.__size == 0:
        return
    elif self.__size == 1:
        return 
    new_head = self._header.next.next
  
    rotate_ele = self._header.next
    current_r = self._trailer.previous
    rotate_ele.previous = current_r
    rotate_ele.next = self._trailer
    self._trailer.previous = rotate_ele
    current_r.next = rotate_ele
    self._header.next = new_head
    new_head.previous = self._header

    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
   
    
  def __str__(self):
    cur = self._header.next
    str_values = ' ' + str(cur.val) 
    q = 0
    cur = cur.next
    if self.__size == 0:
      return '['+ ' ' + "]"
    while q < self.__size-1:
     
      str_values = str_values + ', ' + ' ' + str(cur.val)
      cur = cur.next
      q += 1

        
    return '[' + str_values + ' ' + ']'
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
   

  def __iter__(self):
    self.inter = self._header.next
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    return self

  def __next__(self):
   
    if self.inter == self._trailer:
        raise StopIteration
    value = self.inter.val
    self.inter = self.inter.next
    return value
    

if __name__ == '__main__':
  empty = Linked_List()
  

    
  #get element in empty list
  try:
    empty.get_element_at(0)
  
  except ValueError:
    print('List is empty')

#remove element in empty list
  try:
    empty.remove_element_at(0)
  except ValueError:
    print('empty list')
 #rotate empty list and return string
  
  
  
  
   
  #test = Linked_List()
  
# insert element in list at tail
  try:
    test.append_element(1)
    test.append_element(4)
    test.append_element(2)
    test.append_element(5)
    test.append_element(7)
    print(test)
    test.insert_element_at(4)





    
  except IndexError:
    print('not valid use')
# negative index cases
  try:
    test.append_element(1)
    test.append_element(4)
    test.append_element(2)
    test.append_element(5)
    test.append_element(7)
    test.remove_element_at(-1)
    
  except IndexError:
   print('negative')

  try:
    test.append_element(1)
    test.append_element(4)
    test.append_element(2)
    test.append_element(5)
    test.append_element(7)
    test.insert_element_at(-1)
    
  except IndexError:
   print('negative')

  #rotate list
    test = Linked_List()
    test.append_element(1)
    test.append_element(4)
    test.append_element(2)
    test.append_element(5)
    test.append_element(7)
    test.rotate_left()
    print(test)

    # iteration
    for qr in test:
      print(qr)
    #string 
    str(test)

    
# getting element
  try:
    test.get_element_at(0)
    test.get_element_at(1)
    test.get_element_at(2)
    test.get_element_at(3)
  except IndexError:
    print('out of bounds')


  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
 
