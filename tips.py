import math

# Definim o functie pentru a calcula costul per persoana, rotunjit in sus.
def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

# Definim o functie care calculeaza costul cu tips si costul per persoana cu tips.
def calculate_with_tips(total, number_of_people, tip_percent):
    tip_amount = total * (tip_percent / 100)  # Calculam suma pentru tips.
    total_with_tips = total + tip_amount  # Adaugam tips la suma totala.
    cost_per_person = math.ceil(total_with_tips / number_of_people)  # Calculam costul per persoana cu tips.
    return total_with_tips, cost_per_person  # Returnam suma totala cu tips si costul per persoana cu tips.

while True:
    try:
        total_due = float(input("Introduceți suma totală: "))  # Citim suma totala.
        if not isinstance(total_due, (int, float)):
            raise ValueError("Totalul introdus nu este un număr valid")  # Ridicam o exceptie daca suma introdusa nu este un numar valid.
        number_of_people = int(input("Introduceți numărul de persoane: "))  # Citim numarul de persoane.
        if number_of_people <= 1:
            raise ValueError("Nota nu se poate imparti la o singura persoana")  # Ridicam o exceptie daca numarul de persoane este mai mic sau egal cu 1.
    except ValueError as err:
        print("Nu este o valoare bună, mai încercați o dată.")  # Afisam un mesaj de eroare.
        print("({})".format(err))  # Afisam mesajul de eroare specific exceptiei.
        continue  # Continuăm bucla pentru a relua introducerea datelor corecte

    # Dacă am ajuns aici, datele sunt corecte și ieșim din bucla
    break

amount_due = split_check(total_due, number_of_people)  # Calculam costul per persoana.

print("Opțiuni pentru tips (în procente):")
print("1. 5%")
print("2. 10%")
print("3. 15%")
print("4. 20%")

tip_option = int(input("Alegeți opțiunea de tips (1/2/3/4): ")

if tip_option == 1:
    tip_percent = 5
elif tip_option == 2:
    tip_percent = 10
elif tip_option == 3:
    tip_percent = 15
elif tip_option == 4:
    tip_percent = 20
else:
    print("Opțiune invalidă. Se va folosi 10% tips.")
    tip_percent = 10

total_with_tips, amount_due = calculate_with_tips(total_due, number_of_people, tip_percent)  # Calculam suma totala si costul per persoana cu tips.
total_without_tips = total_due  # Totalul fara tips este acelasi cu suma totala initiala.

print(f"Fiecare persoană trebuie să plătească: {amount_due:.2f} lei")  # Afisam costul per persoana rotunjit la 2 zecimale.
print(f"Totalul cu {tip_percent}% tips rotunjit este: {total_with_tips:.2f} lei")  # Afisam suma totala cu tips rotunjit la 2 zecimale.
print(f"Totalul fără tips este: {total_without_tips:.2f} lei")  # Afisam suma totala fara tips rotunjit la 2 zecimale.