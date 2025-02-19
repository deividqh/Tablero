# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # •••••••••  By David Quesada Heredia davidquesadaheredia@gmail.com ••••••••••
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

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
# from classMenuDvd.Tablero import Rangutan as Rangutan
from Tablero import Rango as Rango
from Tablero import Tablero

# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# El Menu de todo Esto mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
from classXindeX.classXindeX import XindeX 

# Cachar Datos Seguros por Teclado 
from classTeclado.Sdata import Sdata

# ====================================================================================
# DEF: Desarrollo y memoria de la clase Tablero. 
# ====================================================================================
# TABLERO = Rangutan(total_columnas_tablero=50, total_filas_tablero=30, valor_inicial='-')
# TABLERO = None
TABLERO = Tablero(total_columnas_tablero = 10, total_filas_tablero = 20, valor_inicial='-')

# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#                               XINDEX 
# 
# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def main():
    # 1 ■■■■■■■■■■ INSTANCIO EL OBJETO XINDEX 
    The_X_Men = XindeX()
    # 2 ■■■■■■■■■■ CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    The_X_Men.addX(titulo='MenuPpal',  padre=None, ipadre=None,  
                    fraseHead="| - M A I N    O V E R   T A B L E R O - "  , 
                    lst_items=[ ("TABLERO" , info_TABLERO) , ('IMPRIMIR', info_IMPRIMIR) , ("GET" , info_GETTING) , ("PUSH" , info_push) , ("DEL" , info_DEL) , ("RANGOS" , info_RANGO) , ('MISCELANEA', None)] 
                    )
    The_X_Men.addX( titulo='SUB_CREAR', padre='MenuPpal' , ipadre="TABLERO"  , lst_items = [("CREAR Tablero",crear_tablero), ("INICIAR Tablero", iniciar_tablero)] )  
    The_X_Men.addX( titulo='SUB_IMPR' , padre='MenuPpal' , ipadre="IMPRIMIR" , lst_items = [("IMPRIMIR Modo Max sin/sp",print_max_ssp),("IMPRIMIR Modo Max con/sp",print_max_csp) , ("IMPRIMIR Modo Literal",print_literal) , ('IMPRIMIR Modo Fixed sin/sp', print_fixed_ssp), ("IMPRIMIR Modo Fixed con/sp",print_fixed_csp), ('IMPRIMIR Modo Personal', print_personal), ('IMPRIMIR Ambbigous', print_ambigous), ('IMPRIMIR RANGO', print_rango)] )
    The_X_Men.addX( titulo='SUB_GET'  , padre='MenuPpal' , ipadre="GET"      , lst_items = [("GETTING Fila",get_fila), ("GETTING Columna",get_columna), ("GETTING Valor By Fila-Columna", get_fila_columna), ("GETTING Valor By Celda(A:0)", get_celda), ("GETTING Matriz Values", get_matriz_values)])
    The_X_Men.addX( titulo='SUB_PUSH' , padre='MenuPpal' , ipadre="PUSH"     , lst_items = [("PUSH MATRIZ",matriz_to_tablero), ("PUSH LISTA", push_lista) ,("PUSH OVER Fila",push_valor_over_fila), ("PUSH OVER Column",push_valor_over_columna), ('PUSH Valor By Celda (C:3)', push_celda), ('PUSH valor by fila / columna', push_fila_columna)] )
    The_X_Men.addX( titulo='SUB_DEL'  , padre='MenuPpal' , ipadre="DEL"      , lst_items = [("DEL Fila Over TABLERO",del_fila), ("Del Column",del_columna), ("Del Celda", del_celda)] )    
    The_X_Men.addX( titulo='SUB_RANGOS', padre='MenuPpal', ipadre="RANGOS"   , lst_items = [("CREAR Rango",crear_rango), ("BUSCAR Rango",buscar_rango), ("ELIMINAR Rango",delete_rango) , ('VER INFO Rangos Tablero', ver_info_rangos), ('PULL TO RANGO', pull)] )  
    The_X_Men.addX( titulo='SUB_MISC'  , padre='MenuPpal', ipadre="MISCELANEA" , lst_items=[("Prueba Impresion Masiva" , impresion_masiva), ('ULTIMA FILA USADA', last_fila_used)] )    

    # 3 ■■■■■■■■■■ LLAMO A MYSTYCA PARA VISUALIZAR EL MENU 
    retorno = The_X_Men.Mystyca(titulo='MenuPpal', configurado=True, execFunc=True, tipo_marcador='a', execAll=True, Loop=True , padX=50)
    # 4 ■■■■■■■■■■ SALE DEL MENU ________________________________________________________________
    print(f"::: THE END en MAIN() ::: {retorno if retorno else 'no retorno'} ")    
    

# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  TABLERO  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_TABLERO():
    print(""" 
        ■■■■■■■■  I N F O R M E   T A B L E R O    ■■■■■■■■

        TABLERO CREA UN MARCO DE CELDAS VIRTUALES DONDE SE PUEDEN  IMPRIMIR, OBTENER Y DEVOLVER DATOS EN MÚLTIPLES FORMATOS EN EL SCREEN.
        BRACKETS, CREA UN TABLERO CON HEAD, BODY Y PIE .... SIRVE PARA XindeX.
        BADAT, CREA UN TABLERO PARA VISUALIZAR LOS DATOS DE LAS TABLAS DE UNA BASE DE DATOS..... ON PROYECT ;)

        Puedes: 
        ■ [Crear] Tableros: Crea un marco para imprimir datos. Es un Rango, que a su vez es un Conjunto Ordenado y con nombre de Objetos Celdas.
        ■ [Crear] Brackets: Crea un Marco con Límites y 3 secciones: Head, Body, Pie
        ■ [Iniciar] un Tablero: con un valor de inicio para todas las celdas del tablero. 
        ■ [Imprimir] el Tablero en Multiples Formatos.
        ■ [getting] (datos , listas o matrices de valores) o (celdas o listas de celdas o matrices de celdas)
        ■ [push], Pone datos en el tablero. Sobre filas, columnas, celdas y los datos pueden ser datos, listas , matrices.
        ■ CRUD de [Rangos internos].
        ■ [pull] del tablero hacia un Rango
        ■ [borrar] filas, columnas, celdas

    """)

# CREA UN TABLERO Y BORRA EL ANTERIOR.
def crear_tablero(): 
    global TABLERO
    print()
    f_c = Sdata.get_data( key_dict='filas', tipo=int, permite_nulo=False, msg_entrada='\nIntroduce numero de Filas')
    f_c = Sdata.get_data( dicc= f_c, key_dict='columnas', tipo=int, permite_nulo=False, msg_entrada='\nIntroduce numero de columnas')
    # _______________________
    # Pregunta de Seguridad
    continuar = Sdata.get_data( key_dict='if', tipo=bool, permite_nulo = True , msg_entrada=f'\nSeguro que Quieres Continuar?')    
    if continuar['if']==False: 
        print('Crear Anulado... Chaoooo')
        return
    TABLERO = Tablero(total_columnas_tablero = f_c['columnas'], total_filas_tablero = f_c['filas'], valor_inicial='-')
    print('\nCREAR TABLERO ;)\n')

# PONE EL MISMO VALOR EN TODO EL TABLERO.
def iniciar_tablero():
    global TABLERO 
    val = Sdata.get_data( key_dict='val', tipo=str, permite_nulo = True , msg_entrada='\nValor Inicial (este Valor Se pondrá en toda la Tabla) ')    
    # Seguridad_____________
    continuar = Sdata.get_data( key_dict='if', tipo=str, permite_nulo = True , msg_entrada=f'\nSeguro que Quieres Continuar?')    
    if continuar['if']==False: 
        print('Iniciar Anulado... Chaoooo\n')
        return
    TABLERO.iniciar(valor = val['val'])

# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  IMPRIMIR  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_IMPRIMIR():
    print(""" 
        ■■■■■■■■  I N F O R M E   I M P R I M I R    ■■■■■■■■

        Imprime el Rango con configuracion. Es la base de impresion sobre todo. 
        [sp_columna] (int): el espacio entre columnas
        [**kwargs] (dict):  
            ■ [ancho](int)  = ancho de columna fixed or 
            ■ [lista](list) = lista de anchos para cada columna. 
        Ejemplos:
        ■ imprimir( ) => ajusta al maximo de cada columna ( MAX-sin/sp )
        ■ imprimir( sp_columna = 2 ) => maximo de cada columna ( MAX-con/sp )        
        ■ imprimir( ancho = 0 , sp_columna = 0 ) => ( LITERAL PURO ) ....XindeX
        ■ mprimir( ancho = 0 , sp_columna = 2 ) => (LITERAL) (sin espacio para las celdas pero con espacio entre las columnas.)(No muy usado)
        ■ imprimir( ancho = 15 , sp_columna = 5 ) => columnas al 15 todas. █ sp_columna = 5: espacio entre columnas de 5 char
        ■ imprimir( lista = [0,1,5,4,3,2] , sp_columna = 5 ) => cada columna a su ajuste personalizado y si falta de la lista al max █ 5 entre columnas
        ■ imprimir( ancho = 15 , lista = [0,1,5,4,3,2] , sp_columna = 3 ) => cada columna a la lista y si falta el resto al ancho=15. █ deja 3 entre columnas.

    """)

def print_max_ssp():
    global TABLERO
    # print() 
    # val = Sdata.get_data( key_dict='val', tipo=int, permite_nulo = True , msg_entrada='\nTamaño Columna (0 by def)')    
    print('\nI m p r i m i r    M a x  s/sp')    
    print('ancho columna = MAX  |  sp_columna = 0')    
    
    TABLERO.imprimir()

def print_max_csp():
    global TABLERO  
    dat = Sdata.get_data( key_dict='P', tipo = int , permite_nulo = True , msg_entrada='\nINTRODUCE EL ESPACIO ENNTRE LAS COLUMNAS')        
    print('\nI m p r i m i r    M a x  c/sp')    
    
    TABLERO.imprimir(sp_columna = dat['P'])    
