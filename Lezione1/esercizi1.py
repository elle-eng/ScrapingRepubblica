import math

# 1. Booleani e logica
# ---------------------------------------------------------------------------
# Per ciascun esercizio scrivi UNA sola espressione booleana che restituisca
# True / False come da consegna.

# 1.1  Dati x = 7, y = 3  ➜  True se x è dispari E multiplo di y
x = 7
y = 3
dispari_e_multiplo = (x%2 != 0) and (x%y == 0)
print(x, 'e dispari e multiplo di ', y, '?', dispari_e_multiplo)

# 1.2  Dati a = -4, b = 0 ➜  Verifica che almeno uno tra a e b sia zero

a, b = -4, 0
print('Almeno una delle due variabili tra a e b è uguale a 0: ', (a == 0 or b == 0))
# print((a == 0) | (b == 0))

# 1.3  s = "Python"      ➜  True se s inizia con maiuscola O termina con maiuscola
s = "Python"
print("La prima lettera della stringa è maiuscola o l'ultima è minuscola: ", (s[0].isupper()) or (s[-1].islower()))

# 1.4  n = 121            ➜  Verifica se n è un quadrato perfetto E dispari

n = 121
quadrato_perfetto_dispari = isinstance(math.sqrt(n), int) and n%2!=0


# 1.5  lista = [1, 2, 3]  ➜  True solo se la lista NON è vuota E la sua lunghezza è pari
lista = [1,2,3]
print('La lista è pari e contiene elementi: ',(len(lista)%2 == 0) and (len(lista)!=0))


# 1.6  anno = 2024        ➜  È bisestile? (multiplo di 4 e non di 100, oppure multiplo di 400)
anno = 2024
annoBisestile = ((anno % 4 == 0 and anno % 100 != 0) or anno % 400 == 0)
print("L'anno è bisestile: ", annoBisestile)

# 1.7  p, q, r = True, False, False
#       ➜  Porta logica XNOR a tre ingressi (vera se la somma dei True è pari)
p, q, r = True, False, False
xnor = (not p and not q and not r) or ((p and q) and not r) or ((r and q) and not p) or ((p and r) and not q)

# 1.8  age = 17, country = "IT"
#       ➜  Accesso consentito se (età ≥ 18) OPPURE (età ≥ 16 E paese ≠ "IT")
age = 17
country = "IT"
consentAccess = age >= 18 or (age >= 16 and country == "IT")
print('Accesso consentito: ', consentAccess)

# 1.9  s = "ace", t = "cade" ➜  True se iniziano O finiscono con la stessa lettera
s = "ace" 
t = "cade"
print("Le due parole iniziano o finiscono con la stessa lettera: ", ((s[0] == t[0]) or (s[-1] == t[-1])))

# 1.10 num = 0b101101 ➜  True se ESATTAMENTE due bit sono a 0
print('----1.10-----')
num = 0b101101
due_zeri = bin(num)[2:].count('0') == 2


# ---------------------------------------------------------------------------
# 2. Accesso a stringhe (indicizzazione)
# ---------------------------------------------------------------------------
frase = "L'etica del Pythonista"

# 2.1  Stampa il primo e l'ultimo carattere, separati da uno spazio
print(frase[0],' ',frase[-1])

# 2.2  Ottieni la sottostringa "etica" usando indici positivi
print(frase[2:7])

# 2.3  Ottieni la stessa sottostringa usando indici negativi
print(frase[-20:-15])

# 2.6  Crea una nuova stringa composta soltanto dalle vocali presenti (in ordine originale)
print(frase[2] + frase[4] + frase[6] + frase[9] + frase[13] + frase[16] + frase[18] + frase[21])

# 2.7  Sostituisci "etica" con "arte" usando solo slicing (niente .replace)
frase = "L'etica del Pythonista"
frasearte = frase[0:2] + 'arte' + frase[7:]
print('Sostituisci "etica" con "arte" usando solo slicing: ', frasearte)

# 2.8  Booleano: la stringa contiene più lettere maiuscole che minuscole?
maiuscole = (frase[0].isupper()) + (frase[1].isupper()) + (frase[2].isupper()) + (frase[3].isupper()) + (frase[4].isupper()) + (frase[5].isupper()) + (frase[6].isupper()) + (frase[7].isupper()) + (frase[8].isupper()) + (frase[9].isupper()) + (frase[10].isupper()) + (frase[11].isupper()) + (frase[12].isupper()) + (frase[13].isupper()) + (frase[14].isupper()) + (frase[15].isupper()) + (frase[16].isupper()) + (frase[17].isupper()) + (frase[18].isupper()) + (frase[19].isupper()) + (frase[20].isupper()) + (frase[21].isupper())
minuscole = (frase[0].islower()) + (frase[1].islower()) + (frase[2].islower()) + (frase[3].islower()) + (frase[4].islower()) + (frase[5].islower()) + (frase[6].islower()) + (frase[7].islower()) + (frase[8].islower()) + (frase[9].islower()) + (frase[10].islower()) + (frase[11].islower()) + (frase[12].islower()) + (frase[13].islower()) + (frase[14].islower()) + (frase[15].islower()) + (frase[16].islower()) + (frase[17].islower()) + (frase[18].islower()) + (frase[19].islower()) + (frase[20].islower()) + (frase[21].islower())
print('La stringa contiene più maiuscole: ', maiuscole > minuscole)


# 2.9  Quante parole contiene? (usa gli spazi come separatori)
token = frase.split()
print('Quali token: ', token) 
print('Quanti token: ', len(token))

# 2.10 Lista dei caratteri unici in ordine alfabetico (senza ripetizioni)


# ---------------------------------------------------------------------------
# 3. Liste e slicing
# ---------------------------------------------------------------------------
nums = list(range(10))      # [0, 1, 2, ..., 9]
parole = ["alfa", "beta", "gamma", "delta", "epsilon"]

# 3.1  Recupera il penultimo elemento di nums con indice negativo
print("Il penultimo numero di nums è: ", nums[-2])

# 3.2  Sotto-lista dei numeri dispari usando slicing (niente list comprehension)

nums = list(range(10))  
x = nums

print(x)
numsDisp = [nums[1], nums[3], nums[5], nums[7], nums[9]]
print("I numeri dispari di nums sono: ", numsDisp)

# 3.3  Sotto-lista dei multipli di 3 usando slicing con passo (?)

# 3.4  Copia superficiale di nums con slicing; dimostra che id() è diverso

# 3.5  Sostituisci (slice-assignment) i tre elementi centrali di nums con un solo valore 100

# 3.6  Inserisci ["eta", "theta"] PRIMA di "gamma" in parole (senza .insert())

# 3.7  Ottieni ['epsilon', 'delta', 'gamma', 'beta', 'alfa'] con un singolo slice

# 3.8  Con slice-assignment, svuota nums mantenendo la stessa variabile

# 3.9  Concatena nums e parole in mix, poi usa slicing per estrarre solo le stringhe che terminano con "a"

# 3.10 Dividi parole in due metà e ricomponile nell'ordine inverso usando solo slicing e concatenazione