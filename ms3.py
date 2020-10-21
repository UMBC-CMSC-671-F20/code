""" 3x3 magic square problem """

import constraint as c

p = c.Problem()
p.addVariables(range(0, 9), range(1, 9+1))
p.addConstraint(AllDifferentConstraint(), range(0, 9))
p.addConstraint(ExactSumConstraint(15), [0,4,8])
p.addConstraint(ExactSumConstraint(15), [2,4,6])
for row in range(3):
    p.addConstraint(ExactSumConstraint(15),
                          [row*3+i for i in range(3)])
for col in range(3):
    p.addConstraint(ExactSumConstraint(15),
                          [col+3*i for i in range(3)])

for s in p.getSolutions():
    print()
    for row in range(3):
        for col in range(3):
            print(s[row*3+col], end='') 
        print()