def print_literal():
    global TABLERO  
    print('\nI m p r i m i r   L i t e r a l  P u r o')    
    print('ancho columna = 0  |  sp_columna = 0')

    TABLERO.imprimir( ancho = 0 , sp_columna = 0 )
def print_fixed_ssp():
    global TABLERO  
    print('\nI m p r i m i r   F i x e d  s/sp\n')    
    print('sp_columna = 0')
    
    dat = Sdata.get_data( key_dict='x', tipo=int, permite_nulo = True , msg_entrada='\nINTRODUCE EL ANCHO DE  COLUMNA')

    TABLERO.imprimir( ancho = dat['x'] , sp_columna = 0 )

def print_fixed_csp():
    global TABLERO  
    print('\nI m p r i m i r   F i x e d  c/sp\n')    
    dat = Sdata.get_data( key_dict='A', tipo=int, permite_nulo = True , msg_entrada='\nINTRODUCE EL ANCHO DE  COLUMNA ')
    dat = Sdata.get_data( dicc= dat, key_dict='B', tipo=int, permite_nulo = True , msg_entrada='\nINTRODUCE EL ESPACIO ENNTRE LAS COLUMNAS ')

    TABLERO.imprimir( ancho = dat['A'] , sp_columna = dat['B'] )

def print_personal():
    global TABLERO  
    print('\nI m p r i m i r   P e r s o n a l  c/sp \n')    
    print(f'lista = [5,3,4,1,3,2]  |  sp_columna = 3')
    
    TABLERO.imprimir( lista = [5,3,4,1,3,2] , sp_columna = 3 )

def print_ambigous():
    global TABLERO  
    print('\nI m p r i m i r   A m b i g u o u s\n')    
    print(f'lista = [3, 4, 6]  |   sp_columna = 5')
    
    TABLERO.imprimir( ancho = 3 , lista = [3, 4, 6] , sp_columna = 5 )

def print_rango():
    dat = Sdata.get_data( key_dict='R', tipo=str, permite_nulo = False , msg_entrada='\nINTRODUCE EL RANGO A IMPRIMIR')
    
    rango = TABLERO.buscar_rango(nombre_rango = dat['R'])
    if not rango:
        print(f'Rango {dat['R']} NOT FOUND :(  ')
        return
    rango.imprimir(sp_columna = 5)  # maximo de la columna con espacio entre columnas


# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  GETTING  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_GETTING():
    print(""" 
        ■■■■■■■■  I N F O R M E   G E T T I N G    ■■■■■■■■

        OBTENEMOS DATOS DEL TABLERO.

        ■ getting = TABLERO.getting( celda = 'C:2' , b_valor=True )  => Devuelve el valor de la celda. el Valor va Tipado.
        ■ getting = TABLERO.getting( celda = 'C:2' , b_valor=False ) => Devuelve el Objeto Celda.
        
        ■ getting = TABLERO.getting( fila = 2 , columna= 3 , b_valor=False )  => Devuelve el Objeto Celda.
        ■ getting = TABLERO.getting( fila = 2, columna = 3 , b_valor=True )   => Devuleve el valor de la celda definida por fila y columna.

        ■ getting = TABLERO.getting( fila = 2 , fila_to = 5 , b_valor=True )    => Devuelve una matriz de filas de valores desde 'fila' hasta 'fila_to'
        ■ getting = TABLERO.getting( fila = 2 , fila_to = 5 , b_valor=False )   => Devuelve una matriz de filas de celdas desde 'fila' hasta 'fila_to' 

        ■ getting = TABLERO.getting( columna = 2 , columna_to = 5 , b_valor = True  ) => Devuelve una matriz de columnas de valores desde 'columna' hasta 'columna_to'
        ■ getting = TABLERO.getting( columna = 2 , columna_to = 5 , b_valor = False ) => Devuelve una matriz de columnas de celdas desde 'columna' hasta 'columna_to'

        ■ get_values() => Devuelve la matriz de valores de tablero.(list de list)
        ■ get_lst_rangos()  => Devuelve la lista de los rangos usados en tablero (todos los de fila y columna como minimo.)


    """)
# RETORNA UN VALOR DEL TABLERO CUANDO INTRODUCES UNA Cimprime_a_caponELDA (A:0, C:3)
def get_celda():
    cel_v = Sdata.get_data( key_dict='celda', tipo=str, permite_nulo = True , msg_entrada='INTRODUCE CELDA ')
    cel_v = Sdata.get_data(dicc=cel_v , key_dict='elige', tipo='BETWEEN', permite_nulo = True , msg_entrada='Elige Entre: VALOR = 1 , CELDA = 2', valores_between=[1,2])

    if cel_v['elige'] == 1:
        getting = TABLERO.getting( celda = cel_v['celda'] , b_valor=True )
    elif cel_v['elige'] == 2:
        getting = TABLERO.getting( celda = cel_v['celda'] , b_valor=False )
    else:
        return None

    print(getting) if getting else f'GET CELDA :('

