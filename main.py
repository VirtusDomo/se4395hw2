#   Created by: James Anyabine
#   Homework 2: Word Guessing Game
#   Class: CS 4395 HLT
#   Professor: Dr. Karen Mazidi
#

import os
import sys
import re
import math
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from itertools import chain
from random import seed
from random import randint


def reader(filepath):
    #print("\nUsing method 1")
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        # text_in = f.read()
        lines = [line for line in f.readlines()]
    return lines

#Part 2
def lexdivide(lines):
    unique = set()
    tokens = [[l.lower() for l in sublines] for sublines in lines]
    for list in lines:
        for item in list:
            unique.add(item)
    diversity = float(len(unique))/float(len(tokens))
    #print(len(unique), len(tokens))
    formal = '{:.2f}'.format(diversity)
    return formal

#Step 3
def stopAndToken(lines):
    stop_words = set(stopwords.words('english'))
    words_filtered = []
    #Step A
    for line in lines:
        tokens = word_tokenize(line)
        #print(tokens)
        words_filtered.append([x.lower() for x in tokens if x not in stop_words if len(x) > 5 if x.isalpha()])
    #Step B
    wnl = WordNetLemmatizer()
    lemmas = []
    unilem = []
    for line in words_filtered:
        lemmas.append([wnl.lemmatize(t) for t in line])
    for line in lemmas:
        unilem.append(set([x for x in line]))
    unifinal = list(set(chain.from_iterable(unilem)))
    #Step C
    tags = nltk.pos_tag(unifinal)
    nouns = []
    for token, pos in tags:
        if pos == 'NN':
            nouns.append(token)
    #print(poslist)
    print('tokens:', len(words_filtered))
    print('nouns:', len(nouns))

    return words_filtered, nouns

#Part 4
def dictSorter(tokens, nouns):
    nounCnt = {}
    for line in tokens:
        for word in line:
            if word in nouns and word not in nounCnt:
                nounCnt[word] = 1
            elif word in nouns:
                nounCnt[word] += 1

    n = 0
    common = []
    for nouns in sorted(nounCnt, key=nounCnt.get, reverse=True):
        if n >= 50:
            break
        print(nouns, ':', nounCnt[nouns])
        common.append(nouns)
        n += 1
    return common

#Part 5
def guessing(gamewords):
    seed(1234)
    letter = ''
    print("Let's play a word guessing game!")
    def runner():
        user = 5
        test = True
        n = len(gamewords)
        term = []
        letter = ''

        randval = randint(0, n - 1)
        word = gamewords[randval]
        # print _ for length of word
        for i in range(len(word)):
            term.append('_')
        # ask for input of a letter
        print(term)

        while test:
            if user < 0 or letter == '!':
                test = False
                print('Sorry, your word was', word)
                break
            letter = input("Guess a letter:")
            #if letter in word, print Right! and fill matching _ term areas then add point to user
            if letter in word:
                indexes = [m.start() for m in re.finditer(letter, word)]
                for index in indexes:
                    term[index] = letter
                print('Right!')
                print(term)
                user += 1
                print("Score:", user)
            else:
                user -= 1
                print('Sorry, guess again.')
                print(term)
                print("Score:", user)

            if term == word:
                print('You solved it!')
                print()
                print('Guess another word')
                runner()
    runner()

    return 0


def main():
    if len(sys.argv) > 1:
        rp = sys.argv[1]
        listed = reader(rp)
        div = lexdivide(listed)
        tokens, nouns = stopAndToken(listed)
        gameWords = dictSorter(tokens, nouns)
        guessing(gameWords)
    else:
        print('Error, insufficient path please retry.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


