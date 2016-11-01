'''
Created on Oct 30, 2016

@author: zat00
'''
from _sqlite3 import Row


starfile = open("stars.txt")

try:
    int('c')
    print("converted c to int :(")
except:
    print('did not convert c to int :)')

for row in starfile:
    if "Sirius" in row:
        i = 0
        while(i < len(row)):
            try:
                int(row[i])
                break
            except:
                i = i + 1
                
        j = i
        while(j < len(row)):
            if (row[j].isspace()):
                break
            j = j + 1
            
#         print("(i, j): (" + str(i) + ", " + str(j) + ")")
        date =  row[i:j]
        print date[0:2]
        print date[3:5]
        print date[6:9]
                
starfile.close()

ariesfile = open("aries.txt", 'r')

targDate = 
for row in ariesfile:
    