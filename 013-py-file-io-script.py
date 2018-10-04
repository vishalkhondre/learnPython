import platform

class testsuite:
    def __init__(self, tsname, product, module, tstype):
        self._tsname = tsname
        self._product = product
        self._module = module
        self._tstype = tstype
    
    def tsname(self):
        return self._tsname
    
    def product(self):
        return self._product
    
    def module(self):
        return self._module
    
    def tstype(self):
        return self._tstype

def printtestsuite(tsobj):
    if not isinstance(tsobj, testsuite):
        print("This is wrong object you passed !!")
    else:
        print(tsobj.tsname())

def readtestsuitedata():
    with open ("testsuitedata.csv", "r+") as testsuitedata:
        for testsuiteline in testsuitedata:
            print(testsuiteline)
            #words=line.split(',')
            #print(words)

def main():
    readtestsuitedata()
    tsobj1 = testsuite('tsid006', 'tradeflow', 'ndf', 'nstp')
    #print(tsobj1.tsname)
    printtestsuite(tsobj1)
    if tsobj1.product() == 'tradeflow':
        print('let''s do some automation..')

if __name__ == '__main__':
    main()
