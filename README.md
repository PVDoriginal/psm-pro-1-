# Utilizare!

Se poate rula scriptul [main.py](https://github.com/PVDoriginal/psm-pro-1-/blob/main/psm_proj1/main.py), iar dupa la introducerea unui mesaj va calcula probabilitatile ca acesta sa fie scris de fiecare prof in parte!

![image](https://github.com/user-attachments/assets/bb7d79a0-1cf9-4655-9a20-f79f72416920)

# Citate!

Script-ul [checker.py](https://github.com/PVDoriginal/psm-pro-1-/blob/main/psm_proj1/checker.py) primeste un [fisier json](https://github.com/PVDoriginal/psm-pro-1-/blob/main/psm_proj1/data/quotes.json) ce contine o lista de profi si cateva zeci de citate / mesaje de la fiecare. Unele sunt copiate de pe Teams, majoritatea sunt luate din timpul cursurilor. 

![image](https://github.com/user-attachments/assets/9cf8ed54-b95b-4f25-99d9-e4a79555d0da)

# Probabilitati (partea lui Vlad)!


[Checker.py](https://github.com/PVDoriginal/psm-pro-1-/blob/main/psm_proj1/checker.py) parseaza lista citatelor, le separa in cuvinte si scrie in [data.json](https://github.com/PVDoriginal/psm-pro-1-/blob/main/psm_proj1/data/data.json) urmatoarele probabilitati: 

- Pentru fiecare cuvant, **P(cuvant)** (numit total)
- Pentru fiecare cuvant, si ficare prof care l-a spus, **P(cuvant | prof)**
- Mai este adaugat si campul **none**, mai multe detalii la final

![image](https://github.com/user-attachments/assets/ea363a33-e9dd-4086-89ec-ad1c6d62377d)

- Pentru fiecare prof, **P(prof)** (numit iar total)
- Pentru fiecare prof, si fiecare cuvant pe care l-a spus, **P(prof | cuvant)**

![image](https://github.com/user-attachments/assets/cf3a3a47-d537-4637-a05f-7ecf6fa0c8d0)

# Formule 😵

Formula urmatoare sta la baza proiectului. Este derivata din formula lui Bayes.. probabil. Pentru mai multe detalii vorbiti cu Mihai Duzi. 

![WhatsApp Image 2024-11-05 at 16 23 19_8965ae61](https://github.com/user-attachments/assets/8a61e154-db64-40ab-a06e-e8fbeb521720)
![image](https://github.com/user-attachments/assets/4a914817-dcc2-43ba-8a9a-76a2aadc4806)

(Implementarea algoritmului de mai sus, cat si a tot ce este in [main.py](https://github.com/PVDoriginal/psm-pro-1-/blob/main/psm_proj1/main.py), este realizata de Matei Pescariu)  

# Acuratete:

Prin rularea scriptului [self_evaluate](https://github.com/PVDoriginal/psm-pro-1-/blob/main/psm_proj1/self-evaluate.py), se va trece [fiecare citat](https://github.com/PVDoriginal/psm-pro-1-/blob/main/psm_proj1/data/quotes.json) prin algoritmul din [main.py](https://github.com/PVDoriginal/psm-pro-1-/blob/main/psm_proj1/main.py), verificandu-se daca proful returnat ca fiind cel mai probabil este intradevar cel ce a spus citatul. La final se afiseaza procentul de acuratete obtinut: 

![image](https://github.com/user-attachments/assets/6f9f2d21-9ac0-4de2-af0c-9c92757a6885)


# Artificiu de calcul: None

O problema foarte grava ce apare in calculul probabilitatilor este cazul in care un cuvant a fost zis de un singur prof. Atunci P(cuvant | prof) va fi 100%, iar, in functie de formula, va interpreta ca orice mesaj ce contine cuvantul respectiv este sigur scris de proful ala. 

O solutie ar fi sa nu consideram cuvintele de genul. Dar atunci, e posibil ca algoritmul sa 'subestimeze' contributia unui prof la un anumit citat, pentru ca e format in mare parte din cuvinte specifice lui. De exemplu:

![WhatsApp Image 2024-11-05 at 19 36 51_8b3425cc](https://github.com/user-attachments/assets/d4a7c767-11ed-4608-946e-872491755170)

Cel mai bun artificiu pe care l-am gasit a fost sa adaugam la fiecare fiecare cuvant o sansa de 5% sa nu-l fi zis nimeni. Astfel, sansa ca un cuvant de tipul asta sa apartina profului care l-a zis este doar de 95%, in loc de 100%:

![image](https://github.com/user-attachments/assets/3e5d5edb-61b2-4662-8959-dec4e6c688b8)

![image](https://github.com/user-attachments/assets/ab45766e-a1d4-4f56-8b54-a897e4f0bd28)



 


