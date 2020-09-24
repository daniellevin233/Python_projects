import time


def blurg(seq):
    a = next(seq)
    yield a
    for b in seq:
        # print(list(seq))
        mid = (a + b) // 2
        a = b
        yield mid
        yield b


my_iter = iter([0, 8])
my_blurg = blurg(blurg(blurg(blurg(blurg(my_iter)))))


# print(list(my_blurg))

def f1():
    a = []
    for j in range(1000000):
        a.append(j * j)
    for j in range(1000000):
        if 999999 * j == a[j]:
            print('yes')


def f3():
    d = {}
    for j in range(1000000):
        d[j] = j * j
    for j in range(1000000):
        if 999999 * j in d:
            print('yes_d')


# f1(), f3()

def subsets(lst):
    if len(lst) == 0:
        yield []
    else:
        for tail in subsets(lst[1:]):
            yield tail
            yield [lst[0]] + tail


# print(list(subsets([1, 5, 3])))

def time_f(sizes):
    for n in sizes:
        start = time.time()
        f3()
        print("n =", n, " time =", time.time() - start, "seconds")


# time_f([10**5, 10**6, 10**7, 10**8, 10**9])

def count_sums(a, s):
    subs_lst = list(my_subsets(a))
    sums = 0
    for set in subs_lst:
        if sum(set) == s:
            sums += 1
    return sums


def my_subsets(lst):
    if not lst:
        yield []
    else:
        for tail in my_subsets(lst[1:]):
            yield tail
            yield [lst[0]] + tail


# print(count_sums([3, 5, 8, 9, 11, 12, 20], 20))

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_reverse_iterator(head):
    if head.next:
        for data in get_reverse_iterator(head.next):
            yield data
    yield head.data


lst = Node('a', Node('b'))
# for i in get_reverse_iterator1(lst):
#     print(i)
lst1 = Node(1, Node(2))


def zipper(head1, head2):
    while head1:
        next1 = head1.next
        next2 = head2.next
        head1.next = head2
        head2.next = next1
        head1 = next1
        head2 = next2


zipper(lst, lst1)


def split(s):
    split_lst = []
    new_s = ""
    for i in range(len(s)):
        if s[i] != " ":
            new_s += s[i]
            if i + 1 < len(s) and s[i + 1] != " ":
                continue
            else:
                split_lst.append(new_s)
                new_s = ""
    return split_lst

# print(split(" de f ghi a"))

def cartesian_product(lst):
    n_lst = []
    if not lst:
        return [""]
    for char in lst[0]:
        n_lst += cartesian_product_hp(char, lst[1:], n_lst)
    return list(set(n_lst))

def cartesian_product_hp(char, lst, n_lst):
    if not lst:
        return [char]
    for n_char in lst[0]:
        n_lst += cartesian_product_hp(char + n_char, lst[1:], n_lst)
    return n_lst

# print(cartesian_product([['a'], ['b', 'c'], ['d']]))
# print(cartesian_product([['a', 'b'], ['c', 'd', 'e']]))

def interpolate(d):
    def closest(x):
        min_key = 0
        minimal = abs(x)
        for key in d.keys():
            if abs(x - key) <= minimal:
                minimal = abs(x - key)
                min_key = key
        return d[min_key]

    return closest

# d = {0:0, 7:10, 20:30}
# f = interpolate(d)
# print(f(-1), f(5), f(7), f(18))

from functools import reduce
p = reduce(lambda x, y: x - y, [1, 2, 3])
# print(type(reduce(lambda x, y: x+y, [1,2,3])))


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


# print(gcd(15, 10))

def all_increasing(lst):
    for subset in helper(lst):
        print(sorted(subset), end=" ")

def helper(lst):
    if not lst:
        yield []
    else:
        for tail in helper(lst[1:]):
            yield tail
            yield [lst[0]] + tail

# all_increasing([1, 4, 3, 2])
from copy import deepcopy

def find(lst):
    med = len(lst) // 2
    if len(lst) == 2 or lst[med] > lst[med + 1]:
        return med
    if lst[med] < lst[0]:
        return find(lst[:med])
    else:
        return med + find(lst[med + 1:])

# print(find([6, 1, 4, 5]))

my_inner = [0]
my_lst = [None]*4
# print(id(my_lst))
my_lst[0] = my_inner
for i in range(1, len(my_lst)):
    my_lst[i] = my_lst[i-1]
    # print(my_lst)
    my_lst[i][0] += 1


# print(id(my_lst))

def foo(f, n):  ########################################################################################################
    my_iter = iter(range(n))
    def g(x):
        # while n != 0:
        for i in my_iter:
            y = f(x)
            x = y
            # n -= 1


        return x
    return g


# g = foo(f, 3)
# def f(x): return 4*x
# print(g(10))

i = (-1)>0
# print(i)

def shrink(x):
    s, p, n, new_l = 0, x[0] > 0, x[0] < 0, []
    for it in x:
        if (it > 0 and p) or (it < 0 and n):
            s += it
        else:
            new_l.append(s)
            s = it
        p, n = it > 0, it < 0
    return new_l + [s]


# print(shrink([2, 5, -3, -1, -1, 3, -2, -2]))

def set_power(s, n):
    return s_p_hp(s, n, [], [])

def s_p_hp(s, n, cur_l, big_l):
    if len(cur_l) == n:
        big_l.append(cur_l)
        return
    for it in s:
        s_p_hp(s, n, cur_l + [it], big_l)
    return big_l

# print(set_power([7, 8], 3))
a = [[0],[1]]*12
a[3][0] = None
# print(id(a[2]), id(a[1]))
# print(a)
BRACKETS = {'{': '}', '(': ')', '[': ']'}
def b_brackets(br):
    for b in BRACKETS:
        if br.count(b) != br.count(BRACKETS[b]):
            return False
    return True

# print(b_brackets('(({}{}))'))
z = zip([0, 1, 2], [3, 4, 5])
# print(list(z))

def contain(items, world):
    return cont_hp(items, world, set())

def cont_hp(items, world, answers):
    if not items:
        return True
    answer = is_in(items.pop(), world)
    answers.add(answer)
    return (False not in answers) and cont_hp(items, world, answers)

def is_in(item, world):
    if not world:
        return False
    if item == world.pop():
        return True
    return is_in(item, world)
# print(contain([0, 1, 2], [0, 1, 2, 5, 6, 7]))

def merge(w1, w2):
    merge_pre(w1[0], w1[1:], w2)
    merge_pre(w2[0], w1, w2[1:])

def find_pair(lst):
    mid = len(lst) // 2
    if lst[mid-1:mid+1] == ['(', ')']:
        return mid - 1
    if lst[mid-1:mid+1] == ['(', '(']:
        return mid - 1 + find_pair(lst[mid+1:])
    else:
        return find_pair(lst[:mid-1])

L1 = [1, 2, 3]
L2 = L1 + [4]
L3 = L1
L1.append(4)
L4 = L3[:]
L4[3] = [4]
L5 = deepcopy(L4)
print(L1 is L2)
print(id(L2) == id(L3))
print(L1 is L3)
print(L4 is id(L1))
print(L5[3] is L4[3])
