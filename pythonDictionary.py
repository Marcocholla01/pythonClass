# Write a Python script to merge two Python dictionaries.
#Merging Two Python Dictionaries
dic1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
dic2 = {'f':6, 'g':7, 'h':8, 'i':9, 'j':10}

#Merging dic1 and dic2
mergedDic = {**dic1, **dic2}

#Printing Merged Dictionary
print(mergedDic)

# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys
#Printing Dictionary of Square Values
squaredDic = {x:x**2 for x in range(1,16)}

#Printing Dictionary of Square Values
print(squaredDic)

