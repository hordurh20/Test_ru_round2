#Algorithm for the sequence:
   # 1,2,3,6,11,20,37 ...

    #It starts with 1.
    #Then 2
    #Then 3 (0+1+2)
    #Then 6 (1+2+3)
    #Then 11 (2+3+6)
    #Then 20 (3+6+11)
    #Then 37 (6+11+20)

#So the sequence is the sum of the previous three numbers.

n = int(input("Enter the length of the sequence: ")) # Do not change this line

stabilizer = 0
stab_1 = 0
one = 1
for x in range(1, n+1):
    x = stabilizer + stab_1 + one
    stabilizer = stabilizer + stab_1
    stab_1 = stab_1 + one
    print(x)
