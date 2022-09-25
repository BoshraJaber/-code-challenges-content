from  implement_queue_using_stack.implement_queue import Stack , my_queue , Node 

def test_my_queue_enqueue():
    element = my_queue()
    element.enqueue(1)
    element.enqueue(2)
    assert element.stack1.peek() == 2
     

def test_my_queue_dequeue():
    element = my_queue()
    element.enqueue(1)
    element.enqueue(2)
    element.dequeue()
    assert  element.stack2.peek() == 2
       

