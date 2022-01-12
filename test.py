
import nltk
import os
import nltk.corpus
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.util import bigrams, ngrams, trigrams
from nltk.stem import PorterStemmer
from nltk import ne_chunk
import numpy 
import sqlite3

# AI='this is a string used for testing'
# AI_tokens= word_tokenize(AI)
#
string='It seems as if everything he touches turns to gold'
quotes_token = nltk.word_tokenize(string)
print(quotes_token)

quotes_bigrams=list(nltk.bigrams(quotes_token))
print(quotes_bigrams)
#
# quotes_ngrams=list(nltk.ngrams(quotes_token, 4))
#
list(nltk.bigrams
print(pst.stem('having'))
#
NE_sent = "Pedro sleeps in bed all day"
NE_tokenize = word_tokenize(NE_sent)
NE_tags = nltk.pos_tag(NE_tokenize)
NE_NER = ne_chunk(NE_tags)
print(NE_NER)

# con = sqlite3.connect('unknown.db')
# c = con.cursor()
# # c.execute('CREATE TABLE names (first_names TEXT)')
# file= open('names.txt')
# file_data= file.readlines()
# for item in file_data:
#     item=item.strip()
#     query="INSERT INTO names (first_names) values ('" + item + "')"
#     c.execute(query)
#     con.commit()
#     print(item)
# print("Table finished")

NE_sent = "Francesca sleeps in bed all day"
NE_tokenize = word_tokenize(NE_sent)
NE_tags = nltk.pos_tag(NE_tokenize)
for (word, tag) in NE_tags:
    if tag == 'NNP':
        potential_name= word
        con = sqlite3.connect('unknown.db')
        cur = con.cursor()
        query="SELECT * FROM names WHERE first_names='" + str(potential_name) + "'"
        cur.execute(query)
        rows = cur.fetchone()
        print(rows[0])

NE_sent = "water is gay and i am a big gay boy"
NE_tokenize = word_tokenize(NE_sent)
NE_tags = nltk.pos_tag(NE_tokenize)
print(NE_tags)
quotes_ngrams=list(nltk.ngrams(NE_tokenize, 4))
print(quotes_ngrams)
#print(quotes_ngrams)
# con = sqlite3.connect('unknown.db')
# cur = con.cursor()
# cur.execute("SELECT * FROM names")
# rows = cur.fetchall()
# print(rows)

# con = sqlite3.connect('unknown.db')
# cur = con.cursor()
# cur.execute("DROP TABLE names;")
# print("Table dropped")

Sent from Mail for Windows

