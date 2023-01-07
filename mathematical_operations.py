def my_sum(a, b):
    return a + b

def my_prod(*args):
    p = 1
    for i in args:
        p = p * i
    return p
