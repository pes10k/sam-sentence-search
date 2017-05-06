#!/usr/bin/env python3
import os
import re
import pickle
import sys
import pprint
import nltk.data

def coallence_whitespace(text: str) -> str:
    return re.sub('\s\s*', ' ', text, flags=re.U)

sent_detector = nltk.data.load('nltk_data/tokenizers/punkt/english.pickle')
sentence_set = set()

for a_book in os.listdir("corpus"):
    print("processing: ", a_book)
    book_bytes = open(os.path.join("corpus", a_book), 'rb').read()
    book_text = book_bytes.decode('utf8', errors='ignore')
    preprocessed_text = coallence_whitespace(book_text)
    preprocessed_text = re.sub(r'\[.*?\]', '', book_text, flags=re.U | re.M)
    sentences = sent_detector.tokenize(preprocessed_text)
    for sentence in sentences:
        sentence_set.add(coallence_whitespace(sentence))

with open('corpus.pickle', 'wb') as handle:
    pickle.dump(sentence_set, handle)
