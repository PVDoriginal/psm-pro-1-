import numpy as np
import json
import re

with open('data/quotes.json', 'r') as file:
    quotes = json.load(file)

data = dict()  # final data
data['words'] = dict()  # probabilities on each word
data['people'] = dict()  # probabilities on each person

total_quotes = 0
total_words = 0

def trimCitat(s):
    for punctuation in '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~''':
        s = s.replace(punctuation, ' ')

    for number in "0123456789":
        s = s.replace(number, ' ')
        
    return s

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

with open('data/data.json', 'w') as file:
    json.dump(data, file, indent=4)
    
def calcTeacher(citat,teacher):
    multiplication = 1
    
    for word in citat.split():
        #don't consider words not in our database
        if word not in data['words'].keys():
            continue
        
        #don't count words not said by teacher
        if teacher not in data['words'][word]:
            continue
        
        prob_not = 1 - data['words'][word][teacher]
        
        if prob_not > 0:
            multiplication *= prob_not
    
    return 1 - multiplication
        
def main():
    citat_nou = input()
    citat_nou = trimCitat(citat_nou)
    
    for teacher in data['people'].keys():
        print(teacher, end=": ")
        print(calcTeacher(citat_nou,teacher))
    

if __name__=="__main__":
    main()

