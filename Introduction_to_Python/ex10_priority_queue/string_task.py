class StringTask:
    def __init__(self, priority, task_str):
        self.__priority = priority
        self.__task_str = task_str

    def get_priority(self):
        return self.__priority

    def set_priority(self, new_priority):
        self.__priority = new_priority

    def execute(self):
        print(self.__task_str)

    def __str__(self):
        return str((self.__priority, self.__task_str))

    def __eq__(self, other):
        return self.get_priority() == other.get_priority() and \
                self.__task_str == other.__task_str

    def __repr__(self):
        return 'StringTask'+str((self.__priority, self.__task_str))
