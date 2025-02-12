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
from classTeclado.Sdata import Sdata
# ____________________________________________________________
# Para validar: mail, valores entre, fechas... 
from classTeclado.validator import StringTo as VAL

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
                    lst_items=[ ("TABLERO" , None) , ('IMPRIMIR', None) , ("GET" , None) , ("PUSH" , info_push) , ("DEL" , None) , ("RANGOS" , None) , ('MISCELANEA', None)] 
                    )
    The_X_Men.addX( titulo='SUB_CREAR', padre='MenuPpal' , ipadre="TABLERO"  , lst_items = [("CREAR Tablero",crear_tablero), ("INICIAR Tablero", iniciar_tablero)] )  
    The_X_Men.addX( titulo='SUB_IMPR' , padre='MenuPpal' , ipadre="IMPRIMIR" , lst_items = [("IMPRIMIR Modo Max sin/sp",print_max_ssp),("IMPRIMIR Modo Max con/sp",print_max_csp) , ("IMPRIMIR Modo Literal",print_literal) , ('IMPRIMIR Modo Fixed sin/sp', print_fixed_ssp), ("IMPRIMIR Modo Fixed con/sp",print_fixed_csp), ('IMPRIMIR Modo Personal', print_personal), ('IMPRIMIR Ambbigous', print_ambigous)] )
    The_X_Men.addX( titulo='SUB_GET'  , padre='MenuPpal' , ipadre="GET"      , lst_items = [("GETTING Fila",get_fila), ("GETTING Columna",get_columna), ("GETTING Valor By Fila-Columna", get_fila_columna), ("GETTING Valor By Celda(A:0)", get_celda), ("GETTING Matriz Values", get_matriz_values)])
    The_X_Men.addX( titulo='SUB_PUSH' , padre='MenuPpal' , ipadre="PUSH"     , lst_items = [("PUSH MATRIZ",matriz_to_tablero), ("PUSH LISTA", push_lista) ,("PUSH OVER Fila",push_valor_over_fila), ("PUSH OVER Column",push_valor_over_columna), ('PUSH Valor By Celda (C:3)', push_celda), ('PUSH valor by fila / columna', push_fila_columna)] )
    The_X_Men.addX( titulo='SUB_DEL'  , padre='MenuPpal' , ipadre="DEL"      , lst_items = [("DEL Fila Over TABLERO",del_fila), ("Del Column",del_columna), ("Del Celda", del_celda)] )    
    The_X_Men.addX( titulo='SUB_RANGOS', padre='MenuPpal', ipadre="RANGOS"   , lst_items = [("CREAR Rango",crear_rango), ("BUSCAR Rango",buscar_rango), ("ELIMINAR Rango",delete_rango) , ('VER INFO Rangos Tablero', ver_info_rangos) ] )  
    The_X_Men.addX( titulo='SUB_MISC'  , padre='MenuPpal', ipadre="MISCELANEA" , lst_items=[("Prueba Impresion Masiva" , impresion_masiva), ("prueba Sdata", puebas_Sdata)] )    

    # 3 ■■■■■■■■■■ LLAMO A MYSTYCA PARA VISUALIZAR EL MENU 
    retorno = The_X_Men.Mystyca(titulo='MenuPpal', configurado=True, execFunc=True, tipo_marcador='a', execAll=True, Loop=True , padX=50)
    # 4 ■■■■■■■■■■ SALE DEL MENU ________________________________________________________________
    print(f"::: THE END en MAIN() ::: {retorno if retorno else 'no retorno'} ")    
    

# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  TABLERO  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_TABLERO():
    print(""" 
        ■■■■■■■■  I N F O R M E   T A B L E R O    ■■■■■■■■
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
    """)

def print_max_ssp():
    global TABLERO
    print() 
    val = Sdata.get_data( key_dict='val', tipo=int, permite_nulo = True , msg_entrada='\nTamaño Columna (0 by def)')    
    print('\nI m p r i m i r    M a x  s/sp  \n')    
    TABLERO.imprimir()
def print_max_csp():
    global TABLERO  
    pad_x = Sdata.get_data( key_dict='p', tipo = int , permite_nulo = True , msg_entrada='\nINTRODUCE EL ESPACIO ENNTRE LAS COLUMNAS')        
    print('\nI m p r i m i r    M a x  c/sp  \n')    
    TABLERO.imprimir(sp_columna = pad_x['p'])    
