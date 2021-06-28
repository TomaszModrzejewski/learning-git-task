import itertools
##Create a manual list 
x = [1,2,3,4,5]
print (x)
print ("\n")
##copy list
import copy
y = copy.copy(x)
print(y)
print ("\n")
##re-copy list
z=copy.copy(x)
print(z[2])
print ("\n")
import itertools
for i in itertools.count(10, 5):  
    if i == 35:  
        break
    else:  
        print(i, end =" ")

print ("\n")

##infinite iterator
import itertools
from itertools import count
from itertools import islice
for num in islice(count(30), 10):
    print(num) 

print ("\n")

##itertools.cycle
import itertools
count = 0
  
# for in loop 
for i in itertools.cycle('LOOP'): 
    if count > 19: 
        break
    else: 
        print(i, end = " ") 
        count += 1 

print ("\n")

##itertools.repeat
import itertools  
    
# using repeat() to repeatedly print number  
print (list(itertools.repeat('REPEAT', 10))) 