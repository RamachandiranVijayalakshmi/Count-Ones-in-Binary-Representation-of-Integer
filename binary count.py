def a(b):
    return bin(b).count('1')
c=int(input('Enter the interger Value:'))
print('Count Ones in Binary Representation of Integer',a(c))