# OBTIENE UN VALOR DEL TABLERO x FILA Y COLUMNA
def get_fila_columna(): 
    global TABLERO
    fc = Sdata.get_data( key_dict='f', tipo=int ,  permite_nulo=False, msg_entrada='INTRODUCE FILA ')    
    fc = Sdata.get_data( dicc = fc, key_dict='c', tipo=int ,  permite_nulo=False, msg_entrada='INTRODUCE COLUMNA ')    
    getting = TABLERO.getting( fila=fc['f'], columna=fc['c'], b_valor=False )
    print(getting) if getting else f'GETTING :('

# OBTIENE UNA FILA
def get_fila():
    global TABLERO
    print('OBTIENE UNA LISTA DE DICCIONARIO DE UNA FILA ENTERA')
    dh = Sdata.get_data( key_dict='fd', tipo=int ,  permite_nulo=False, msg_entrada ='(Get Fila) INTRODUCE FILA DESDE ')    
    dh = Sdata.get_data( dicc=dh , key_dict='fh', tipo=int ,  permite_nulo=False, msg_entrada='(Get Fila) INTRODUCE FILA HASTA ')    

    getting = TABLERO.getting( fila=dh['fd'], fila_to=dh['fh'], b_valor=True )
    print(getting) if getting else f'GETTING :('

# OBTIENE UNA COLUMNA
def get_columna():
    global TABLERO
    col = Sdata.get_data( key_dict='f', tipo=int, msg_entrada='(GET COLUMNA )INTRODUCE COLUMNA DESDE')    
    col = Sdata.get_data( dicc= col, key_dict='t', tipo=int, msg_entrada='(GET COLUMNA )INTRODUCE COLUMNA HASTA')    

    # lst_columnas = TABLERO.get_columnas(columna_from=col['f'], columna_to=col['t'], b_valor=True)
    getting = TABLERO.getting( columna=col['f'], columna_to=col['t'], b_valor=True )
    print (getting) if getting else f'GET COLUMNAS :('

def get_matriz_values():
    global TABLERO
    lst_values = TABLERO.get_values()
    print(lst_values)


# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  DEL  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_DEL():
    print(""" 
        ■■■■■■■■  I N F O R M E   D E L E T E   ■■■■■■■■

        ELIMINA LOS DATOS DEL TABLERO PONIENDO EL VALOR_INICIAL DE TABLERO.
        SE PUEDEN ELIMINAR:
        ■ Valores en Objeto Celda   ==> TABLERO.delet e(fila = 2 , columna = 3 )  █   TABLERO.delet e(fila = 2 , columna = 'C' )
        ■ Valores en Columna        ==> TABLERO.delet e(columna = 3)   █   TABLERO.delet e(columna = 'C')
        ■ Valores en Fila           ==> TABLERO.delet e(fila=2)
        ■ Valores en Rango          ==> TABLERO.delet e(rango = 'nombre_rango_1')    █   TABLERO.delet e(rango = Rango1)  
        ■ Rango                     ==> TABLERO.delet e(rango = 'nombre_rango_1', b_rango=True)   █   TABLERO.delet e(rango = Rango1, b_rango=True)
    
    """)
# PONE EL VALOR DE TABLERO.valor_inicial EN TODO EL TABLERO.
def del_celda():
    global TABLERO
    dat = Sdata.get_data( key_dict='F', tipo=int, msg_entrada='INTRODUCE FILA A BORRAR')    
    dat = Sdata.get_data( dicc = dat, key_dict='C', tipo=str, msg_entrada='INTRODUCE COLUMNA A BORRAR [0, "a", "A"] ')
    
    # OBTENEMOS LA CELDA DEL TABLERO
    celda = TABLERO.getting(fila=dat['F'], columna=dat['C'])    # b_valor = False byDef
    if not celda: return

    # LE PONEMOS EL VALOR INICIAL EN SU LUGAR
    
    TABLERO.delete(fila=dat['F'], columna=dat['C'])
    # TABLERO.push(data_push=TABLERO.get_valor_inicial(), celda_inicio=celda.nombre_celda)

# ELIMINA LOS VALORES DE TODA UNA FILA Y DEJA EL VALOR INICIAL
def del_fila():
    global TABLERO
    dat = Sdata.get_data( key_dict='F', tipo=int, msg_entrada='INTRODUCE FILA TO DEL')        
    
    # ■■ OBTENGO LA FILA A BORRAR. AQUÍ SE PODRÍAN ELIMINAR VARIAS FILAS A LA VEZ.
    matriz = TABLERO.getting(fila=dat['F'], fila_to=dat['F'] , b_valor = False )
    if not matriz: return    

    # UN AVISO AL ELIMINAR, ES CORTESÍA
    dat = Sdata.get_data( dicc = dat, key_dict='IF', tipo=bool, msg_entrada=f'\nSeguro que Quieres Continuar?')        
    if dat['IF']==False: 
        print('Crear Anulado... Chaoooo') 
        return 
    # ■■ OPERO. TB PUEDO HACER UN PUSH DEL VALOR INICIAL SOBRE LA FILA CON REPETIR = TRUE 
    TABLERO.delete(fila=dat['F'])
    # for fila in matriz:
    #     for celda in fila:
    #         celda.valor = TABLERO.get_valor_inicial()

