# learn about python data types
# learn about strings

# define string
myfirststr = 'spam grrr!'
print(len(myfirststr))

myfirstchar = myfirststr[0] # the first item in myfirststr string
print(myfirstchar)

mysecondchar = myfirststr[1] # the second item in myfirststr string
print(mysecondchar)

# this will throw error => indexerror string index out of range
#myerrorchar = myfirststr[25]
#print(myerrorchar)
try:
    myerrorchar = myfirststr[25]
except:
    print('oh god.. error!!!')

# look index from end
mylastchar = myfirststr[-1] # the last character of the string
print(mylastchar)

mysecondlastchar = myfirststr[-2] # the seocnd last character of string
print(mysecondlastchar)

# learn to slice the string
# take out some portion of the string
mysomeportion = myfirststr[1:4] # take out first four characters from string
print(mysomeportion)

mysomeportion = myfirststr[0:4] # take out first four characters from string
print(mysomeportion)

mysomeportion = myfirststr[1:3] # take out first four characters from string
print(mysomeportion)

#first value in range is optional and it takes defualt 0 that means start of the string
mysomeportion = myfirststr[:6] # take out first four characters from string
print(mysomeportion)

mysomeportion = myfirststr[:-1]
print(mysomeportion)

mysomeportion = myfirststr[:]
print(mysomeportion)

# learn some opeartions such as concatenation, repetition
s = 'string'
s = 'my ' + s + ' '
print(s)

myrepeatstr = s * 3
print(myrepeatstr)

