import numpy as np
import json
import re

def trimCitat(s):
    for punctuation in '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~''':
        s = s.replace(punctuation, ' ')

    for number in "0123456789":
        s = s.replace(number, ' ')
        
    return s

def processInput():
    with open('data/quotes.json', 'r') as file:
        quotes = json.load(file)

    data = dict()  # final data
    data['words'] = dict()  # probabilities on each word
    data['people'] = dict()  # probabilities on each person

    total_quotes = 0
    total_words = 0

    for person in quotes:

        data['people'][person] = dict()
        data['people'][person]['total'] = len(quotes[person])
        data['people'][person].setdefault('total_words', 0)

        for quote in quotes[person]:
            total_quotes += 1
            s = quote
            
            s = trimCitat(s)
            
            for word in s.split():
                word = word.lower()
                total_words += 1
                data['words'].setdefault(word, dict())
                data['words'][word].setdefault('total', 0)

                data['words'][word].setdefault(person, 0)

                data['words'][word]["total"] += 1
                data['words'][word][person] += 1

                data['people'][person].setdefault(word, 0)
                data['people'][person][word] += 1

                data['people'][person]['total_words'] += 1

    # Percentage of times words said by a person. Percentage of total words
    for word in data['words']:
        for person in data['words'][word]:
            if person == 'total':
                continue

            data['words'][word][person] = round(data['words'][word][person] / data['words'][word]['total'], 4)

        data['words'][word]['total'] = round(data['words'][word]['total'] / total_words, 4)

    for person in data['people']:
        for word in data['people'][person]:
            if word == 'total' or word == 'total_words':
                continue

            data['people'][person][word] = round(data['people'][person][word] / data['people'][person]['total_words'], 4)

        data['people'][person]['total'] = round(data['people'][person]['total'] / total_quotes, 4)
        
    print("read and processed")
    return data

def writeInput(data):
    with open('data/data.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Updated JSON")

def main():
    data = processInput()
    writeInput(data)

if __name__=="__main__":
    main()