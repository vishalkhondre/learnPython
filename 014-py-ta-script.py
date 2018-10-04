import platform

class testcase:
    def __init__(self, **kwargs):
        self._tcname = kwargs['tcname']
        self._product = kwargs['product']
        self._module = kwargs['module']
        self._tctype = kwargs['tctype']
    
    def tcname(self):
        return self._tcname
    
    def product(self):
        return self._product
    
    def module(self):
        return self._module
    
    def tctype(self):
        return self._tctype

def printtestcase(tsobj):
    if not isinstance(tsobj, testcase):
        print("This is wrong object you passed !!")
    else:
        print(tsobj.tcname())

def readtestcasedata():
    with open ("testsuitedata.csv", "r+") as testcasedata:
        for testcaseline in testcasedata:
            print(testcaseline)
            #words=line.split(',')
            #print(words)

def main():
    readtestcasedata()
    tsobj1 = testcase(tcname='tsid006', product='myflow', module='m5', tctype='web')
    #print(tsobj1.tsname)
    printtestcase(tsobj1)
    if tsobj1.product() == 'myflow':
        print('let''s do some automation..')

if __name__ == '__main__':
    main()
