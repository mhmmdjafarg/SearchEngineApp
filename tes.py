from nltk.util import pr, print_string
import fungsi
import re

sentence = "Welcome to run on running on server the Class Classes?, and some case Except that quality of life then revive survival welcome and coming throught with the woo."
sentence = fungsi.removePunctuantion(sentence)
print(sentence)



listword = fungsi.removeStopwords(sentence)
print(listword)
stem = fungsi.stemming(listword)
print(stem)