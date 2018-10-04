def main():
    shapestr = shape(triangle)
    print(shapestr)
    sayhelloword = decoratorexample(1)
    print(type(sayhelloword))
    print(id(sayhelloword))
    print(sayhelloword)
    
def triangle(fname):
    return f"Hi {fname}, this is triangle"

def circle(fname):
    return f"Hi {fname}, this is circle"

def shape(f):
    return f("Vishal")

def decoratorexample(num):
    def wrapper(num):
        print("This is before calling funtion")
        #func()
        print("This is after calling function")
    #return wrapper

    def wrappermore(num):
        print("Before not sure")
        #func()
        print("after not sure")
    #return wrappermore

    if num == 1:
        return wrapper
    else:
        return wrappermore

@decoratorexample
def sayhelloword():
    print("Hello world!")

if __name__ == '__main__':
    main()
