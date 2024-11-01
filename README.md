# Initial probabilities

The initial probabilites are computed from a JSON file containing a list of quotes from each person.

For instance, a sample example would be: 

![image](https://github.com/user-attachments/assets/fc834016-682a-415a-99c4-e4c6545b85d0)


They are saved in another JSON file, with the following format:

- The file is divided in 2 subsections, 'words' and 'people'. 
- In the 'words' section, you can find a list of every word used in the collected data. Each word has a 'total' value, the probability of getting this word when picking a random one (P(word)), and then a field for each different person that used it, containing the probability of that word belonging to that person (P(person | word)).

![image](https://github.com/user-attachments/assets/15e181df-a5d7-4f1e-9729-bb5f32b8f4f8)

- In the 'people' section, you can find a list containing all the people. Each one has a 'total' value, the probability of a random quote belonging to that person (P(person)), and then a field for each different word that person has used, containing the probaiblity of picking that word when selecting a random word written by that person (P(word | person))

![image](https://github.com/user-attachments/assets/fa9a2849-d36f-4b4f-bbb1-87374d90baf9)

 
