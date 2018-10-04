import platform

class testcase:
    def __init__(self, **kwargs):
        self._tcname = kwargs['tcname'] if 'tcname' in kwargs else 'default-tcname'
        self._product = kwargs['product'] if 'product' in kwargs else 'defailt-prodct'
        self._module = kwargs['module'] if 'module' in kwargs else 'default-module'
        self._tctype = kwargs['tctype'] if 'tctype' in kwargs else 'default-tctye'
    
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

def readtestcasedataV1():
    testcaselines = []
    with open ("testcasedata.csv", "r+") as testcasedata:
        for testcaseline in testcasedata:
            testcaseline = testcaseline.rstrip('\n')
            testcaselines.append(testcaseline)
    return testcaselines

def readtestcasedataV2():
    testcaselines = [testcaseline.rstrip('\n') for testcaseline in open("testcasedata.csv") ]
    return testcaselines

def populatetcobject(tclist):
    tcobjs = []
    for tcs in tclist:
        ltcname, lproduct, lmodule, ltctype = tcs.split(',')
        tcobj = testcase(tcname=ltcname, product=lproduct, module=lmodule, tctype=ltctype)
        tcobjs.append(tcobj)
    return tcobjs

def main():
    tclines = readtestcasedataV2()
    tcobjs = populatetcobject(tclines)
    for tcs in tcobjs:
        printtestcase(tcs)

if __name__ == '__main__':
    main()
