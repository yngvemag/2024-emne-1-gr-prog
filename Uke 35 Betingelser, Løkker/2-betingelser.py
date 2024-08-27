
# ==================================================================
# If statement
# ------------------------------------------------------------------
"""
if <sant>:
    do something
else:
    do something else
"""

"""
if <sant>:    
    do something
elif <sant>:
    do this instead
else:
    do something else
"""

# 1. Vi har to variabler x og y av typen int
# a) Hvis de er like print 'x og y er like'
# b) Hvis x > y print 'x er større enn y'
# c) Hvis x < y print 'x er mindre enn y'
x: int = 25
y: int = 25

# legg merke til '=='. Det er sammenlikning, Enkel '=' betyr tilordning
if x == y:
    print('x og y er like')
elif x > y:
    print('x er større enn y')
else:
    print('x er mindre enn y')


