#2. Napisz program, który wyświetli plan wycieczki – wybierając losowo z listy 10 największych miast w Polsce miasta do odwiedzenia.
# Miast ma być 10, nie mogą się powtarzać.
import random
# miasta zostaly wybrane do innej tablicy ktora nie zawiera powtorzen
miasta = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań',
          'Gdańsk', 'Szczecin', 'Warszawa', 'Lublin', 'Katowice',
          'Białystok', 'Gdynia', 'Częstochowa', 'Warszawa', 'Sosnowiec',
          'Kielce', 'Warszawa', 'Warszawa', 'Rzeszów', 'Zabrze']

wszystkiezpowtorzeniami = set(miasta)
unikalne =list(wszystkiezpowtorzeniami)
plan_wycieczki=random.sample(unikalne,10)
#print(plan_wycieczki)


print("Plan wycieczki:")
for i, miasto in enumerate(plan_wycieczki):
    print("{0}. {1}".format(i+1, miasto))