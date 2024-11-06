import numpy as np
import json
import re
import checker

with open('data/data.json', 'r') as file:
    data = json.load(file)
    
def calcTeacher(citat,teacher):
    multiplication = 1
    
    for word in citat.split():
        word = word.lower()
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
    
    print("Introduceti un citat: ", end = "")
    citat_nou = input()
    while(citat_nou != "-1"):
        citat_nou = checker.trimCitat(citat_nou)
        
        solutions = []
        
        for teacher in data['people'].keys():
            chance = calcTeacher(citat_nou,teacher)
            solutions.append([teacher,chance])
            
        solutions = sorted(solutions, key = lambda x : -x[1])
        
        print("")

        if solutions[0][1] == 0:
            print("Cel mai probabil, citatul a fost zis de: Nimeni :(")
        else:
            print("Cel mai probabil, citatul a fost zis de: ", solutions[0][0])
            print("")

        for i in range(len(solutions)):
            print(solutions[i][0], end=": ")
            print(str(round(solutions[i][1] * 100, 2)) + "%")
        
        print("Introduceti un citat: ", end ="")
        citat_nou = input()

    

if __name__=="__main__":
    main()

