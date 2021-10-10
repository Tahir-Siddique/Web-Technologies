def max_of_three(a,b,c):
    return max([a,b,c])

def findDivisble(devisibleBy,notMultipleOf,rangeA,rangeB):
    list=[]
    for x in range(rangeA, rangeB):
        if (x%devisibleBy==0) and (x%notMultipleOf!=0):
            list.append(str(x))
    return list

print(f"Maximum Number : {max_of_three(3,4,5)}")
print (f"Divisble by 7 but not multiple of 5 between 1000 and 2000 : {findDivisble(7,5,1000,2000)}")

