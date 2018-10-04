def main():
    _xkwargs = {"Triangle":3, "Circle":0, "Square":4}
    _xargs = ('a','b', 'c', 10, 12, [10,20,30])
    circleshapes()
    squareshapes()
    dynamicshapes('circle', 'square', 'triangle', 9, ['a', 'b'],  (1,2,3), {'one':1, 'Two':2},True, None, 20.2)
    kwdynamicshapes(**_xkwargs)
    dynamicshapes(*_xargs)
    for idx in inclusive_range(2,10,2):
        print(idx)

def circleshapes():
    print("This is circle")

def squareshapes():
    print("This is square")

#passing dynamich arguments
def dynamicshapes(*args):
    if len(args):
        for shape in args:
            print(shape)

#passing dynamic keyword argments
def kwdynamicshapes(**kwargs):
    if len(kwargs):
        for key in kwargs:
            print(f"key = {key} and value = {kwargs[key]}")

def inclusive_range(*args):
    _xerror=False
    start = 0
    step = 1
    if len(args):
        if len(args) == 1:
            stop = args[0]
        elif len(args) == 2:
            (start, stop) = args
        elif len(args) == 3:
            (start, stop, step) = args
        else:
            _xerror = True
    else:
        _xerror = True
    if _xerror:
        print("You've entered wrong arguments")
    else:
        #generators
        i = start
        while(i <= stop):
            yield i
            i += step

if __name__ == '__main__':
    main()