# ELIMINA LOS VALORES DE TODA UNA COLUMNA Y DEJA EL VALOR INICIAL
# USO OTRO MÉTODO(PUSH) DISTINTO QUE EN DEL_FILA (OPERO)
def del_columna():
    global TABLERO
    dat = Sdata.get_data( key_dict='C', tipo=str, msg_entrada='INTRODUCE LA COLUMNA A BORRAR [0, "a", "A"] ')    
    celda = TABLERO.get_celda(fila=0, columna=dat['C'])
    if not celda: 
        return
    # UN AVISO AL ELIMINAR, ES CORTESÍA
    dat = Sdata.get_data( dicc = dat, key_dict='IF', tipo=bool, msg_entrada=f'\nSeguro que Quieres Continuar?')        
    if dat['IF']==False: 
        print('Crear Anulado... Chaoooo') 
        return 

    TABLERO.delete(columna = celda.columna)
    # TABLERO.push(data_push=TABLERO.get_valor_inicial(), celda_inicio=f'{celda.letra}:0', b_lineal=False, repetir=True, eje='Y')



# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  RANGO  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_RANGO():
    print(""" 
        ■■■■■■■■  I N F O R M E   R A N G O   ■■■■■■■■
    GESTIONA LA LISTA lst_rangos del Objeto TABLERO.

    • [crear_rango] Dentro del Objeto TABLERO se pueden creaar Objetos Rango() .... self.lst_rangos(list)
                  Se necesita un nombre(str) y una dimension(str) que puede ser: celda_fin  ó  filasXcolumnas
                  [valor_entrada] Se va a introducir siempre 'plano' si es un iterable y su valor si no es iterable. puede ser una matriz.
    
    • [buscar_rango] = Da informacion sobre el objeto rango. Si No se introduce el Nombre del rango, Da información sobre el Tablero.
    
    • [delet e_rango] = Elimina un Objeto Rango de self.lst_rangos. Devuelve el objeto Rango.
    
    • [ver_info_rangos] = Da información de los rangos de TABLERO. puedes filtrar X  like_name y X  flag   para el listado.
    
    • [pull] = Lleva los datos desde TABLERO hasta el rango pasado como argumento.
    
    • [pull_All] = Lleva los datos desde TABLERO hasta todos los rangos. Admite FILTRO LIKE para nombre.

    """)

#  CREACION DE UN RANGO DENTRO DE TABLERO
def crear_rango():
    global TABLERO
    dat = Sdata.get_data( key_dict='R', tipo=str, msg_entrada='NOMBRE DEL RANGO')    
    dat = Sdata.get_data( dicc= dat, key_dict='C', tipo=str, msg_entrada='CELDA DE INICIO ( A:0 ) ')    
    dat = Sdata.get_data( dicc= dat, key_dict='D', tipo=str, msg_entrada='DIMENSION ( 3x4 ) ó  CELDA-FIN ( M:8 )')  

    # rango = Rango(nombre_rango = dat['nm'], celda_inicio = dat['cld'], dimension = dat['dim'] , valor_inicial = '-') 

    # print('RANGO CREADO :)') if rango else f'REVISA LOS DATOS DE ENTRADA, EL RANGO NO HA SIDO CREADO :('

    rango = TABLERO.crear_rango(nombre=dat['R'], celda_inicio=dat['C'], dimension=dat['D'])
    print('RANGO CREADO :)') if rango else f'REVISA LOS DATOS DE ENTRADA, EL RANGO NO HA SIDO CREADO :('

# BUSCAR UN RANGO POR NOMBRE
def buscar_rango():
    global TABLERO
    dat = Sdata.get_data( key_dict='n', tipo=str, msg_entrada='NOMBRE DEL RANGO A BUSCAR', permite_nulo=True)    
    if dat['n'] == '':
        print(TABLERO)
    else:
        rango = TABLERO.buscar_rango(nombre_rango=dat['n'])
        print (rango) if rango else f'BUSCAR RANGO :('

def delete_rango():
    global TABLERO
    dat = Sdata.get_data( key_dict='R', tipo=str, msg_entrada='NOMBRE DEL RANGO A ELIMINAR')    
    # rango = TABLERO.delete_rango(rango = dat['R'])
    retorno = TABLERO.delete(rango=dat['R'], b_rango=True)
    print(retorno) if retorno else f'BORRAR RANGO :('

