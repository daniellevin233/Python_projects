##############################################################################
# FILE : ex10.py
# WRITER : Daniel Levin , daniellevin , 336462874
# EXERCISE : intro2cs ex10 2017-2018
# DESCRIPTION: Working with priority queue as linked list
# Realisation of different function for working with priority queues inside
# PriorityQueue class
# Classes: Node, PriorityQueue, PriorityQueueIterator
##############################################################################

###########
# imports #
###########

import copy
from node import Node
from priority_queue_iterator import PriorityQueueIterator

########################
# class implementation #
########################


class PriorityQueue:

    HEAD_QUEUE_INDEX = 0
    TAIL_OF_QUEUE_VALUE = None

    def __init__(self, tasks=[]):
        """
        Constructor for object of type PriorityQueue
        :param tasks: start list of tasks that need to input to the queue
        """
        self.__queue = []  # further this list will contain only queue head
        self.__queue_size = 0
        self.__head = None
        if tasks:
            self.__append(tasks)
        self.cur = self.__head

    def enque(self, task):
        """
        This method put the given task into the queue regarding the priorities
        of the tasks that are already in the queue. If there are some tasks
        with the same priorities they will be ordered in accordance to
        coming order. I.e. earlier the task was input, closer to the head of
        the queue it will be.
        :param task: the object of type task that we gonna put into the queue
        """
        new_node = Node(task)
        cur_node, prev_node = self.__head, None
        while cur_node and \
                task.get_priority() <= cur_node.get_task().get_priority():
            prev_node = cur_node
            cur_node = cur_node.get_next()
        if prev_node:
            prev_node.set_next(new_node)
        new_node.set_next(cur_node)
        self.__queue_size += 1
        if self.get_head() is cur_node:  # check if need to change queue head
            self.set_head(new_node)

    def peek(self):
        """
        :return: object of type task - that is inside the head of the queue
        """
        if self.__queue_is_empty():  # the queue is empty - return None
            return None
        return self.__queue[self.HEAD_QUEUE_INDEX].get_task()

    def deque(self):
        """
        Method delete the head of the queue - the Node that is there
        :return: object of type task - that was inside the head of the queue
        """
        if self.__queue_is_empty():  # the queue is without head - return None
            return None
        head_task = self.__head.get_task()
        self.set_head(self.__head.get_next())  # set new head
        self.__queue_size -= 1
        return head_task

    def change_priority(self, old, new):
        """
        Method change the priority of the task with old priority to new
        priority for the first node with old priority that we are meeting
        :param old: float - priority that need to find and change
        :param new: float - priority that need to put after changing
        :return: None if the queue is empty or if there are no tasks with
        old priority - the queue won't be changed
        """
        if self.__queue_is_empty():
            return None
        cur_node = prev_node = self.__head
        while cur_node.get_task().get_priority() != old:
            if cur_node.has_next():
                prev_node = cur_node
                cur_node = cur_node.get_next()
            else:  # there is no task with priority "old"
                # don't touch the queue
                return None
        cur_node.get_task().set_priority(new)
        self.__remove_node_from_queue(cur_node, prev_node)
        self.enque(cur_node.get_task())

    def __remove_node_from_queue(self, node, prev_node):
        """
        Method removes the given node from the queue.
        :param node: object of type Node that need to remove
        :param prev_node: object of type Node that is previous to the node
        i.e. that prev_node points to node
        """
        prev_node.set_next(node.get_next())
        self.__queue_size -= 1

    def __append(self, tasks):
        """
        Method appends the queue with the given tasks
        :param tasks: list of objects of type task - to be added
        """
        self.__head = Node(tasks[0])  # declare first task as the head node
        self.__queue_size += 1  # our first node in the queue
        self.__head.set_next(self.TAIL_OF_QUEUE_VALUE)  # fix pointer to None
        for task in tasks[1:]:  # enter all the other tasks into the queue
            self.enque(task)

    def __queue_is_empty(self):
        """
        Method checks if the list representing the queue is empty or not.
        :return: True if queue list is empty
        False otherwise
        """
        if not self.__queue:
            return True
        else:
            return False

    def get_head(self):
        """
        :return: object of type Node - head of the queue
        """
        return self.__head

    def get_size(self):
        """
        :return: integer - size of queue - number of tasks there
        """
        return self.__queue_size

    def set_head(self, new_head):
        """
        Method set new head of the queue
        :param new_head: Node - node to be set as new head
        """
        self.__head = new_head
        self.__queue.append(new_head)  # append to queue list the new head

    def __len__(self):
        """
        :return: integer - size (length) of the queue in the current moment
        """
        return self.__queue_size

    def __iter__(self):
        """
        Iterator for object of type PriorityQueue
        :return: iterable object
        """
        return PriorityQueueIterator(self)

    def __next__(self):
        """
        Next method for our iterable object - priority queue
        :return: task of the current node
        """
        if self.cur:
            task_for_returning = self.cur.get_task()
            self.cur = self.cur.get_next()
            return task_for_returning
        raise StopIteration

    def __str__(self):
        """
        Method creates the string representation for object of type
        PriorityQueue
        :return: string containing the list of tasks that are in the
        queue to the given moment of time
        """
        tasks_lst = []
        for task in self:
            tasks_lst.append(task)
        return str(tasks_lst)

    def __add__(self, other):
        """
        This method create the queue that is addition of other queue and
        self queue. It means that it is sum operation for priority queues
        :param other: object of type PriorityQueue that we wanna add to self
        :return: queue containing all the tasks from other and self
        """
        new_queue = copy.deepcopy(self)  # queue representing sum of 2 others
        for task in other:
            new_queue.enque(task)
        return new_queue

    def __eq__(self, other):
        """
        This method is equation for the queues, two queues are equal iff
        all tasks are equal
        :param other: priority queue that we are comparing to
        :return: True if queues are identical, False otherwise
        """
        if self.get_size() != other.get_size():
            return False
        for task_index, cur_our_task in enumerate(self):
            if cur_our_task != list(other)[task_index]:
                return False
        return True
