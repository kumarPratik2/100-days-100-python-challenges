#opens the file 
Text = open('Sample.txt')

#reads the file and stores its contents in 'x' variable as string
x = Text.read()

#splits 'x' string into individual words and stores it as list in words
words = x.split()

#prints the length of 'words' list
print(f'Total number of words in the given text: {len(words)}')

#closes the file
Text.close()