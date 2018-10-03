class myfirstclass:
    x = 5
    y = 8
    z = 10
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r
    a=60
    b=70
    c=80

obj1 = myfirstclass(10,20,30)
obj1.o = 100
print(obj1.x)
print(obj1.y)
print(obj1.z)
print(obj1.p)
print(obj1.q)
print(obj1.r)
print(obj1.a)
print(obj1.b)
print(obj1.c)
print(obj1.o)

obj2 = myfirstclass(1,2,3)
print(obj2.c)

