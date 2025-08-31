# Esercizi su tuple, liste, metodi delle liste e dizionari in Python (senza cicli, if, keys, values, items)

# 1. Crea una lista con i numeri da 1 a 10 e stampa il terzo elemento.
fino_a_dieci = list(range(11))
print(fino_a_dieci[2])

# 2. Aggiungi alla lista precedente il numero 11 e poi rimuovi il numero 5.
fino_a_dieci.append(11)
fino_a_dieci.append(5)
print(fino_a_dieci)
fino_a_dieci = [x for x in fino_a_dieci if x != 5]
print('lista senza cinque:',fino_a_dieci)

# 3. Ordina la lista in ordine crescente.
fino_a_dieci.sort(reverse=True)
print('lista ordinata:',fino_a_dieci)

# 4. Crea una nuova lista con i quadrati dei numeri da 1 a 5.
quadrati_fino_5 = [x**x for x in range(1,6)]
print(quadrati_fino_5)

# 5. Data la lista ["mela", "banana", "pera"], sostituisci "banana" con "arancia".
frutta = ["mela", "banana", "pera"]
frutta[1] = "arancia"
print(frutta)

# 6. Crea una tupla con tre elementi: un numero, una stringa e un booleano.
es_tupla = (1, "Elena", True)

# 7. Concatena due tuple e assegna il risultato a una nuova variabile.
sec_tupla = (1, 2, 3) 
tupla_conc = es_tupla + sec_tupla
print(tupla_conc)

# 8. Crea un dizionario con le chiavi "nome", "età", e "città".
dict = {
    "nome": "Elena",
    "eta": "26",
    "città": "Palermo"
}

# 9. Aggiungi al dizionario la chiave "email" e assegna un valore.
dict["email"] = ""
print(dict)

# 10. Estrai in tre variabili distinte le tre singole chiavi presenti nel dizionario del punto 8 e i relativi valori.

nome1 = dict["nome"]
età1 = dict["eta"]
città1 = dict["città"]
