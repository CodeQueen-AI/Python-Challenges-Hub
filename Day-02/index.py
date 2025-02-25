#Day-2 Challenge
user_input = input("Enter a Sentence: ")
words = user_input.split()
words_count = len(words)
print("Number of words in the sentence: ", words_count)

#Bonus Challenge
words = user_input.split()
reverse_text = words.reverse()
reverse_text = ' '.join(words)
print("Reverse of the sentence: ", reverse_text)
