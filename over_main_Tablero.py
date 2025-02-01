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
# from classMenuDvd.Tablero_X_Men import Tablero
# from classMenuDvd.Tablero_X_Men import Rangutan as Rangutan
from classMenuDvd.Tablero_X_Men import Rango as Rango

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
TABLERO = None

# ######################################################################
# ######################## xindex ######################################
# ######################################################################
def main():
    # 1- INSTANCIO EL OBJETO XINDEX ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    The_X_Men = XindeX()
    # 2- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    The_X_Men.addX(titulo='MenuPpal',  padre=None, ipadre=None,  
                    fraseHead="| - M A I N    O V E R   T A B L E R O - "  , 
                    lst_items=[ ("TABLERO" , None),("GET" , None), ("SET" , None), ("DEL" , None), ("RANGOS" , None), ('MISCELANEA', None)] 
                    )
    The_X_Men.addX(     titulo='SUB_CREAR', padre='MenuPpal', ipadre="TABLERO" , lst_items=[("Crear Tablero",crear_tablero), ("Iniciar Tablero", iniciar_tablero), ("Imprimir Modo Literal",print_tablero), ("Imprimir Modo Tabla",print_ajustado), ("Set Marco",set_marco)])  
    The_X_Men.addX(     titulo='SUB_GET'  , padre='MenuPpal', ipadre="GET"     , lst_items=[("Get Fila",get_fila), ("Get Column",get_columna), ("Get Valor By Fila-Columna", get_fila_columna), ("Get Valor By Celda(A:0)", get_celda)])
    The_X_Men.addX(     titulo='SUB_SET'  , padre='MenuPpal', ipadre="SET"     , lst_items=[("Set Fila",set_valor_over_fila), ("Set Column",set_valor_over_columna), ("Set Valor By Fila-Columna", set_fila_columna), ('Set Valor By Celda(A:0)', set_celda)])
    The_X_Men.addX(     titulo='SUB_DEL'  , padre='MenuPpal', ipadre="DEL"     , lst_items=[("Del Fila",del_fila), ("Del Column",del_columna), ("Del Celda", del_xy)])    
    The_X_Men.addX(     titulo='SUB_RANGOS', padre='MenuPpal', ipadre="RANGOS" , lst_items=[("Crear Rango",crear_rango), ("Buscar Rango",buscar_rango), ("Eliminar Rango",eliminar_rango), ("Ver Rango", ver_rango) , ("Tablero to Rango",tablero_to_rango), ("Rango To Tablero",rango_to_tablero),("Lista To Rango ['lista', 'de', 'ejemplo']",lista_to_rango) , ("Lista To Tablero",lista_to_tablero), ('Matriz To Tablero', matriz_to_tablero), ("Imprime Rango",imprime_prango), ('Imprime Rango From Fila / To Fila', prango_to)])  
    The_X_Men.addX(     titulo='SUB_MISC'  , padre='MenuPpal', ipadre="MISCELANEA" , lst_items=[("Prueba Recursiv",prueba_recursiva), ("T+ (Menu Simulation)",tablero_plus), ("-", None)])    

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
    f_c = TeclD.byTcld( listaStrKeys=['fila', 'col'], listaDef=[(int, False), (int, False)])
    # _______________________
    # Pregunta de Seguridad
    continuar = TeclD.byTcld( listaStrKeys=['if'], listaDef=[(bool, True)], msgIntro=f'\nSeguro que Quieres Continuar?')    
    if continuar['if']==False: 
        print('Crear Anulado... Chaoooo')
        return
    # _____________________
    # Creamos el tablero
    TABLERO = Rangutan(total_filas_tablero = f_c['fila'], total_columnas_tablero = f_c['col'] , valor_inicial='-')
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
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    TABLERO.inicializa_tablero(value=val['val'])
    print(f'Iniciar a {val['val']}  ;)\n')

