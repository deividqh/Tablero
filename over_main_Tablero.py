# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# OBJETO     T A B L E R O
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
import os           
from enum import Enum

import tkinter as tk
import threading

import time

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# El objeto de estas pruebas xxxxxxxxxxxxxxxxxxxxxxxxxx
# from classMenuDvd.Tablero_X_Men import Rangutan as Rangutan
from classMenuDvd.Tablero_X_Men import Rango as Rango
from classMenuDvd.Tablero_X_Men import Tablero

# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# El Menu de todo Esto mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
from classMenuDvd.classXindeX import XindeX 
# _____________________________________________________________________________
# Cachar Datos Seguros por Teclado 
from classTeclado.listTOdict_Tcld import listTOdict_byTcld as TeclD
# ____________________________________________________________
# Para validar: mail, valores entre, fechas... 
from classTeclado.validator import ValidReg as VAL

# ====================================================================================
# DEF: Desarrollo y memoria de la clase Tablero. 
# ====================================================================================
# TABLERO = Rangutan(total_columnas_tablero=50, total_filas_tablero=30, valor_inicial='-')
# TABLERO = None
TABLERO = Tablero(total_columnas_tablero = 10, total_filas_tablero = 20, valor_inicial='-')

# ######################################################################
# ######################## xindex ######################################
# ######################################################################
def main():
    # 1- INSTANCIO EL OBJETO XINDEX ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    The_X_Men = XindeX()
    # 2- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    The_X_Men.addX(titulo='MenuPpal',  padre=None, ipadre=None,  
                    fraseHead="| - M A I N    O V E R   T A B L E R O - "  , 
                    lst_items=[ ("TABLERO" , None) , ('IMPRIMIR', None) , ("GET" , None) , ("PUSH" , None) , ("DEL" , None) , ("RANGOS" , None) , ('MISCELANEA', None)] 
                    )
    The_X_Men.addX( titulo='SUB_CREAR', padre='MenuPpal', ipadre="TABLERO" , lst_items=[("Crear Tablero",crear_tablero), ("Iniciar Tablero", iniciar_tablero)] )  
    The_X_Men.addX( titulo='SUB_IMPR', padre='MenuPpal', ipadre="IMPRIMIR" , lst_items = [ ("Imprimir Modo Max sin/sp",print_max_ssp),("Imprimir Modo Max con/sp",print_max_csp) , ("Imprimir Modo Literal",print_literal) , ('Imprimir Modo Fixed sin/sp', print_fixed_ssp), ("Imprimir Modo Fixed con/sp",print_fixed_csp), ('Imprimir Modo Personal', print_personal), ('Imprimir Ambbigous', print_ambigous)] )
    The_X_Men.addX( titulo='SUB_GET'  , padre='MenuPpal', ipadre="GET"     , lst_items=[("Get Fila",None), ("Get Columna",None), ("Get Valor By Fila-Columna", None), ("Get Valor By Celda(A:0)", None), ("Get Matriz Values", None)])
    The_X_Men.addX( titulo='SUB_SET'  , padre='MenuPpal', ipadre="SET"     , lst_items=[("PUSH Matriz",None),("PUSH Fila",None), ("PUSH Column",None), ("PUSH Valor", None), ('PUSH Valor By Celda (C:3)', None), ('PUSH valor by fila / columna')] )
    The_X_Men.addX( titulo='SUB_DEL'  , padre='MenuPpal', ipadre="DEL"     , lst_items=[("Del Fila",None), ("Del Column",None), ("Del Celda", None)] )    
    The_X_Men.addX( titulo='SUB_RANGOS', padre='MenuPpal', ipadre="RANGOS" , lst_items=[("Crear Rango",crear_rango), ("Buscar Rango",buscar_rango), ("Eliminar Rango",eliminar_rango), ("Ver Rango", ver_rango) ] )  
    The_X_Men.addX( titulo='SUB_MISC'  , padre='MenuPpal', ipadre="MISCELANEA" , lst_items=[("Prueba Recursiv" , prueba_recursiva), ("T+ (Menu Simulation)", None)] )    

    # 3- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦
    retorno = The_X_Men.Mystyca(titulo='MenuPpal', configurado=True, execFunc=True, tipo_marcador='a', execAll=False, Loop=True , padX=50)
    # 4- SALE DEL MENU ________________________________________________________________
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")    
    
