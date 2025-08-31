dict = {
    "nome": "Elena",
    "eta": "26",
    "città": "Palermo"
}

print(list(dict.keys()))
print(list(dict.values()))
print(list(dict.items()))

# nome = input("inserisci nome: ")
# eta = input("inserisci eta: ")

print("ciao sono " + dict["nome"] + " e ho " + dict["eta"] + " anni.")
print("ciao sono",dict["nome"],'e ho',dict["eta"],'anni.')
# format
print("ciao sono {} e ho {} anni.".format(dict["nome"], dict['eta']))
print(f"ciao sono {dict['nome']} e ho {dict['eta']} anni.")
# print(f"ciao sono {nome} e ho {eta} anni.")

if 20 >= 4:
    print('20 maggiore di 4') #indentazione
    num = 100
if 56 == 56:
    print('56 == 56')
elif 100 > 20:
    print('100 > 20')
else:
    print('20 minore di 4')
print('va oltre')

print(num)

numeri = [12,4,5,67]

if 5 not in numeri: #numeri deve essere una struttura iterabile
    print('5 in numeri')
    exit() #per terminare il programma con successo (senza errori)

print('cane\ngatto')

string = 'Mocty Python'
# string[2] = 'n' #NON VA BENE
string = '                      ' +string[:2] + 'n' + string[3:]
print(string.upper().strip()) #metto la stringa in maiuscolo e poi tolgo glispazi vuoti a sinistra e a destra

print(string.find('Monty')) #l indice dove inizia Monty in string. -1 se non c'e'

print(string.replace('Monty', 'Elena'))

nome_binario = (str(bin(ord('E'))) + str(bin(ord('l')))+ str(bin(ord('e')))+str(bin(ord('n')))+str(bin(ord('a')))).replace('0b','')
print('Elena in binario:',nome_binario)
primo_carattere = chr(int('0' + str(bin(int(nome_binario[0:8],base=2))).replace('0b','')[:-1],base=2))
print(primo_carattere)

