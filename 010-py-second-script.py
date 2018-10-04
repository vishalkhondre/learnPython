# learn about python data types
# learn about strings
# some more advanced string operations
#import argparse
#import googleapiclient
#from googleapiclient import discovery
#from six.moves import input
#import time
#import os
#from google.oauth2 import service_account

# credentials = service_account.Credentials.from_service_account_file(
#        'techcoe-devops-dev-03c8fb70136b.json')

#project_id = 'techcoe-devops-dev'
#compute = googleapiclient.discovery.build('compute', 'v1')
#zone = 'us-central1-c'

#result = compute.instances().list(project=project, zone=zone).execute()

# print(result)


import platform

def main():
    showmsg()
    shownumbers()
    learnwhile()
    learnfor()
    learnfibo()
    learnfunction(1000)
    learndatatypes()
    #learnwhileloop()
    learnforloop()

def showmsg():
    fname = 'James'
    lname = 'Bond'
    print('This is platform version {0}'.format(platform.platform()))
    print('This is python version {0}'.format(platform.python_version()))
    if True:
        print('This is True...')
    else:
        print("This is False")
    if False:
        print("This is True")
    else:
        print("This is False!!")
    # This is cool, instead of format function
    print(f"Hello {fname} {lname}, how are you doing")


def shownumbers():
    x = 10
    y = 20
    if x < y:
        print(f"x < y: x is {x} and y is {y}")


def learnwhile():
    idx = 0
    words = ['one', 'two', 'three', 'four', 'five']
    while (idx < 5):
        print(words[idx])
        idx += 1


def learnfor():
    words = ['one', 'two', 'three', 'four', 'five']
    for element in words:
        print(element)


def learnfibo():
    a, b = 0, 1
    while (b < 1000):
        a, b = b, a+b
        print(b, end=' ', flush=True)
    print('')


def learnfunction(n):
    print(n)


def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

def nonereturn():
    pass

def learndatatypes():
    x = 5
    dtx = type(x)
    print(f"x is of datatype {dtx}")

    y=5.12
    dty = type(y)
    print(f"y is of data type {dty}")

    z = True
    dtz = type(z)
    print(f'z is of data type {dtz}')

    str="This is string"
    dtstr = type(str)
    print(f"str is of data type {dtstr}")

    nonedt = nonereturn()
    dtnonedt = type(nonedt)
    print(f"nonedt is of data type {dtnonedt}")

def learnwhileloop():
    mypassword='jamesbond'
    inputpassword='check'
    maxattempts=5
    cnt=0
    auth=False
    while(mypassword!=inputpassword):
        cnt += 1
        inputpassword = input(f"{cnt}: Enter your Password:")
        if cnt == maxattempts:
            break
    else:
        auth=True
    print("Sucessful" if auth else "login failed, Contact support team!")

def learnforloop():
    chocolates = ['dailymilk', 'coffbite', 'choco', 'gems', 'popins']
    for chocolate in chocolates:
        print(chocolate, end=' ', flush=True)
    print()

if __name__ == '__main__':
    main()
    z = 30
    num1 = 0
    if False:
        num1 = 10
    else:
        num2 = 20
    print(z)
    print(num1)
    print(num2)
    if isprime(5):
        print('This is prime number')
