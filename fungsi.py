import re
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

# pip install nltk
# nltk.download('punkt')
# nltk.download('stopwords')

# Menerima string dari text
# F.S String sudah murni siap untuk diolah (sudah di stem, remove stopword, remove punctuation)
def ProcessString(text):
    text = removePunctuantion(text)
    list_word = removeStopwords(text)
    list_word = stemming(list_word)
    return list_word


# dilakukan ProcessString ke semua text pada array of text
def ProcessAllString(array_of_text):
    array_of_array_of_words = []

    for text in array_of_text:
        array_of_array_of_words.append(ProcessString(text))

    return array_of_array_of_words


# Mengembalikan kaliamt pertama atau maximal 50 char
# Menerima input string dari full text
# Kekurangan mungkin kalau input berupa format html akan kesulitan
def getFirstSentence(text):
    EndSentece = ".!?:;"
    countChar = 0
    firstSentence = ""
    for char in text:
        firstSentence += char
        countChar += 1
        if char in EndSentece:
            break
        if countChar > 70 and char == ' ':
            firstSentence += "...."
            break
    return firstSentence


# Menerima input berupa array of string yang 
# I.S sudah dihilangkan stopword dan punctuationnya
def stemming(text):
    # Create a Snowball stemmer 
    stemmer = SnowballStemmer('english')
    stemmed_text = []
    for word in text:
        stemmed_text.append(stemmer.stem(word))
    return stemmed_text


# Return array of stringg yang sudah diremove stopwords dan lowercase
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
# Mengembalikan string
def removePunctuantion(sentence):
    sentence = re.sub(r'[^\w\s]', '', str(sentence))
    return sentence


# Menampilkan total data banyaknya kata
# indeks baris untuk kata indeks kolom untuk 
# contoh : data[2][2] artinya banyaknya kata ke-i=2 di dokumen 2 
def printdata(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end=" ")
        print()


# worded_text adalah sebuah text yang sudah menjadi pecahan word2.
# setiap kata akan diperiksa, 
# jika sudah ada di array w maka tidak akan di masukkan ke array
# jika belum ada maka akan dimasukkan
def wordlist(w, array_of_words):

    for word in array_of_words:
        if word not in w:
            w.append(word)
    return w


# list semua word yang muncul di semua dokumen
def word_list_total(array_of_array_of_words):
    # inisiasi w dengan array kosong
    w = []

    # setiap dokumen akan dilakukan fungsi wordlist
    for array_of_words in array_of_array_of_words:
        w = wordlist(w, array_of_words)

    return w


# Menghitung banyaknya kata word di dalam dokumen text.
# word adalah kata yang ingin dicari banyaknya pada array_of_words.
def word_count(word, array_of_words):
    # inisiasi count dengan 0
    count = 0
    # pengecekan semua kata pada text.
    # jika kata pada text (word_in_text) merupakan 
    # kata yang ingin dicari banyaknya (word),
    # maka count naik. 
    for word_in_text in array_of_words:
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


string_array = ["blue cake",
                "i want blue cake, and he wants cake of blue", "blue colored cake"]

array_of_array_of_words = ProcessAllString(string_array)

word_list = word_list_total(array_of_array_of_words)

print(array_of_array_of_words)
print(word_list)

word_data = [[0 for j in range(len(array_of_array_of_words))]
             for i in range(len(word_list))]

for i in range(len(word_list)):
    for j in range(len(array_of_array_of_words)):
        word_data[i][j] = word_count(word_list[i], array_of_array_of_words[j])

printdata(word_data)

query = [word_data[i][0] for i in range(len(word_list))]
ranks = [0 for i in range(len(array_of_array_of_words)-1)]
array_of_sim = [0 for i in range(len(array_of_array_of_words)-1)]

for j in range(1, len(array_of_array_of_words)):
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
            f.close()
        return arrayStringSemua