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