def ver_info_rangos():
    global TABLERO
    dat = Sdata.get_data( key_dict='N', tipo=str, msg_entrada='NOMBRE DEL RANGO A BUSCAR', permite_nulo=True)    
    dat = Sdata.get_data( dicc = dat, key_dict='L', tipo=str, msg_entrada='LIKE NAME', permite_nulo=True)    
    dat = Sdata.get_data( dicc = dat, key_dict='F', tipo=str, msg_entrada='FLAG', permite_nulo=True)    
    TABLERO.ver_rangos(nombre_rango = dat['N'] , like_name = dat['L'] , flag = dat['F'])
       
def pull():    
    global TABLERO
    dat = Sdata.get_data( key_dict='R', tipo=str, msg_entrada='NOMBRE DEL RANGO A BUSCAR( NULL = ALL )', permite_nulo=True)    

    if dat['R'] == '':       # BUSCA TODOS LOS RANGOS
        TABLERO.pull_all()
    else:
        TABLERO.pull(rango = dat['R'])



# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  PUSH  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_push():
    print(""" 
        ■■■■■■■■  I N F O R M E   P U S H  ■■■■■■■■


        
        CREA UN RANGO CON data_push EN CELDA_INICIO, LO FORMATEA SEGUN  b_lineal, eje y repetir. 
        
        [data_push](any, matriz): LOS DATOS PUEDEN SER TIPOS PYTHON, ITERADORES(LIST, TUPLE, SET), MATRICES.
        [celda_inicio](Objeto Celda) Celda de inicio del Rango donde se va a introducir data_push. 
                                     Entra como objeto para tener acceso a filas y columnas para formar las dimensiones para el Rango.
        ■■  'EJE' = 'X' o 'Y'  ■ solo en caso de que data_push sea list.
        ■■  'REPETIR': True, False ■ solo en caso de que data_push sea str 
        ■■  b_lineal: True, si se hace el cruce lineal (como vengan las celdas en linea)(self.__push_plana)
                    False, Si el cruce Celda a Celda coincidente(self.cross())
                                        
                    En caso de que data_push sea un str, se puede introducir:
                    'H' para REPETIR data_push horizontalmente celda_inicio hasta fin linea
                    'V', para REPETIR data_push verticalmente  desde celda_inicio hasta fin columna.

        • LOS ARGUMENTOS ( excepto data_push ) VIENEN VALIDADOS DE self.push().
        • CREO UN OBJETO ■ Rango  CON ■ data_push CON ■ celda_inicio  COMO PRIMERA CELDA DEL RANGO.
        • EN EL RANGO SIEMPRE SE METEN LOS DATOS DE FORMA PLANA.
        ENTONCES LO QUE HAGO ES JUGAR CON LAS ■ DIMENSIONES  PARA CONTROLAR COMO ENTRAN LOS DATOS EN EL RANGO. 
        • PARA MATRICES, A VECES, HAY QUE HACER RELLENOS, QUE SE HACEN CON self.valor_inicial
        • HAY 10 TIPOS DE OBJETOS RANGOS DISTINTOS QUE SE PUEDEN FORMAR:
        ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        █ 1- MATRIZ_LINEAL  █ 2- MATRIZ_CUADRADA     █ 3- RANGO-RANGO             █ 4- LISTA_VERTICAL      █ 5-  LISTA_HORIZONTAL                  █
        █ 6- STR_CELDA      █ 7- STR_REPETIDO_FILA   █ 8- STR_REPETIDO_COLUMNA    █ 9- STR_TO_LISTAWORDS   █ 10- X_TO_CELDA (int, float, bool,...) █
        ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
         
        ■■■ TABLERO.push( data_push = '◙◙◙' )  ▓  celda_inicio = 'A:0' ▓ b_lineal = False ▓ repetir = False ▓ eje = 'X'
            SI MATRIZ ◙◙◙   Mete la matriz en 'A:0' de forma matricial. ni ■ eje ni ■ repetir tienen efecto.
            SI LIST   ◙◙◙   Mete la lista de forma Horizontal. 
            SI STR    ◙◙◙   Intro 'Loren Ipsum' desde A:0  ocupando una celda.
            SI OTRO   ◙◙◙   Intro X desde A:0 ocupando una celda.
        
        ■■■ TABLERO.push( data_push = '◙◙◙' , celda_inicio = 'C:3')   ▓ b_lineal = False  ▓ repetir = False ▓ eje = 'X'
            SI MATRIZ ◙◙◙   Mete la matriz en 'C:3' de forma matricial. ni ■ eje ni ■ repetir tienen efecto.
            SI LIST   ◙◙◙   Mete la lista de forma Horizontal.
            SI STR    ◙◙◙   Intro 'Loren Ipsum' desde A:0  ocupando una celda.
            SI OTRO   ◙◙◙   Intro X desde A:0 ocupando una celda.
        
        ■■■ TABLERO.push( data_push = '◙◙◙', celda_inicio = 'C:3' , b_lineal = False )    ▓ repetir = False ▓ eje = 'X'
            SI MATRIZ ◙◙◙   Mete la matriz en C:3 de Forma MATRICIAL (b_lineal = False ). ni ■ eje ni ■ repetir tienen efecto.
            SI LIST   ◙◙◙   Mete la list(items separados por comas) en C:3 , b_lineal no le afecta(una lista siempre es plana), si eje = None, en list pasa a 'X' (horizontal) byDef 
            SI STR    ◙◙◙   Mete el str en C:3. 
                            Si b_lineal = False (byDef) introduce la cadena en la celda. 
            SI OTRO   ◙◙◙   Mete X en C:3.
        
        ■■■ TABLERO.push( data_push = '◙◙◙', celda_inicio = 'C:3' , b_lineal = True)      ▓ repetir = False ▓ eje = 'X'
            SI MATRIZ ◙◙◙   Mete la matriz en C:3 de Forma LINEAL (b_lineal = True ). ni ■ eje ni ■ repetir tienen efecto.
            SI LIST   ◙◙◙   Mete la list(items separados por comas) en C:3 , b_lineal no le afecta(una lista siempre es plana), 
                            Si eje = None es 'X' (horizontal) byDef 
            SI STR    ◙◙◙   Si b_lineal = True introduce la cadena separando las palabras como una lista a partir de la celda en el eje X. DIMESION 1 X n
            SI OTRO   ◙◙◙   Mete X en C:3. [eje] no le afecta. [repetir] no le afecta. [b_lineal] no le afecta. DIMESION 1 X 1
        
        ■■■ TABLERO.push( data_push = '◙◙◙', celda_inicio = 'C:3', b_lineal = True ,  eje = 'Y' , repetir = True  ) 
            SI MATRIZ ◙◙◙   Mete la matriz en C:3 de forma LINEAL pero manteniendo la Matriz. ni ■ eje ni ■ repetir tienen efecto.
                            Coge los items de entrada en plano y los mete en la matriz con la dimension según las filas y columnas de data_push.(no ideal)
                            ni [eje] ni [repetir] le afectan. DIMESION n X m
            SI LIST   ◙◙◙   Mete la List en C:3. [eje] = 'Y' mete la lista VERTICAL. [repetir] no le afecta. DIMESION n x 1
            SI STR    ◙◙◙   Mete el str en C:3. [eje] = 'Y' no le afecta. [repetir] hace que repita el string  desde C:3 hasta el final de la fila.
            SI OTRO   ◙◙◙   Mete X en C:3. [eje] 'Y' no le afecta. [repetir] no le afecta. [b_lineal] no le afecta. DIMESION 1X1
        
        ■■■ TABLERO.push(data_push = '◙◙◙', celda_inicio = 'C:3', b_lineal = False, eje = 'X' , repetir = True )  
            SI MATRIZ ◙◙◙ Mete la matriz de forma MATRICIAL. ni ■ eje ni ■ repetir tienen efecto.   DIMESION n X m
            SI LIST   ◙◙◙ Mete la lista de forma lineal sobre el eje X (HORIZONTL). ■ b_lineal no tiene efecto pq una LISTA siempre es LINEAL. DIMESION 1 X n
            SI STR    ◙◙◙ Mete el string en la celda de inicio. DIMESION 1X1 
            SI OTRO   ◙◙◙ Mete el datoX(int, float, bool) en la celda de inicio. DIMESION 1X1
        
        ■■■ TABLERO.push(data_push = '◙◙◙', celda_inicio = 'C:3', b_lineal = False, eje = 'X'   )  ▓ repetir = False
            SI MATRIZ ◙◙◙ Mete la matriz de forma MATRICIAL. ni ■ eje ni ■ repetir tienen efecto. DIMESION n X m
            SI LIST   ◙◙◙ Mete la lista de forma lineal sobre el eje X (HORIZONTL)  DIMESION 1Xn
            SI STR    ◙◙◙ Mete el string en la celda de inicio.                  DIMESION 1X1
            SI OTRO   ◙◙◙ Mete el datoX(int, float, bool) en la celda de inicio. DIMESION 1X1
        
        ■■■ TABLERO.push(data_push = '◙◙◙', celda_inicio = 'C:3', b_lineal = False, eje = 'Y'   )  ▓ repetir = False
            SI MATRIZ ◙◙◙ Mete la matriz de forma LINEAL (le da igual la estructura de datos, los va a aplanar y meter uno x uno en la matriz.)
            SI LIST   ◙◙◙ Mete la lista de forma lineal sobre el eje Y (VERTICAL)
            SI STR    ◙◙◙ Mete el string en la celda de inicio. ni ■ eje ni ■ repetir tienen efecto.
            SI OTRO   ◙◙◙ Mete el datoX(int, float, bool) en la celda de inicio. ni ■ eje ni ■ repetir tienen efecto.
    
    """)

