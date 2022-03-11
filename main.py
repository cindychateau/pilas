from Node import Node
from Pila import Pila

pila = Pila()

n1 = Node('N1')
n2 = Node('N2')
n3 = Node('N3')

pila.push(n1)
pila.imprimePila()
print('-----')

pila.push(n2)
pila.imprimePila()
print('-----')

pila.push(n3)
pila.imprimePila()

print('-----')
n4 = Node('N4')
pila.push(n4)
pila.imprimePila()


print('-----')
pila.pop()
pila.imprimePila()