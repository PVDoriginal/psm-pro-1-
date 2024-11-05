import numpy as np
import json
import re
import checker
import main

with open('data/quotes.json', 'r') as file:
    quotes = json.load(file)

total_quotes = 0
correct_quotes = 0
for person in quotes:
    total_quotes += len(quotes[person])

    for quote in quotes[person]:
        print(quote)
        quote = checker.trimCitat(quote)

        max_teacher = ""
        max_pb = 0

        for teacher in quotes:
            pb = main.calcTeacher(quote, teacher)
            if pb > max_pb:
                max_pb = pb
                max_teacher = teacher

        print(max_teacher)

        if max_teacher == person:
            correct_quotes += 1
            print("OK")
        else:
            print("NO")

print("acuratete: " + str(round(correct_quotes / total_quotes * 100, 2)) + "%")