# IMPRIME UN TABLERO CON TAMAÑO FIJO DE COLUMNAS(SE PIDE POR TECLADO.)
def print_tablero():
    global TABLERO
    print() 
    val = TeclD.byTcld( listaStrKeys=['val'], listaDef=[(int, True)], msgIntro='\nTamaño Columna (0 by def)... ')    
    """ >>> Define el espacio reservado para cada columna/celda  """
    if TABLERO:
        print()
        TABLERO.to_print(numSP=val['val'], b_columnas_head='A' , b_num_filas=True,  b_ajustado=False)
        # TABLERO.to_print(numSP=val['val'], b_columnas_head='A' , b_num_filas=True)
        # TABLERO.to_print(numSP=val['val'], b_columnas_head=False)
        # TABLERO.to_print(numSP=val['val'], bHead=True)
    print('\nPRINT TABLERO ;)') 

# IMPRIME UN TABLERO AJUSTANDO EL TAMAÑO (PIDE MARGEN)
def print_ajustado():
    global TABLERO  
    pad_x = TeclD.byTcld( listaStrKeys=['p'], listaDef=[(int, True)], msgIntro='\npadX (0 by def)... ')        
    if TABLERO:
        print()
        TABLERO.to_print( b_columnas_head='A', b_num_filas=True,  b_ajustado=True, pad_x=pad_x['p'])
        # TABLERO.to_print(numSP=val['val'], bHead=True)
    print('\nPRINT TABLERO AJUSTADO;)') 

# ESTABLECE UN VALOR EN UNA CELDA PIDIENDO FILA Y COLUMNA
def set_fila_columna():      
    global TABLERO
    f_c_v = TeclD.byTcld( listaStrKeys=['fila', 'col','valor'], listaDef=[(int, False), (str, False), (str, True)])
    set_v = TABLERO.xy(fil=f_c_v['fila'], col=f_c_v['col'], valor=f_c_v['valor'])
    print('\nset_value :)') if set_v == True else 'set_fila_columna :('

# ESTABLECE UN VALOR EN UNA CELDA (A:0)
def set_celda():
    cel_v = TeclD.byTcld( listaStrKeys=['celda', 'valor'], listaDef=[(str, False), (str, True)])    
    set_v = TABLERO.celda(celda=cel_v['celda'], valor=cel_v['valor'])
    print('\nSet Value :)\n') if set_v == True else '\nSet Value :(\n'  

# ESTABLECE UN VALOR EN UNA FILA
def set_valor_over_fila():
    global TABLERO
    f = TeclD.byTcld( listaStrKeys=['f'], listaDef=[(int, False)], msgIntro='\nIntroduce Fila to Set')        
    fila = TABLERO.get_lst_filas(filaFrom=f['f'], filaTo=f['f'])
    if not fila: return
    val = TeclD.byTcld( listaStrKeys=['v'], listaDef=[(str, True)], msgIntro=f'\nIntroduce Valor to Set en fila {f['f']}')    
    
    # Cacho cada columna por su self.get_dicc_numcol_value
    TABLERO.set_valor_over_fila(fila_to_set=f['f'], valor=val['v'])
    # generic_cols = TABLERO.get_dicc_numcol_value()
    # for i,columna in enumerate(generic_cols):
    #     TABLERO.xy(fil=f['f'], col=columna, valor=val['v'])

