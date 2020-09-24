########################
# class implementation #
########################


class PriorityQueueIterator:

    def __init__(self, queue):
        """
        Constructor of class PriorityQueueIterator.
        :param queue: object of type PriorityQueue that we gonna make iterable
        """
        self.cur = queue.get_head()

    def __iter__(self):
        """
        Iterator for object of type PriorityQueue
        :return: iterable object - itself
        """
        return self

    def __next__(self):
        """
        The method next that implements iterating onto iterable
        object of type PriorityQueue
        :return: the task of the node that pointer points on in the
        current moment, or StopIteration if this one doesn't exist
        """
        if self.has_next():
            task_for_returning = self.cur.get_task()
            self.cur = self.cur.get_next()
            return task_for_returning
        raise StopIteration

    def has_next(self):
        """
        Method checks if the current node exists, or not
        :return: True if the next node is defined
        False if next node doesn't exist
        """
        if self.cur:
            return True
        return False
