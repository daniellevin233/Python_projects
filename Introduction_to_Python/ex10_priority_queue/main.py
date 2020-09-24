from priority_queue import *
from string_task import *
from random import randint, uniform, choice, seed
import string

MAX_PRIORITY = 1000
MAX_MSG_LENGTH = 40

FIRST_QUEUE_SEED = 5
SECOND_QUEUE_SEED = 10

FIRST_QUEUE_LENGTH = 6
SECOND_QUEUE_LENGTH = 4

def get_random_task():
    priority = randint(0, MAX_PRIORITY)
    N = randint(1, MAX_MSG_LENGTH)
    text = ''.join(choice(string.ascii_uppercase + string.digits)
                    for _ in range(N))

    return StringTask(priority,text)

def get_tasks(num):
    return [get_random_task() for _ in range(num)]

def basic_test_equal(q1, q2, res):
    '''
    This method tests if q1 is equal to q2, 
    our expected result to be printed is "res"
    '''
    print("We are expecting the result %s, got %s\n" % (q1 == q2, res))

    
def print_queue_tasks(q):
    for task in q:
        print(task)
    #print an empty line, for ease of reading
    print()

def test_0():
    seed(FIRST_QUEUE_SEED)
    tasks = get_tasks(FIRST_QUEUE_LENGTH)

    seed(SECOND_QUEUE_SEED)
    tasks2 = get_tasks(SECOND_QUEUE_LENGTH)

    q1 = PriorityQueue(tasks)
    q2 = PriorityQueue(tasks2)

    basic_test_equal(q1, q1, True)
    basic_test_equal(q1, q2, False)
    basic_test_equal(FIRST_QUEUE_LENGTH, len(q1), True)
    
def test_1():
    seed(FIRST_QUEUE_SEED)
    tasks = get_tasks(FIRST_QUEUE_LENGTH)

    seed(SECOND_QUEUE_SEED)
    tasks2 = get_tasks(SECOND_QUEUE_LENGTH)

    q1 = PriorityQueue(tasks)
    q2 = PriorityQueue(tasks2)
    
    '''The result of the next command should be:
    (897, 'LMYTBX0KJQEVTA')
    (880, 'C1FNV6XJVR8FTUTLFJT')
    (637, 'W7B3PDKHX4PY8GPAN')
    (610, 'ETWT4UL44LDQBWZB90XYA2')
    (417, 'LYKEI2IIAANNKKSUM8')
    (47, 'MHP3W6W7Q3GX')
    '''
    print_queue_tasks(q1)
    
    '''The result of the next command should be:
    (862, '0PCC5TE8FJYXJHG')
    (585, '14A')
    (211, '5RKC75UEPXC0IWY0SQ3LTXI3P2YCAP')
    (137, 'T8XPU9214EU6K')
    '''
    print_queue_tasks(q2)
    
    q3 = q1 + q2
    
    '''The result of the next command should be:
    (897, 'LMYTBX0KJQEVTA')
    (880, 'C1FNV6XJVR8FTUTLFJT')
    (862, '0PCC5TE8FJYXJHG')
    (637, 'W7B3PDKHX4PY8GPAN')
    (610, 'ETWT4UL44LDQBWZB90XYA2')
    (585, '14A')
    (417, 'LYKEI2IIAANNKKSUM8')
    (211, '5RKC75UEPXC0IWY0SQ3LTXI3P2YCAP')
    (137, 'T8XPU9214EU6K')
    (47, 'MHP3W6W7Q3GX')
    '''
    print_queue_tasks(q3)
    
    q3.change_priority(417, 637)

    
    '''The result of the next command should be:
    (897, 'LMYTBX0KJQEVTA')
    (880, 'C1FNV6XJVR8FTUTLFJT')
    (862, '0PCC5TE8FJYXJHG')
    (637, 'W7B3PDKHX4PY8GPAN')
    (637, 'LYKEI2IIAANNKKSUM8')
    (610, 'ETWT4UL44LDQBWZB90XYA2')
    (585, '14A')
    (211, '5RKC75UEPXC0IWY0SQ3LTXI3P2YCAP')
    (137, 'T8XPU9214EU6K')
    (47, 'MHP3W6W7Q3GX')
    '''
    print_queue_tasks(q3)
    
    q3.change_priority(637, 1)
    
    '''The result of the next command should be:
    (897, 'LMYTBX0KJQEVTA')
    (880, 'C1FNV6XJVR8FTUTLFJT')
    (862, '0PCC5TE8FJYXJHG')
    (637, 'LYKEI2IIAANNKKSUM8')
    (610, 'ETWT4UL44LDQBWZB90XYA2')
    (585, '14A')
    (211, '5RKC75UEPXC0IWY0SQ3LTXI3P2YCAP')
    (137, 'T8XPU9214EU6K')
    (47, 'MHP3W6W7Q3GX')
    (1, 'W7B3PDKHX4PY8GPAN')
    '''
    print_queue_tasks(q3)
    
    task = q3.deque()
    
    '''The result of the next command should be:
    (897, 'LMYTBX0KJQEVTA')
    '''
    print(task, "\n")
    
    '''The result of the next command should be:
    (880, 'C1FNV6XJVR8FTUTLFJT')
    (862, '0PCC5TE8FJYXJHG')
    (637, 'LYKEI2IIAANNKKSUM8')
    (610, 'ETWT4UL44LDQBWZB90XYA2')
    (585, '14A')
    (211, '5RKC75UEPXC0IWY0SQ3LTXI3P2YCAP')
    (137, 'T8XPU9214EU6K')
    (47, 'MHP3W6W7Q3GX')
    (1, 'W7B3PDKHX4PY8GPAN')
    '''
    print_queue_tasks(q3)

def test_2():
    task1 = StringTask(3, "I")
    task2 = StringTask(2, "Love")
    task3 = StringTask(1, "Chocolate!")
    
    q = PriorityQueue()
    q.enque(task3)
    q.enque(task2)
    q.enque(task1)
    
    '''The result of the next command should be:
    (3, 'I')
    (2, 'Love')
    (1, 'Chocolate!')
    '''
    print_queue_tasks(q)
    
    '''The result of the next command should be:
    [(3, 'I'), (2, 'Love'), (1, 'Chocolate!') ]
    '''
    print(q)

def test_3():
    task1 = StringTask(3, "I")
    task2 = StringTask(2, "Love")
    task3 = StringTask(1, "Chocolate!")
    
    q = PriorityQueue()
    q.enque(task3)
    q.enque(task2)
    q.enque(task1)
    
    q.deque()
    q.deque()
    
    '''The result of the next command should be:
    (1, 'Chocolate!')
    '''
    print_queue_tasks(q)
    
 
def main():
    test_0()
    # test_1()
    # test_2()
    # test_3()

if __name__ == "__main__":
    main()
