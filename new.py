for line in open("textFiles/vol-4.txt"):
     for word in line.split():
         if word.endswith('ing'):
             print(word)