locations = ['Georgia', 'Armenia', 'Hungary', 'Italy', 'Germany'] #This code stores the name of 5 countries in a list.
 
print("Original order:") #I print the list in its original order. 
print(locations)
 
print("\nAlphabetical:")#I used sorted() to print the list in alphabetical order without modifying the actual list.
print(sorted(locations))
 
print("\nOriginal order:")#I showed that the list is still in its original order by printing it.
print(locations)
 
print("\nReverse alphabetical:") #I use sorted() to print the list in reverse alphabetical order without changing the order of the original list.
print(sorted(locations, reverse=True))
 
print("\nOriginal order:") #I showed that the list is still in its original order by printing it again.
print(locations)
 
print("\nReversed:")#I used reverse() to change the order of the list.
locations.reverse()
print(locations)#I print the list to show that its order has changed.
 
print("\nOriginal order:")#I used reverse() to change the order of the list again. 
locations.reverse()
print(locations)# I print the list to show it’s back to its original order.
 
print("\nAlphabetical")#I used sort() to change the list so it’s stored in alphabetical order. 
locations.sort()
print(locations)#I print the list to show that its order has been changed.
 
print("\nReverse alphabetical") #I used sort() to change the list so it’s stored in reverse alphabetical order. 
locations.sort(reverse=True)
print(locations)#I print the list to show that its order has changed.