# PUSH MATRIZ
def matriz_to_tablero():
    global TABLERO
    matriz = [
        [1, 2, 3],
        [4, 5,6, 0],
        [7, 8, 9]
    ]
    dat = Sdata.get_data( key_dict='C', tipo=str, permite_nulo=True, msg_entrada='INTRODUCE CELDA (pejem: M:8 ) Xa Posicionar la MATRIZ')
    retorno = TABLERO.push(data_push = matriz , celda_inicio = dat['C'] )
    if retorno:    
        print('\nMATRIZ TO TABLERO\n')
        TABLERO.imprimir( sp_columna = 3 )

# ESTABLECE UN VALOR EN UNA CELDA PIDIENDO FILA Y COLUMNA
def push_fila_columna():      
    global TABLERO
    dat = Sdata.get_data( key_dict='F', tipo=int, permite_nulo=False, msg_entrada='INTRODUCE FILA TO PUSH')
    dat = Sdata.get_data( dicc=dat, key_dict='C' , tipo=int, permite_nulo=False, msg_entrada='INTRODUCE COLUMNA TO PUSH')
    dat = Sdata.get_data( dicc=dat, key_dict='V', tipo=str, permite_nulo=False, msg_entrada='INTRODUCE VALOR')
    
    celda_inicio = TABLERO.getting(fila = dat['F'], columna = dat['C'])

    if celda_inicio:
        TABLERO.push(data_push = dat['V'], celda_inicio = celda_inicio.nombre_celda , b_lineal=False )

