#!/usr/bin/python3

# map coloring 

from __future__ import print_function
from constraint import Problem

def color (map, colors=['red','green','blue']):
    (vars, adjoins) = parse_map(map)
    p = Problem()
    p.addVariables(vars, colors)
    for (v1, v2) in adjoins:
        p.addConstraint(NEQ, [v1, v2])
    solution = p.getSolution()
    if solution:
        for v in sorted(vars):
            print("{}:{} ".format(v, solution[v]), end='')
        print()
    else:
        print('No solution found :-(')

def parse_map(neighbors):
    """Given a string like 'X:Y Z; Y:Z' returns a tuple of regions and
    adjoining pairs.  The syntax is a region name followed by ':'
    followed by 0 or more region names, followed by ';', repeated for
    each region.  Given 'X: Y' you don't need 'Y: X'.  Example:
      >>> parse_map('X:Y Z; Y:Z') 
      ([X,Y,Z], [(X,Y),(Y,X),(X,Z),(Z,X),(Y,Z),(Z,Y)])
    """
    adjoins = []
    regions = set()
    specs = [spec.split(':') for spec in neighbors.split(';')]
    for (A, Aneighbors) in specs:
        A = A.strip();
        regions.add(A)
        for B in Aneighbors.split():
            regions.add(B)
            adjoins.append((A,B))
    return (list(regions), adjoins)

def NEQ (x, y):
    """ Function for the not equal operator """
    return x != y

# two example problems from russell and norvig

australia = "SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: "
    
usa = """WA: OR ID; OR: ID NV CA; CA: NV AZ; NV: ID UT AZ; ID: MT WY UT;
         UT: WY CO AZ; MT: ND SD WY; WY: SD NE CO; CO: NE KA OK NM; NM: OK TX;
         ND: MN SD; SD: MN IA NE; NE: IA MO KA; KA: MO OK; OK: MO AR TX;
         TX: AR LA; MN: WI IA; IA: WI IL MO; MO: IL KY TN AR; AR: MS TN LA;
         LA: MS; WI: MI IL; IL: IN; IN: KY; MS: TN AL; AL: TN GA FL; MI: OH;
         OH: PA WV KY; KY: WV VA TN; TN: VA NC GA; GA: NC SC FL;
         PA: NY NJ DE MD WV; WV: MD VA; VA: MD DC NC; NC: SC; NY: VT MA CA NJ;
         NJ: DE; DE: MD; MD: DC; VT: NH MA; MA: NH RI CT; CT: RI; ME: NH;
         HI: ; AK: """

if __name__ == "__main__":
    print('AUSTRALIA in three colors')
    color(australia)
    print()
    print('USA in three colors')
    color(usa)
    print()
    print('USA in four colors')
    color(usa, colors=['red', 'green', 'blue', 'yellow'])

