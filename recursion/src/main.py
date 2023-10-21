#recursion: fibonacci

# f(0) = 0 f(1) = 1 fn(n) = f(n-1) + f(n-2)

def fib(n):
    # base case recursion
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursion case
    return fib(n-1) + fib(n-2)

# entrypoint
# for i in range(10):
#     print(fib(i))

def reverse_list(str):
    # base case
    if len(str) < 2:
        return str
    # recursion case
    return reverse_list(str[1:]) + str[0]
    
def print_list(lst):
    # base case
    if not lst:
        return
    # recursive case
    print(lst[0])
    print_list(lst[1:])       

def is_in_list(n, lst):
    # base case
    if not lst:
        return False
    # recursive case
    return lst[0] == n or is_in_list(n, lst[1:])



print(is_in_list("a","adriwno"))
