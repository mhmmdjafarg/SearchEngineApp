import re
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

# pip install nltk
# nltk.download('punkt')
# nltk.download('stopwords')


def removeStopwords(sentence):
    # Lowecase sentence
    sentence = sentence.lower()
    # remove punctuantion
    sentence = removePunctuantion(sentence)
    # Set up list of stopwords
    stop_words = set(stopwords.words('english'))
    # Pisahkan per kata
    word_token = word_tokenize(sentence)
    # Masukkan kedalam array
    filtered_sentence = []
    for word in word_token:
        if word not in stop_words:
            filtered_sentence.append(word)
    return filtered_sentence


# Menghapus punctuation menggunakan module re
def removePunctuantion(sentence):
    sentence = re.sub(r'[^\w\s]', '', str(sentence))
    return sentence


def printdata(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end=" ")
        print()


def word_list_text(w, text):
    for char in '-.,\n':
        text = text.replace(char, ' ')
    text = text.lower()

    word_list = text.split()

    for word in word_list:
        w.append(word)
    return w


def wordlist(w, text):
    for char in '-.,\n':
        text = text.replace(char, ' ')
    text = text.lower()

    word_list = text.split()

    for word in word_list:
        if word not in w:
            w.append(word)
    return w


def word_list_total(string_array):
    w = []

    for text in string_array:
        w = wordlist(w, text)

    return w


def word_count(word, text):
    w = []
    w = word_list_text(w, text)
    count = 0

    for word_in_text in w:
        if word_in_text == word:
            count += 1

    return count


def panjang(a):
    total = 0
    for i in range(len(a)):
        total += a[i]*a[i]
    return total**0.5


def dot_product(v, u):
    # prekondisi : len(v) == len(u)
    result = 0
    for i in range(len(v)):
        result += v[i]*u[i]
    return result


def similarity(v, u):
    return dot_product(v, u)/(panjang(v)*panjang(u))


string_array = ["bolu biru",
                "aku beli bolu biru makan bolu biru", "bolu warna biru"]

word_list = word_list_total(string_array)

print(word_list)

word_data = [[0 for j in range(len(string_array))]
             for i in range(len(word_list))]

for i in range(len(word_list)):
    for j in range(len(string_array)):
        word_data[i][j] = word_count(word_list[i], string_array[j])

printdata(word_data)

query = [word_data[i][0] for i in range(len(word_list))]
ranks = [0 for i in range(len(string_array)-1)]
array_of_sim = [0 for i in range(len(string_array)-1)]

for j in range(1, len(string_array)):
    word_vektor = [word_data[word][j] for word in range(len(word_list))]
    sim = similarity(query, word_vektor)
    idx = j
    for i in range(j):
        if sim > array_of_sim[i]:
            temp = array_of_sim[i]
            array_of_sim[i] = sim
            sim = temp

            temp = ranks[i]
            ranks[i] = j
            j = temp

print(ranks)


def txtToString():
    path = os.path.join(os.getcwd() , 'uploads')
    if os.path.isdir(path):
        listFile = os.listdir(path) #kebentuk array ada nama2 file di uploads
        arrayStringSemua = []
        for i in listFile:
            fileDirectory = os.path.join(path , i)
            f = open(fileDirectory , 'r')
            arrayStringSemua.append(f.read())
        return arrayStringSemua