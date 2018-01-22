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
