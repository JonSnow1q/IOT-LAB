print("Enter a sentence ")
sentence = input()
words = sentence.split()
word_count = 0
character_count = 0
for word in words:
    word_count += 1
    character_count += len(word)
print("Total Numbers of Words in the sentence are : ",word_count)
print("Total Numbers of characters in the sentence excluding spaces are : ",character_count)
print("Total Numbers of characters in the sentence including spaces are :",character_count+word_count-1)
