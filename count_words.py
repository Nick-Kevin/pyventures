"""
    This program counts words in a text
"""
import re

# this pattern indetifies whole words and a combination of letters and numbers
PATTERN = r"\b\w[a-zA-Z]+|[a-zA-Z]\w+\b|[a-zA-Z]"

print("Tape or paste your text !")
text = input()
words_list = re.findall(PATTERN, text)
word_count = len(words_list)

print("There are " + str(word_count) + " words in your text.")