# ESTABLECE UN VALOR EN UNA CELDA (A:0)
def push_celda():
    global TABLERO
    dat = Sdata.get_data( key_dict='C', tipo=str, permite_nulo=True, msg_entrada='INTRODUCE CELDA TO PUSH')
    dat = Sdata.get_data( dicc=dat,  key_dict='V', tipo=str, permite_nulo=True, msg_entrada='INTRODUCE VALOR')
    dat = Sdata.get_data( dicc=dat , key_dict='CL', tipo='between' , msg_entrada='Elige Entre: (L)ista ó (C)adena', permite_nulo=False, valores_between=['L','C'])    
    
    b_lineal = False
    if dat['CL'] == 'L':
        b_lineal = True
    elif dat['CL'] == 'C':
        b_lineal = False

    TABLERO.push(data_push = dat['V'], celda_inicio = dat['C'] , b_lineal = b_lineal)

# ESTABLECE UN VALOR EN UNA FILA
def push_valor_over_fila():
    global TABLERO
    dat = Sdata.get_data( key_dict='F', tipo=int, permite_nulo=False , msg_entrada='INTRODUCE FILA TO PUSH')            
    dat = Sdata.get_data( dicc=dat,  key_dict='V', tipo=str, permite_nulo=True, msg_entrada=f'INTRODUCE VALOR')    
    
    # celda_inicio = f'{TABLERO.celda_inicio.letra}:{dat['F']}'
    celda_inicio = TABLERO.getting(celda=f'{TABLERO.celda_inicio.letra}:{dat['F']}')    

    if celda_inicio:
        TABLERO.push(data_push = dat['V'], celda_inicio = celda_inicio.nombre_celda, b_lineal=False, eje='X' , repetir = True )
    
# ESTABLECE UNA COLUMNA
def push_valor_over_columna():
    global TABLERO
    dat = Sdata.get_data( key_dict='C', tipo=int, permite_nulo=False, msg_entrada='INTRODUCE COLUMNA TO PUSH')    
    dat = Sdata.get_data( dicc=dat, key_dict='V', tipo=str, permite_nulo=False, msg_entrada=f'INTRODUCE VALOR')    
            
    celda_inicio = TABLERO.getting(columna=dat['C'], fila=0)

    if celda_inicio:
        TABLERO.push(data_push = dat['V'], celda_inicio = celda_inicio.nombre_celda, b_lineal=False, eje='Y' , repetir = True  )

def push_lista():
    global TABLERO
    b_lineal = None
    dat = Sdata.get_data( key_dict='L', tipo=list , msg_entrada='INTRODUCE LISTA SEPARANDO POR COMAS (1,2,3,...)', permite_nulo=False)
    dat = Sdata.get_data( dicc=dat , key_dict='i', tipo=str , msg_entrada='INTRODUCE CELDA DE INICIO', permite_nulo=False)
    dat = Sdata.get_data( dicc=dat , key_dict='VH', tipo='between' , msg_entrada=['(Y)VERTICAL', '(X)HORIZONTAL'], permite_nulo=False, valores_between=['X','Y'])    
    
    # if dat['VH'] == 'V':
    #     b_lineal = True
    # else:
    #     b_lineal = False
    TABLERO.push(data_push=dat['L'], celda_inicio=dat['i'] , b_lineal=True, eje = dat['VH'])

def last_fila_used():
    global TABLERO
    ultima_fila_usada = TABLERO.last_fila_used()
    print(f'\nULTIMA FILA USADA = {ultima_fila_usada}')

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

def impresion_masiva():
    global TABLERO
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

    # retorno = tablero.push(data_push = matriz_pruebas, celda_inicio = 'C:3' )
    retorno = tablero.push(data_push = matriz_pruebas, celda_inicio = 'A:1' )
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
    

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # •••••••••  By David Quesada Heredia davidquesadaheredia@gmail.com ••••••••••
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■