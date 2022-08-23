
def agregar(lista,num):
    lista.append(num)
    return lista

def borrar(lista,posicionLista):
    lista.remove(posicionLista)
    return lista
    
def buscar(lista,num):
    i = lista.index(num)
    return(i)