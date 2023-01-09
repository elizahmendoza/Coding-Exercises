glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
 
word = 'string'
print(f"\n{word.title()}: {glossary[word]}"),
 
word = 'comment'
print(f"\n{word.title()}: {glossary[word]}"),
 
word = 'list'
print(f"\n{word.title()}: {glossary[word]}"),
 
word = 'loop'
print(f"\n{word.title()}: {glossary[word]}"),
 
word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}"),

#This programme is called a glossary.
#I used 5 programming words I learned  in the previous chapters. I used those words as the keys in my glossary, and stored their meanings as values.
#I printed the words followed by a colon and then its meaning. I used the newline character (\n) to insert a blank line between each word-meaning pair in my output.    