import fungsi

sentence = "Welcome to run on running on server the Class Classes\n"
listword = fungsi.removeStopwords(sentence)

text = fungsi.stemming(listword)
print(text)