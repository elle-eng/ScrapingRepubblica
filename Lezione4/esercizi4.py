
# Esercizio 1: Pari o dispari
# Chiedi un numero all’utente e stampa se è pari o dispari.
numero = int(input("Inserisci un numero: "))
if numero%2==0: 
    print("Il numero " + str(numero) + " è pari." )
else:
    print("Il numero " + str(numero) + " è dispari." )

# Esercizio 2: Controllo iniziale stringa
# Chiedi all’utente una parola e stampa True se inizia con la lettera "s".
parola = input("Scegli una parola: ")

if parola.lower().startswith("s"):
    print("La parola " + parola + " inizia con s.")
else:
    print("La parola " + parola + " NON inizia con s.")

# Esercizio 3: Invertire una stringa
# Chiedi una frase e stampala al contrario usando slicing.
frase = input("Scrivi una frase: ")
frase_al_contrario = frase[::-1]
print(frase_al_contrario)

# Esercizio 4: Rimuovere vocali
# Chiedi una frase all’utente e stampala senza vocali (a, e, i, o, u).

vocali = ['a', 'e', 'i', 'o', 'u']
senza_vocali = ""

for lettera in frase:
    if lettera not in vocali:
        senza_vocali = senza_vocali + lettera

print(senza_vocali)

# Esercizio 5: Slicing su lista
# Dalla lista [1, 2, 3, 4, 5, 6, 7], stampa solo i numeri da 3 a 6 inclusi.
numeri = [1, 2, 3, 4, 5, 6, 7]
print(numeri[2:-1])

# Esercizio 6: Verifica parola contenuta
# Chiedi una frase e verifica se contiene la parola "python".
if "python" in frase.lower():
    print("La frase " + frase + " contiene la parola Python")
else: 
    print("La frase " + frase + " NON contiene la parola Python")

# Esercizio 7: Somma di lista
# Crea una lista con 5 numeri a tua scelta e stampa la loro somma.
numeri_a_scelta = [3, 45, 23, 53]
somma = sum(numeri_a_scelta)

# print(somma)

# # Esercizio 8: Iniziali nome e cognome
# # Chiedi il nome e il cognome all’utente e stampa le iniziali (es. "Mario Rossi" -> "M.R.").
nome = input("Il tuo nome: ")
cognome = input("Il tuo cognome: ")
iniziali = nome[0] + "." + cognome[0] + "."
print(iniziali)

# # Esercizio 9: Parola più lunga
# # Chiedi una frase all’utente e stampa la parola con più caratteri.


# Esercizio 10: Numeri crescenti
# Chiedi all’utente due numeri: se il primo è maggiore, stampa "decrescente", altrimenti "crescente".
primo_numero = int(input())
secondo_numero = int(input())

if primo_numero > secondo_numero: 
    print("Ordine decrescente")
elif secondo_numero > primo_numero: 
    print("Ordine crescente")
else:
    print("I numeri sono uguali")

# Esercizio 11: Modifica lista
# Crea una lista con 3 colori. Sostituisci il secondo con "viola" e stampa la lista aggiornata.
colori = ["giallo", "rosso", "blu"]
colori[1] = "viola"
print(colori)

# Esercizio 12: Caratteri pari di una stringa
# Chiedi una stringa e stampa solo i caratteri che stanno in posizione pari (indice 0, 2, 4...).
stringa = input("Inserisci una stringa: ")
print(stringa[0::2])