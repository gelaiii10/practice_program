#ask the user to input a complete statement
statement = input("Please enter a complete statement: ")
words = statement.split() #split the statement into words
#count the number of words
word_count = len(words)
print(word_count) #print the number of word