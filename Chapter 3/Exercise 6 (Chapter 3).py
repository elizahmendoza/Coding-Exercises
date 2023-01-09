guests = ['Diana Spencer', 'Marilyn Monroe', 'Audrey Hepburn']
 
name = guests[0].title()
print(f"{name}, please come to dinner.")
 
name = guests[1].title()
print(f"{name}, please come to dinner.")
 
name = guests[2].title()
print(f"{name}, please come to dinner.")
 
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
 
# Marilyn can't make it! Let's invite Michael instead.
del(guests[1])
guests.insert(1, 'Michael Jackson')
 
# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
 
name = guests[1].title()
print(f"{name}, please come to dinner.")
 
name = guests[2].title()
print(f"{name}, please come to dinner.")
 
# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'Frida Kahlo')
guests.insert(2, 'Leonardo Da Vinci')
guests.append('Whitney Houston')
 
name = guests[0].title()
print(f"{name}, please come to dinner.")
 
name = guests[1].title()
print(f"{name}, please come to dinner.")
 
name = guests[2].title()
print(f"{name}, please come to dinner.")
 
name = guests[3].title()
print(f"{name}, please come to dinner.")
 
name = guests[4].title()
print(f"{name}, please come to dinner.")
 
name = guests[5].title()
print(f"{name}, please come to dinner.")
 
# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")
 
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")
 
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")
 
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")
 
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")
 
# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")
 
name = guests[1].title()
print(f"{name}, please come to dinner.")
 
# Empty out the list.
del(guests[0])
del(guests[0])
 
# Prove the list is empty.
print(guests)

#I started with the program from Exercise 3-5. I added a new line that prints a message saying that I can invite only two people for dinner.
#I used pop() to remove guests from the list one at a time until only two names remain in the list. 
#Each time a name is popped from the list, a message is printed to that person letting them know that I'm sorry I can’t invite them to dinner.
#I print a message to each of the two people still on the list, letting them know they’re still invited.
#I used the 'del' function to remove the last two names from the list, so now it's empty. 
# I print the list to make sure the list is empty at the end of the program.    