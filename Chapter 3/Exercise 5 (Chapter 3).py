guests = ['Diana Spencer', 'Marilyn Monroe', 'Audrey Hepburn']
 
name = guests[0].title()
print(f"{name}, please come to dinner.")
 
name = guests[1].title()
print(f"{name}, please come to dinner.")
 
name = guests[2].title()
print(f"{name}, please come to dinner.")
 
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
 
# Jack can't make it! Let's invite Michael instead.
del(guests[1])
guests.insert(1, 'Michael Jackson')
 
# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
 
name = guests[1].title()
print(f"{name}, please come to dinner.")
 
name = guests[2].title()
print(f"{name}, please come to dinner.")

#I started with the program from Exercise 3-4 and then added a print() call at the end of the programme stating the name of the guest who can’t make it.
#I modified the list, replacing the name of the guest who can’t make it with the name of the new person I am inviting.
#I then printed a second set of invitation messages, one for each person who is still in the list.