# ====================================================================================
# ====================================================================================
# CREA UN TABLERO Y BORRA EL ANTERIOR.
def crear_tablero(): 
    global TABLERO
    print()
    f_c = TeclD.byTcld( listaStrKeys=['filas', 'columas'], listaDef=[(int, False), (int, False)])
    # _______________________
    # Pregunta de Seguridad
    continuar = TeclD.byTcld( listaStrKeys=['if'], listaDef=[(bool, True)], msgIntro=f'\nSeguro que Quieres Continuar?')    
    if continuar['if']==False: 
        print('Crear Anulado... Chaoooo')
        return
    TABLERO = Tablero(total_columnas_tablero = f_c['columnas'], total_filas_tablero = f_c['filas'], valor_inicial='+')
    print('\nCREAR TABLERO ;)\n')

# PONE EL MISMO VALOR EN TODO EL TABLERO.
def iniciar_tablero():
    global TABLERO 
    val = TeclD.byTcld( listaStrKeys=['val'], listaDef=[(str, True)], msgIntro='\nValor Inicial (este Valor Se pondrá en toda la Tabla) ')    
    # Seguridad_____________
    continuar = TeclD.byTcld( listaStrKeys=['if'], listaDef=[(bool, True)], msgIntro=f'\nSeguro que Quieres Continuar?')    
    if continuar['if']==False: 
        print('Iniciar Anulado... Chaoooo\n')
        return
    TABLERO.init_tablero(value = val['val'])
# IMPRIME UN RANGO
def print_max_ssp():
    global TABLERO
    print() 
    val = TeclD.byTcld( listaStrKeys=['val'], listaDef=[(int, True)], msgIntro='\nTamaño Columna (0 by def)... ')    
    print('\nI m p r i m i r    M a x  s/sp  \n')    
    TABLERO.imprimir()
def print_max_csp():
    global TABLERO  
    pad_x = TeclD.byTcld( listaStrKeys=['p'], listaDef=[(int, True)], msgIntro='\npadX (0 by def)... ')        
    print('\nI m p r i m i r    M a x  c/sp  \n')    
    TABLERO.imprimir(sp_columna=pad_x['p'])    
def print_literal():
    global TABLERO  
    print('\nI m p r i m i r   L i t e r a l  P u r o \n')    
    TABLERO.imprimir( ancho = 0 , sp_columna = 0 )
def print_fixed_ssp():
    global TABLERO  
    print('\nI m p r i m i r   F i x e d  s/sp  \n')    
    TABLERO.imprimir( ancho = 2 , sp_columna = 0 )
def print_fixed_csp():
    global TABLERO  
    print('\nI m p r i m i r   F i x e d  c/sp \n')    
    TABLERO.imprimir( ancho = 5 , sp_columna = 1 )
def print_personal():
    global TABLERO  
    print('\nI m p r i m i r   P e r s o n a l  c/sp \n')    
    TABLERO.imprimir( lista = [5,3,4,1,3,2] , sp_columna = 3 )
def print_ambigous():
    global TABLERO  
    print('\nI m p r i m i r   A m b i g u o u s   \n')    
    TABLERO.imprimir( ancho = 3 , lista = [3, 4, 6] , sp_columna = 5 )

# ESTABLECE UN VALOR EN UNA CELDA PIDIENDO FILA Y COLUMNA
def set_fila_columna():      
    global TABLERO
    f_c_v = TeclD.byTcld( listaStrKeys=['fila', 'col','valor'], listaDef=[(int, False), (str, False), (str, True)])
    
    tablero.push(data_push = matriz_pruebas, celda_inicio = 'C:3' )

# ESTABLECE UN VALOR EN UNA CELDA (A:0)
def set_celda():
    cel_v = TeclD.byTcld( listaStrKeys=['celda', 'valor'], listaDef=[(str, False), (str, True)])    
    
    tablero.push(data_push = matriz_pruebas, celda_inicio = 'C:3' )

# ESTABLECE UN VALOR EN UNA FILA
def set_valor_over_fila():
    global TABLERO
    f = TeclD.byTcld( listaStrKeys=['f'], listaDef=[(int, False)], msgIntro='\nIntroduce Fila to Set')        
    fila = TABLERO.get_lst_filas(filaFrom=f['f'], filaTo=f['f'])
    if not fila: return
    val = TeclD.byTcld( listaStrKeys=['v'], listaDef=[(str, True)], msgIntro=f'\nIntroduce Valor to Set en fila {f['f']}')    
    
    tablero.push(data_push = matriz_pruebas, celda_inicio = 'C:3' )
    
