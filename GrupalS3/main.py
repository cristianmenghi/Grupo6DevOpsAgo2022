# Crear un programa en Phyton que:
# 1. Permita ingresar elementos en una lista de enteros
# 2. Permita borrar elementos en una lista de enteros
# 3. Si un entero está o no en la lista
# Se sugiere crear un Menú de opciones para ello y que las operaciones de Listas se realicen en módulos.

# Para los menus usamos urwid https://urwid.org/tutorial/index.html 
import urwid # pip install urwid 
from pydialog import Dialog
from operaciones import *

# Inicializo lista vacia
lista=[]

# # Creo las opciones del menu
# opciones = u'Agregar Buscar Borrar Salir'.split()

# # creamoe el menu con las opciones.
# def menu(title, opciones):
#     body = [urwid.Text(title), urwid.Divider()]
#     for c in opciones:
#         button = urwid.Button(c)
#         urwid.connect_signal(button, 'click', item_chosen, c)
#         body.append(urwid.AttrMap(button, None, focus_map='reversed'))
#     return urwid.ListBox(urwid.SimpleFocusListWalker(body))

# # Que acciones hace cada opcion.
# def item_chosen(button, choice):
#     response = urwid.Text([u'Accion ', choice, u'\n'])
#     match choice:
#         case str(Agregar):
#             done = urwid.Button(u'Ok Agregar')
#         case str(Buscar):
#             done = urwid.Button(u'Ok Buscar')
#         case str(Borrar):
#             done = urwid.Button(u'Ok Borrar')
#         case Salir:
#             done = urwid.Button(u'Salir')
#     urwid.connect_signal(done, 'click', exit_program)
#     main.original_widget = urwid.Filler(urwid.Pile([response,
#         urwid.AttrMap(done, None, focus_map='reversed')]))

# # salir del programa.
# def exit_program(button):
#     raise urwid.ExitMainLoop()

# main = urwid.Padding(menu(u'IntroDevOps S3 Grupal', opciones), left=2, right=2)
# top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
#     align='center', width=('relative', 60),
#     valign='middle', height=('relative', 60),
#     min_width=20, min_height=9)
# urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()

TEST
lista=[10,5,2,3]
print("---add---")
agregar(lista,8)
print(lista)
print("---search---")
p = buscar(lista,2)
print("posicion : " + str(p))
print("---del---")
borrar(lista, p)
print(lista)



