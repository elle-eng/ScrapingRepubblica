# list

l = [34,2,4]
l.append(100)
l.insert(1,1000)
print(l)
l[2] = 20
print(l)
print(l.index(20)) 
l.append(4)
print('number of 4: ',l.count(4))
l.sort()
print("l",l)

l.append([34,1,89])
print('l: ', l) #[34,1000,20,4,100, 4, [34,1,89]]
l.extend([44,2,100])
print('l: ', l) #[34,1000,20,4,100, 4, [34,1,89], 44,2,100]

print(l.pop(0)) #rimuove e restituisce il primo elemento (all indice zero)
print('l', l)
# tuple - sono immutabili, ossia una volta dichiarate, non posso piu essere modificate
numeri = (12,40,5) #va bene anche numeri = 12,40,5
print('tupla numeri:',numeri[1])
print(numeri.index(12))
# numeri[1] = 1000

# dict - una sequenza non ordinata di coppie chiave-valore
persona = {
    "nome": "Andrei",
    "eta": 25,
    1: 'uno',
    ('a','b'): 'c'
}

print(persona["nome"])
print(persona[('a','b')])

#set
# casting
# if