# ESTABLECE UNA COLUMNA
def set_valor_over_columna():
    global TABLERO
    col = TeclD.byTcld( listaStrKeys=['c'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Set  [0, "a", "A"]')    
    val = TeclD.byTcld( listaStrKeys=['v'], listaDef=[(str, True)], msgIntro=f'\nIntroduce el Valor a introducir en la Columna < {col['c']} > ')    
    
    tablero.push(data_push = matriz_pruebas, celda_inicio = 'C:3' )

# RETORNA UN VALOR DEL TABLERO CUANDO INTRODUCES UNA Cimprime_a_caponELDA (A:0, C:3)
def get_celda():
    cel_v = TeclD.byTcld( listaStrKeys=['celda'], listaDef=[(str, False)])
    valor = TABLERO.celda(celda=cel_v['celda'])

# OBTIENE UN VALOR DEL TABLERO x FILA Y COLUMNA
def get_fila_columna(): 
    global TABLERO
    f = TeclD.byTcld( listaStrKeys=['f'], listaDef=[(int, False)], msgIntro='\nIntroduce Fila to Get Valor ')    
    c = TeclD.byTcld( listaStrKeys=['c'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Get Valor [0, "a", "A"] ')    

# OBTIENE UNA FILA
def get_fila():
    global TABLERO
    print('OBTIENE UNA LISTA DE DICCIONARIO DE UNA FILA ENTERA')
    f_f = TeclD.byTcld( listaStrKeys=['ff'], listaDef=[(int, False)], msgIntro='\n(Get Fila) Introduce Fila Desde... ')    
    f_t = TeclD.byTcld( listaStrKeys=['ft'], listaDef=[(str, False)], msgIntro='\n(Get Fila) Introduce Fila Hasta... ')    

# OBTIENE UNA COLUMNA
def get_columna():
    global TABLERO
    col = TeclD.byTcld( listaStrKeys=['col'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Get  [0, "a", "A"]')    

# PONE EL VALOR DE TABLERO.valor_inicial EN TODO EL TABLERO.
def del_xy():
    global TABLERO
    f = TeclD.byTcld( listaStrKeys=['f'], listaDef=[(int, False)], msgIntro='\nIntroduce Fila to Borrar Valor ')    
    c = TeclD.byTcld( listaStrKeys=['c'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Borrar Valor [0, "a", "A"] ')    

# ELIMINA TODA UNA FILA Y DEJA EL VALOR INICIAL DE LA CLASE self.valor_inicial.
def del_fila():
    global TABLERO
    f = TeclD.byTcld( listaStrKeys=['f'], listaDef=[(int, False)], msgIntro='\nIntroduce Fila to Del')        
    fila = TABLERO.get_lst_filas(filaFrom=f['f'], filaTo=f['f'])
    if not fila: return
    # _______________________
    continuar = TeclD.byTcld( listaStrKeys=['if'], listaDef=[(bool, False)], msgIntro=f'\nSeguro que Quieres Continuar?')    
    if continuar['if']==False: print('Crear Anulado... Chaoooo') ; return 

# __________________________________
# ELIMINA TODA UNA COLUMNA Y DEJA EL VALOR INICIAL DE LA CLASE self.valor_inicial.
def del_columna():
    global TABLERO
    c = TeclD.byTcld( listaStrKeys=['c'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Borrar Valor [0, "a", "A"] ')    


def set_marco():
    global TABLERO

# __________________________________
# Llama  a la clase Tablero_Plus que avanza la funcionalidad de Tablero y crea Estructura de Salida tipo Menu
def tablero_plus():
    pass

# Crea un Rango
def crear_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['nm'], listaDef=[(str, False)], msgIntro='\nNombre del  R a n g o  ')    
    c = TeclD.byTcld( listaStrKeys=['cld'], listaDef=[(str, False)], msgIntro='C e l d a   d e   i n i c i o ( A:0 ) ')    
    d = TeclD.byTcld( listaStrKeys=['dim'], listaDef=[(str, False)], msgIntro='D i m e n s i o n ( 3x4 )  ó  C e l d a - F i n  ( M:8 )')  

    rango = Rango(nombre_rango= n['nm'], celda_inicio=c['cld'], dimension=d['dim'] , valor_inicial = '-')    
    if rango: 
        print('RANGO CREADO :)')

def buscar_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, False)], msgIntro='\nNombre del Rango ')    

def eliminar_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, False)], msgIntro='\nNombre del  R a n g o  A Eliminar')    

def ver_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, True)], msgIntro='\nNombre del R a n g o  a Buscar(None = All)')    
    v = TeclD.byTcld( listaStrKeys=['v'], listaDef=[(bool, True)], msgIntro='\nV e r   V a l o r e s ( v )(intro)  |   Ver Datos( f )')    

    if n['n'] == '':
        pass    
    else:       
        pass 

