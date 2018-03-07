"""practice script for lesson 5: https://codility.com/media/train/5-Stacks.pdf"""
N = 5
STACK = [0]*N
SIZE = 0
# def push(arg_x):
#     """temp function docstring"""
#     global SIZE
#     STACK[arg_x] = arg_x
#     SIZE += 1
#     print({"FUN":"push(arg_x)", "arg_x":arg_x, "STACK":STACK, "SIZE":SIZE})
# def pop():
#     """temp function docstring"""
#     global SIZE
#     SIZE -= 1
#     print({"FUN":"pop()", "STACK":STACK, "SIZE":SIZE})
#     return(STACK[SIZE])
QUEUE = [0]*N
HEAD, TAIL = 0, 0
def push(arg_x):
    """temp function docstring"""
    print({"FUN":"1.push(arg_x)", "arg_x":arg_x, "TAIL":TAIL, "QUEUE":QUEUE})
    global TAIL
    TAIL = (TAIL + 1) % N
    QUEUE[TAIL] = arg_x
    print({"FUN":"2.push(arg_x)", "arg_x":arg_x, "TAIL":TAIL, "QUEUE":QUEUE})
def pop():
    """temp function docstring"""
    global HEAD
    print({"FUN":"1.pop()", "HEAD":HEAD, "QUEUE":QUEUE})
    HEAD = (HEAD + 1) % N
    print({"FUN":"2.pop()", "HEAD":HEAD, "QUEUE":QUEUE})
    return QUEUE[HEAD]
def size():
    """temp function docstring"""
    print({"FUN":"size():(TAIL - HEAD + N) % N", "TAIL":TAIL, "HEAD":HEAD, "N":N})
    return (TAIL - HEAD + N) % N
def empty():
    """temp function docstring"""
    print({"FUN":"empty(): HEAD == TAIL", "TAIL":TAIL, "HEAD":HEAD})
    return HEAD == TAIL
def grocery_store(arr_a):
    """Model Solution - O(n)"""
    len_n = len(arr_a)
    local_size, result = 0, 0
    for ndx_j in range(len_n):
        if arr_a[ndx_j] == 0:
            local_size += 1
        else:
            local_size -= 1
            result = max(result, -local_size)
    return result
grocery_store([0,0,0,1,0,1,0,1,1,0,1])
