# Crear un programa en Phyton que:
# 1. Permita ingresar elementos en una lista de enteros
# 2. Permita borrar elementos en una lista de enteros
# 3. Si un entero está o no en la lista
# Se sugiere crear un Menú de opciones para ello y que las operaciones de Listas se realicen en módulos.

from operaciones import *

# Inicializo lista vacia
lista=[]
# Creo las opciones del menu
opciones = {
            1: 'Agregar',
            2: 'Buscar', 
            3: 'Borrar', 
            4: 'Salir',
            }
# Imprimo las opciones del menu.
def print_menu():
    for key in opciones.keys():
        print (key, '--', opciones[key] )

# funcion main del app.
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Ingrese su opcion: '))
        except:
            print('Opción incorrecta...')
        match option:
            case 1:
                print("Ingrese los num a la lista pej: 2 enter 3 enter 5, para finalizar deje enter. :")
                try:
                    while True:
                        val = input()
                        if not val:
                            break
                        agregar(lista,val)
                except EOFError:
                    print("Error, no in1greso nada")
                print("Elemenots guardados")
                print(lista)   
            case 2:
                print("Ingrese num a buscar, pej 5 :")
                try: 
                    val = input()
                    b = buscar(lista,val)
                except EOFError:
                    print("Error, no ingreso nada")
                print("Existe num en lista: ")  
            case 3:
                print("Ingrese num a borrar, pej 5 :")
                print(lista)
                try:
                    val=[]
                    val = input()
                    r = buscar(lista,val)
                    borrar(lista,r)
                except EOFError:
                    print("Error, no ingreso nada")
                print("Resultado" + str(lista))  
            case 4:
                print("Saliendo")
                exit()



