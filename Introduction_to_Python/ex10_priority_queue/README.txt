daniellevin
336462874
Daniel_Levin

I discussed the exercise with: PELEG LABSUPPORT

==============================================================================
=  README for ex10: realisation of priority queue using linked list as
=  data structure
=  Realisation of 3 classes: Node, PriorityQueue, PriorityQueueIterator
=  Realisation of different functions for working with priority queues
==============================================================================

It includes three files:
    1. priority_queue.py - contains class PriorityQueue representing linked
list - priority queue
    2. node.py - contains class Node representing node in linked list with
task as data and pointer to the next Node
    3. priority_queue_iterator.py - contains class for creating iterable object out of
PriorityQueue object

==================
=  Description:  =
==================

With the help of the 'priority_queue.py' it is possible to build
priority queue. Need to create object PriorityQueue and put list of tasks
as parameter.
Methods that are accessible:
enque(task) - enter the task into the queue
peek() - to get the task from the head of the queue
deque() - to get the task from the head of the queue and to delete the head
change_priority(old, new) - to change the priority of the task with the
old priority to new prioirity

Operations that are defined for priority queues:
    len(q) - return number of the tasks that are in the queue now
    iter(q) - create iterable object out of priority queue
    next(q) - return task of the next node in priority queue - iterator
    str(q) - return string with list of tasks in the priority order
    q1 + q2 - add(q1, q2) - adds all the tasks of queue q1 to the queue q2
    q1 == q2 - eg(q1, q2) - return True if all the tasks of two queues
    are equal, False otherwise

========================
= additional questions =
========================

task 9 - if we will try to iterate on our queue one more time, anything wont
    be printed because the implementation of iterator for priority queue
    that we have inside the class PriorityQueue, hence we dont create new
    iterator each time that iteration on queue was called. We have one init
    for the class, so we cant create new object every time or denote some
    properties be defaultive each time that iteration is called.
    This explains why calling twice to iteration will print the tasks
    only once.

task 10 - the answer is contrary to one of task 9, because of creating
    the separate class for PriorityQueueIterator, every time that iteration
    is called code, implements new object of type PriorityQueueIterator, and
    each calling will produce new print operation. So each time we do
    iteration from the first element of the queue that is inited in the
    PriorityQueueIterator constructor, the tasks will  be printed from the
    beginning.

task 12 - '+' - __add__(self, other) - denote size(self) = n, size(other) = m
     works in O(n*m). The loop that runs in O(m), and each iteration makes
     enque of the task into the queue newqueue that is of size 'n' in the
     start position. Enque works in O(size(self)) that is O(n).
     So the entire running time will be O(m)*O(n) = O(n*m).

task 13 - __eq__(self, other) - denote size(self) = n, size(other) = m
    then the first comparison in the function takes O(1) hence we implemented
    operatoin of get_size() in O(1), and '==' of integer numbers takes O(1)
    in python.
    The loop runs O(n) time in the worst case, because we run on 'self' queue,
    its size n, and if the queues are equal we will need to run on it up
    to the end.
    Furthermore getting value from list by it index (string 206), takes O(1).
    So the entire running time is O(n), because all operations O(1) are
    neglective.

============
= Hey doc! =
============