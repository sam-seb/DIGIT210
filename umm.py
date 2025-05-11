import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

filepath4 = 'source/vol-4.txt'
f = open(filepath4, 'r', encoding='utf8').read()
filepath5 = 'source/vol-5.txt'
g = open(filepath5, 'r', encoding='utf8').read()
# Make a list of tokens in your text.
# tokenList = f.split()
tokenList4 = word_tokenize(f)
tokenList5 = word_tokenize(g)
# How is NLTK's word_tokenize() different from just splitting on spaces? Here's an example of how it's different:
# Look for "don't" in the output of this cell and see how it's split.
print(tokenList4)
print(tokenList5)

# Reduce the complexity by: 1) lowercasing them, and 2) returning the set() of words (remove multiple of the same value)
lowercaseTokens4 = [token.lower() for token in tokenList4]
uniqueTokens4 = set(lowercaseTokens4)
print(uniqueTokens4)

lowercaseTokens5 = [token.lower() for token in tokenList5]
uniqueTokens5 = set(lowercaseTokens5)
print(uniqueTokens5)


nltk.help.upenn_tagset('NNS')

POStagged4 = pos_tag(uniqueTokens4)
POStagged5 = pos_tag(uniqueTokens5)
tagsIwant = ['VB', 'VBZ', 'ADJ', 'NOUN', 'VERB']
# This is a Python list comprehension that'll help us with our list of tuples [(word, tag), (word, tag), ...]
shortList4 = [word for word, NOUN in POStagged4 if NOUN in tagsIwant]
print(len(shortList4))
print(shortList4)

shortList5 = [word for word, VERB in POStagged5 if VERB in tagsIwant]
print(len(shortList5))
print(shortList5)
