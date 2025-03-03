#Write a Python program that takes a sentence from the user and counts the number of words in it!
sentence = input("Enter a sentence: ")  
word_count = len(sentence.split()) 
print(f"The total number of words is: {word_count}")

#Bonus Challenge
# Write a Python program that takes a sentence as input and reverses the entire sentence.
sentence = input("Enter a sentence: ")  
reversed_sentence = ' '.join(sentence.split()[::-1])  
print("Reversed sentence:", reversed_sentence)
