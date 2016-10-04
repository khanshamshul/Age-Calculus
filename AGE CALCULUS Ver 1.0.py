###Age_Calculus is a free program written in python for FYCS Practical

import math
##Take input from user

a=int(input('ENTER CURRENT YEAR (YYYY) =')) 
b=int(input('ENTER YOUR DATE OF BIRTH (YYYY) ='))
c= a-b

##Error for invalid year
if b>a:
       print('ENTER VALID DATE OF BIRTH')
else:
       print('YOUR CURRENT AGE IS =',c)
       
       
