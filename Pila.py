from Node import Node

class Pila:
    def __init__(self):
        self.top = None
    
    #PILA: TOP: NONE
    #nuevoNodo: N1 next:None
    #top: nuevoNodo-> N1

    #nuevoNodo = N2 next: None
    #N2.next = N1
    #top = N2

    def push(self, nuevoNodo):
        if self.top != None:
            nuevoNodo.next = self.top
        self.top = nuevoNodo

    def imprimePila(self):
        aux = self.top
        while aux != None:
            print(aux.caracter)
            aux = aux.next   


    #PILA: 
    #top-N4 next:N3; 
    #N3 next: N2; 
    #N2: next: N1; 
    #N1 next: None

    #aux = N4
    #top = N3
    #N4.next = None

    #PILA:
    #top: N3 next: N2;
    #N2 next:N1;
    #N1 next: None;
    def pop(self):
        aux = self.top
        if aux != None:
            self.top = aux.next
            aux.next = None

    def peek( self ):
        return self.top 
    