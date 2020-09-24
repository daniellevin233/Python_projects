
class Node:

    def __init__(self, task, next=None):
        """
        Constructor for object of type Node
        :param task: object of type task - the task that will be
        in the node (self)
        :param next: the object of type Node or None - the object that
        node (self) will point to
        """
        self.__task = task
        self.__next = next

    def get_priority(self):
        """
        :return: float - priority of the task in the node (self)
        """
        return self.__task.get_priority()

    def set_priority(self, new_priority):
        """
        This method sets new_priority for the task in the node (self)
        :param new_priority: float - priority to be set
        """
        self.__task.set_priority(new_priority)

    def get_task(self):
        """
        :return: object of type task - task from the node (self)
        """
        return self.__task

    def get_next(self):
        """
        :return: object of type Node - Node that is next to the node (self)
        *each node holds pointer to its next node
        """
        return self.__next

    def set_next(self, next_node):
        """
        This method sets next_node for the node (self)
        :param next_node: the object of type Node - that is set to be the next
        """
        self.__next = next_node

    def has_next(self):
        """
        Method checks if pointer of the node (self) points to another Node
        :return: True if the next of the node (self) exists
        False if next of the node (self) is None
        """
        if self.__next:
            return True
        else:
            return False


