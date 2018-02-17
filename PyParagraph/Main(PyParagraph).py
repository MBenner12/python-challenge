import re
import os

# open csv 
filename = input("Paragraph_1.txt ")
filepath = os.path.join("raw_data",filename)

# Declare Variables
words = []
word_length = 0
word_count = 0
sentences = []
sentence_count = 0
words_per_sentence = 0
total_letters = 0
paragraph = ""

#Read text and start counting (NEED TO SPLIT)
with open(filepath, 'r', newline="") as text:
    paragraph = text.read()
    words = paragraph.split(" ")
    sentences = re.split("[\.\!\?]\s", paragraph)
    word_count = len(words)
    sentence_count = len(sentences)
    words_per_sentence = word_count/sentence_count

    for character in paragraph:
        if character.isalpha() == True:
            total_letters = total_letters + 1
    
    word_length = total_letters/word_count

# Print Analysis
print("Paragraph Analysis")
print("-----------------")
print(f"Word Count: {word_count}")
print(f"Sentence Count: {sentence_count}")
print(f"Avg Letter Count: {word_length}")
print(f"Avg Sentence Length: {words_per_sentence}")