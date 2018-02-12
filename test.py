def multiadder(n):
    assert n > 0
    if n == 1:
        return lambda x: x
    else:
        return lambda a: lambda b: multiadder(n - 1)(a + b)

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def repeat_sum(f, x, n):
    total, k = 0, 0
    while k <= n:
        total = total + x
        x = f(x)
        k = k + 1
    return total
def sum_squares(n):
    f = lambda x : pow(k+1, 2)
    return repeat_sum(f, 0, n)
compose1(multiadder(4)(1000), multiadder(3)(10)(1000))(1)(2)(3)

def countdown(n):
    if n == 1:
        print(n)
    else:
        print(n)
        countdown(n - 1)
        print(n)
'''
# Constructor
def tree(root, branches=[]):
    return [root] + list(branches)
# Selectors
def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)
t = tree(1,
[tree(3,
[tree(4),
tree(5),
tree(6)]),
tree(2)])
'''
def height(t):
    if is_leaf(t):
        return 0
    else:
        return max([height(b) + 1 for b in branches(t)])

def prune(t, k):
    if k == 0:
        return tree(root(t))
    else:
        return tree(root(t), [prune(b, k - 1) for b in branches(t)])

def hailstone_tree(n, h):
    if h == 0:
        return tree(n)
    else:
        if (n - 1) % 3 == 0 and n > 4:
            return tree(n, [hailstone_tree(2 * n, h -1), hailstone_tree((n - 1) // 3, h - 1)])
        else:
            return tree(n, [hailstone_tree(2 * n, h -1)])

def find_path(tree, x):
    if root(tree) == x:
        return [root(tree)]
    else:
        a = [[root(tree)] + find_path(b, x) for b in branches(tree)]
        if [i for i in a if x in i]:
            return [i for i in a if x in i][0]
        else:
            return []
def add_this_many(x, el, lst):
    count = sum([1 for i in lst if i == x])
    for i in range(count):
         lst.append(el)
lst = [1, 2, 4, 2, 1]

def memory(n):
    def execute(f):
        nonlocal n
        n = f(n)
        print(n)
        return execute
    return execute

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)
    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))
def remove_duplicates(lnk):
    if len(lnk) == 1 or not lnk:
        return
    else:
        if lnk[1] == lnk[0]:
            lnk.rest = lnk.rest.rest
            remove_duplicates(lnk)
        else:
            remove_duplicates(lnk.rest)
    return lnk

def reverse(lnk):
    current, items = lnk, []
    while current is not Link.empty:
        items += [current.first]
        current = current.rest
    current = lnk
    while current is not Link.empty:
        current.first = items[-1]
        items = items[:-1]
        current = current.rest
    return lnk

def multiply_lnks(lnks):
    if len(lnks) == 1:
        return lnks[0]
    if min([len(lnk) for lnk in lnks]) == 0:
        return Link.empty
    else:
        elems = [lnk.first for lnk in lnks]
        product = 1
        for elem in elems:
            product *= elem
        return Link(product, multiply_lnks([lnk.rest for lnk in lnks]))
class Tree:
    def __init__(self, root, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.root = root
        self.branches = branches

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.root, branches_str)

    def is_leaf(self):
        return not self.branches

def widest_level(t):
    levels = []
    x = [t]
    while x:
        x, level = [b for t in x for b in t.branches], [b.root for t in x for b in t.branches]
        levels = sum([levels, [level]], [])
    return max(levels, key = len)
def redundant_map(t, f):

    t.root = f(t.root)
    new_f = lambda x: f(f(x))
    t.branches = [redundant_map(b, new_f) for b in t.branches]
    return t
def max_product(lst):
    if not lst:
        return 1
    if len(lst) == 1:
        return lst[0]
    else:
        return max([lst[0] * max_product(lst[2:]), lst[1] * max_product(lst[3:])])
def foo(lst):
    return [lst[i] * i for i in range(len(lst)) if i % 2 == 0]

def prod(lst):
    product = 1
    while lst:
        product *= lst[0]
        lst = lst[1:]
    return product
def eval_tree(tree):

    if tree.is_leaf():
        return tree.root
    else:
        if tree.root == '+':
            return sum([eval_tree(b) for b in tree.branches])
        if tree.root == '*':
            return prod([eval_tree(b) for b in tree.branches])

def quicksort_list(lst):

    if len(lst) == 1:
        return lst
    pivot = lst[0]
    less = [i for i in lst[1:] if i < pivot]
    greater = [i for i in lst[1:] if i > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)
def empty(s):
    return s is Link.empty
def extend_link(s, t):
    if empty(s):
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))
def quicksort_link(link):
    """
    >>> s = Link(3, Link(1, Link(4)))
    >>> quicksort_link(s)
    Link(1, Link(3, Link(4)))
    """
    if link.rest is Link.empty:
        return link
    pivot, others = link.first, link.rest
    less, greater = Link(1), Link(1)
    while link.rest is not Link.empty:
        curr, rest = link, link.rest
#        if rest == ():
#            None
        if rest.first > pivot:
            greater = extend_link(greater, Link(rest.first))
        else:
            less = extend_link(less, Link(rest.first))
        link = link.rest
    less = less.rest
    greater = greater.rest
    return extend_link(extend_link(quicksort_link(less), Link(pivot)), quicksort_link(greater))

def sums(n, k):
    if k > n or k == 0:
        return []
    y = []
    for x in range(1, n - k + 1):
        y.extend([[x] + s for s in sums(n - x, k - 1)])
    return y
