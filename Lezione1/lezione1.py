#python e' un linguaggio interpretato - altri tipi di linguaggi sono quelli compilati
#python e' un linguaggio ad alto livello - ci sono anche i linguaggi a basso livello
print('ciao')
print(34+56)

num = 45
nome = "Andrei"
print(num)
print(nome)
print(nome)

#operazioni interi
s = 23 + 45
diff = 23-45
molt = 23 *4
div = 23/4 #5,75
div_intera = 23//4 #5
resto = 23%4

print('somma: ', s,'diff:',diff,'molt:',molt,'div:',div,'div_intera:',div_intera,'resto:',resto)

#operazioni tra stringhe -> concatenazione di stringhe
cognome = "Zanet"
nome_completo = nome + " " + cognome
print(nome_completo)
print(len(cognome))

print(cognome[0]) #primo carattere

#l ultimo indice di una stringa e' sempre uguale alla sua lunghezza - 1

print('----ultimo carattere----')
print(cognome[3])
print(cognome[-1])
print(cognome[len(cognome)-1])

print(cognome[1:3]) #dall indice 1 al 3 escluso
print(cognome[:2]) #dall inizio fino all indice 2 escluso
print(cognome[2:]) #dall indice 2 fino alla  fine

#es
parola = "amare"
da_rimuovere = "re"
nuova_parola = parola.replace(da_rimuovere, "")
print(nuova_parola)

print(parola[:-2])

t = True
f = False

#operazioni con i booleani

#operatori di confronto: <,<=,>,>=,==,!= (diverso)

b1 = 23 >= 34
b2 = 23 != 34
print(b1)
print(b2)

#operatori booleani: and, or, not
b3 = b1 and True
print('b3',b3)
b4 = b1 or True
print('b4', b4)
b5 = not True
print(b5)

#lista
numeri = [23,4,52,5,7]
print(numeri)
print(len(numeri))
print(numeri[0])
print(numeri[-1])
print(numeri[2:5])
print(numeri[3:])
print(numeri[:3])
print(numeri[:])

#metodi su strighe
print(parola)
parola = parola.capitalize()
print(parola)
print(parola.upper())
print(parola.lower())