# ESTABLECE UNA COLUMNA
def set_valor_over_columna():
    global TABLERO
    col = TeclD.byTcld( listaStrKeys=['c'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Set  [0, "a", "A"]')    
    val = TeclD.byTcld( listaStrKeys=['v'], listaDef=[(str, True)], msgIntro=f'\nIntroduce el Valor a introducir en la Columna < {col['c']} > ')    
    if TABLERO.set_valor_over_columna(columna=col['c'], valor=val['v']):
        print('Set Columna ;)\n')
    else:
        print('Set Columna ;(\n')

# RETORNA UN VALOR DEL TABLERO CUANDO INTRODUCES UNA Cimprime_a_caponELDA (A:0, C:3)
def get_celda():
    cel_v = TeclD.byTcld( listaStrKeys=['celda'], listaDef=[(str, False)])
    valor = TABLERO.celda(celda=cel_v['celda'])
    print(f'\nValor en [ {cel_v['celda']} ] =  {valor}\n')

# OBTIENE UN VALOR DEL TABLERO x FILA Y COLUMNA
def get_fila_columna(): 
    global TABLERO
    f = TeclD.byTcld( listaStrKeys=['f'], listaDef=[(int, False)], msgIntro='\nIntroduce Fila to Get Valor ')    
    c = TeclD.byTcld( listaStrKeys=['c'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Get Valor [0, "a", "A"] ')    
    valor_en_tablero = TABLERO.xy(fil=f['f'], col=c['c'])    
    print(f'valor en Tablero: {valor_en_tablero}\n')

# OBTIENE UNA FILA
def get_fila():
    global TABLERO
    print('OBTIENE UNA LISTA DE DICCIONARIO DE UNA FILA ENTERA')
    f_f = TeclD.byTcld( listaStrKeys=['ff'], listaDef=[(int, False)], msgIntro='\n(Get Fila) Introduce Fila Desde... ')    
    f_t = TeclD.byTcld( listaStrKeys=['ft'], listaDef=[(str, False)], msgIntro='\n(Get Fila) Introduce Fila Hasta... ')    
    rng1=TABLERO.get_lst_filas(filaFrom=f_f['ff'], filaTo=f_t['ft'])
    print()
    TABLERO.imprime_a_capon(lst_rangos=rng1)

# OBTIENE UNA COLUMNA
def get_columna():
    global TABLERO
    col = TeclD.byTcld( listaStrKeys=['col'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Get  [0, "a", "A"]')    
    lst_columna = TABLERO.get_columna(columna=col['col'])    
    if lst_columna: print(lst_columna)

# PONE EL VALOR DE TABLERO.valor_inicial EN TODO EL TABLERO.
def del_xy():
    global TABLERO
    f = TeclD.byTcld( listaStrKeys=['f'], listaDef=[(int, False)], msgIntro='\nIntroduce Fila to Borrar Valor ')    
    c = TeclD.byTcld( listaStrKeys=['c'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Borrar Valor [0, "a", "A"] ')    
    try:
        TABLERO.del_xy(f['f'], c['c'])
    except Exception as e:
        print('Del Celda ;(\n')    
    finally:
        print('Del Celda :)\n')    

# ELIMINA TODA UNA FILA Y DEJA EL VALOR INICIAL DE LA CLASE self.valor_inicial.
def del_fila():
    global TABLERO
    f = TeclD.byTcld( listaStrKeys=['f'], listaDef=[(int, False)], msgIntro='\nIntroduce Fila to Del')        
    fila = TABLERO.get_lst_filas(filaFrom=f['f'], filaTo=f['f'])
    if not fila: return
    # _______________________
    # Pregunta de Seguridad
    continuar = TeclD.byTcld( listaStrKeys=['if'], listaDef=[(bool, False)], msgIntro=f'\nSeguro que Quieres Continuar?')    
    if continuar['if']==False: print('Crear Anulado... Chaoooo') ; return 

    TABLERO.set_valor_over_fila(fila_to_set=f['f'], valor=TABLERO.get_valor_inicial())

    

# __________________________________
# ELIMINA TODA UNA COLUMNA Y DEJA EL VALOR INICIAL DE LA CLASE self.valor_inicial.
def del_columna():
    global TABLERO
    c = TeclD.byTcld( listaStrKeys=['c'], listaDef=[(str, False)], msgIntro='\nIntroduce Columna to Borrar Valor [0, "a", "A"] ')    
    try:
        TABLERO.set_valor_over_columna(columna=c['c'], valor=TABLERO.get_valor_inicial())        
    except Exception as e:
        print('Del Columna ;(\n')
    finally:
        print('Del Columna ;)\n')


def set_marco():
    global TABLERO
    # if TABLERO.set_valor_over_columna(columna='0', valor='|')==True:
    #     print('Set Columna 0 ;)')
    # else:
    #     print('Set Columna 0 ;(')

    # if TABLERO.set_valor_over_columna(columna=TABLERO.data['int_cf'], valor='|')==True:
    #     print('Set Columna 0 ;)')
    # else:
    #     print('Set Columna 0 ;(')
    lst_retorno = TABLERO.get_lst_max_filas()
    if lst_retorno:
        print(lst_retorno)
    print(f'\nmax len(filas) en self.tablero = {TABLERO.get_max_filas()}')
    print('W.I.P.  :)\n')

# __________________________________
# Llama  a la clase Tablero_Plus que avanza la funcionalidad de Tablero y crea Estructura de Salida tipo Menu
def tablero_plus():
    from classMenuDvd.Tablero_X_Men import Monkey_Men
    print('\nC l a s e   T a b l e r o   P l u s \n')
    TPlus = Monkey_Men(dimension = "30x50", head = ['E n t r a d a','  d e   P r u e b a'] , pie = [['S a l i d a'], ['Fila 2 Salida']] , pad_x = 50 , x_pad = 5 , margen = 0)

# Crea un Rango
def crear_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['nm'], listaDef=[(str, False)], msgIntro='\nNombre del  R a n g o  ')    
    c = TeclD.byTcld( listaStrKeys=['cld'], listaDef=[(str, False)], msgIntro='C e l d a   d e   i n i c i o ( A:0 ) ')    
    d = TeclD.byTcld( listaStrKeys=['dim'], listaDef=[(str, False)], msgIntro='D i m e n s i o n ( 3x4 )  ó  C e l d a - F i n  ( M:8 )')  

    rng = TABLERO.crear_rango( nombre = n['nm'] , celda_inicio = c['cld'] , dimension = d['dim'] )
    if rng != None:
        print(f'{rng}\nRango Creado :) \n')  if  rng  else   f'Rango {n['nm']} - {c['cld']} - {d['dim']}\n Crear Rango :(\n'

def buscar_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, False)], msgIntro='\nNombre del Rango ')    
    rango = TABLERO.buscar_rango(nombre_a_buscar=n['n'])

    print(f'{rango}\n') if rango else f'Rango {n['n']} no encontrado :( \n'

def eliminar_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, False)], msgIntro='\nNombre del  R a n g o  A Eliminar')    
    rango=TABLERO.buscar_rango(nombre_a_buscar=n['n'])
    if rango:
        b_borrado = TABLERO.elimina_rango(nombre_a_borrar=rango.data['nombre'])    
        print(f'Del Rango {n['n']} :( \n')   if  b_borrado == None    else    f'{rango.data['nombre']} Borrado :) \n'

def ver_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, True)], msgIntro='\nNombre del R a n g o  a Buscar(None = All)')    
    v = TeclD.byTcld( listaStrKeys=['v'], listaDef=[(bool, True)], msgIntro='\nV e r   V a l o r e s ( v )(intro)  |   Ver Datos( f )')    

    if n['n'] == '':
        TABLERO.ver_rango(b_valores=v['v'])
    else:        
        TABLERO.ver_rango(nombre_rango = n['n'], b_valores=v['v'])
    print()

