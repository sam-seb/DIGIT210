import nltk
import matplotlib
import matplotlib.pyplot as plt
import os

f = open("textFiles/vol-4.txt")
raw = f.read()
# ebb: Now you need to tokenize your text so NLTK can process it in bitty pieces

splitEmUp = raw.split()
print(f"splitEmUp = {splitEmUp[-100:]}")
# We need to make a special NLTK "Text Object" of this
# so you can use NLTK functions like concordance on it.
op = nltk.Text(splitEmUp)

concordance = op.concordance("")
print(concordance)



