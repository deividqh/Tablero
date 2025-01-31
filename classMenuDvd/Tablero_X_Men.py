# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""  :::  S T T S  :::  R A N G O  :::  T A B L E R O  :::  R A N G U T A N  :::::   M O N K E Y _ K I N G   """
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████

# STTS: Def las funciones estaticas que se pueden usar en Rango, Tablero y Tablero-Plus
# ============================================================================================
# RANGO: Def un Objeto virtual con datos sobre un rango. La lógica la maneja Tablero.
# ============================================================================================
# TABLERO: Def Un marco tipo excel con Rangos y operaciones complejas para imprimir en Screen
# ============================================================================================
# RANGUTAN : HEREDA DE TABLERO
# Monkey_Men: CREA UN MENU CON CABECERA / CUERPO / PIE Y MARCO..... ESPECIAL PARA XINDEX
# ============================================================================================
""" 
Para el alfabeto lowerstrig, upperstring. """
import string           

class SttS():

    """ DICCIONARIOS FUNDAMENTALES QUE DEFINEN LETRA:NUMERO Y NUMERO:LETRA EN MAYUSCULA Y MINUSCULA(4 DICCIONARIOS).
    USADOS PARA REFERENCIAR LAS COLUMNAS POR SU LETRA Y OBTENER SU NUMERO AUTOMATICAMENTE O VICEVERSA. """
    _min_ln = None      # minusculas letra - numero 
    _min_nl = None      # minusculas numero - letra

    _may_ln = None      # mayusculas letra - numero 
    _may_nl = None      # mayusculas numero - letra

    @staticmethod
    def _inicializa_diccs_letra_numero():
        """ >>> Inicializa los diccionarios estáticos si aún no están inicializados. """
        if SttS._min_ln is None or SttS._min_nl is None: 
            SttS.set_dicc_columnas_min()

        if SttS._may_ln is None or SttS._may_nl is None:
            SttS.set_dicc_columnas_may()
      
    
    # ________________________________________
    # [dicc1] ==>  'a':0, 'b':1, ... 'az'=702 |  [dicc2] ==>   0:'a', 1:'b', ... 702:'az'
    @staticmethod
    def set_dicc_columnas_min():
        try:
            SttS._min_ln = {letra: i for i, letra in enumerate(string.ascii_lowercase)}
            index = len(SttS._min_ln)
            for first in string.ascii_lowercase:
                for second in string.ascii_lowercase:
                    SttS._min_ln[f"{first}{second}"] = index
                    index += 1
            # Invertido____________________________________________
            SttS._min_nl = {v: k for k, v in SttS._min_ln.items()}

        except Exception as e:
            print(f"Error Grave set_dicc_columnas_min::: {e}")
            return None, None
        finally:
            return SttS._min_ln , SttS._min_nl
    # ________________________________________
    #  [dicc1] ==> 'A':0, 'B':1, ... 'AZ':702  |  [dicc2] ==>   0:'A', 1:'B', ... 702:'AZ'
    @staticmethod
    def set_dicc_columnas_may():
        """ RETORNA 2 DICCIONARIOS => 'A':0, 'B':1, ... 'AZ':702  y otro invertido =>  0:'A', 1:'B', ... 702:'AZ' """
        try:
            SttS._may_ln = {letra: i for i, letra in enumerate(string.ascii_uppercase)}
            index = len(SttS._may_ln)
            for first in string.ascii_uppercase:
                for second in string.ascii_uppercase:
                    SttS._may_ln[f"{first}{second}"] = index
                    index += 1

            # El invertido lo hacemos facil con una lista de comprension :)
            SttS._may_nl = {v: k for k, v in SttS._may_ln.items()}

        except Exception as e:
            print(f"Error Grave set_dicc_columnas_may::: {e}")
            return None, None
        
        finally:
            return SttS._may_ln , SttS._may_nl 

    # ____________________________________________________________________
    # Convierte una cadena del tipo 20x15 en (20,15)   ó   A:13 en (A,13)
    @staticmethod
    def desata_binomio(cadena:str, char:str=':'):
        """
        Descompone una cadena en dos partes separadas por un carácter dado.
            [cadena] (str): La cadena a descomponer (e.g., 'A:0', '20x15').
            [char] (str): El carácter que separa las dos partes de la cadena (por defecto ':').
        Retorno:
            tuple: (str, str) con las dos partes de la cadena. Devuelve (None, None) si la head es inválida.
        Ejemplo:
            >>> SttS.desata_binomio("A:0")
            ('A', '0')
            >>> SttS.desata_binomio("20x15", char='x')
            ('20', '15')
        """
        try:
            cadena = str(cadena).upper()
            lst_f_c = cadena.split( sep = char, maxsplit = -1 )
            if not lst_f_c: 
                return None, None
            if len(lst_f_c)!=2: return None, None
        except Exception as e:
            return None, None
        finally:
            pass
        # SIEMPRE ES F , C 
        try:
            primer_binomio = str(lst_f_c[0]).strip()
            segundo_binomio = str(lst_f_c[1]).strip()
        except Exception as e:
            print(f"Error::: desata_binomio::: {e}")
            return None, None
        finally:
            return primer_binomio, segundo_binomio

    # 
    # VALIDA UNA FILA ENTRE DOS VALORES POSIBLES FROM Y TO ________________
    @staticmethod
    def b_fila_valida(fil, from_incl , to_incl ):
        try:
            fil=int(fil)
            if from_incl <= fil <= to_incl:  
                return True
            else:
                return False
        except Exception as e:
            return False

    # 
    # VALIDA QUE UNA COLUMNA ESTA EN EL RANGO FROM - TO _________________
    @staticmethod
    def b_columna_valida(col, from_incl , to_incl):
        """ >>> Valida que una columna puede estar dentro del rango total de columnas posibles(desde a hasta az) 
        """
        # __________________________________________
        # Si no existen los diccionarios, los crea.
        SttS._inicializa_diccs_letra_numero()

        """ Viene como [Letra] y esta entre las combinacioes posibles('az' maximo, 'bn' sería falso) """
        if col in SttS._may_ln or col in SttS._min_ln:            
            numero_letra = SttS.letra_to_numcol(col)
            if numero_letra == None: 
                return False
            if from_incl <= numero_letra <= to_incl:  
                return True
            else:
                return False

        """ Viene como [Numero] y esta entre las combinacioes posibles. 
        Lo typeo para que de igual si viene como 1 o como '1'         """
        if int(col) in SttS._may_nl or int(col) in SttS._min_nl:
            if from_incl <= col <= to_incl:  
                return True
            else:
                return False

        return False        
        
    # 
    # DE LETRA A NUMERO  ____________________________________________
    @staticmethod
    def letra_to_numcol(letra):
        """ Entra una 'C' y sale un 3  o None si no encuentra 
        >>> Ejemplo: numero_columna = self.letra_to_num_col('C') 
        >>> print(numero_columna) ==> 2
        """
        # __________________________________________
        # Si no existen los diccionarios, los crea.
        SttS._inicializa_diccs_letra_numero()       
        
        # Paso la letra a   m i n u s c u l a  para poder buscar solamente en un diccionario y no tener que buscar en los 2 
        letra = str(letra).strip().upper()
        if letra in SttS._may_ln:
            return SttS._may_ln[letra]            
        else: 
            return None
    
    # 
    # SUMA UNA CANTIDAD A UNA LETRA ____________________________________________
    @staticmethod
    def suma_letra(letra, cantidad_sumar):
        """ Suma una cantidad a una letra y devuelve la letra resultante """
        # resultado = None
        try:
            letra = str(letra).strip().upper()
            SttS._inicializa_diccs_letra_numero()                       

            numero_letra = SttS.letra_to_numcol(letra=letra)
            if 0 <= numero_letra < len(SttS._may_ln.keys()):
                resultado = int(numero_letra) + int(cantidad_sumar)  # -1 => pq se empieza a contar desde la letra de inicio
                if resultado in SttS._may_nl:
                    """ Letra encontrada """
                    return SttS._may_nl[resultado]            
                else: 
                    return None
        except Exception as e:
            print(f'Error suma_letra :::: {e}')
            return None

    # 
    # IGUALA LAS LISTAS ____________________________________________________
    @staticmethod
    def igualar_listas(listaKeys, listaToReLong, valor_relleno='Loren'):
        """             
        Trata las longitudes de las listas y las igualo según listaKeys como referencia.
        La que se Re-dimensiona creciendo o decreciendo para igualarse con listaKeys.
        [valor_relleno]: en caso de que listaKeys>listaToRelong, hay que rellenar con un nuevo valor. en caso de funciones, None(by Def)
        [Ejemplo de uso]:
        >>> listTOdict_byTcld_ToString.igualar_listas(listaKeys=listaKeys, listaToReLong=listaTipos)        
        listaKeys y listaTipos son inmutables, se pasan por referencia y no hay que retornar valor. Aun así se retorna
        """
        if len(listaKeys)==len(listaToReLong):
            return listaToReLong
        elif len(listaKeys)>len(listaToReLong):
            # print("long dicc > longTipo.....tipos hasta longTipo y luego Tipo=str y PERMITENULL=False")
            listaNewTipos=[valor_relleno for i, (k) in enumerate(listaKeys) if i >= len(listaToReLong)]
            listaToReLong = listaToReLong + listaNewTipos
            # print(listaToReLong)
        else:
            # print("long dicc < longTipo.....vale hasta la long del dicc- hay que reducir la dimension del la listaToReLong")
            longListaTipos = len(listaToReLong)
            longListaKeys  = len(listaKeys)
            for i in range(longListaKeys , longListaTipos ):
                listaToReLong.pop()

        return listaToReLong
        pass
     # mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm (ia)         wip
    @staticmethod
    def es_lista_de_listas(matriz):
        """ Usada por matriz_to_tablero para validar que es una lista de listas para imprimir. """
        # Verificar si es una lista
        if not isinstance(matriz, list):
            return False
        
        # Verificar que cada elemento dentro de la lista principal sea también una lista
        for elemento in matriz:
            if not isinstance(elemento, list):
                return False
        
        return True
    # 
    # mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm    
    # Entra una cadena separada por un caracter (coma) y devuelve una l i s t a   c o n   c a d a   i t e m 
    @staticmethod
    def cadena_to_lista(cadena:str, char:str=','):  
        """ >>> Entra Una cadena separada por comaas, retorna una list de coma en coma 
        Entra: 'cadena, de , ejemplo' |   Sale: ['cadena', 'de', 'ejemplo'] """      
        try:
            if not isinstance(cadena, str): return None
            # Quita Espacios delante y detras_________________
            cadena = cadena.strip()
            # Eliminar comas al inicio o al final_____________
            if cadena.startswith(char) or cadena.endswith(char):
                cadena = cadena.strip(char)
            # Convierte la cadena en una lista________________
            lst_retorno = cadena.split(sep=char)
            if not lst_retorno: return 
            # Quita los espacios de delante y detras de cada item_______
            lst_to_tablero = [str(item).strip() for item in lst_retorno]
        except Exception as e:
            return None
        finally:
            return lst_retorno


    # 'frase ejemplo' en 'f r a s e  E j e m p l o_____________________________________________
    @staticmethod
    def frase_to_char_espacio(frase:str, b_tipo_titulo:bool=False):
        try:
            frase = str(frase).strip()
            if b_tipo_titulo==True:
                frase=str(frase).title()
            # Convertir la cadena en una lista de caracteres, preservando espacios
            lista_caracteres = [char if char!=' ' else '  ' for char in frase]
            # Unir los caracteres con un espacio intercalado
        except Exception as e:
            return frase
        finally:
            return ' '.join(lista_caracteres)
    
    # ccccccccccccccccccccccccccccccccccccccccccc
    # ENTRA UNA CELDA (C:2) Y DEVUELVO   3 , 2
    @staticmethod
    def row_col_by_celda(celda:str):
        """ >>> From 'C:4' To fila 4, columna 3         """
        # Validaciones
        fila    = None
        columna = None
        try:
            if not isinstance(celda, str): return None, None
            letra_columna , fila = SttS.desata_binomio(cadena=celda, char=':')
            if not letra_columna: return None, None
            columna = SttS.letra_to_numcol(letra=letra_columna)               
            if not fila or not columna: return None, None            
            
            fila = int(fila) 
            columna = int(columna)
        except Exception as e:
            print(f'Error en num_col_by_celda{e}')
            return None, None
        finally:
            return int(fila), int(columna)        

    # ______________________________________________________________
    # Convierte una dimension del tipo 20x15 en filas=20, columnas=15
    @staticmethod
    def filas_columnas_from_dimension(dimension:str):
        dimension = dimension.upper()
        try:
            filas , columnas = SttS.desata_binomio(cadena=dimension, char='X')
            if filas and columnas:
                filas    = int(filas)
                columnas = int(columnas)
            return filas, columnas
        except Exception as e:
            print(f"Error::: get_filas_columnas_from_dimension::: {e}")
            return None, None    



    # ██████████████████████  R E C U R S I V A S  █████████████████████████
    @staticmethod
    def getFormato(self, lista):
        """ 
        Establece el formato según la listaTitulo pasada, que es una lista de str tipo:
        >>> listaTitulosPrint=["Item", "Level", "Contador", "Posicion", "FilaR", "ColumR"]        
        -Puede ser un formato ajustado = True al tamaño maximo de CADA COUMNA o ajustado = False, se ajuta al tamaño del maximo str de la lista
        
        -Se Basa en saber cuantas columnas quieres(listaTitulos) y formatear cada linea al formato generado dinamicamente.
        >>> strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}"  
        """
        totalLen=0
        strformato=''        
        # if not isinstance(lista, list): return None
        maximo = SttS.get_maximo(lista)        

        for i in range (len(listaTitulo)):
            strformato += "{:<" + str(maximo) + "}"

        totalLen = maximo

        # print(strformato)
        return strformato, totalLen

    @staticmethod
    def get_maximo(lista=None):
        """ Se trata de conseguir saber cual es el maximo valor en una lista de datos """
        # Funcion Recursiva para Recorrer listas y devolver el str mas largo
        max_len_datos=SttS.max_len_rcrsv(iterator = lista)
        # _____________________
        # CALCULO EL MAXIMO DE ESPACIO 
        
        return max_len_datos

    # encuentra la la longitud en un iterator 
    @staticmethod
    def max_len_rcrsv( iterator):
        lst_cadenas = SttS.get_lista_rcrsv_item(iterator=iterator)
        lst_levels  = SttS.get_lst_rcrsv_level(iterator=iterator)
        """ Llama a la funcion recursiva para obtener una lista de str de cada fila de la matriz. """
        
        if lst_cadenas:

            lst_len=[f'{len(str(cad))}' for cad in lst_cadenas]
            return max(lst_len)

    # Busqueda recursiva por un iterator lista
    @staticmethod
    def get_lista_rcrsv_item( iterator, retorno=None):
        """ >>> Devuelve los valores que se va encontrando en una estructura de listas de izquierda a derecha. Retorna una lista.
        Ejemplo: >>> lst_items = get_lst_rcrsv_level( [1,[2,3], 4, [5,6,7]], retorno=None)
                >>> print(lst_items) ==> [1,2,3,4,5,6,7]
        """
        if retorno == None: 
            retorno=[]        

        if isinstance(iterator, list) or isinstance(iterator, tuple):
            for subList in iterator:
                SttS.get_lista_rcrsv_item(iterator=subList, retorno=retorno)
        else:
            retorno.append(iterator)
        return retorno

        pass

    # Busqueda recursiva por un iterator lista
    @staticmethod
    def get_lst_rcrsv_level( iterator, retorno=None, level=None):
        """ >>> Devuelve el nivel que se va encontrando en una estructura, leyendo los items de izquierda a derecha.
        Ejemplo: >>> lst_levels = get_lst_rcrsv_level( [1,[2,3], 4, [5,6,7]], level=None)
                >>> print(lst_levels) ==> [0,1,1,0,1,1,1]
        """
        # p r i m e r a   v u e l t a  
        if retorno == None and level == None : 
            level = 0        
            retorno = []

        # p r o c e s o  r e c u r s i v o
        if isinstance(iterator, list) or isinstance(iterator, tuple):
            level += 1
            for subList in iterator:
                SttS.get_lst_rcrsv_level(iterator=subList, retorno=retorno, level=level)
        else:
            retorno.append(level)
        # R e t o r n o 
        return retorno

        pass
        if isinstance(iterator, list) or isinstance(iterator, tuple):
            level += 1
            for subList in iterator:
                SttS.get_lst_rcrsv_level(iterator=subList, retorno=retorno, level=level)                                       

        elif isinstance(iterator, dict): 
            t_fila = [(key, *item) for key, item in iterator.items()][0]          
            """ >>> Convierte el dicc en una list (key , valor en str)... con el primer elemento la key del diccionario 
            """
            fila_str = [str(item) for item in t_fila]
            """ >>> Convierte a string cada elemento de la lista 
            """
            retorno.append(fila_str)

    # Entra una lista o diccionario de str y devuelve una lista en str.... para convertir una matriz en una lista de str.
    @staticmethod
    def convierteToString( lista):
        lista_str_retorno=[]
        if not isinstance(lista, list): 
            return None
        for iterator in lista:
            if isinstance(iterator, list) or isinstance(iterator, tuple):
                lista_str_retorno.append(*iterator)
                """ se mete en str todo el contenido de la lista. 
                """                                        
            elif isinstance(iterator, dict): 
                t_fila = [(key, *item) for key, item in iterator.items()][0]          
                """ >>> Convierte el dicc en una list (key , valor en str)... con el primer elemento la key del diccionario 
                """
                fila_str = [str(item) for item in t_fila]
                """ >>> Convierte a string cada elemento de la lista 
                """
                lista_str_retorno.append(fila_str)
        
        return lista_str_retorno

    @staticmethod
    def to_str_rcrsv(iterator , lst_retorno=None):
        # if not isinstance(iterator, list): return None
        if lst_retorno == None: 
            lst_retorno = []

        if isinstance(iterator, list) or isinstance(iterator, tuple):
            for item in iterator:
                SttS.to_str_rcrsv(item, lst_retorno)            
        elif isinstance(iterator, dict):                            
            t_fila = [(key, item) for key, item in iterator.items()][0]          
            """ >>> Convierte el dicc en una list (key , valor en str)... con el primer elemento la key del diccionario 
            """
            fila_str = [str(item) for item in t_fila]
            """ >>> Convierte a string cada elemento de la item 
            """
            lst_retorno.append(fila_str)
            SttS.to_str_rcrsv(t_fila, lst_retorno)

        else:            
            lst_retorno.append(iterator)
        
        return lst_retorno


# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
""" 
                                        -  R A N G O  -  
"""
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ============================================================================================
# Rango no hereda ni usa tablero para establecerse. 
# Rango es una clase que se instancia en Tablero en una lista o en un diccionario .... ya veremos
# Tablero es quien gestiona Rango a través de su lista de rangos.
# ============================================================================================
# Rango es un concepto. una dimension con un inicio y un final y sobre todo ...UN NOMBRE
# Rango es un diccionario de informacion de una estructura cuadrada 2x2 o rectangular 3x2 o 2x3 .... CONTINUA
# Esa informacion del diccionario de Rango(data) es la que se usará en tablero para almacenar los rangos que se quieran crear en una lista o diccionario....veremos :)
# De esta manera tablero puede acceder a sus rangos guardados y usar la lógica para crear operaciones complejas con los rangos en terminal.
# ============================================================================================
""" 
Para expresarme regularmente """
import re

"""
Enumeracion Que define que tipos de rango puede haber: 
de celda, de fila, de columna , de cuadrado, de rectangulo"""
from enum import Enum as TypeRng
class Type_Rng(TypeRng):    
    CELDA = 0 
    FIL = 1
    COL = 2
    CUADR = 3
    RECTG = 4    
# rrrrrrrrrrrrrrrrr
# rrrrrrrrrrrrrrrrr
# rrrrrrrrrrrrrrrrr
# >>> Con la celda de inicio[C:2] y la dimension(3x4) ( o celda fin[H:8] ) tenemos todos los datos para crear un rango......
class Rango():
    """ Clase que crea un Rango. Que Qué es un rango? y tu lo pregutas...
    Un rango es una coleccion de datos. Equiparacion con celdas.... información. 
    Contiene como variables fundamentales la variable data, dicc, matriz, 
    b_ghost==True cambia el funcionamiento del rango y pasa de tener reflejo inmediato a ser un objeto virtual.
    
    """
    def __init__(self, nombre_rango, celda_inicio='A:0', dimension = "1x1" ,  b_oculto = False, valor_inicio='', b_ghost=False):
        """
        Inicializa un rango con información sobre celdas de inicio y fin, dimensiones y más.
            nombre_rango (str): Nombre del rango.
            celda_inicio (str): Celda inicial en formato 'Letra:Fila' (e.g., 'A:0').
            dimension (str): Dimensiones en formato 'FilasxColumnas' o celda final (e.g., '1x1', 'C:3').
        Retorno:
            None: Configura las propiedades del rango, como `data`, `dicc` y valores derivados.
        Ejemplo:
            >>> rango = Rango(nombre_rango="Ejemplo_1", celda_inicio="B:2", dimension="3x4")
            >>> rango = Rango(nombre_rango="Ejemplo_2", celda_inicio="B:2", dimension="D:5")
            >>> print(rango.data)
            {'nombre': 'Ejemplo', 'fila_inicio': 1, 'columna_inicio': 1, ...}
        """        

        
        # V A L I D A C I O N   I N C I A L 
        if not isinstance(dimension, str): return None
        
        self.valor_inicio = valor_inicio      # Por defecto = ''
        """ >>> Valor que tendrán todas las celdas por defecto. 
        """

        """ C e l d a   d e   i n i c i o  """        
        try:
            fila_celda_inicio , letra_celda_inicio , columna_celda_inicio = self.get_data_inicio(celda_inicio=celda_inicio)        
        except Exception as e:
            print(f'Error init Rango: {e}')
            return None        
        
        """ D i m e n s i o n  """  
        try:      
            dimension_filas, dimension_columnas = self.desempaqueta_dimension(dimension=dimension , fila_inicio = fila_celda_inicio, columna_inicio = columna_celda_inicio)         
            if dimension_filas == None and dimension_columnas == None: 
                return None        
        except Exception as e:
            print(f'Error init Rango: {e}')
            return None        


        """ D a t o s   F i n   ... (a partir de celda_inicio y dimension) """
        try:
            fila_fin,  columna_fin , letra_columna_fin, celda_fin = self.get_data_fin(fila_celda_inicio=fila_celda_inicio, 
                                                                                    letra_celda_inicio=letra_celda_inicio, 
                                                                                    dimension_filas=dimension_filas, 
                                                                                    dimension_columnas=dimension_columnas)
        except Exception as e:
            print(f'Error __init__ Rango :::: {e}')

        pass

        # A S I G N A C I O N   D E   V A L O R E S           
        
        self.es_numerico = False    # Variable para saber si puedo hacer operaciones en el rango
        self.b_oculto = b_oculto    
        """ >>> Si no quieres que se vea en self.ver_rango con rango a None (ver Todos) 
            sirve para marcar el primer rango ('Tabero') como oculto... es todo el panel y son muchos valores que mostraar. así es mas agíl.
            con las filas pasa parecido.....en Monkey_Men
        """
                                    
        self.flag = ''              # No lo uso de momento, pero el objeto es hacer "marcas especiales" en aplicacion.
        self.family = ''            # No lo uso de momento, pero el objeto es hacer "familias" en aplicacion.
        self.b_ghost = b_ghost      
        """ >>> True, no se copia de tablero directamente al crear el rango (es virtual, para operar) 
                False, se crea y se copian los valores de tablero.         """
        pass
        # Info ::: L o s   B a s i c o s    ....Load del diccionario del Rango
        self.data = {
            'nombre': nombre_rango,                    # identificador del rango(str)
            'fila_inicio'   : fila_celda_inicio,       # Fila inicio       (int)
            'columna_inicio': columna_celda_inicio,    # Columna inicio    (int)
            'fila_fin'   : fila_fin,                   # Fila fin          (int)
            'columna_fin': columna_fin,                # Columna fin       (int)
        }
        # Info ::: L o s   c a l c u l a d o s / derivados
        self.data['letra_inicio']   = letra_celda_inicio    # Letra inicio      (str)
        self.data['letra_fin']      = letra_columna_fin     # Letra fin         (str)
        self.data['celda_inicio']   = celda_inicio
        self.data['celda_fin']      = celda_fin 
        # Generamos los valores derivados
        self.data['total_filas']    = int(self.data['fila_fin']) - int(self.data['fila_inicio']) + 1
        self.data['total_columnas'] = int(self.data['columna_fin']) - int(self.data['columna_inicio']) + 1
        self.data['total_celdas'] = int(self.data['total_filas']) * int(self.data['total_columnas'])  # Total de celdas
        pass

        # Xa LAS C A D E N A S   D E    I M P R E S I O N   ....EN VER , BUSCAR Y __STR__
        self.dicc__str__ = {'nombre': self.data['nombre'] , 
                    'celda_inicio': self.data['celda_inicio'], 
                    'celda_fin': self.data['celda_fin'], 
                    'total_celdas': self.data['total_celdas'] , 
                    'total_filas': self.data['total_filas'], 
                    'total_columnas': self.data['total_columnas'] , 
                    'Oculto?' : self.b_oculto, 
                    'Ghost?': self.b_ghost
                    }
        self.b__str__print_head = True
        """ >>> True(byDef) Indica que se tienen que imprimir las cabeceras en __str__  y False que se imprimen por fuera."""
                
        
        # D I C C I O N A R I O   D E L   R A N G O: C E L D A S   I M P L I C A D A S  :   V A L O R E S                    
        self.dicc = self.get_dicc_celda_valor(dimension_columnas=dimension_columnas, dimension_filas=dimension_filas, letra_celda_inicio=letra_celda_inicio, fila_celda_inicio=fila_celda_inicio)                       
        """ >>> ALMACENO CELDA:VALOR EN UN DICCIONARIO.... VIRTUAL 
        Es conflictivo, pq no se sabe aun si es un rango valido, pero rango es un concepto, una idea ;) ... ya se validará
        quiero que sea un diccionario (key)celda : (valor)valor....pero valor va  ser = None en este punto.
        - En Tablero o la clase que lo use es la que tiene que escribir en self.tablero, o leer de self.tablero y asignar a rango o etc....
        """

        # M A T R I Z   D E L   R A N G O . con esto ya....
        self.matriz = self.get_matriz()
        """ >>> Matriz de diccionarios del rango con el par {numero_columna:valor} x numero de filas 
        Ejemplo_1: self.matriz[10][5] => accede a la fila 10 , columna 5 relativa al rango!!          
        Ejemplo_2;  self.matriz[10][SttS._may_ln['E']]"""        
        pass
        """ .... y  siempre que se hacen operaciones sobre rango.dicc, tengo que espejarlas en la matriz. """
        self.dicc_to_matriz()

    # _____________________
    # Print de la clase
    def __str__(self):
        """Devuelve una representación legible del diccionario de datos.
        """
        # Validacion
        if not self.data: return ''

   
        if self.b__str__print_head == True:
            # Cabeceras de la tabla
            titulos = ["Rango", "Inicio", "Fin", "Total Celdas", "Filas", "Columnas", "Es Oculto", "Ghost"]
            tamanos_columnas = [25, 10, 10, 15, 8, 10, 10, 10]

            # Valores de los datos
            valores = [
                self.data.get("nombre", "N/A"),
                self.data.get("celda_inicio", "N/A"),
                self.data.get("celda_fin", "N/A"),
                self.data.get("total_celdas", "N/A"),
                self.data.get("total_filas", "N/A"),
                self.data.get("total_columnas", "N/A"),
                "Sí" if self.b_oculto else "No",
                "Sí" if self.b_ghost else "No"
            ]

            # Formateo de cabeceras y datos
            cabeceras = "".join([f"{titulo:<{ancho}}" for titulo, ancho in zip(titulos, tamanos_columnas)])
            datos = "".join([f"{str(valor):<{ancho}}" for valor, ancho in zip(valores, tamanos_columnas)])

            # Resultado final
            return f"{cabeceras}\n{'-' * sum(tamanos_columnas)}\n{datos}"
        else:
            return f"\nDatos del Rango( {self.data['nombre']} ): [ {self.data['celda_inicio']} ]  To [ {self.data['celda_fin']} ] Total Celdas: {self.data['total_celdas']} => {self.data['total_filas']} Filas y {self.data['total_columnas']} Columnas .......es Oculto?: {self.b_oculto} ..... Ghost?: {self.b_ghost}"  
            # return f'\n Rango :('

    # V a l o r e s   F R O M   d i c c   T O   m a t r i z
    def dicc_to_matriz(self):
        """ >>> Pasa los valores de self.dicc (celda:valor) a self.matriz [int-fila][int-columna] 
        Esto es así pq intuyo que es mas sencillo imprimir rangos a través de matriz que de dicc........veremos  """
        try:
            for i, valor in enumerate(self.dicc.values()):
                """ Pasa de lineal a matricial """
                fila =   i // self.data['total_columnas']       # division entera
                columna = i % self.data['total_columnas']       # modulo de la division
                if (0 <= fila < self.data['total_filas']) and (0 <= columna < self.data['total_columnas']):
                    self.matriz[fila][columna] = valor

        except Exception as e:
            print(f'Error dicc_to_matriz {celda} :::: {e}')
            return None

    # D e s e m p a q u e t a   D i m e n s i o n   y  devuelve fila y columna
    def desempaqueta_dimension(self, dimension, fila_inicio , columna_inicio):
        """ 
        [dimension]  puede ser Celda o dimension
            Si celda: necesita fila_inicio y columna de inicio para calcular la dimension final. 
                >>> dimension_fila = fila_fin - fila_ini + 1 
                >>> dimension_columna = columna_fin - columna_ini + 1 
            Si dimension: Se extraen los valores de la cadena y se devuelve el resultado.
        """
        b_dimension_es_celda=True
        letra_columna = None
        columna = None
        dimension_columnas = None
        dimension_filas = None
        
        dimension = dimension.upper()                                               # Para poner la x minuscula.
        if ':' in dimension:
            bi_columna , bi_fila = SttS.desata_binomio(dimension, ':')
            """ d i m e n s i o n   c o m o   C E L D A _ F I N A L  ( M:13 ) hay que transformar esto en una dimension
            """
            try:
                bi_fila = int(bi_fila)  
                letra_columna   = bi_columna
                # Saca el numero de columna de la dimension, que es con lo que se va a calcular la dimension.
                columna = SttS.letra_to_numcol(letra=letra_columna)

                if columna != None:
                    bi_columna = int(columna) 
                else:
                    return None, None
                """ A p l i c a   l a   F o r m u l a  """    
                dimension_filas = int(bi_fila) - int(fila_inicio) + 1
                dimension_columnas = int(bi_columna) - int(columna_inicio) + 1

                # Valida que la columna fin sea mayor que la columna inicio. y que la fila fin sea mayor que la fila inicio.
                if dimension_filas < 0 or dimension_columnas < 0:
                    return None, None

            except Exception:
                return None, None
        
        else:
            if 'X' in dimension:
                try:
                    """ d i m e n s i o n   c o m o   d i me n s i o n ( 3x4 )"""
                    dimension_filas , dimension_columnas = SttS.desata_binomio(dimension, 'X')
                    if dimension_filas == None or dimension_columnas == None:
                        return None, None
                    dimension_filas     = int(dimension_filas)                                     # si no es bueno, casca
                    dimension_columnas  = int(dimension_columnas)                                      # si no es bueno, casca
                except Exception as e:
                    print(f'Error init Rango: {e}')
                    return None, None
            else:
                return None, None
        
        return dimension_filas, dimension_columnas

    # O b t i e n e   l o s   d a t o s   d e   l a   c e l d a _ i n i c i o 
    def get_data_inicio(self, celda_inicio):
        try:
            """ C e l d a   d e   i n i c i o  """
            celda_inicio = str(celda_inicio).upper()
            letra_celda_inicio , fila_celda_inicio = SttS.desata_binomio(celda_inicio, ':')
            fila_celda_inicio = int(fila_celda_inicio)            
            if SttS.b_columna_valida(col=letra_celda_inicio, from_incl=0, to_incl=10000000) == False:
                return None
            columna_celda_inicio = SttS.letra_to_numcol(letra=letra_celda_inicio)
        except Exception as e:
            print(f'Error init Rango: {e}')
            return None
        finally:
            return fila_celda_inicio, letra_celda_inicio , columna_celda_inicio

    # O b t i e n e   l o s   d a t o s   d e   l a   c e l d a _ f i n 
    def get_data_fin(self,fila_celda_inicio, letra_celda_inicio, dimension_filas, dimension_columnas):
        """ Estrategia para colocar todos los rangos en su sitio.
            >>> pejemplo   celda_inicio = 'C:2' , dimension = '3x2'

            1-  celda_inicio='C:2' -> fila_iniciocio=2 , columna_iniciocio=2 
                dimension = '3x2' => dimension_filas=3 , dimension_columnas = 2 
                
            2-  fila_fin = fila_celda_inicio + dimension_filas - 1 => 2 + 3 - 1 ==> 4
                columna_fin = letra_celda_inicio + dimension_columnas  => 2 + 2 -1 ==> 3

            3- celda_fin = to_letra(columna_fin):fila_fin
        """
        try:
            # >>> 1-
            columna_celda_inicio = SttS.letra_to_numcol(letra=letra_celda_inicio)
            if columna_celda_inicio == None: return None, None, None, None
            # >>> 2-
            fila_fin = fila_celda_inicio + dimension_filas - 1         
            columna_fin = columna_celda_inicio + dimension_columnas - 1 
            # letra_columna_fin = SttS.suma_letra(letra=letra_celda_inicio, cantidad_sumar=dimension_columnas-1)
            letra_columna_fin = SttS._may_nl[columna_fin]
            # >>> 3-        
            celda_fin = f'{letra_columna_fin}:{fila_fin}'
        except Exception as e:
            print(f'Error __init__ Rango :::: {e}')
            return None, None, None, None

        return fila_fin, columna_fin, letra_columna_fin, celda_fin
    
    # D I C C I O N A R I O   D E L   R A N G O:   C E L D A S   :   V A L O R E S  
    def get_dicc_celda_valor(self, dimension_columnas, dimension_filas, letra_celda_inicio, fila_celda_inicio):
        """ >>> ALMACENO CELDA:VALOR EN UN DICCIONARIO.... VIRTUAL 
        Es conflictivo, pq no se sabe aun si es un rango valido, pero rango es un concepto, una idea ;) ... ya se validará
        quiero que sea un diccionario (key)celda : (valor)valor....pero valor va  ser = None en este punto.
        - En Tablero o la clase que lo use es la que tiene que escribir en self.tablero, o leer de self.tablero y asignar a rango o etc....
        """
        dicc_celdas_rng = {}
        try:
            for i in range(dimension_filas):
                for j in range(dimension_columnas):                
                    
                    sig_letra = SttS.suma_letra(letra = letra_celda_inicio , cantidad_sumar = j )
                    """ >>> Uso suma_letra desde la columna de celda de inicio para calcular la siguiente celda """

                    celda = f'{sig_letra}:{i + fila_celda_inicio}'
                    
                    dicc_celdas_rng[celda] = self.valor_inicio         # celda : valor
                    """ >>> V a l o r   I n i c i a l   sobre cada celda del rango """
        except Exception as e:
            return None
        finally:
            return dicc_celdas_rng
    
    # M A T R I Z   D E L   R A N G O :
    def get_matriz(self):
        try:
            # Es una representación matricial del rango. Vale para mil cosas, entre ellas acceder al rango por [fila][columna].         
            dicc_col_value = { c:self.valor_inicio for c in range(self.data['total_columnas'])}
            """ >>> GENERO UN DICCIONARIO 0:'', 1:'', 2:'' , 3:''......columna:valor (representa una fila de valores) """
            if dicc_col_value:
                return [copy.deepcopy(dicc_col_value) for f in range(self.data['total_filas'])]
                """ >>> Con el diccionario columna_valor lo multiplico por el numero de filas totales y 
                le hago una   c o p i a   p r o f u n d a   para que tenga entidad propia. """
            else:
                return None
        except Exception as e:
            return None        

    # _____________________o c u l t o   para ver. no para buscar.
    def get_b_oculto(self):
        if isinstance(self.b_oculto, bool):
            return self.b_oculto
        else:
            self.b_oculto=False
            return self.b_oculto

    # _____________________oculto para ver. no para buscar.....de momento
    def set_b_oculto(self, valor=True):
        self.b_oculto = valor

    # _________________________________________________________    
    # Obtiene el valor de una clave del diccionario de datos.
    # Tambien lo establece pero esto lo tengo a parlamento _____________________W.I.P
    def config(self, key, valor=None):        
        """ 
        Cambia los datos de configuracion del rango.
        [key](str): clave en el objeto rango a cambiar o establecer
        [valor](any) Any que se quiera imprimir o guardar.(establece/set valor)
                     None: obtiene/get valor
        NOTA: La funcion que la llame tiene que tener en cuenta que si se paasa con valor != None, al cambiar la configuracion fundamental del rango, van a inicializarse sus valores y puede llamar a 
        self.tablero_to_rango para introducirle los valores....u otras funciones. 
        Retorno: None, si ha habido cualquier error.
                 True, si ha ido todo bien.
        >>> Ejemplo_1: nombre_rango = self.config('nombre')
        >>> Ejemplo_2: self.config['nombre', 'nombre_rango_cambiado']
        """

        if valor == None:             return self.data.get(key, None)
        
        # Limito las claves que se pueden cambiar
        lst_valid_key = ['nombre',  'b_oculto', 'b_ghost' ]
        if not key in lst_valid_key:     return None

        if key == 'nombre':
            if not isinstance(value, str): return None
            self.rango.data['nombre'] = value
        elif key == 'b_oculto':
            if not isinstance(value, bool): return None
            self.rango.b_oculto = value
            pass
        elif key == 'b_ghost':            
            if not isinstance(value, bool): return None
            self.rango.b_ghost = value
            pass
        
    #     elif key == 'celda_fin':
    #         """ D a t o s   F i n  """
    #         try:
    #             fila, columna = SttS.row_col_by_celda(celda=value)
    #             if fila == None or columna == None:                 return None
    #             letra = SttS._may_nl.get([columna], None)
    #             if not letra:                 return None
    #         except Exception as e:
    #             print(f'Error Config: {e}')
    #             return None

    #         # R e c a l c u l a   c e l d a _ f i n   y   l o s   v a l o r e s   d e r i v a d o s 
    #         if self. __paquete_datos_derivados() == None: return None

    #     elif key == 'dimension':
    #         """ D i m e n s i o n  """   
    #         try:           
    #             dimension_filas, dimension_columnas = self.desempaqueta_dimension(dimension=value)         
    #             if dimension_filas == None or dimension_columnas == None: 
    #                 return None        
    #         except Exception as e:
    #             print(f'Error Config: {e}')
    #             return None 
            
    #         # R e c a l c u l a   c e l d a _ f i n   y   l o s   v a l o r e s   d e r i v a d o s 
    #         if self. __paquete_datos_derivados() == None: return None

    #     elif key == 'celda_inicio':
    #         try:
    #             # C e l d a   d e   i n i c i o         
    #             fila_celda_inicio , letra_celda_inicio , columna_celda_inicio = self.get_data_inicio(celda_inicio=value)
    #             self.data['letra_inicio']   = letra_celda_inicio    # Letra inicio      (str)

    #         except Exception as e:
    #             print(f'Error Config: {e}')
    #             return None  
            
    #         # R e c a l c u l a   c e l d a _ f i n   y   l o s   v a l o r e s   d e r i v a d o s 
    #         if self. __paquete_datos_derivados() == None: return None

        
    #     else:
    #         pass
    #     pass
    
    # ACTUALIZA LOS DATOS DERIVADOS(NO FUNDAMENTALES) DE UN RANGO
    # def __paquete_datos_derivados(self):
    #     """ Def: cuando se llama a self.config con las key 'celda_inicio', 'celda_fin' o 'dimension' se llama a esta funcion para actualizar todos los valores derivados de los fundamentales. 
    #     La funcion que la llame tiene que tener en cuenta que al cambiar la configuracion fundamental del rango, van a inicializarse sus valores y puede llamar a self.tablero_to_rango para introducirle los valores....u otras funciones.
    #     """
    #     # D a t o s   F i n   ... (a partir de celda_inicio y dimension)
    #     try:
    #         fila_fin,  columna_fin , letra_columna_fin, celda_fin = self.get_data_fin(fila_celda_inicio=self.data['celda_inicio'], letra_celda_inicio=self.data['letra_inicio'], dimension_filas=self.data['total_filas'], dimension_columnas=self.data['total_columnas'])
            
    #         # Generamos los valores derivados 
    #         self.data['letra_fin']      = letra_columna_fin     # Letra fin         (str)
    #         self.data['celda_fin']      = celda_fin 
            
    #         # Generamos los valores derivados calculados
    #         self.data['total_filas']    = int(self.data['fila_fin']) - int(self.data['fila_inicio']) + 1
    #         self.data['total_columnas'] = int(self.data['columna_fin']) - int(self.data['columna_inicio']) + 1
    #         self.data['total_celdas']   = int(self.data['total_filas']) * int(self.data['total_columnas'])  # Total de celdas
    #     except Exception as e:
    #         print(f'Error PAQUETE DATOS :::: datos :::: {e}')
    #         return None

    #     # D I C C I O N A R I O   D E L   R A N G O: C E L D A S   I M P L I C A D A S  :   V A L O R E S
    #     try:
    #         self.dicc = self.get_dicc_celda_valor(dimension_columnas=dimension_columnas, dimension_filas=dimension_filas, letra_celda_inicio=letra_celda_inicio, fila_celda_inicio=fila_celda_inicio)                                   
    #     except Exception as e:
    #         print(f'Error PAQUETE DATOS :::: dicc :::: {e}')
    #         return None
        
    #     # M A T R I Z   D E L   R A N G O :
    #     try:
    #         self.matriz = self.get_matriz()
    #     except Exception as e:
    #         print(f'Error PAQUETE DATOS :::: matriz :::: {e}')
    #         return None

        

# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
""" 
                        T A B L E R O  : ... somos cuadrados (Berto y BuenaFuente) 
"""
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████

import copy             # Para realizar copia profunda de self.tablero

class Tablero():
    """ >>> Crea un MARCO para Imprimir Onda Excel....Usa un LIST DE DICCIONARIOS. a,b,c,d...az con valores 0,1,2,3,...702 que se usa para referenciar las columnas.
    Cada diccionario tiene N columnas. de la A a la Z, y representa una FILA.    
        Se pueden crear tantas filas como sea necesareo rellenando el valor con None o con '' 
        acceder al tablero a una posicion self.xy(0,'A', valor] para escribir |  self.xy(0, 'A') pejemplo para leer """
    # ______________________________________________________________________
    # C O N S T A N T E S   D E   C L A S E ....(Tablero.SP  ó Tablero.TAB)
    SP  = ' '
    TAB = f'{SP*4}'
    pass
    def __init__(self, total_columnas_tablero, total_filas_tablero = 10 , valor_inicial=''):

        # super.__init__( total_columnas_tablero=total_columnas_tablero, 
        #                 total_filas_tablero = total_filas_tablero , 
        #                 valor_inicial=valor_inicial )
        
        # ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        # M O N T O   L A   E S T R U C T U R A   D E   C O L U M N A S ..... (sobre la que voy a trabajar)
       
        SttS._inicializa_diccs_letra_numero()

        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        # V A L I D A C I O N   D E   D A T O S   D E   E N T R A D A 
       
        # Valida Numero de columnas.... no mayor de az(702)
        if total_columnas_tablero >= len( SttS._may_ln ):
            total_columnas_tablero = len( SttS._may_ln.keys() )-1
        pass

        # ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻
        # C A R G O   L O S   D A T O S  D E  L A   C L A S E        
        self.numero_columnas = total_columnas_tablero        
        self.numero_filas = total_filas_tablero
        self.valor_inicial = valor_inicial

        self.dicc_numcol_value = { c:self.valor_inicial for c in range(self.numero_columnas)}
        """ >>> dicc (key):numero_columna (value): '-'   X   numero_columnas (...de 0 a numero_columnas) """
        
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        self.tablero = [copy.deepcopy(self.dicc_numcol_value) for f in range(self.numero_filas)]
        """ >>> Por cada fila hace una copia profunda del diccionario (numero_columna:valor), que almacena en tablero.
        El resultado final es una lista de diccionarios numero_columna:valor  y se puede acceder a tablero por 
        acceso_1: self.tablero[numero fila][numero de columna]              ==> acceso por indice
        acceso_2: self.tablero[numero fila][SttS._may_nl[numero columna]]   ==> 
        """
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        if not self.tablero: return
        """ >>> tablero: Es una lista de diccionarios que conforman una fila. 
        self.tablero[2][3] => fila 2, columna 3 |  self.tablero[2][self.dicc_may_letr_num['C']] => fila 2, columna 3
        self.tablero[1]['3']='jeje'
        """
        self.inicializa_tablero(value=self.valor_inicial)
        pass
    
    # _________________________________str__
    def __str__(self):
        for dicc_fila in self.tablero:
            print(*dicc_fila)
        pass
    
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # G E T T E R ' S  / S E T T E R ' S   
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # _____________________________________________
    # Devuelve el numero de filas del self.tablero
    def get_numero_filas_tablero(self):
        return len(self.tablero) if self.tablero else 0
    
    def ultima_fila(self):
        return len(self.tablero) - 1 if self.tablero else 0
    # ____________________________________________
    def get_numero_columnas_tablero(self):
        return self.numero_columnas if self.numero_columnas else 0
    
    def ultima_columna(self, b_formato_letra = False):
        if b_formato_letra == False:
            return self.numero_columnas - 1 if self.numero_columnas else 0
        else:
            letra = SttS._may_nl(self.numero_columnas - 1)
            return letra if self.numero_columnas else 0
        
    # _______________________________
    def get_dicc_numcol_value(self):
        return self.dicc_numcol_value if self.dicc_numcol_value else None
        
    # _______________________________
    def get_valor_inicial(self):
        return self.valor_inicial if self.valor_inicial else ''        
    # _______________________________
    def set_valor_inicial(self, valor_inicial):        
        self.valor_inicial=valor_inicial
    
    # Puede devolver una copia de tablero o una copia profunda(elClon=True)
    def get_tablero(self, esX2=False):
        if not self.tablero: return None
        return self.tablero if esX2==False else copy.deepcopy(self.tablero)
      
    # mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    # INICIALIZA LOS VALORES DEL TABLERO CON UN VALOR DE ENTRADA O '-'  - over tablero - 
    def inicializa_tablero(self, value=''):
        try:
            for i, lst_fila in enumerate(self.tablero):
                for j in range(self.numero_columnas):
                    self.tablero[i][j] = value
                    # self.xy(i, j, value)    # la otra posibilidad.  
        except Exception as e:
            print(f'Error inicializa_tablero :::: {e}')
            return 
        
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # G E T / S E T   U N   V A L O R   E N   T A B L E R O  - over tablero - 
    def xy(self, fil, col, valor='<<<out>>>'):
        """ >>> xy(3, 5, valor='hola') : pone el valor 'hola' en la posicion fila=3, columna=5
                xy(3, 5) : obtiene el valor de la posicion fila=3, columna=5
        """
        if not self.tablero: return None
        # Valida  FILA
        # if not isinstance(fil, int): return None
        try:
            fil=abs(int(fil))
            if not (0 <= fil < len(self.tablero)):  
                return None
        except Exception as e:
            return None
        
        # VALIDACION COLUMNA
        try:
            col=int(col)
            """ Se convierte a entero y si falla es que viene en formato letra y se trata en la excepcion. """
        except Exception as e:
            col = SttS.letra_to_numcol(letra=col)
            if col == None: 
                return None
            # if  not (0 <= col < self.numero_columnas) :
            if  not (0 <= col < len(self.tablero[0].keys())) :
                return None
            
        """ 
        RECORREMEOS EL TABLERO """
        for i, dicc_fila in enumerate(self.tablero):
            if i == fil:
                if valor == '<<<out>>>':       # para get. le pongo uno imposible? para que solo cuando no tenga valor sea get. y en caso contrario, que coja el '' y el None
                    return dicc_fila[col]      # Devuelve un valor
                else:
                    if valor == None: 
                        valor = self.valor_inicial

                    dicc_fila[col] = valor     # Pone un valor
                    return True
        pass

    # ddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    # E L I M I N A   U N   V A L O R   E N  TA B L E R O  - over tablero - 
    def del_xy(self, fila, columna):
        retorno = self.xy(fil=fila, col=columna, valor=self.valor_inicial)
        print('Borrar :( ') if retorno == None else ('Borrar ;)')

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    #                  -  O V E R   F I L A S   Y   C O L U M N A S    - 

    #  ESTABLECE UN VALOR EN UNA FILA  - over tablero - 
    def set_valor_over_fila(self , fila_to_set=0, valor=''):        
        fila = self.get_lst_filas(filaFrom=fila_to_set, filaTo=fila_to_set)
        if not fila: return
        # if fila_to_set not in self.dicc_may_num_letra: return
        if fila_to_set not in SttS._may_nl: return

        # Cacho cada columna por su self.get_dicc_numcol_value
        try:
            generic_cols = SttS._may_ln if SttS._may_ln else None
            if not generic_cols: return 
            for i,columna in enumerate(generic_cols):
                self.xy(fil=fila_to_set, col=columna, valor=valor)

        except Exception as e:
            print(f'Error::: set_valor_over_fila {e}')
            return False
    
    # ESTABLECE UN VALOR EN UNA COLUMNA ENTERA DE TABLERO - over tablero - 
    def set_valor_over_columna(self, columna, valor):
        col = SttS.letra_to_numcol(letra=columna)           
        if col == None:
            """ No es una letra. será un Numero? """
            try:
                col = int(columna)
            except Exception as e:
                print(f'Error set_valor_over_columna: {e}')
                return None
        # print(len(self.tablero[1]))     #Longitud de las columnas

        # _____________________________________________
        # Llama a la funcion que cambia el valor y devuelve True en una lista....o None si hay error.
        lst_columna=[ self.xy(fil=i, col=col, valor=valor) for i in range(self.get_numero_filas_tablero())]

        return lst_columna if lst_columna else False


    # DEVUELVE 1 FILA (DICC DE TABLERO)  - over tablero - 
    def __get_dicc_fila(self, fila):
        """ >>> Devuelve el dicc que se corresponde con una fila en la list self.tablero """
        for f , dicc_cols in enumerate(self.tablero):
            if f == fila:
                return dicc_cols
    
    # DEVUELVE UN RANGO DE FILAS CONSECUTIVAS - over tablero - 
    def get_lst_filas(self, filaFrom, filaTo):
        """ >>> Devuelve una list de filas de  self.tablero """
        # Validacion fisica
        try:
            filaFrom=int(filaFrom)
            filaTo=int(filaTo)
        except Exception as e:
            return None
        
        # Validacion Logica
        if filaFrom > filaTo: return None
        if  (0 > filaFrom > len(self.tablero)): return None
        # _______________________________________________
        # Recorro cada fila del diccionario del tablero: 
        lst_retorno=[]
        for f, dicc_cols in enumerate(self.tablero):
            if  filaFrom <= f <=filaTo:
                lst_retorno.append(dicc_cols)

        # print(lst_retorno)
        return lst_retorno

    #  F R O M   F I L A ( i n t  )   T O     L I S T _ S T R   - over tablero - 
    def get_fila(self, filaBusca):
        """ >>> Obtiene una lista de str de values de self.tablero 
        """
        # if not self.valid_ROW(fila=filaBusca): return None
        if SttS.b_fila_valida(fil=filaBusca, from_incl=0, to_incl=len(self.tablero)) == False: 
            return None
        for f, dicc_cols in enumerate(self.tablero):
            if  f == filaBusca:
                return dicc_cols.values()      
    
    # 
    # F R O M   C O L U M N A ( i n t )  T O     L I S T   V A L O R E S . - over tablero - 
    def get_columna(self, columna):     

        col = SttS.letra_to_numcol(letra=columna)
        if col == None:
            """ No es una letra. será un Numero? """
            try:
                col = int(columna)
            except Exception as e:
                print(f'Error get_columna:::: {e}')
                return None
        pass
        lst_columna=[ self.xy(fil=i, col=col) for i in range(self.get_numero_filas_tablero()) ]
        """>>> Formo la lista de retorno con los valores de la columna """    
        # rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr            
        return lst_columna if lst_columna else None    
    
    # L E N   M A X   D E   U N A   C O L U M N A 
    def get_max_columna(self, columna):
        lst_columna = self.get_columna(columna=columna)
        longitudes = [len(str(item)) for item in lst_columna]
        return max(longitudes) if longitudes else 0                
    
    # ____ L o n g i t u d   d e l   c o n t e n i d o   d e   l a   f i l a  (el total) maxima de toda la matriz self.tablero    - over tablero -   
    def get_max_filas(self):
        """ Para imprimir marco horizontal """
        lst_fila    = []
        long_fila   = 0
        for dicc_fila in self.tablero:
            long_fila=0
            for cadena in dicc_fila.values():
                long_fila += len(str(cadena))
            pass
            lst_fila.append(long_fila)    
                
        return max(lst_fila) if lst_fila else 0
    
    # ____ L i s t a   c o n   l a s   l o n g i t u d e s   d e l   c o n t e n i d o   d e   c a d a   f i l a  (el total) maxima  
    def get_lst_max_filas(self):
        """ Para imprimir marco horizontal """
        lst_fila    = []
        long_fila   = 0
        for dicc_fila in self.tablero:
            long_fila=0
            for cadena in dicc_fila.values():
                long_fila += len(cadena)

            lst_fila.append(long_fila)    
                
        return lst_fila if lst_fila else None

    # ULTIMA FILA CON USO DE UN TABLERO
    def last_fila_used(self):
        """ Para imprimir marco horizontal """
        lst_fila    = []
        long_fila   = 0
        for dicc_fila in self.tablero:
            long_fila=0
            for cadena in dicc_fila.values():
                long_fila += len(cadena)
            pass
            lst_fila.append(long_fila)    
        # Encuentra la última fila usada recorriendo las longitudes al revés
        if not lst_fila: 
            return -1
        for index in range(len(lst_fila) - 1, -1, -1):
            if lst_fila[index] > 0:
                return index  # Retorna el índice de la última fila usada

        return -1  # Si no hay filas usadas, retorna -1

    # ____ L i s t a   d e   v a l o r e s   d e l   t a b l e r o  x  r o w 
    def get_lst_values_by_fila(self, numfila):
        """ >>> obtiene una lista de fila por su numero """
        # if self.valid_ROW(numfila)==False: return None
        if SttS.b_fila_valida(fil=numfila, from_incl=0, to_incl=len(self.tablero)) == False: 
            return None
        dicc_fila = self.get_lst_filas(numFila, numFila)
        if dicc_fila:
            return [str(value) for key, value in dicc_fila ]
   
    # ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    # I M P R I M I R   B Y   C O L   E N   T A B L E R O  SEGURAMENTE SE ELIMINARÁ PARA IMPRIMIR EL RANGO - TABLERO  - Prnt(nombre_rango='Tablero',.....)
    #   de esta manera puedo imprimir rangos y operar todo a través de los rangos
    #   La idea es que los datos externos (out) se tienen que traducir a un rango siempre.
    def to_print(self, b_ajustado=False , b_columnas_head=False , b_num_filas=False,  numSP=1 , pad_x=0 ):
        """ 
        [b_ajustado] (bool): True, presenta la tabla en modo columnas ancho el maximo de la tabla.. False, presenta la tabla según lo que de sin formato format.
        [b_columnas_head] : False, No muestra la cabecera de letras de columna, True, Si muestra(para las pruebas) 
        [b_num_filas]=False,  no muestra el numero de filas del final de linea. True, Si la numeración de linea.
        [fila]=None , muestra sólo una fila concreta-
        [numSP]=1 para b_ajustado = True, es el número de 
        [pad_x](int)(con b_ajustado = True), es el espacio entre el final de la columna y el siguiente item.
        """
        # ________________________
        # Valida que haya tablero
        if not self.tablero: print('TO PRINT-> :(') ; return 
        # _________________________________________ SE ESTABLECE LA CADENA STR DE FORMATO() DE CADA FILA
        str_format = self.__get_formato_to_print(len_columnas = numSP, b_ajustado=b_ajustado, pad_x=pad_x)        
        
        # >>> I m p r i m e   N u m e r o s   de cabecera de columa....si tal            
        print(str_format.format(*self.dicc_numcol_value)) if b_columnas_head==True else None
        
        """ >>>  I m p r i m e   L e t r a s   de cabecera de columna....si tal """
        dicc_letras = {char:num_col for char,num_col in SttS._may_ln.items() if num_col in self.dicc_numcol_value}
        print(str_format.format(*dicc_letras)) if b_columnas_head=='A' else None
        
        """ >>> I m p r i m e   v a l o r e s  """
        for i in range(len(self.tablero)):
            lst_filas=self.get_fila(filaBusca=i)
            if b_num_filas != False:
                print(str_format.format(*lst_filas), end=f'  [{i}]\n')  # end=f'  [{i}]\n'  Esto hace que acabe con el número de fila :)
            else:
                print(str_format.format(*lst_filas))  # Cuando b_num_filas == False, no imprime los numeros de las Filas
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # FORMATO IMPR _____________________________
    def __get_formato_to_print(self,  b_ajustado=False, len_columnas=5,pad_x=0):        
        """ >>> 
        strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}" 
        [len_columnas](int) : Longitud de la columna fijo... cuando b_ajustado = False
        [b_ajustado](bool) : True: metodo auto-ajuste al tamaño de columna maximo ; False= sin auto-ajuste... usa len_columnas.
        [pad_x](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y el siguiente.
        """  
        totalLen=0
        strformato=''
        if b_ajustado == False:
            for i in range (self.numero_columnas):
                strformato += "{:<" + str(len_columnas) + "}"
        else:
            if pad_x >= 0:
                """ Ajustado y con PadX -> calcula el maximo de la columna y le añade un margen de pad_x """
                for i in range (self.numero_columnas):
                    maximo = self.get_max_columna(columna=i)
                    maximo += pad_x
                    strformato += "{:<" + str(maximo) + "}"
            else:
                for i in range (self.numero_columnas):
                    maximo = self.get_max_columna(columna=i)
                    strformato += "{:<" + str(maximo) + "}"
        # print(strformato)
        return strformato

    # ========================================================================================
    # IMPR
    def impr_1(self):
        for i, dicc_fila in enumerate(self.tablero):
            print(dicc_fila)
    def imprime_a_capon(self, lst_rangos=None, separador=' '):
        """ >>> imprime a capón el tablero. acumula los valores en una fila y estos quedan separados por un separador(str)  """
        if lst_rangos==None: 
            lst_rangos=self.tablero
        if not lst_rangos or not isinstance(lst_rangos, list):  
            return None

        for i, dicc_fila in enumerate(lst_rangos):
            for col, valor in dicc_fila.items():
                if valor == '': 
                    impr_v = self.valor_inicial
                else:
                    impr_v = valor

                print(f'{impr_v}', end = separador)
            print()
    def row_to_print(self):
        """ >>> imprime Basandose en las filas. no en las columnas.  """
        
        self.to_print(numSP = 0, b_columnas_head='A' , b_num_filas=True,  b_ajustado=False)

        len_fila_max = self.get_max_filas()

        # for i in range(len(self.tablero)):
        #     lst_filas=self.get_fila(filaBusca=i)
        #     if b_num_filas != False:
        #         print(strformato.format(*lst_filas), end=f'  [{i}]\n')  # end=f'  [{i}]\n'  Esto hace que acabe con el número de fila :)
        #     else:
        #         print(strformato.format(*lst_filas))  # Cuando b_num_filas == False, no imprime los numeros de las Filas
    
    
    # ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    #                             -  C E L D A S  -  
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    
    
    # SET/GET   U N   V A L O R   E N   U N A   C E L D A  (A:0)  E N  T A B L E R O 
    def celda(self, celda, valor=None):
        """ >>> Valor == None -> devuelve el valor   |   Valor != None -> Pone el valor en Tablero y devuelve True/False 
        Esto limita el valor de la celda de Tablero a != None... No me gusta... Análisis """
        
        f , c = self.__celda_to_fil_col(celda=celda)
        """ >>> Desempaqueta celda -> (int)fila , (int)columna
        """
        if f is None or c is None:
            return None

        if valor == None:
            set_v = self.xy(fil=f, col=c)
            return set_v if set_v != None else False
        else:
            set_v = self.xy(fil=f, col=c, valor=valor)
            return True if set_v == True else False   

    # ENTRA UNA CELDA (C:2) Y DEVUELVO   3 , 2
    def __celda_to_fil_col(self, celda):
        """ >>> From 'C:4' To fila 4, columna 3 
        Valida que la celda está en el tablero.
        """
        # Validaciones
        if not self.tablero: return None, None
        if not isinstance(celda, str): return None, None
        
        try:
            letra_columna , fila = SttS.desata_binomio(cadena=celda, char=':')                        
            columna = SttS.letra_to_numcol(letra=letra_columna)                           
            if columna == None: return None, None
            fila = int(fila) 
            columna = int(columna)
            # if not fila and not columna: return None, None            
            """ 
            Valida que la fila está dentro del Tablero. """
            if SttS.b_fila_valida(fil=fila, from_incl=0, to_incl=len(self.tablero)-1) == False:
                return None, None                
            """ 
            Valida que la columna está dentro del Tablero. """
            if SttS.b_columna_valida(col=columna, from_incl=0, to_incl=len(self.tablero[0])-1) == False: 
                return None, None
        
            return fila, columna
        except Exception as e:
            print(f'Error __celda_to_fil_col:\n{e}')
            return None, None
        
       # ccccccccccccccccccccccccccccccccccccccccccc
    
    # ENTRA UNA fila y columna (3 , 2) y devuelvo una celda (C:2)
    def celda_by_fil_col(self, fila, columna):
        if not self.tablero: return None
        """ 
        >>> Valida que la fila está dentro del Tablero. """
        if SttS.b_fila_valida(fil=fila, from_incl=0, to_incl=len(self.tablero)-1) == False: 
            return None
        """ 
        >>> Valida que la columna está dentro del Tablero. """
        if SttS.b_columna_valida(col=columna, from_incl=0, to_incl=len(self.tablero[0])-1) == False: 
            return None
        try:        
            """ Lo trato como número.... si casca, es letra. """
            columna = int(columna)
            letra = SttS._may_nl[columna]
            celda = f'{letra}:{fila}'
        except Exception as e:
            """ viene como letra """
            celda = f'{columna}:{fila}'

        return celda

# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
"""
                                 -  R A N G U T A N  -    
"""
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████

class Rangutan(Tablero):
    """ >>> Determina los  R a n g o s   E N   E L   T A B L E R O (su papá).
    """
    BASE_RANGO_TABLERO = 'rango_tablero'
    BASE_RANGO_FILA = 'rango_fila_'
    BASE_RANGO_COLUMNA = 'rango_columna_'


    def __init__(self, total_columnas_tablero:int, total_filas_tablero:int = 10 , valor_inicial='' ):
        """ >>> Define un Tablero y Maneja una lista de rangos rigiendo las operaciones sobre los rangos
        Clase defiida aparte y no en tablero para dar abstración a las operaciones sobre los rangos en tablero 
        """
        super().__init__(total_columnas_tablero  = total_columnas_tablero,  
                        total_filas_tablero = total_filas_tablero , 
                        valor_inicial = valor_inicial)

         # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # L I S T A   D E   R A N G O S   D E   T A B L E R O        
        self.lst_rangos=[]   
        """ Cada Tablero pueda tener su coleccion de rangos y por lo tanto hacer operaciones complejas con los datos en su ambito"""

        # self.char_padx = ' '    # caracter de relleno de la impresion. desde la última celda escrita hasta el final.

        # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
        # E S T R U C T U R A   D E   D A T O S   D E L   T A B L E R O   ==>   R A N G O                
        dimension = f'{total_filas_tablero}x{total_columnas_tablero}'                
        
        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # R a n g o _ t a b l e r o 
        self.rango_tablero = self.crear_rango(nombre=self.BASE_RANGO_TABLERO, celda_inicio='A:0', dimension=dimension, b_ghost=False)
        """ >>> b_ghost = False hace que se cargue con el valor inicial del tablero. 
        """
        if self.rango_tablero:
            self.rango_tablero.b_oculto = True
            self.rango_tablero.flag = 'SYS'
            """ >>> Lo hago oculto pq este es el rango Virtual sobre Tablero... tiene todas las celdas """
            print('rango_tablero ~)')
        else:
            print('rango_tablero ~(')
            return None
        pass
        
        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # C r e a   u n   r a n g o   p o r   f i l a , ..... se pueden imprimir filas individuales con Prango y Prango_rows       
        for i, fila in enumerate(self.rango_tablero.matriz):
            nombre_rango_fila = self.__new_nombre_secuencial(cadena=self.BASE_RANGO_FILA)
            celda_inicio = f'A:{i}'
            dimension_fila = f'1x{len(fila)}'
            rango = self.crear_rango(nombre = nombre_rango_fila, 
                                    celda_inicio = celda_inicio, 
                                    dimension = dimension_fila , 
                                    b_ghost=False )
            if rango: 
                if self.valida_limites_rango(rango = rango ) == False:
                    self.elimina_rango(nombre_rango=rango.data['nombre'])
                else: 
                    rango.flag = 'RNG_ROW'

        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # C r e a   u n   R a n g o   p o r   C o l u m n a        
        for j in range(len(self.rango_tablero.matriz[0])):
            dimension_columna = f'{len(self.rango_tablero.matriz)}x1'
            nombre_rango_columna = self.__new_nombre_secuencial(cadena=self.BASE_RANGO_COLUMNA)
            celda_inicio = f'{self.celda_by_fil_col(fila=0, columna=j)}'
            if nombre_rango_columna:
                rango = self.crear_rango(nombre = nombre_rango_columna, celda_inicio=celda_inicio, dimension=dimension_columna , b_ghost=False )
                rango.flag = 'RNG_COL'
            

    # sssssssssssssssssssssssssssssssssssssssssssssssssss
    # C r e a   u n   n o m b r e   s e c u e n c i a l 
    def __new_nombre_secuencial(self, cadena:str, separador:str='_'):
        """ Crea un nuevo nombre en lst.rangos a partir de una cadena de head. """
        lst_nombres = [rango.data['nombre'] for rango in self.lst_rangos]
        lst_match = [nombre for nombre in lst_nombres if cadena in nombre]
        
        if lst_match:
            # Extraer el número secuencial al final de cada nombre
            lst_num = []
            for match in lst_match:
                partes = match.split(separador)
                if partes[-1].isdigit():
                    lst_num.append(int(partes[-1]))
            # Generar el nuevo nombre con el siguiente número
            nuevo_numero = max(lst_num) + 1 if lst_num else 0
            return f'{cadena}{nuevo_numero}'
        else:
            # Si no hay coincidencias, se usa el primer número
            return f'{cadena}0'

    # ███████████████████████████████████████████████████████████████████████████████████
    # - C R E A R   R A N G O  - 
    def crear_rango(self, nombre:str, celda_inicio:str='A:0', dimension:str='1x1', b_ghost:bool=False):
        """
        Crea un nuevo rango si no existe un rango con el mismo nombre o propiedades.
            [nombre] (str): Nombre único para identificar el rango.
            [celda_inicio] (str): Celda inicial del rango (e.g., 'A:0').
            [dimension] (str): Dimensión del rango en formato 'FilasxColumnas' (e.g., '3x2').
            [b_ghost](bool):True (by Def), crea un rango y se carga desde tablero. 
                            False, para que un rango sea cargado desde tablero.
        Retorno:
            Rango: El rango creado si es válido y único.
            None: Si el rango ya existe o hay un error.
        Ejemplo:
            >>> tablero.crear_rango("MiRango", "A:0", "3x2")
            >>> tablero.crear_rango("MiRango", "A:0", "B:2")
        """
        if not self.tablero: return None
                
        rango = None
        try:
            rango = Rango(nombre_rango = nombre, celda_inicio = celda_inicio, dimension = dimension, b_ghost=b_ghost)
            if rango:
                # No admite rangos  o u t   o f   t a b l e r o 
                if self.valida_limites_rango(rango = rango) == False:       return None
                
                # No admite rangos  r e p e t i d o s  de nombre
                if self.b_existe_nombre_rango(nombre_a_buscar = rango.data['nombre']) == True:  return None

                # L o s   f a n t a s m a s   no   se   cargan  de   tablero .... luego self.tablero_to_rango()
                if rango.b_ghost == False:
                    # self.tablero_to_rango(nombre_rango=rango.data['nombre'])
                    for celda in rango.dicc.keys():
                        valor_celda_en_tablero = self.celda(celda=celda)
                        """ >>> cruzo cada celda con el tablero 
                        """
                        if valor_celda_en_tablero != False and valor_celda_en_tablero != None:
                            rango.dicc[celda] = valor_celda_en_tablero
                        else:
                            rango.dicc[celda] = self.valor_inicio
                        """ >>> Y asigno el valor de la celda en el tablero al valor del rango. 
                        """
                    pass
                    rango.dicc_to_matriz()
                    """ .... y  siempre que se hacen operaciones sobre rango.dicc, tengo que espejarlas en la matriz. """
                

                #  e s _ n u m e r i c o .... luego llamar a self.es_rango_numerico()
                """ >>> posibilita hacer operaciones a través del rango"""                
                try:
                    for valores in rango.dicc.values():
                        valores = int(valores)                    
                    rango.es_numerico = True
                except Exception as e:
                    rango.es_numerico = False

                # O t r o   p a r a   l a   s a c a  :)
                self.lst_rangos.append(rango)
                return rango
        except Exception as e:
            print(e)
            return None
       
    # rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    # D E V U E L V E   T y p e _ R n g 
    def get_rango_type(self, nombre_rango:str):
        """ >>> un rango puede ser: de celda, de fila, de columna , de cuadrado, de rectangulo """
        rango = self.buscar_rango(nombre_a_buscar = nombre_rango)    
        if self.valida_limites_rango(rango=rango) == False: return None
        if not rango: return None        
        if rango.data['total_filas'] == 1 and rango.data['total_columnas'] == 1:
            typo = Type_Rng(CELDA)        
        elif rango.data['total_filas'] == 1:
            typo = Type_Rng(COL)
        elif rango.data['total_columnas'] == 1:
            typo = Type_Rng(FIL)
        if rango.data['total_filas'] == rango.data['total_columnas'] :
            typo = Type_Rng(CUADR)
        else:
            typo = Type_Rng(RECTG)
        return typo

    # rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    # valida si los valores de un rango son todo números
    def es_rango_numerico(self, nombre_rango:str):
        rango = self.buscar_rango(nombre_a_buscar = nombre_rango)    
        if not rango: return None        
        if self.valida_limites_rango(rango=rango) == False: return None
        lst_ret = []
        try:
            for valores in rango.dicc.values():
                valores = int(valores)
            return True
        except Exception as e:
            return False

    # rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    # VALIDA SI UN RANGO ESTÁ EN EL TABLERO O SE SALE
    def valida_limites_rango(self, rango):
        if not self.tablero: 
            return False
        # lst_num_col = [int(value) for value in self.dicc_numcol_value]
        """ >>> Creo la lista de enteros de las columnas usadas de Tablero para hacer la validacion """
        if rango.data['columna_fin'] in self.tablero[0].keys():
            if 0 <= rango.data['fila_fin'] < len(self.tablero):
                return True
        pass
        return False

    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    # BUSCAR RANGO .... POR NOMBRE O POR INDICE
    def buscar_rango(self, nombre_a_buscar:str=None, b_index:bool=False):
        """ Busca un rango en lst_rangos. 
        [nombre_a_buscar](str) = None, busca todos los ragos.
        [b_index](bool) = False , devuelve el rango. | True, devuelve el indice en lst_rangos. Si nnombre_a_buscar == None, b_index no tiene efecto.
        """
        # Validacion
        if not self.lst_rangos: 
            return None        
        if nombre_a_buscar == None:
            """ Devuelve todos los rangos """
            return [rango for rango in self.lst_rangos]
        else:
            """ Busca el x nombre """
            for i, rango in enumerate(self.lst_rangos):
                if rango.data['nombre'] == nombre_a_buscar:
                    if b_index == False:
                        return rango
                    else:
                        return i
        return None

    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    # VER RANGO    
    def ver_rango(self, nombre_rango:str = '', b_valores:bool = False, flag:str = ''):
        """ Imprime por consola los rangos (tanto valores como datos) de los rangos que no estan marcados b_oculto. 
        [nombre_rango](str) =>None, imprime todo | =>str imprime el rango elegido si no es b_oculto.
        [b_valores](bool): =>False, imprime los datos del rango =>True, imprime los datos de los rangos
        >>> Ejemplo_1: tablero_ej.ver_rango(nombre_rango='r1', b_valores=False) => ver las propiedades de 'r1' por terminal.
        >>> Ejemplo_2: tablero_ej.ver_rango(nombre_rango='r1', b_valores=True) => ver los valores de 'r1' por terminal.
        >>> Ejemplo_3: tablero_ej.ver_rango(nombre_rango=None, b_valores=True) => ver los valores de todos los rangos por terminal.
        >>> Ejemplo_4: tablero_ej.ver_rango(nombre_rango=None, b_valores=False) => ver las propiedades de todos los rangos por terminal.
        """
        if not self.lst_rangos:
            print('Ver Rango :( ')
            return
        if nombre_rango == '':
            """ Todos """
            # for rango in self.lst_rangos:
            # if rango.b_oculto == False:
            if b_valores == False:
                """ >>> Queremos info del rango """                        
                print(self.imprimir_info_rangos(lista_rangos = self.lst_rangos, flag = flag), end='\n')  
            else:
                """ >>> Queremos valores del rango """
                self.imprimir_valores_rangos(lista_rangos = self.lst_rangos, celdas_por_linea=4)
        else:
            """ x nombre """
            for rango in self.lst_rangos:
                if rango.data['nombre'] == nombre_rango:
                    if  b_valores == False:
                        rango.b_print__str__ = True                        
                        print(rango)                                    
                        print(self.imprimir_info_rangos(lista_rangos = [rango.data['nombre']], flag = flag), end='\n') 
                    else:                        
                        self.imprimir_valores_rangos(lista_rangos = [rango.data['nombre']], celdas_por_linea = 4)
                        # print(rango.dicc)
        pass
    
    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    # Para las funciones ver_rango y buscar_rango y cuando está marcado mas de un rango para visualizar.
    def imprimir_info_rangos(self, lista_rangos:list, b_valores:bool = False,  flag:str = ''):
        """ >>> Imprime una lista de rangos formateados.
        [lista_rangos]: Lista de los ragos a imprimir su información.
        [familia]: Familia que quieres que se imprima.
        [flag]: flag que quieres que se imprima.
        """
        if not lista_rangos:
            return "No hay rangos para mostrar."

        # Cabeceras comunes
        titulos = ["Rango", "Inicio", "Fin", "Total Celdas", "Filas", "Columnas", "Oculto?", "Ghost?"]
        tamanos_columnas = [25, 10, 10, 15, 8, 10, 10, 10]
        cabeceras = "".join([f'{titulo:<{ancho}}' for titulo, ancho in zip(titulos, tamanos_columnas)])
        separador = "-" * sum(tamanos_columnas)

        # Recolección de datos
        filas = []
        for rango in lista_rangos:            
            valores = [
                rango.data.get("nombre", "N/A"),
                rango.data.get("celda_inicio", "N/A"),
                rango.data.get("celda_fin", "N/A"),m,
                rango.data.get("total_celdas", "N/A"),
                rango.data.get("total_filas", "N/A"),
                rango.data.get("total_columnas", "N/A"),
                "Sí" if rango.b_oculto else "No",
                "Sí" if rango.b_ghost else "No"
            ]
            fila = "".join([f"{str(valor):<{ancho}}" for valor, ancho in zip(valores, tamanos_columnas)])
            filas.append(fila)

        # Construcción final del resultado
        return f"{cabeceras}\n{separador}\n" + "\n".join(filas)
    
    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    def imprimir_valores_rangos(self, lista_rangos:list, celdas_por_linea:int=8):
        """ >>> Imprime una lista de valores que hay en los rangos formateados el número de celdas por línea impresa. 
        [lista_rangos]: lista de los rangos que se quieren imprimir.
        [celdas_por_linea]: numero de celdas que se imprimen por línea.
        """
        if not lista_rangos:
            return "No hay rangos para mostrar."

        # Cabeceras comunes
        titulos = ["Rango", "Inicio", "Fin", "Total Celdas", "Filas", "Columnas", "Es Oculto", "Ghost"]
        tamanos_columnas = [25, 10, 10, 15, 8, 10, 10, 10]
        cabeceras = "".join([f"{titulo:<{ancho}}" for titulo, ancho in zip(titulos, tamanos_columnas)])
        separador = "-" * sum(tamanos_columnas)

        cuenta_rangos = 0
        # Recolección de datos
        filas = []
        for rango in lista_rangos:
            cuenta_rangos += 1
            valores = [
                rango.data.get("nombre", "N/A"),
                rango.data.get("celda_inicio", "N/A"),
                rango.data.get("celda_fin", "N/A"),
                rango.data.get("total_celdas", "N/A"),
                rango.data.get("total_filas", "N/A"),
                rango.data.get("total_columnas", "N/A"),
                "Sí" if rango.b_oculto else "No",
                "Sí" if rango.b_ghost else "No"
            ]
            fila = "".join([f"{str(valor):<{ancho}}" for valor, ancho in zip(valores, tamanos_columnas)])
            filas.append(fila)

            # Formatear las celdas del rango
            contador = 0
            salida_celdas = []
            for celda, valor in rango.dicc.items():
                salida_celdas.append(f"{celda}: {valor}")
                contador += 1

                # Cada vez que se completa una línea, añadirla como nueva fila
                if contador == celdas_por_linea:
                    filas.append(" " * 4 + " | ".join(salida_celdas))  # Sangría para diferenciar de los datos del rango
                    salida_celdas = []
                    contador = 0

            # Imprimir las celdas restantes si quedaron al final
            if salida_celdas:
                filas.append(" " * 4 + " | ".join(salida_celdas))

            if cuenta_rangos >= 10:
                input('\nPulsa una tecla para continuar .....')
                cuenta_rangos = 0
            # Construcción final del resultado
            print (f"{cabeceras}\n{separador}\n" + "\n".join(filas))

    # ELIMINA RANGO DE LA LISTA
    def elimina_rango(self, nombre_rango:str):
        i_rango = self.buscar_rango(nombre_a_buscar=nombre_rango, b_index=True)        
        if i_rango !=None:
            try:
                rango = self.lst_rangos.pop(i_rango)
                return rango
            except Exception as e:
                print(f'Error Elimina Rango: :::: {e}')
                return None
        else:
            print('Rango fuera de rango ;) introduce uno correcto plis')
            return None

    # Verificar si ya existe un rango con el mismo nombre en lst_rangos
    def b_existe_nombre_rango(self, nombre_a_buscar:str):
        if any(rango.data['nombre'] == nombre_a_buscar for rango in self.lst_rangos):
            # print(f"Error: Ya existe un rango con el nombre '{nombre_a_buscar}'.")
            return True
        return False

    # mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    # Verificar si ya existe un rango con las mismas propiedades ( no usado y util )            wip
    def get_lst_compara_data_rango(self, rango_a_buscar):
        """ Compara las propiedades de un rango pasado como argumento con la lista de rangos de Tablero.
        [rango_a_buscar](Rango): objeto tipo rango. 
        Retorno:True si existen las mismas propiedades....y que quien lo llame decida que hacer con esto.
                False, si no existen esas mismas propiedades en el tablero.
        >>> 
        >>> Ejemplo: lst_rangos = b_compara_data_rango(rango_ejemplo) 
                     if lst_rangos:
                        for rango in lst_rangos:
                            print(f'el Rango {rango.data['nombre']} tiene las mismas propiedades que {rango_a_buscar.data.['nombre']}')        
        """        
        total_filas = rango_a_buscar.data['total_filas']
        total_columans = rango_a_buscar.data['total_columnas']
        lst_retorno = []
        for rango in self.lst_rangos:
            if (rango.data['celda_inicio'] == rango_a_buscar.data['celda_inicio'] and
                    rango.data['total_filas'] == total_filas and
                    rango.data['total_columnas'] == total_columnas):
                # print(f"Error: Ya existe un rango con las mismas propiedades (celda_inicio: {celda_inicio}, dimension: {dimension}).")
                # return rango
                lst_retorno.append(rango) 
        pass
        if lst_retorno:
            return lst_retorno
        else:
            return None
            
    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    def rango_to_tablero(self, nombre_rango:str):
        """ Escribe un rango en un tablero. """
        rango = self.buscar_rango( nombre_a_buscar = nombre_rango )
        if not rango: return None
        
        for celda, valor in rango.dicc.items():
            self.celda( celda = celda , valor = valor )
        return True

    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    def tablero_to_rango(self, nombre_rango:str = ''):
        """ >>> Pasa datos del tablero al rango  
        [nombre_rango]:(str) nombre del rango que quieres pasar desde el tablero.
        Retorno: True, :) , None, :(
        """
        if nombre_rango == '':
            rango = self.buscar_rango( nombre_a_buscar = self.BASE_RANGO_TABLERO )
        else:
            rango = self.buscar_rango( nombre_a_buscar = nombre_rango )
        if not rango: 
            return None
        else:
            for celda, valor in rango.dicc.items():
                valor_celda_en_tablero = self.celda(celda=celda)
                """ >>> cruzo cada celda con el tablero 
                """
                rango.dicc[celda] = valor_celda_en_tablero
                """ >>> Y asigno el valor de la celda en el tablero al valor del rango. 
                """
            pass

        rango.dicc_to_matriz()
        """ .... y  siempre que se hacen operaciones sobre rango.dicc, tengo que espejarlas en la matriz. """
        return True

    # Otra manera de cargar los rangos, en este caso, del tablero a las filas.
    def tablero_to_all(self):
        """ pasa todos los datos desde el tablero hacia los rangos de fila 
        y los carga en la matriz y dicc de Rango"""
        try:
            lst_rangos_fila = [rango for rango in self.lst_rangos if self.BASE_RANGO_FILA in rango.data['nombre'] and rango.b_ghost == False]
            if not lst_rangos_fila:
                return None
            for rango in lst_rangos_fila:
                self.tablero_to_rango(nombre_rango = rango.data['nombre'])            
                pass
                


        except Exception as e:
            print(f'{e}')
            return None
        finally:
            return True

    # ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    #                               -  I M P R E S I O N  -
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    # I m p r i m e   u n   R a n g o . 
    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    def Prango(self, nombre_rango, column_adjust = None , pad_x = 0):    
        """ 
        I m p r i m e   u n   r a n g o  d i r e c t a m e n t e . N O   l o   i m p r i m e   s o b r e   t a b l e r o .
        [column_adjust] (None): True, ajusta al len maximo de cada columna , pad_x es la separacion entre columnas.(maximo columna)
        int,  Ajuste fixed para todas las columnas. si pad_x = 0 => modo literal/talcual , si pad_x > 0 => espacio después de la última línea fijo.
              No controla los len de las columnas. (fixed), pero si la longitud de la fila para aplicar el pad_x
        list: (int) Ajusta cada columa al tamaño del item de la list. (personalizado.)

        ['pad_x']  : el espacio entre columnas cundo b_ajustado = True , el espacio final antes del ultimo char de linea cuando b_ajustado = False
        ejemplo_1: TABLERO.Prango(nombre_rango = 'rango_1' , column_adjust = None , pad_x = 0 ) => ajusta al maximo de cada columna(mode tabla)
        ejemplo_2: TABLERO.Prango(nombre_rango = 'rango_1' , column_adjust = None , pad_x = 2 ) => ajusta al maximo de cada columna(mode tabla) pero dejando un espacio entre celdas de 2
        ejemplo_3: TABLERO.Prango(nombre_rango = 'rango_1' , column_adjust = 1 , pad_x = 0 ) => literal pero deja un espacio por celda.
        ejemplo_4: TABLERO.Prango(nombre_rango = 'rango_1' , column_adjust = 0 , pad_x = 0 ) => literal / tal cual....XindeX
        ejemplo_5: TABLERO.Prango(nombre_rango = 'rango_1' , column_adjust = 15 , pad_x = 5 ) => columnas al 15 todas. pero no restrictivo. al final deja pad_x=5 con la ultima columna para posible marco.
        ejemplo_6: TABLERO.Prango(nombre_rango = 'rango_1' , column_adjust = [0,1,5,4,3,2] , pad_x = 15 ) => cada columna a su ajuste y deja 15 self.char_padx
        """
        if nombre_rango == None:
            nombre_rango = self.BASE_RANGO_TABLERO
        rango = self.buscar_rango( nombre_a_buscar = nombre_rango )
        if not rango: return None

        # width = kwargs.get('width', 0)  # Si no existe, usa 0
        # pad_x = kwargs.get('pad_x', 0)  # Si no existe, usa 0
        # width = abs(width)
        # pad_x = abs(pad_x)

        if rango.b_ghost == True: return None
        """ >>> Si eres un rango ghost, no tienes nada que hacer por aquí :( 
        """

        """ ffffffffffffffffffffffffffffffffffffffffff 
        >>> E s t a b l e c e   e l   F o r m a t o 
        """

        if column_adjust == None:            
            if pad_x == 0:   
                """ >>> Ajusta a tamaño columnas ajustado al maximo, pero no deja espacio con la siguiente columna([pad_x]==0). 
                hay que controlar las coordenadas para imprimir ( A:0, C:2) o rangos... """
                str_format = self.__formato_to_prango_maxcol( rango= rango, pad_x = 0  )
            
            else:
                """ >>> Ajusta a tamaño columnas ajustado al maximo, pero SI deja espacio con la siguiente columna([pad_x]==0). 
                hay que controlar las coordenadas para imprimir ( A:0, C:2) o rangos... """
                str_format = self.__formato_to_prango_maxcol( rango= rango, pad_x = pad_x  )
            pass
        elif isinstance(column_adjust, int):
            column_adjust = abs(column_adjust)
            pad_x = abs(pad_x)
            if column_adjust == 0 and pad_x == 0:                   
                """ >>> l i t e r a l  |  Formato fixed | se mantienen las coordenadas | sin tamaño de columna | escribes literalmente 
               """
                str_format = self.__formato_to_prango_fixed( rango= rango, len_columnas = 0, pad_x = 0)
                pass
            
            elif column_adjust > 0 and pad_x == 0:                   
                """ Modo literal con tamaño de columna minimo """
                str_format = self.__formato_to_prango_fixed( rango= rango, len_columnas = column_adjust, pad_x = 0)
            
            elif column_adjust == 0 and pad_x > 0:                   
                """ columna Sin tamaño fijo pero no restrictivo. Con pad_x > 0 . 
                El pad_x se aplica al final del ultimo texto como ' ' o como self.char_padx . 
                puede valer para xindex """
                str_format = self.__formato_to_prango_fixed( rango= rango, len_columnas = 0, pad_x = pad_x)
                lst_max_len = self.get_lst_max_filas(rango = rango)

            elif column_adjust > 0 and pad_x > 0:                   
                str_format = self.__formato_to_prango_fixed( rango= rango, len_columnas = column_adjust, pad_x = pad_x)
                lst_max_len = self.get_lst_max_filas(rango = rango)
            pass
        elif isinstance(column_adjust, list):
            """ >>> Entra con una lista de int con el tamaño del formato para cada columna de la lista. 
            Y o   E l i j o  d e s d e   f u e r a   el tamaño de las columnas. < Modo  personalizado >
            El pad_x da igual en este caso, se le aplica el que haya """            
            # Validacion del tipo
            try:
                lst_lens = [int(item) for item in column_adjust]
                str_format = self.__formato_to_prango_list(rango=rango, lista=lst_lens , pad_x=0)
            except Exception:
                return None
            pass
            
        else:
            return
        
        """ pppppppppppppppppppppppppppppppppppppppppppppppppp
        >>> I m p r i m e   v a l o r e s  
        """
        
        # Paso los valores de rango.dicc a rango.matriz
        rango.dicc_to_matriz()
        
        # Recorro las filas
        for i in range( rango.data['total_filas'] ):
            lst_filas = self.__get_fila_rango_prango(rango=rango , fila_a_buscar = i )
            print(str_format.format(*lst_filas))  # Cuando b_num_filas == False, no imprime los numeros de las Filas
    
    # # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    #   F R O M   F I L A   T O   F I L A 
    def Prango_rows(self, desde:int, hasta:int, column_adjust = None , pad_x:int = 0 ):
        """ >>> imprime desde la fila hasta la fila con las mismas características que Prango 
        [desde](int): el numero de la fila de inicio.
        [hasta](int): el numero de la fila de fin.
        [column_adjust](int, bool, list)    .... ver documentacion de Prango.
        [pad_x](int):                        .... ver documentacion de Prango.
        """
        # Cogemos sólo los nombres de los rangos que tienen 'rango_fila_' en su nombre
        lst_nombre_rango = [rango.data['nombre'] for rango in self.lst_rangos  if self.BASE_RANGO_FILA in rango.data['nombre'] ]

        if not lst_nombre_rango: 
            return None
        for i , nombre_rango in enumerate(lst_nombre_rango):
            if desde <= i <= hasta:
                self.Prango(nombre_rango = nombre_rango  , column_adjust = column_adjust , pad_x = pad_x)
    
    def Prango_cols(self, desde:int, hasta:int, column_adjust = None , pad_x:int = 0):
        """ >>> imprime desde la column hasta la columna con las mismas características que Prango 
        """
        # Cogemos sólo los nombres de los rangos que tienen 'rango_columna_' en su nombre
        lst_nombre_rango = [rango.data['nombre'] for rango in self.lst_rangos  if self.BASE_RANCO_COLUMNA in rango.data['nombre'] ]
        if not lst_nombre_rango: 
            return None
        for i , nombre_rango in enumerate(lst_nombre_rango):
            if desde <= i <= hasta:
                self.Prango(nombre_rango = nombre_rango  , column_adjust = column_adjust , pad_x = pad_x)

    #  Devuelve los  v a l u e s   de   u n a   f i l a   d e   u n   r a n g o .
    def __get_fila_rango_prango(self, rango,  fila_a_buscar:int):
        if not rango: 
            return None
        if SttS.b_fila_valida( fil = fila_a_buscar , from_incl=0, to_incl = rango.data['total_filas'] ) == False: 
            return None
        for f, dicc_cols in enumerate(rango.matriz):
            if  f == fila_a_buscar:
                return dicc_cols.values()

    # FORMATO IMPR _____________________________
    def __formato_to_prango_maxcol(self, rango, pad_x = 0 ):        
        """ >>> Pone cada columna a su maximo 
        strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}" 
        [len_columnas](int)(list) : Longitud de la columna fijo... cuando b_ajustado = False
        [pad_x](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y el siguiente.
        """  
        totalLen=0
        strformato=''
        if pad_x >= 0:
            """ Ajustado y con PadX -> calcula el maximo de la columna y le añade un margen de pad_x """
            for i in range (rango.data['total_columnas']): 
                maximo = self.get_max_columna(columna=i)
                maximo += pad_x
                strformato += "{:<" + str(maximo) + "}"
        else:
            for i in range (rango.data['total_columnas']):
                maximo = self.get_max_columna(columna=i)
                strformato += "{:<" + str(maximo) + "}"

        # print(strformato)
        return strformato
    
    # FORMATO IMPR _____________________________
    def __formato_to_prango_fixed(self, rango, len_columnas = 0, pad_x=0):        
        """ >>> Imprime un Rango sin ajuste de ventanas.
        [len_columnas](int) : Longitud de la columna fijo... cuando b_ajustado = False
        [pad_x](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y el siguiente.
        """  
        totalLen = 0
        strformato = ''
        """ >>> strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}"  """                

        for i in range (rango.data['total_columnas']):
            strformato += "{:<" + str(len_columnas + pad_x) + "}"
        return strformato
    
    # FORMATO IMPR _____________________________
    def __formato_to_prango_list(self, rango, lista , pad_x=0):        
        """ >>> Imprime un Rango sin ajuste de ventanas.
        [len_columnas](int) : Longitud de la columna fijo... cuando b_ajustado = False
        [pad_x](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y el siguiente.
        """  
        strformato = ''
        """ >>> strformato += "{:<" + str(len(item)) + "}"  pejem: {:<"+str(15)+"}"  """                
        
        # iguala las listas
        lista = SttS.igualar_listas(listaKeys = rango.matriz[0], listaToReLong = lista, valor_relleno=0)

        # crea el formato
        for item in lista:
            strformato += "{:<" + str(item) + "}"
        return strformato

    # ____ L i s t a   c o n   l a s   l o n g i t u d e s   d e l   c o n t e n i d o   d e   c a d a   f i l a  (el total) maxima  
    def get_lst_max_filas(self, rango):
        """ obtiene la longitud de cada fila del rango. Sobreescribe la misma funcion de tablero """

        lst_fila    = []
        long_fila   = 0
        for dicc_fila in rango.matriz:
            long_fila=0
            for cadena in dicc_fila.values():
                long_fila += len(str(cadena))

            lst_fila.append(long_fila)    

        # lst_fila = [sum(len(cadena) for cadena in dicc_fila.values()) for dicc_fila in rango.matriz]                
        return lst_fila if lst_fila else None
  
    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    #               O U T   O F   T A B L E R O         -   R A N G U T A N   - 
    # # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    """ Desde Fuera hacia el rango - tablero  """
    # mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    def lista_to_rango(self, lista, nombre_rango):
        """ Entra una lista de valores y se la asigna directamente al rango uno a uno..."""
        rango = self.buscar_rango( nombre_a_buscar = nombre_rango )
        if not rango: return None
        
        """ Recorro el diccionario y meto los valores hasta que quepan validando la existencia en cada momento """
        for i, celda in enumerate( rango.dicc.keys() ):
            if 0 <= i < len(lista):
                rango.dicc[celda] = lista[i]
            else:
                break
        pass
        rango.dicc_to_matriz()
        return True
    
    # mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    def lista_to_tablero(self, lista, celda_inicio, pega_horizontal = True):
        """ >>> Entra una lista y acaba en el tablero:  1- Crea un rango oculto de lista( misma_fila ) 
        puede entrar una lista o un str separado por comas que se convertirá en una lista.
        """
        # lista _________________________________
        if isinstance(lista, list):
            pass
        elif isinstance(lista, str):
            lista_from_str = SttS.cadena_to_lista(cadena = lista)
            lista = lista_from_str
        else:
            return None
        # Dimension______________________________
        dimension_vertical = f'{ len(lista) }x1'
        dimension_horizontal = f'1x{ len(lista) }'
        nombre_rango_aux = 'rango_aux'
        dimension = dimension_vertical if pega_horizontal == False else dimension_horizontal
        """ 
        Crea un Rango Auxiliar """
        rango_aux = self.crear_rango( nombre = nombre_rango_aux , celda_inicio = celda_inicio, dimension = dimension , b_ghost=True )
        """ 
        lista To Rango Auxiliar """
        lst_to_rng =  self.lista_to_rango( lista = lista , nombre_rango = nombre_rango_aux )
        if not lst_to_rng: return None
        """ 
        Rango auxiliar to  Tablero """
        self.rango_to_tablero( nombre_rango = nombre_rango_aux )
        # if not lst_rng_to_tbl: return None
        """ 
        Elimina el rango auxiliar """
        del_rng_aux = self.elimina_rango( nombre_rango = nombre_rango_aux )

        if del_rng_aux:
            return True
        else:
            return False
    
    
    # mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm     wip
    def matriz_to_tablero(self, matriz, celda_inicio):
        """ >>> Entra una lista de listas (matriz) y acaba en el tablero:  
        1- Crea un rango oculto de matriz( rectangulo o cuadrado ) 

        self.matriz_to_tablero([[3, 2, 1] , [4, 5, 9] , [15, 29, 32]])      -> matriz simetrica
        self.matriz_to_tablero( [[3, 2, 1] , [4, 5] , [15, 9, 29, 32]] )    -> matriz NO simetrica"""
        try:
            rango_aux = self.matriz_to_rango( matriz = matriz , celda_inicio = celda_inicio , nombre_rango = 'rango_aux' )
            if not rango_aux: return False
            
            # Los datos trabajados sobre el rango los pasamos al tablero
            retorno = self.rango_to_tablero( nombre_rango = rango_aux.data['nombre'] )
            if  retorno == False:
                return False            
        except Exception as e:
            return False
        finally:
            return True
        
    def matriz_to_rango(self, matriz:list, nombre_rango:str = '', celda_inicio:str='A:0'):
        """ Pasa los valores de una matriz a un rango creado """
        retorno = SttS.es_lista_de_listas( matriz = matriz )
        if not retorno: return False
        filas = len(matriz)

        # Calculo la longitud de la dimension de la matriz maxima(por si no es simetrica.)
        lst_len_matriz = [len(item) for item in matriz]
        columnas = max(lst_len_matriz) if lst_len_matriz else 0
        
        # Creo una fila de columnas para rellenar los huecos
        lst_aux = [i for i in range(columnas)]

        # hago la matriz de entrada uniforme y relleno los vacios con el valor Inicial.
        for i  in range(len(matriz)):
            matriz[i] = SttS.igualar_listas(listaKeys = lst_aux, listaToReLong = matriz[i], valor_relleno = self.get_valor_inicial())

        # Saco la dimension para crear su rango ghost
        dimension = f'{filas}x{columnas}'

        b_eliminar_rango = False
        # Creo un nombre de rango único. si no mete nombre de rango, lo creo yo y luego lo elimino. Si mete nombre de rango, no lo elimino.
        if nombre_rango == '':
            nombre_rango = 'rango_aux_'
            b_eliminar_rango = True

        nombre_rango = self.__new_nombre_secuencial(cadena = nombre_rango)        
        pass
        try:
            # Creo el rango ghost
            rango_aux = self.crear_rango( nombre = nombre_rango , celda_inicio = celda_inicio, dimension = dimension , b_ghost=True )
            if not rango_aux: return False
            
            # Paso la matriz a una lista de izquierda a derecha de arriba a abajo.
            lst_matriz = [item for sublist in matriz for item in sublist]            
            if not lst_matriz: return False

            # ahora le pso la lista de la matriz pasada al rango ghost creado
            retorno = self.lista_to_rango( lista = lst_matriz , nombre_rango = nombre_rango )
            if not retorno: return False

            if b_eliminar_rango:
                rango_lista = self.elimina_rango( nombre_rango = nombre_rango )
                return rango_lista  if rango_lista  else False
            else:
                return rango_aux
            # Retorno solo si retorno existe
            
        except Exception as e:
            return False

   
    
    # ???????????????????????????????????????????????????????????????????????????????????
    # ???????????????????????????????????????????????????????????????????????????????????
    # Pruebas reconocimiento listas recursivas 
    def prueba_recursiva_Rangutan(self, matriz):
        """ 1-Reconoce el DataFrame. 2-Crea un Rango ghost 3-Pasamos el DataFrame al Rango. 4-...... """       

        lst_retorno = SttS.to_str_rcrsv(iterator = matriz)
        print(lst_retorno)


