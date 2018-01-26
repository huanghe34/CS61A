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