def tablero_to_rango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, True)], msgIntro='\nNombre del  R a n g o  to Transfer ')    
    rango = TABLERO.tablero_to_rango( nombre_rango = n['n'] )
    print(f'Transferencia de {n['n']} completada :) \n') if rango == True else f'Transferencia de {n['n']} Error :( \n'


def rango_to_tablero():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, True)], msgIntro='\nNombre del  R a n g o  to Transfer ')    
    retorno = TABLERO.rango_to_tablero( nombre_rango = n['n'] )
    print(f'Transferencia de {n['n']} completada :) \n') if retorno != None else f'Transferencia de {n['n']} Error :( \n'


def lista_to_rango():
    global TABLERO
    # lista = ['lista', 'de', 'ejemplo']
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, True)], msgIntro='\nNombre del  R a n g o  sobre el que operar')    
    lista = TeclD.byTcld( listaStrKeys=['l'], listaDef=[(str, True)], msgIntro='\nIntroduce los items de la lista separados por comas')    
    cadena = str(lista['l']).strip()
    lst_to_tablero = cadena.split(sep=',')
    if not lst_to_tablero: return 
    lst_to_tablero = [str(item).strip() for item in lst_to_tablero if str(item) != '']
    
    TABLERO.lista_to_rango(lista=lst_to_tablero, nombre_rango=n['n'])

    b_tablero = TeclD.byTcld( listaStrKeys=['vf'], listaDef=[(bool, True)], msgIntro='Lo Quieres tambien en el tablero( V ) o sólo en el rango( F )?')    
    if b_tablero['vf'] == True:
        TABLERO.rango_to_tablero( nombre_rango = n['n'] )

