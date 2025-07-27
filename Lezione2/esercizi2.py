# 1. List Comprehension: 
#    Data la lista `numeri = [1, 2, 3, 4, 5, 6, 7]`, crea una nuova lista contenente solo i numeri pari.

numeri = [1, 2, 3, 4, 5, 6, 7]
numPari = [x for x in numeri if x%2 == 0]
print('Numeri pari: ', numPari)

# 2. List Comprehension:
#    Genera una lista di quadrati dei numeri da 1 a 20 che siano multipli di 3.
numeri20 = list(range(1,21))
quad_multipli_3 = [x**2 for x in numeri20 if x%3 == 0]
print('1.0.' , quad_multipli_3)

# 3. Casting:
#    Converte ogni elemento della lista `numeri = ["1", "2", "3", "4"]` in intero.
numeri = ["1", "2", "3", "4"]
numInt = [int(x) for x in numeri]
print(type(numInt[1]))

# 4. Casting:
#    Dato `valori = [10, "20", "trenta", 40]`, filtra e mantieni solo quelli che possono essere castati a interi.
valori = [10, "20", "trenta", 40]
castInt = [int(x) for x in valori if isinstance(x, int) or (isinstance (x, str) and x.isdigit())]
print ("1.1.", castInt)

# 5. isinstance():
#    Dato `dati = [1, "due", 3.0, True, None]`, crea due liste: una con solo numeri interi, una con solo stringhe.
dati = [1, "due", 3.0, True, None]
stringhe = [x for x in dati if isinstance(x, str)]
interi = [x for x in dati if isinstance(x, int) and not isinstance(x, bool)]
print('stringhe: ',stringhe)
print('interi',interi)


# 6. isinstance():
#    Dato `oggetti = [[], {}, (), set(), 42]`, separa quelli che sono collezioni (`list`, `dict`, `tuple`, `set`).
oggetti = [[], {}, (), set(), 42]
collezioni = [x for x in oggetti if isinstance(x, list) and isinstance(x, dict) and isinstance(x, tuple) and isinstance(x, set)]
print('Per esclusione: ', collezioni)


# 7. join():
#    Dato `parole = ["questo", "è", "un", "test"]`, unisci tutte le parole con uno spazio tra di esse.
parole = ["questo", "è", "un", "test"]
frase = ' '.join(parole)
print(frase)


# 8. join():
#    Dato `numeri = [1, 2, 3, 4]`, uniscili in una stringa separata da trattini (`-`), dopo averli convertiti in stringhe.
numeri = [1, 2, 3, 4]
stringaNum = [str(x) for x in numeri]
fraseNum = '-'.join(stringaNum)
print(fraseNum)


# 9. split():
#    Dividi la stringa `"ciao,come,va"` in una lista di parole.
stringa = "ciao,come,va"
stringa2 = stringa.split(',')
print(stringa2)

# 10. split():
#     Scrivi una funzione che riceve una stringa di numeri separati da virgola e restituisce una lista di interi.
numVirgola = "1,2,3,4,5,6,7"
numSplit = numVirgola.split(',')
intNum = [int(x) for x in numSplit]
print(intNum)