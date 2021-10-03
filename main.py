"""
Write a program that performs term frequency on its input.

Given this text file of words as input Download this text file of words as 
input, display the 25 most frequent words and their corresponding frequencies,
ordered by decreasing value of frequency (most frequent is first). Make sure
your program normalizes for capitalization (eg "zebra" and "Zebra" both count as
just "zebra"). Also, ignore certain words, which we call stop words, like "the,"
"for", etc. Use this file of stop words Download Use this file of stop words .
Don't worry about the order of words that have equivalent frequencies.

Follow the example requirements in the Prologue of Exercises in Programming
Style Download Prologue of Exercises in Programming Style . Note that the
sections "word index" and "words in context" are extra - you can ignore those
sections. You might find the "Pythonisms" section helpful.

You may use any programming language you wish for this assignment.
"""

def increment_word_frequency(word_frequency_dic, word):
    frequency = word_frequency_dic.get(word)
    if (frequency == None):
        frequency = 0
    word_frequency_dic[word] = frequency + 1

text_file_of_words_name = r"./neuromancer.txt";
file_of_stop_words_name = r"./stop_words.txt";
text_file_of_words = open(text_file_of_words_name)
file_of_stop_words = open(file_of_stop_words_name) 

list_of_stop_words = file_of_stop_words.read()
list_of_text_file_words = text_file_of_words.read()

word_frequency_dic = {} 
for word in list_of_text_file_words.lower().replace('\n','').replace('\t',
        "").replace(",","").replace(".","").replace('\"', "").split(' '):
    word = word.strip()
    if not (word in list_of_stop_words):
       increment_word_frequency(word_frequency_dic, word) 

counter = 1; 
for w in sorted(word_frequency_dic, key=word_frequency_dic.get, reverse=True):
    if (counter > 25):
        break
    print(str(counter) + ')', w, word_frequency_dic[w])
    counter += 1
 