# Entra una lista en forma de lista o str separado por comas y lo introduce en el tablero 
# No hace falta rango, lo crea la funcion lista_to_tablero() de forma auxiliar y luego lo elimina
def lista_to_tablero():
    global TABLERO
    str_lista = TeclD.byTcld( listaStrKeys=['l'], listaDef=[(str, True)], msgIntro='\nIntroduce  L i s t a   separada por comas (1,2,3,...)')
    
    celda = TeclD.byTcld( listaStrKeys=['ci'], listaDef=[(str, True)], msgIntro='\nIntroduce C e l d a  en Tablero ( M:8 ) donde colocar la lista ... ')
    
    pos = TeclD.byTcld( listaStrKeys=['pos'], listaDef=[(bool, True)], msgIntro='Lo Quieres Vertical( V ) o Horizontal( F )?')    
    if pos['pos'] == True:
        retorno = TABLERO.lista_to_tablero(lista=str_lista['l'], celda_inicio = celda['ci'], pega_horizontal = False)    
    else:
        retorno = TABLERO.lista_to_tablero(lista=str_lista['l'], celda_inicio = celda['ci'], pega_horizontal = True)    

    if retorno == True: 
        print('\nLista llevada al tablero con Exito :)')
    else:
        print('\nLista llevada al tablero con Error :(')

def matriz_to_tablero():
    global TABLERO
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    celda = TeclD.byTcld( listaStrKeys=['ci'], listaDef=[(str, True)], msgIntro='\nIntroduce C e l d a  en Tablero (pejem: M:8 ) donde colocar la matriz ... ')
    tablero = TABLERO.matriz_to_tablero(matriz=matriz, celda_inicio=celda['ci'])
    if tablero == True:
        print('\nMatriz llevada al tablero con Exito :)')
    else:
        print('\nMatriz llevada al tablero con Error :(')


def imprime_prango():
    global TABLERO
    n = TeclD.byTcld( listaStrKeys=['n'], listaDef=[(str, True)], msgIntro='\nNombre del   R a n g o  a imprimir ..... ')    
    
    adjust = TeclD.byTcld( listaStrKeys=['adjust'], listaDef=[(str, True)], msgIntro='Ajuste al  M a x i m o  de columna: (None) , F i x e d : (int) , P e r s o n a l (list) ') 

    pad_x = TeclD.byTcld( listaStrKeys=['pad_x'], listaDef=[(int, False)], msgIntro='P a d X  ....')    

    # Al pedir una cadena para que tenga varias posibilidades, cuando permito nulo devuelve cadena vacia ''
    if adjust['adjust'] == '':

        TABLERO.Prango(nombre_rango=n['n'], column_adjust = None , pad_x = pad_x['pad_x'] )
    
    elif adjust['adjust'].isdigit():
        fixed_columna=abs(int(adjust['adjust']))
        TABLERO.Prango(nombre_rango=n['n'], column_adjust = fixed_columna , pad_x = pad_x['pad_x'] )
    
    else:
        if ',' in adjust['adjust']:
            lst_cadena = TABLERO.SttS.cadena_to_lista(cadena = adjust['adjust'], char=',')
            if lst_cadena: TABLERO.Prango(nombre_rango=n['n'], column_adjust= lst_cadena ,  pad_x = pad_x['pad_x'] )
        else:
            print('Dato/s de Entrada Error :( \n')

def prango_to():
    global TABLERO    
    fila_desde = TeclD.byTcld( listaStrKeys=['desde'], listaDef=[(int, True)], msgIntro='\nFila Desde.... ')    
    fila_hasta = TeclD.byTcld( listaStrKeys=['hasta'], listaDef=[(int, True)], msgIntro='\nFila Hasta.... ')    
    
    retorno = TABLERO.tablero_to_all_rango_fila()
    TABLERO.Prango_rows(desde=fila_desde['desde'], hasta=fila_hasta['hasta'], column_adjust = None , pad_x = 2)
    print('tablero to all rango fila  :) ') if retorno else f'tablero to all :( '


def prueba_recursiva():
    rango = Rango(nombre_rango= "r2d2", celda_inicio="A:0", dimension="30x50" , valor_inicio = [33, 55.5, 'Hola Flipy', 12])
    print()
    print(rango)

# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls') 
    print('\nI N I C I O')   
    # ---- Empezamos!!
    main() 
    

