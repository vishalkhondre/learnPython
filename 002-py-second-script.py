#Import the sys module
import sys

#check the execution enviroment platform
_eeplatform = sys.platform
print(_eeplatform)

#understand some basics of strings and * operator
print('hello world')
print('spam! ' * 4)
print(3 * 4)

#finally conclude first script
print('This is my first python script')

def myfirstfunc():
    print('Hi I''m in funtion..')

myfirstfunc()

class myfirstclass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def myfirstclassfunc(self):
        print(self.var1)
        print(self.var2)

myfirstobj = myfirstclass('Helloo..', 10)

myfirstobj.myfirstclassfunc()

