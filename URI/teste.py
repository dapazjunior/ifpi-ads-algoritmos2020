
#Exercise 9.3
fin = open('words.txt')

def avoids(word,letter):
    for char in word:
        if char in letter:
            return False
    return True

letter = raw_input('What letters to exclude? ')
count = 0
for line in fin:
    word = line.strip()
    if avoids(word, letter):
        count += 1
        print(word)

percent = (count / 113809.0) * 100

print (str(percent)) + "% of the words don't have " + letter + '.'