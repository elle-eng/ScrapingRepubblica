num = 45
print('num',num)
num2 = num
num2 = 100
print('num2', num2)
print('num',num)

print('------------------')
l = [34,2,6,3]
print('l',l) #[34,2,6,3]
l2 = list(l)
l2.append(1000)
print('l2', l2) #[34,2,6,3,1000]
print('l',l) #[34,2,6,3]

#list comprehension

#creare una lista con gli elementi doppi di l
l_doppi = [x*2 for x in l]
print(l_doppi)

#creare una lista con gli elementi di l come stringhe
l_str = [str(numero) for numero in l]
print(l_str)

#creare una lista con gli elementi pari divisi per 2
l_filtrata_mappata = [numero//2 for numero in l if numero % 2 == 0]
print(l_filtrata_mappata)