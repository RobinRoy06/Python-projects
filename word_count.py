with open("lorem.txt","r") as file:
    words = file.read().split()

word_count = len(words)

print("There are ", word_count , "in the file")
