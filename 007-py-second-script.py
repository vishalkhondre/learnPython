# learn about python data types
# learn about strings
# some more advanced string operations

myline = '     abc,pqr,xyz    '

#split on delimiter into a list of substrings
mylinewords = myline.split(',')
print(mylinewords)

#print(mylinewords[2])

#find the offset of the substring in myline
print(myline.find('pq'))

# convert to upper case
print(myline.upper())

#combine mutiple operations 
print(myline.upper().lstrip().rstrip().split(','))

#some foramtting string operations
mystr = '{0} Vishal how are {1} doing todat'.format('Hello', 'you')
print(mystr)

print('hello world !!!')