def print_literal():
    global TABLERO  
    print('\nI m p r i m i r   L i t e r a l  P u r o \n')    
    TABLERO.imprimir( ancho = 0 , sp_columna = 0 )
def print_fixed_ssp():
    global TABLERO  
    print('\nI m p r i m i r   F i x e d  s/sp  \n')    
    x = Sdata.get_data( key_dict='x', tipo=int, permite_nulo = True , msg_entrada='\nINTRODUCE EL ANCHO DE  COLUMNA')
    TABLERO.imprimir( ancho = x['x'] , sp_columna = 0 )
def print_fixed_csp():
    global TABLERO  
    print('\nI m p r i m i r   F i x e d  c/sp \n')    
    a = Sdata.get_data( key_dict='a', tipo=int, permite_nulo = True , msg_entrada='\nINTRODUCE EL ANCHO DE  COLUMNA ')
    a = Sdata.get_data( dicc= a, key_dict='x', tipo=int, permite_nulo = True , msg_entrada='\nINTRODUCE EL ESPACIO ENNTRE LAS COLUMNAS ')
    TABLERO.imprimir( ancho = a['a'] , sp_columna = a['x'] )
def print_personal():
    global TABLERO  
    print('\nI m p r i m i r   P e r s o n a l  c/sp \n')    
    TABLERO.imprimir( lista = [5,3,4,1,3,2] , sp_columna = 3 )
def print_ambigous():
    global TABLERO  
    print('\nI m p r i m i r   A m b i g u o u s   \n')    
    TABLERO.imprimir( ancho = 3 , lista = [3, 4, 6] , sp_columna = 5 )

# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  GETTING  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_GETTING():
    print(""" 
        ■■■■■■■■  I N F O R M E   G E T T I N G    ■■■■■■■■
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
    """)
# PONE EL VALOR DE TABLERO.valor_inicial EN TODO EL TABLERO.
def del_celda():
    global TABLERO
    f = Sdata.get_data( key_dict='f', tipo=int, msg_entrada='\nIntroduce Fila to Borrar Valor ')    
    c = Sdata.get_data( key_dict='c', tipo=str, msg_entrada='\nIntroduce Columna to Borrar Valor [0, "a", "A"] ')    


# ELIMINA LOS VALORES DE TODA UNA FILA Y DEJA EL VALOR INICIAL
def del_fila():
    global TABLERO
    dat = Sdata.get_data( key_dict='F', tipo=int, msg_entrada='INTRODUCE FILA TO DEL')        
    # OBTENGO LA FILA A BORRAR. AQUÍ SE PODRÍAN ELIMINAR VARIAS FILAS A LA VEZ.
    matriz = TABLERO.getting(fila=dat['F'], fila_to=dat['F'] , b_valor = False )
    if not matriz: return    

    # UN AVISO AL ELIMINAR, ES CORTESÍA
    dat = Sdata.get_data( dicc = dat, key_dict='IF', tipo=bool, msg_entrada=f'\nSeguro que Quieres Continuar?')        
    if dat['IF']==False: 
        print('Crear Anulado... Chaoooo') 
        return 
    
    # OPERO. TB PUEDO HACER UN PUSH DEL VALOR INICIAL SOBRE LA FILA CON REPETIR = TRUE 
    for fila in matriz:
        for celda in fila:
            celda.valor = TABLERO.get_valor_inicial()

# ELIMINA LOS VALORES DE TODA UNA COLUMNA Y DEJA EL VALOR INICIAL
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

    TABLERO.push(data_push=TABLERO.get_valor_inicial, celda_inicio=f'{celda.letra}:0', b_lineal=True, repetir=True)



# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  RANGO  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_RANGO():
    print(""" 
        ■■■■■■■■  I N F O R M E   R A N G O   ■■■■■■■■
    >>> GESTIONA LA LISTA lst_rangos

    [crear_rango] Dentro del Objeto TABLERO se pueden creaar Objetos Rango() .... self.lst_rangos(list)
                  Se necesita un nombre(str) y una dimension(str) que puede ser: celda_fin  ó  filasXcolumnas
                  [valor_entrada] Se va a introducir siempre 'plano' si es un iterable y su valor si no es iterable. puede ser una matriz.
    [buscar_rango] = Da informacion sobre el objeto rango. Si No se introduce el Nombre del rango, Da información sobre el Tablero.
    [delet e_rango] = Elimina un Objeto Rango de self.lst_rangos. Devuelve el objeto Rango.
    [ver_info_rangos] = Da información de los rangos de TABLERO. puedes filtrar X  like_name y X  flag   para el listado.


    """)
#  CREACION DE UN RANGO DENTRO DE TABLERO
def crear_rango():
    global TABLERO
    dat = Sdata.get_data( key_dict='nm', tipo=str, msg_entrada='NOMBRE DEL RANGO')    
    dat = Sdata.get_data( dicc= dat, key_dict='cld', tipo=str, msg_entrada='CELDA DE INICIO ( A:0 ) ')    
    dat = Sdata.get_data( dicc= dat, key_dict='dim', tipo=str, msg_entrada='DIMENSION ( 3x4 ) ó  CELDA-FIN ( M:8 )')  

    # rango = Rango(nombre_rango = dat['nm'], celda_inicio = dat['cld'], dimension = dat['dim'] , valor_inicial = '-') 

    # print('RANGO CREADO :)') if rango else f'REVISA LOS DATOS DE ENTRADA, EL RANGO NO HA SIDO CREADO :('

    rango = TABLERO.crear_rango(nombre=dat['nm'], celda_inicio=dat['cld'], dimension=dat['dim'])
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
    dat = Sdata.get_data( key_dict='r', tipo=str, msg_entrada='NOMBRE DEL RANGO A ELIMINAR')    
    rango = TABLERO.delete_rango(nombre_rango = dat['r'])
    print(rango) if rango else f'BORRAR RANGO :('

def ver_info_rangos():
    global TABLERO
    dat = Sdata.get_data( key_dict='N', tipo=str, msg_entrada='NOMBRE DEL RANGO A BUSCAR', permite_nulo=True)    
    dat = Sdata.get_data( dicc = dat, key_dict='L', tipo=str, msg_entrada='LIKE NAME', permite_nulo=True)    
    dat = Sdata.get_data( dicc = dat, key_dict='F', tipo=str, msg_entrada='FLAG', permite_nulo=True)    
    TABLERO.ver_rangos(nombre_rango = dat['N'] , like_name = dat['L'] , flag = dat['F'])
       


# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  PUSH  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
def info_push():
    print(""" 
        ■■■■■■■■  I N F O R M E   P U S H  ■■■■■■■■
        ■■■ TABLERO.push( data_push = '◙◙◙' )  ▓  celda_inicio = 'A:0' ▓ b_lineal = False ▓ repetir = False ▓ eje = None
            SI MATRIZ ◙◙◙   Mete la matriz en 'A:0' de forma matricial. 
            SI LIST ◙◙◙     Mete la lista de forma Horizontal.
            SI STR ◙◙◙      Intro 'Loren Ipsum' desde A:0  ocupando una celda.
            SI OTRO ◙◙◙     Intro X desde A:0 ocupando una celda.
        
        ■■■ TABLERO.push( data_push = '◙◙◙' , celda_inicio = 'A:0')   ▓ b_lineal = False  ▓ repetir = False ▓ eje = None
            SI MATRIZ ◙◙◙   Mete la matriz en 'A:0' de forma matricial. 
            SI LIST ◙◙◙     Mete la lista de forma Horizontal.
            SI STR ◙◙◙      Intro 'Loren Ipsum' desde A:0  ocupando una celda.
            SI OTRO ◙◙◙     Intro X desde A:0 ocupando una celda.
        
        ■■■ TABLERO.push( data_push = '◙◙◙', celda_inicio = 'C:3' , b_lineal = False )    ▓ repetir = False ▓ eje = None
            SI MATRIZ ◙◙◙
            SI LIST ◙◙◙
            SI STR ◙◙◙
            SI OTRO ◙◙◙
        
        ■■■ TABLERO.push( data_push = '◙◙◙', celda_inicio = 'C:3' , b_lineal = True)      ▓ repetir = False ▓ eje = None
            SI MATRIZ ◙◙◙
            SI LIST ◙◙◙
            SI STR ◙◙◙
            SI OTRO ◙◙◙
        
        ■■■ TABLERO.push( data_push = '◙◙◙', celda_inicio = 'C:3', b_lineal = True ,  eje = 'Y' , repetir = True  ) 
            SI MATRIZ ◙◙◙
            SI LIST ◙◙◙
            SI STR ◙◙◙
            SI OTRO ◙◙◙
        
        ■■■ TABLERO.push(data_push = '◙◙◙', celda_inicio = 'C:3', b_lineal = False, eje = 'X' , repetir = True )  
            SI MATRIZ ◙◙◙
            SI LIST ◙◙◙
            SI STR ◙◙◙
            SI OTRO ◙◙◙
        
        ■■■ TABLERO.push(data_push = '◙◙◙', celda_inicio = 'C:3', b_lineal = False, eje = 'X'   )           ▓ repetir = False
            SI MATRIZ ◙◙◙
            SI LIST ◙◙◙
            SI STR ◙◙◙
            SI OTRO ◙◙◙
        
        ■■■ TABLERO.push(data_push = '◙◙◙', celda_inicio = 'C:3', b_lineal = False, eje = 'Y'   )  ▓ repetir = False
            SI MATRIZ ◙◙◙
            SI LIST ◙◙◙
            SI STR ◙◙◙
            SI OTRO ◙◙◙
    
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
    dat = Sdata.get_data( dicc=dat, key_dict='V', tipo=int, permite_nulo=False, msg_entrada='INTRODUCE VALOR')
    
    celda_inicio = TABLERO.getting(fila=dat['F'], columna=['C'])
    if celda_inicio:
        TABLERO.push(data_push = data['V'], celda_inicio = celda_inicio.nombre )

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
    dat = Sdata.get_data( dicc=dat , key_dict='VH', tipo='between' , msg_entrada=['(V)ERTICAL', '(H)ORIZONTAL'], permite_nulo=False, valores_between=['V','H'])    
    
    if dat['VH'] == 'V':
        b_lineal = True
    else:
        b_lineal = False
    TABLERO.push(data_push=dat['L'], celda_inicio=dat['i'] , b_lineal=b_lineal)



# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ESTO NO CORRESPONDE AQUI, PERO REALMENNTE ES DONDE ESTOY HACIENDO LAS PRUEBAS ASÍ QUE EL BUEN SDATA ES ESTE ▓▓▓▓▓▓▓▓▓▓▓▓▓
def puebas_Sdata():
    from datetime import date 
    from datetime import time 

    lista = Sdata.get_data( key_dict='l', tipo=list , msg_entrada='INTRODUCE LISTA SEPARANDO POR COMAS (1,2,3,...)', permite_nulo=True)
    lista = Sdata.get_data( dicc=lista , key_dict='ci',tipo=str , msg_entrada='INTRODUCE LA CELDA DE INCIO SOBRE EL TABLERO ( M:8 )', permite_nulo = False)
    lista = Sdata.get_data( dicc=lista , key_dict='pos', tipo='between' , msg_entrada=['VERTICAL', 'HORIZONTAL'], permite_nulo=False, valores_between=['V', 'H'])    
    lista = Sdata.get_data( dicc=lista , key_dict='dat', tipo = date , msg_entrada='INTRODUCE FECHA (dd/mm/yyyy)')    
    lista = Sdata.get_data( dicc=lista , key_dict='hor', tipo = time , msg_entrada='INTRODUCE HORA (HH:MM)', permite_nulo=True)    
    lista = Sdata.get_data( dicc=lista , key_dict='bool', tipo = bool , msg_entrada='QUIERES CONTINUAR?')    

    print(f'lista: {lista['l']} - str:  {lista['ci']} - between: {lista['pos']} - fecha: {lista['dat']} - hora: {lista['hor']} - bool {lista['bool']}    ')
    # print(f'lista: {lista['l']} - fecha: {lista['dat']} - hora: {lista['hor']} - bool {lista['bool']}    ')
    if lista.get('pos', False) == True:
        pass
    else:
        pass


    
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
    

