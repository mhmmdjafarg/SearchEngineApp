import fungsi
import re

sentence = "Welcome to run on running on server the Class Classes?, and some case Except that quality of life then revive survival welcome and coming throught with the woo."
listword = fungsi.removeStopwords(sentence)

# text = fungsi.stemming(listword)
# print(text)


tes = fungsi.getFirstSentence(sentence)
print(tes)