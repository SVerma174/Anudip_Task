'''1. Write a Python program to Get Only unique items from two sets.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}'''

# Take input for set1
set1=set(map(int,input("Enter the number separated by space : ").split()))
# Take input for set2
set2=set(map(int,input("Enter the number separated by space : ").split()))

#Geting Only unique items from two sets
unique_items=(set1-set2).union(set2-set1)
# printing the unique item 
print("Unique items of the both the set are :",unique_items)



