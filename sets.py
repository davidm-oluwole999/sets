#create a set
my_set= {1,2,3,4,5}
print(my_set)

# add an item to a set, no duplicate values
my_set.add(6)
print(my_set)

#remove item from set
my_set.remove(3)
print(my_set)

#check for an item in a set
if 3 in my_set:
    print(my_set)

# union operation (combine two sets)
set1= {1,2,3}
set2= {3,4,5}
result= set1 | set2
print (result)

#intersections (common items between sets)
result1= set1 & set2
print(result1)