# ████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""  
                            -   M O N K E Y - M E N   -  
"""
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████

            # Usa la clase Tablero para Crear un Menu con 3 tableros distintos: Head, Body, Pie 
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# _________________________________________________________________________________________________
# V A R I A B L E S   G L O B A L E S   Y   C O N S T A N T E S   P A R A   T A B L E R O  P L U S
"""
Enumeracion que contiene los indices por letra y concepto de una posicion en una fila para un menu de 2 items... 'index' , 'item-menu' """
from enum import Enum as Fila
class FILA(Fila):    
    marco_i = 0  ; A = 0      # Columna Para el Marco
    x_margen = 1 ; B = 1      # Columna para el margen inicial
    sp1 = 2      ; C = 2      # Columna espacio pre item
    item1 = 3    ; D = 3      # Columna item
    sp2 = 4      ; E = 4      # Columna entre
    item2 = 5    ; F = 5      # Item
    sp3 = 6      ; G = 6      # Columna post item
    margen_x = 7 ; H = 7      # Columna para el margen final
    marco_f = 8  ; I = 8      # Columna para el marco

"""
Enumeracion que contiene los indices por letra y concepto de una posicion en una fila para un menu de 2 items... 'index' , 'item-menu' """
from enum import Enum as Menu

# import pyfiglet         # Letras compuestas de diferentes tamaños
# from colorama import Fore, Style    # Colores

class MENU(Menu):    
    HEAD = 0      # Tablero de cabecera
    BODY = 1      # Tablero del body(contenido)
    FOOT = 2      # Tablero del pie (Salida)


# TTTTTTTTTTTTTTTTTTTTTTTTT
# TTTTTTTTTTTTTTTTTTTTTTTTT
class Monkey_Men(Rangutan):
    """ >>> Def: Define las partes esenciales de un Menu Creando y manteniendo una lista de Tableros =>  Head  + Cuerpo + Pie + 
    linaje ::: Tablero -> Rangutan -> Monkey_Men   
    Definicion de Monkey_Men(x linea): 
    y_head  => margen + marco_h * total
    Head    => margen + marco_h + x_pad +DATA_ENTRADA) + pad_x + marco_h
    head_y  => margen + marco_h * total

    Cuerpo(x Fila)  => :  margen + marco_v + X_pad + DATA + pad_x + marco

    y_pie   => margen + marco_h_fin_datos * total
    Pie     => margen + marco_h +  DATA_SALIDA + marco_h
    pie_y   => margen + marco_h * total

    >>> DATA_ENTRADA:  Datos de entrada(HEAD) del menu. Puede ser un str o una lista de str o matriz de str
    >>> DATA:          Datos del cuerpo del menu. Puede ser un str o una lista de str o matriz de str
    >>> DATA_SALIDA:   Datos de salida(PIE) del menu. Puede ser un str o una lista de str o matriz de str
    """   
    NUM_CHAR = 40                        
    ESPACIO  = ' '

    def __init__(self,  dimension:str= "20x10", head = None, pie = None, margen = 0,  pad_x:int = 30 , x_pad:int = 3):        
        """ >>> Inicializa el Menu con los valores de la cabecera y el pie.
        [titulo](str): Titulo del Menu 
        [dimension](str): Dimension del Menu
        [head](str)(list): Frase del Head
        [pie]:(str)(list): Frase del Pie
        [x_pad]: Espacio entre el marco y el contenido
        [pad_x](int): Espacio desde el último caracter de la linea y el margen
        """

        self.num_filas, self.num_columnas = SttS.filas_columnas_from_dimension(dimension=dimension)
        if not self.num_filas or  not self.num_columnas: return None

        # M e   c o n f i g u r o   c o m o   R a n g u t a n e r o   por lo tanto tengo un Tablero
        super().__init__(total_columnas_tablero = self.num_columnas, 
                        total_filas_tablero = self.num_filas , 
                        valor_inicial='' )
        
        if not self.tablero: 
            print('\n\nNo se ha podido crear el tablero!!!!!!\n\n')
            return None
        
        """ >>> D e f i n i c i o n   d e   E s p a c i o s  H o r i z o n t a l e s"""
        self.pad_x = pad_x
        self.x_pad = x_pad
        self.margen = margen

        """  >>> C a r a c t e r  e s   H o r i  z o n t a l e s   x a   M a r c o  """
        self.marco_h = '█'    # 219       >>> caracter de la linea de inicio y cierre de: Head / Body / Pie

        """ >>> C h r a r s   V e r t i c a l e s   p a r a   e l   M a r c o   d e   l a   C a b e c e r a   y   e l   P i e """
        self.y_head = '■' # 254       >>> caracter de la primera linea de cabecera.
        self.head = head               # >>> La Frase Que se pone en el Head del Menu:                
        self.head_y = '▄'   # 220       >>> caracter de la linea de cierre del Head
        
        self.y_pie = '═'      # 205       >>> caracter de la linea de cierre               
        self.pie = pie            # >>> informacion del pie(Salida Help Repeat)
        self.pie_y = '■'  # 254       >>> caracter de la ultima linea de cierre del Pie
        
        """ >>> Lista de celdas  R e s e r v a d a s  x a   M a r c o """
        self.lst_celdas_reservadas_marco = []
        
        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
        """ >>>  G E S T I O N   D E   L O S   T A B L E R O S  """
        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
        self.dicc_gorila = {}

        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
        """ C R E A R   T A B L E R O  :  HEAD """
        # Puede venir en formato string, list o matriz(list de list de str).
        if self.head:
            if isinstance(self.head, str):
                """ >>> Si es un str, celda() o xy()  """
                self.tablero_head = Rangutan(total_columnas_tablero = self.num_columnas, total_filas_tablero = 1)
                self.tablero_head.celda(celda = 'C:0' , valor = self.head)
                pass
            elif isinstance(self.head, list):
                if SttS.es_lista_de_listas(matriz = self.head):
                    """ >>> CACHAR FILAS Y COLUMNAS. Si es una lista de listas, matriz_to_tablero() """
                    filas = len(self.head)
                    self.tablero_head = Rangutan(total_columnas_tablero = self.num_columnas, total_filas_tablero = filas)
                    self.tablero_head.matriz_to_tablero(matriz = self.head, celda_inicio = 'C:0')
                    pass                
                else:
                    """ >>> Si es una lista de str, lista_to_tablero() 1 X COLUMNAS"""
                    self.tablero_head = Rangutan(total_columnas_tablero = self.num_columnas, total_filas_tablero = 1)
                    self.tablero_head.lista_to_tablero(lista = self.head, celda_inicio = 'C:0')
                    pass
            
            self.tablero_head.tablero_to_all()
            self.dicc_gorila['head'] = self.tablero_head
            
        """ Borrar. solo para pruebas """
        HEAD = self.dicc_gorila['head']
            
        
        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
        """ C R E A R   T A B L E R O  :   PIE """
        # Puede venir en formato string, list o matriz(list de list de str).
        if self.pie:
            if isinstance(self.pie, str):
                """ >>> Si es un str, celda() o xy()  """
                self.tablero_pie  = Rangutan(total_columnas_tablero = self.num_columnas, total_filas_tablero = 1)
                self.tablero_pie.celda(celda = 'C:0' , valor = self.pie)
                pass
            elif isinstance(self.pie, list):
                if SttS.es_lista_de_listas(matriz = self.pie):
                    """ >>> cachar filas y columnas... luego, Si es una lista de listas, matriz_to_tablero() """
                    filas = len(self.pie)
                    self.tablero_pie  = Rangutan(total_columnas_tablero = self.num_columnas, total_filas_tablero = filas) 
                    self.tablero_pie.matriz_to_tablero(matriz = self.pie, celda_inicio = 'C:0')
                    pass
                else:
                    """ >>> cachar columnas y 1 x len(self.pie).... luego,  Si es una lista de str, lista_to_tablero() """
                    self.tablero_pie  = Rangutan(total_columnas_tablero = self.num_columnas, total_filas_tablero = 1)
                    self.tablero_pie.lista_to_tablero(lista = self.pie, celda_inicio = 'C:0')
                    pass
            # self.tablero_pie  = Rangutan(total_columnas_tablero = self.num_columnas, total_filas_tablero = 2)        
            self.tablero_pie.tablero_to_all()
            self.dicc_gorila['pie'] = self.tablero_pie

            """ Borrar. solo para pruebas """
        PIE = self.dicc_gorila['pie']
        

        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
        """ C R E A C I O N   D E L    M A R C O  """       # █219 ▄220  ▀223 ■254 ▓178 ▒177 ░176 »175 «174 ┼167 ╣185 ┤180 
        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦       
        self.set_marco(margen = self.margen ,  x_pad = self.x_pad, pad_x = self.pad_x)


        """ THE END .... de aqui en adelante borrar. """

        """ R E L L E N O   D E   P R U E B A S   . . .   B O R R A R   """       # █219 ▄220  ▀223 ■254 ▓178 ▒177 ░176 »175 «174 ┼167 ╣185 ┤180 
        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦       

        """ Relleno del body de pruebas......  
        Hay que r e d e f i n i r   l a s   f i l a s   ú t i l e s    teniendo en cuenta los caracteres del marco.
        para cuaando se llame a Prango o to_print o Prango_rows
        Reducir prango y prango_to a una sola funcion de impresion... Prango(incluir from - to ) """        
        # Los Pasos  para imprimir tiene que ser: 
        # 1-Asignacion de datos en body + 2-Creacion_marco + 3-preparacionImpresion + 4-Impresion
        # self.xy(fil=4, col='B', valor = self.ESPACIO*self.x_pad)
        self.xy(fil=4, col='E', valor='En un lugar de la mancha jAJAJAJAJAJAJAJAJA')
        matriz = [
            [1, 2, 3],
            [4, 5],
            [7, 8, 9, 8]
        ]        
        retorno = self.matriz_to_tablero(matriz = matriz, celda_inicio = 'M:8')

        
        # HEAD.xy(fil=1, col='C', valor = 'F r a s e   d e   E n t r a d a')
        # PIE.xy(fil=0, col='C', valor = 'F r a s e   d e   S a l i d a')
        

        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
        """ - P R E P A R A C I O N   X A    I M P R E S I O N   D E L   M E N U  - """
        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦       
        
        # Recopilando los datos para colocar el marco... incluye: margen, len(marco_h), x_pad, data , pad_x, len(marco_h)
        len_head = HEAD.get_max_filas()
        len_body = self.get_max_filas()
        len_pie = PIE.get_max_filas()
        maximo : int = max(len_head, len_body, len_pie)
        print(f'longitud maxima del menu = {maximo}')
        
        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
        # self.total_len: int = self.margen + len(self.marco_h) + self.x_pad + maximo + self.pad_x + len(self.marco_h)
        self.total_len: int = maximo 


        # paso del tablero al rango principal.... de esta forma puedo imprimir con Prango
        HEAD.tablero_to_rango()
        # colocando el pie
        lst_length_head = HEAD.get_lst_max_filas( rango = HEAD.rango_tablero )
        print(lst_length_head)        
        lst_num_faltan = [ self.total_len - int(length)  for length in lst_length_head ]
        """ >>> Devuelve una lista con las longitudes que faltan para completar la longitud total 
        """
        for i, faltan in enumerate(lst_num_faltan):
            HEAD.xy(fil=i, col= HEAD.ultima_columna(), valor=f'{self.ESPACIO * ( faltan + self.pad_x )}█')
        HEAD.tablero_to_rango()
        # print(f'{'█'*self.total_len}')

        # paso del tablero al rango principal..... de esta forma puedo imprimir con Prango...in the future
        self.tablero_to_rango()
        # colocando el pie
        lst_length = self.get_lst_max_filas( rango = self.rango_tablero )
        print(lst_length)
        lst_num_faltan = [ self.total_len - int(length) for length in lst_length ]
        # lst_num_faltan = [ self.total_len - self.pad_x for length in lst_length ]
        for i, faltan in enumerate(lst_num_faltan):
            self.xy(fil=i, col= self.ultima_columna(), valor=f'{self.ESPACIO * (faltan + self.pad_x)}█')
        self.tablero_to_rango()

        # paso del tablero al rango principal..... de esta forma puedo imprimir con Prango
        PIE.tablero_to_rango()
        # colocando el pie
        lst_length_pie = PIE.get_lst_max_filas( rango = PIE.buscar_rango(PIE.BASE_RANGO_TABLERO) )
        print(lst_length_pie)
        lst_num_faltan_pie = [ self.total_len - int(length) for length in lst_length_pie ]
        for i, faltan in enumerate(lst_num_faltan_pie):
            PIE.xy(fil=i, col= PIE.ultima_columna(), valor=f'{self.ESPACIO * (faltan + self.pad_x)}█')
        PIE.tablero_to_rango()

        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
        """ -  I M P R E S I O N   D E L   M E N U  - """
        # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦       
        print()
        print(f'{'▀' * ( maximo )}')        #220
        # HEAD.to_print(b_ajustado = False, numSP=0, b_columnas_head = False    , b_num_filas=False, pad_x=0)
        HEAD.Prango( nombre_rango = HEAD.BASE_RANGO_TABLERO, column_adjust = 0 , pad_x = 0)
        print(f'{'▄' * ( maximo  )}')          #220
        
        # self.to_print(b_ajustado = False, numSP=0, b_columnas_head = False  , b_num_filas =True, pad_x=0)
        # self.Prango( nombre_rango = self.BASE_RANGO_TABLERO, column_adjust = 0 , pad_x = 0)        
        self.tablero_to_rango()
        self.Prango_rows(desde = 1, hasta =25, column_adjust = 0 , pad_x = 0 )

        print(f'{'▀' * ( maximo )}')    
        PIE.Prango( nombre_rango = PIE.BASE_RANGO_TABLERO, column_adjust = 0, pad_x = 0)
        print(f'{'▀' * ( maximo )}')        #223 ■
        # print(f'{'■' * ( maximo + self.x_pad + 2 )}')        #223 ■
        

    # Impresion de l clase
    def __str__(self):                
        return f'Sin Asignacion .... WIP'

    # __________________________________________________________________
    # CAMBIA EL ESTILO(CARACTERES DE CABECERA, PIE, PRE-NUM , POST-NUM )
    def style(self, y_head:str = '', head:str = '' ,  head_y:str = '' ,  y_pie:str = '' , marco_h:str = '' , pie:str = '' , pie_y:str= '' , pad_x:int = 0 , x_pad:int = 0):
        """ >>> Cambia el estilo de los caracteres del menu 
        Se pueden cambiar todos los char, la head y la pie. """
        if y_head: self.y_head = y_head
        if head: self.head = head
        if head_y: self.head_y = head_y
        if marco_h: self.marco_h = marco_h
        if y_pie: self.y_pie = y_pie
        if pie: self.pie = pie
        if pie_y: self.pie_y = pie_y
        if pad_x: self.pad_x = pad_x
        if x_pad: self.x_pad = x_pad
    
    # def texto_fuente_color(self, texto, fuente="mini", color=Fore.CYAN):
    #     ascii_art = pyfiglet.figlet_format(texto, font=fuente)
    #     return color + ascii_art + Style.RESET_ALL
    
    

    # mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    # PONE UN MARCO EN TODO EL TABLERO (TODAS SUS FILAS CON '|'  Y EN TODAS SUS COLUMNAS '_' o '-' o '~' o '='
    def set_marco(self, margen:int = 0, x_pad:int = 5, pad_x:int = 40):
        """ >>> Pone un marco en todo el tablero (todas sus filas con '|'  y en todas sus columnas '_' o '-' o '~' o '='
        [margen] (int) el margen entre el inicio de linea y el marco.
        [pad_x] (int) espacio entre el final de la linea y el marco. se asigna a la ultima columna del tablero.
        [x_pad] (int) espacio entre el inicio de la linea y el inicio del contenido. se asigna a la column B. 

        """
        if not self.tablero: 
            return None
        if not self.dicc_gorila: 
            return None

        # V a l i d a c i o n   d e   t i p o s   y   e v i t o   v a l o r e s   n e g a t i v o s 
        try:
            margen=abs(margen)
            x_pad=abs(x_pad)
            pad_x=abs(pad_x)
        except Exception as e:
            return False

        # C a c h o   e l   h e a d   y   e l   p i e ... creados en __init__
        try:
            HEAD = self.dicc_gorila['head'] if self.dicc_gorila['head'] else None
            PIE  = self.dicc_gorila['pie']  if self.dicc_gorila['pie']  else None
        except Exception as e:
            return False

        # ::: M A R C O   o v e r   h e a d :::        
        if HEAD:
            try:
                HEAD.set_valor_over_columna(columna='A', valor=f'{self.ESPACIO * margen}█{self.ESPACIO * x_pad}') 
                HEAD.set_valor_over_columna(columna=HEAD.ultima_columna(), valor = f'{self.ESPACIO * pad_x}█')         
                # HEAD.set_valor_over_columna(columna='B', valor=self.ESPACIO*self.x_pad)
                # HEAD.set_valor_over_columna(columna=HEAD.ultima_columna(),  valor=self.ESPACIO*self.pad_x)    
            except Exception as e:
                return False

        # ::: M A R C O   o v e r   b o d y ::: .... si hay tablero, hay body.
        self.set_valor_over_columna(columna='A', valor=f'{self.ESPACIO * margen}█{self.ESPACIO * x_pad}')
        self.set_valor_over_columna(columna=self.ultima_columna(), valor = f'{self.ESPACIO * pad_x}█')

        # ::: M A R C O   o v e r   p i e :::
        if PIE:
            try:
                PIE.set_valor_over_columna( columna = 'A', valor = f'{self.ESPACIO * margen}█{self.ESPACIO * x_pad}' )                
                PIE.set_valor_over_columna( columna = PIE.ultima_columna(), valor = f'{self.ESPACIO * pad_x}█' )
                # PIE.set_valor_over_columna(columna='B', valor=self.ESPACIO*self.x_pad)
                # PIE.set_valor_over_columna(columna=PIE.ultima_columna(), valor=self.ESPACIO*self.pad_x)         
            except Exception as e:
                return False
        
        # ahora tengo que cachar la lista de self.lst_celdas_reservadas_marco para no introducir datos en las celdas marco
        self.lst_celdas_reservadas_marco = [f'{self.rango_tablero.data['letra_inicio']}:{i}' for i in range(self.num_filas)]        
        self.lst_celdas_reservadas_marco +=[f'{self.rango_tablero.data['letra_fin']}:{i}' for i in range(self.num_filas)]
        return True    
    
    def es_reservada(self, celda)->bool:
        """ >>> Valida si la celda es una celda reservada para el marco. """
        return True if celda in self.lst_celdas_reservadas_marco else False
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================