def tablero_to_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, True)], msgIntro='\nNombre del  R a n g o  to Transfer ')    


def rango_to_tablero():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, True)], msgIntro='\nNombre del  R a n g o  to Transfer ')    


def lista_to_rango():
    global TABLERO
    # lista = ['lista', 'de', 'ejemplo']
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, True)], msgIntro='\nNombre del  R a n g o  sobre el que operar')    
    lista = TeclD.byTcld( listaStrKeys=['l'], listaDef=[(str, True)], msgIntro='\nIntroduce los items de la lista separados por comas')    
    cadena = str(lista['l']).strip()
    lst_to_tablero = cadena.split(sep=',')
    if not lst_to_tablero: return 
    lst_to_tablero = [str(item).strip() for item in lst_to_tablero if str(item) != '']
    
# Entra una lista en forma de lista o str separado por comas y lo introduce en el tablero 
# No hace falta rango, lo crea la funcion lista_to_tablero() de forma auxiliar y luego lo elimina
def lista_to_tablero():
    global TABLERO
    str_lista = TeclD.byTcld( listaStrKeys=['l'], listaDef=[(str, True)], msgIntro='\nIntroduce  L i s t a   separada por comas (1,2,3,...)')
    
    celda = TeclD.byTcld( listaStrKeys=['ci'], listaDef=[(str, True)], msgIntro='\nIntroduce C e l d a  en Tablero ( M:8 ) donde colocar la lista ... ')
    
    pos = TeclD.byTcld( listaStrKeys=['pos'], listaDef=[(bool, True)], msgIntro='Lo Quieres Vertical( V ) o Horizontal( F )?')    
    if pos['pos'] == True:
        pass
    else:
        pass


def matriz_to_tablero():
    global TABLERO
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    celda = TeclD.byTcld( listaStrKeys=['ci'], listaDef=[(str, True)], msgIntro='\nIntroduce C e l d a  en Tablero (pejem: M:8 ) donde colocar la matriz ... ')
    

def prueba_recursiva():
    matriz_pruebas = [  ['wIP', 12, '14', 16], 
                        [23 , '25', 27], 
                        [37, "WIP" , '34' ]]
    rango = Rango(nombre_rango= "r2d2", celda_inicio="B:0", dimension="5X5" , valor_inicial = '-')
    print()
    print(rango)
    print('\nV e r   V a l o r e s:\n')
    rango.get_values()
    
    print('\nV e r   R A N G O \n')
    rango.ver_matriz()
    
    print('\nI m p r i m i r    M a x  s/sp  \n')    
    rango.imprimir()
    
    print('\nI m p r i m i r    M a x  c/sp  \n')    
    rango.imprimir(sp_columna=2)
    
    print('\nI m p r i m i r   L i t e r a l  P u r o \n')    
    rango.imprimir( ancho = 0 , sp_columna = 0 )
    
    print('\nI m p r i m i r   F i x e d  s/sp  \n')    
    rango.imprimir( ancho = 2 , sp_columna = 0 )
    
    print('\nI m p r i m i r   F i x e d  c/sp \n')    
    rango.imprimir( ancho = 5 , sp_columna = 1 )
    
    print('\nI m p r i m i r   P e r s o n a l  c/sp \n')    
    rango.imprimir( lista = [5,3,4,1,3,2] , sp_columna = 3 )
    
    print('\nI m p r i m i r   A m b i g u o u s   \n')    
    rango.imprimir( ancho = 15 , lista = [3] , sp_columna = 5 )

    tablero = Tablero(total_columnas_tablero = 15, total_filas_tablero = 10, valor_inicial='-')

    retorno = tablero.push(data_push = matriz_pruebas, celda_inicio = 'C:3' )
    # tablero.push(data_push = [1,2,'3',4,[5,6]], celda_inicio = 'B:1' )
    if retorno:    
        print('\nI m p r i m i r   T a b l e r o   c o n   P u s h \n')
        tablero.imprimir( sp_columna = 3 )
# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls') 
    print('\nI N I C I O')   
    # ---- Empezamos!!
    main() 
    

