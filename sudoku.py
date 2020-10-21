# Sudoku puzzle solver by Luigi Poderico (www.poderico.it), adapted by
# Tim Finin (finin@Umbc.edu)

from __future__ import print_function
from constraint import Problem, AllDifferentConstraint
import time

def sudoku(initValue):

    p = Problem()

    # Define a variable for each cell: 11,12,13...21,22,23...98,99
    for i in range(1, 10) :
        p.addVariables(range(i*10+1, i*10+10), range(1, 10))

    # Each row has different values
    for i in range(1, 10) :
        p.addConstraint(AllDifferentConstraint(), range(i*10+1, i*10+10))

    # Each colum has different values
    for i in range(1, 10) :
        p.addConstraint(AllDifferentConstraint(), range(10+i, 100+i, 10))

    # Each 3x3 box has different values
    p.addConstraint(AllDifferentConstraint(), [11,12,13,21,22,23,31,32,33])
    p.addConstraint(AllDifferentConstraint(), [41,42,43,51,52,53,61,62,63])
    p.addConstraint(AllDifferentConstraint(), [71,72,73,81,82,83,91,92,93])

    p.addConstraint(AllDifferentConstraint(), [14,15,16,24,25,26,34,35,36])
    p.addConstraint(AllDifferentConstraint(), [44,45,46,54,55,56,64,65,66])
    p.addConstraint(AllDifferentConstraint(), [74,75,76,84,85,86,94,95,96])

    p.addConstraint(AllDifferentConstraint(), [17,18,19,27,28,29,37,38,39])
    p.addConstraint(AllDifferentConstraint(), [47,48,49,57,58,59,67,68,69])
    p.addConstraint(AllDifferentConstraint(), [77,78,79,87,88,89,97,98,99])

    # add unary constraints for cells with initial non-zero values
    for i in range(1, 10) :
        for j in range(1, 10):
            value = initValue[i-1][j-1]
            if value:
                p.addConstraint(lambda var, val=value: var == val, (i*10+j,))

    return p.getSolution()

# some sample problems

easy = [
  [0,9,0,7,0,0,8,6,0],
  [0,3,1,0,0,5,0,2,0],
  [8,0,6,0,0,0,0,0,0],
  [0,0,7,0,5,0,0,0,6],
  [0,0,0,3,0,7,0,0,0],
  [5,0,0,0,1,0,7,0,0],
  [0,0,0,0,0,0,1,0,9],
  [0,2,0,6,0,0,0,5,0],
  [0,5,4,0,0,8,0,7,0]]

hard = [
  [0,0,3,0,0,0,4,0,0],
  [0,0,0,0,7,0,0,0,0],
  [5,0,0,4,0,6,0,0,2],
  [0,0,4,0,0,0,8,0,0],
  [0,9,0,0,3,0,0,2,0],
  [0,0,7,0,0,0,5,0,0],
  [6,0,0,5,0,2,0,0,1],
  [0,0,0,0,9,0,0,0,0],
  [0,0,9,0,0,0,3,0,0]]

very_hard = [
  [0,0,0,0,0,0,0,0,0],
  [0,0,9,0,6,0,3,0,0],
  [0,7,0,3,0,4,0,9,0],
  [0,0,7,2,0,8,6,0,0],
  [0,4,0,0,0,0,0,7,0],
  [0,0,2,1,0,6,5,0,0],
  [0,1,0,9,0,5,0,4,0],
  [0,0,8,0,2,0,7,0,0],
  [0,0,0,0,0,0,0,0,0]]


# http://bit.ly/SmTPOM
extreme = [
  [1,0,0,0,0,0,0,0,9],
  [0,0,9,6,0,3,1,0,0],
  [0,5,0,0,7,0,0,4,0],
  [0,4,0,9,0,6,0,8,0],
  [0,0,6,0,0,0,4,0,0],
  [0,1,0,7,0,4,0,2,0],
  [0,9,0,0,2,0,0,1,0],
  [0,0,1,3,0,5,7,0,0],
  [7,0,0,0,0,0,0,0,3]]

# http://bit.ly/SmTJ9T
worlds_hardest = [
  [8,0,0,0,0,0,0,0,0],
  [0,0,3,6,0,0,0,0,0],
  [0,7,0,0,9,0,2,0,0],
  [0,5,0,0,0,7,0,0,0],
  [0,0,0,0,4,5,7,0,0],
  [0,0,0,1,0,0,0,3,0],
  [0,0,1,0,0,0,0,6,8],
  [0,0,8,5,0,0,0,1,0],
  [0,9,0,0,0,0,4,0,0]]

def print_puzzle(p):
    for row in p:
        for val in row:
            print(val, end=' ')
        print()

def print_solution(s):
    for i in range(1, 10):
        for j in range(1, 10):
            print(s[i*10+j], end=' ')
        print()


def solve_and_print(puzzle):
    print('PUZZLE\n')
    print_puzzle(puzzle)
    start = time.time()    
    s = sudoku(puzzle)
    print('\nSOLUTION in {} sec\n'.format(time.time() - start))
    print_solution(s)
    print()
    
def main():
    for puzzle in [easy, hard, very_hard, extreme, worlds_hardest]:
        solve_and_print(puzzle)
        
if __name__ == "__main__":
    main()
    
