import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "PYTHON/recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador
    
def inicio():
    system('cls')
    print('*' * 44)
    print('*' + ' '*5 + 'Bienvenido al listado de recetas' + ' '*5 + '*')
    print('*' * 44)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total de recetas: {contar_recetas(mi_ruta)}")
    
    eleccion = 'x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1, 7):
        print("Elige una opción:")
        print('''
        [1.] Leer receta
        [2.] Crear nueva receta
        [3.] Crear nueva categoría
        [4.] Eliminar receta
        [5.] Eliminar categoría
        [6.] Salir del programa''')
        eleccion = input()
    return int(eleccion)

def mostrar_categorias(ruta):
    print("Categorías: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    
    return lista_categorias
    
def elegir_categoria(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range (1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoría: ")
    
    return lista[int(eleccion_correcta) -1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    
    return lista_recetas
    
def elegir_recetas(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) +1):
        eleccion_receta = input("\nElige una receta: ")
        
    return lista[int(eleccion_receta) -1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nueva_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nueva_receta)
        
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta "{nueva_receta}" ha sido creada.')
            existe = True
        else:
            print('Lo siento, esa receta ya existe')

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva categoría: ")
        nueva_categoria = input()
        ruta_nueva = Path(ruta, nueva_categoria)
        
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu categoría "{nueva_categoria}" ha sido creada.')
            existe = True
        else:
            print('Lo siento, esa categoría ya existe')

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta "{receta.name}" ha sido eliminada.')

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoría "{categoria}" ha sido eliminada.')

def volver_inicio():
    eleccion_inicio = 'x'
    while eleccion_inicio.lower() != 'q':
        eleccion_inicio = input("\nPresiona Q para colver al inicio.")
        

finalizar_programa = False    

while not finalizar_programa:

#mostrar menu de inicio

    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
            
    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
            
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
            
    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
            
    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
            
    elif menu == 6:
        print("Adios")
        finalizar_programa = True
        