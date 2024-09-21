stackSize = []

def stack_is_empty():
    if len(stackSize) == 0:
        return True

def stack_is_not_empty():

    return True if stackSize == 0 else False

def stack_push(value):
    global stackSize
    stackSize += 1


def stack_pop():
    global stackSize
    if stackSize > 0:
        stackSize -= 1
    else: return stack_is_empty()

def stack_count():
    global stackSize
    return stackSize