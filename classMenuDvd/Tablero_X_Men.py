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
    #  [dicc1] ==> 'A':0, 'B':1, ... 'AZ':702  |  [dicc2] ==>   0:'A', 1:'B', ... 702:'AZ'

    @staticmethod
    def set_dicc_columnas_may():
        """ RETORNA 2 DICCIONARIOS => 'A':0, 'B':1, ... 'AZ':702  y otro invertido =>  0:'A', 1:'B', ... 702:'AZ' 
        SttS._may_ln , SttS._may_nl
        """
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

    # VALIDA UNA FILA ENTRE DOS VALORES POSIBLES FROM Y TO ________________
    @staticmethod
    def b_fila_valida(fila, from_incl , to_incl ):
        try:
            fila=int(fila)
            if from_incl <= fila <= to_incl:  
                return True
            else:
                return False
        except Exception as e:
            return False

    # VALIDA QUE UNA COLUMNA ESTA EN EL RANGO FROM - TO _________________
    @staticmethod
    def b_columna_valida(columna, from_incl , to_incl):
        """ >>> Valida que una columna puede estar dentro del rango total de columnas posibles(desde a hasta az) 
        """
        # __________________________________________
        # Si no existen los diccionarios, los crea.
        SttS._inicializa_diccs_letra_numero()

        """ Viene como [Letra] y esta entre las combinacioes posibles('az' maximo, 'bn' sería falso) """
        if columna in SttS._may_ln or columna in SttS._min_ln:            
            numero_letra = SttS.letra_to_numcol(columna)
            if numero_letra == None: 
                return False
            if from_incl <= numero_letra <= to_incl:  
                return True
            else:
                return False

        """ Viene como [Numero] y esta entre las combinacioes posibles. 
        Lo typeo para que de igual si viene como 1 o como '1'         """
        if int(columna) in SttS._may_nl or int(columna) in SttS._min_nl:
            if from_incl <= columna <= to_incl:  
                return True
            else:
                return False

        return False        
        
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

    # IGUALA LAS LISTAS ____________________________________________________
    @staticmethod
    def igualar_listas(lista_keys, lista_to_relong, valor_relleno='Loren'):
        """             
        Trata las longitudes de las listas y las igualo según lista_keys como referencia.
        La que se Re-dimensiona creciendo o decreciendo para igualarse con lista_keys.
        [valor_relleno]: en caso de que lista_keys>listaToRelong, hay que rellenar con un nuevo valor. en caso de funciones, None(by Def)
        [Ejemplo de uso]:
        >>> listTOdict_byTcld_ToString.igualar_listas(lista_keys=lista_keys, lista_to_relong=listaTipos)        
        lista_keys y listaTipos son inmutables, se pasan por referencia y no hay que retornar valor. Aun así se retorna
        """
        if len(lista_keys)==len(lista_to_relong):
            return lista_to_relong
        elif len(lista_keys)>len(lista_to_relong):
            # print("long dicc > longTipo.....tipos hasta longTipo y luego Tipo=str y PERMITENULL=False")
            listaNewTipos=[valor_relleno for i, (k) in enumerate(lista_keys) if i >= len(lista_to_relong)]
            lista_to_relong = lista_to_relong + listaNewTipos
            # print(lista_to_relong)
        else:
            # print("long dicc < longTipo.....vale hasta la long del dicc- hay que reducir la dimension del la lista_to_relong")
            longListaTipos = len(lista_to_relong)
            longListaKeys  = len(lista_keys)
            for i in range(longListaKeys , longListaTipos ):
                lista_to_relong.pop()

        return lista_to_relong
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

    # 'frase ejemplo' en 'f r a s e  E j e m p l o' 
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
    
    # ENTRA UNA CELDA (C:2) Y DEVUELVO   3 , 2 . HACE VALIDACIONES DE TIPO
    @staticmethod
    def fc_by_celda(celda:str):
        """ >>> From 'C:4' To fila 4, columna 3         """
        # Validaciones
        fila    = None
        columna = None
        try:
            if not isinstance(celda, str): return None, None
            letra_columna , fila = SttS.desata_binomio(cadena=celda, char=':')
            if not letra_columna: return None, None
            columna = SttS.letra_to_numcol(letra=letra_columna)               
            if  fila == None or columna == None: return None, None            
            
            fila = int(fila) 
            columna = int(columna)

        except Exception as e:
            print(f'Error en num_col_by_celda{e}')
            return None, None
        finally:
            return abs(fila), abs(columna)        

    # ENTRA UNA fila y columna (3 , 2) y devuelvo una celda (C:2)
    @staticmethod
    def celda_by_fc(fila:int, columna:int):
        try:        
            """ Lo trato como número.... si casca, es letra. """
            columna = int(columna)
            letra = SttS._may_nl[columna]
            celda = f'{letra}:{fila}'
        except Exception as e:
            """ viene como letra """
            celda = f'{columna}:{fila}'

        return celda

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
    
    # Entra una matriz o lista y la convierte recursivmente en una lista de elementos unicos. No contempla dict.
    @staticmethod
    def aplanar_matriz(matriz):
        """ >>> Funcion recursiva que aplana matrices(listas de listas) o listas o datos. 
        [data] es cualquier dato de entrada(menos diccionarios, que los añade como un valor.)
        Retorno: lst de una sola dimension.
        Ejemplo: SttS.aplanar_matriz( [3,4,[5,6,7],8,[9,10]] ) -> [3,4,5,6,7,8,9,10]
        """
        lista = []
        try:
            for elemento in matriz:
                if isinstance(elemento, list) or isinstance(elemento, tuple)  or isinstance(elemento, set) :
                    lista.extend(SttS.aplanar_matriz(matriz=elemento))
                else:
                    lista.append(elemento)
        except Exception as e:
            print(f'Error ::: aplanar_matriz ::: {e}')
            return None
        return lista

    # lo contrario de SttS.aplanar_matriz(). 
    @staticmethod
    def encuadrar_matriz(matriz:list):
        """ >>> Pasa los valores de una matriz a un rango creado a partir de una celda determinada del rango.
        la diferencia con set_data_plana() es que set_data_plana lo mete lineal, valor por valor. 
        push_matriz mete una matriz con su forma en el rango. Para ello tiene que ser menor que el rango.
        en caso de ser mayor se puede crear un rango para tener acceso a su lst_celdas y verificar si coinciden.

        entra [3, 2, [4, 6]] y devuelve => [ [3,''] , [2,''] , [4,6] ]      3 filas x 2 columnas.
        entra [[3, 2] , [4, 6]] y devuelve => [ [3,2] , [4,6] ]             2 filas x 2 columnas.
        entra [3, 2, 4, 6] y devuelve => [3,2,4,6]                          1 filas x 4 columnas ... o 1 columna x 4 filas ;)
        entra [3, [2], 4, 6] y devuelve => [3,2,4,6]                        1 filas x 4 columnas ... o 1 columna x 4 filas ;)


        """
        # Validaciones previas con la dimension... la vuelvo plana por si acaso
        matriz_plana = SttS.aplanar_matriz(matriz=matriz)
        if not matriz_plana: return None 

        b_valid = SttS.es_lista_de_listas( matriz = matriz )
        if not b_valid: return None
        """ 
        >>> Calculo la longitud de la dimension de la matriz maxima(por si no es simetrica.) """
        try:
            filas = len(matriz)
            lst_len_matriz = [len(item) for item in matriz]
            columnas = max(lst_len_matriz) if lst_len_matriz else 0
            
            dimension = f'{filas}X{columnas}'       # Saco la dimension
        except Exception as e:
            return None

        """ 
        >>> Creo la nueva matriz uniforme """
        try:        
            # Creo una fila de columnas para rellenar los huecos
            lst_max_columna = [i for i in range(columnas)]

            # hago la matriz de entrada uniforme y relleno los vacios con el valor Inicial fila x fila 
            for i  in range(len(matriz)):
                matriz[i] = SttS.igualar_listas(lista_keys = lst_max_columna, lista_to_relong = matriz[i], valor_relleno = Celda.VALOR_INICIAL)
        except Exception as e:
            return None
        
        # Retorno ....la matriz recuadrada a su columna maxima
        return matriz

# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
""" 
                                        -  C E L D A   -  
"""
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# >>> Con la celda de inicio[C:2] y la dimension(3x4) ( o celda fin[H:8] ) tenemos todos los datos para crear un rango......
class Celda():
    """ >>> Clase que Define una Celda como entidad con fila y columna.....de momento es un concepto. 
    Cobra cuerpo en Rango. 
    HIPOTESIS ═> Rango podría heredar de Celda y Tablero podría heredar de Rango, siendo definido por celda inicio y celda fin.
    VALOR_INICIAL = ''
    """
    VALOR_INICIAL = ''
    
    def __init__(self, valor = None , **kwargs):
        """ >>> Crea una celda y le asigna un valor de inicio.
        [fila](int):  Fila de la celda.
        [columna](int/str): 
        [valor]:
        Retorno:            
        >>> ej: Celda(fila=3, columna=0, valor = 'Hola') => pone el valor 'Hola' sobre la celda A:2
        >>> ej: Celda(celda="A:2" , valor = 'Hola')      => pone el valor 'Hola' sobre la celda A:2
        >>> ej: Celda(celda='A:2') => Pone el valor '' sobre la celda A:2
        
        """     
        # ▄▄▄▄▄▄▄▄▄▄  Establece los dicc validos para columna: letra:numero y numero:letra
        SttS._inicializa_diccs_letra_numero()

        # ▄▄▄▄▄▄▄▄▄▄  RECOGE LOS VALORES DE FILA , COLUMNA  O CELDA.
        self.fila = kwargs.get('fila', None)
        self.columna = kwargs.get('columna', None)
        self.nombre_celda = kwargs.get('celda', None)
        self.letra = ''
        
        # ▄▄▄▄▄▄▄▄▄▄  EVALUA EL RESULTADO
        if self.nombre_celda == None and self.fila == None and self.columna == None: 
            return None
        
        elif self.nombre_celda != None:             # Si entra una celda, la descompone en fila y columna y lo Prioriza sobre fila y columna en caso de querer meter tb esos valores.
            try:
                self.fila, self.columna = SttS.fc_by_celda(celda=self.nombre_celda)   # devuelve los valores abs de fila y columna o None, None
                if self.fila == None or self.columna == None: 
                    return None
                self.letra = SttS._may_nl[self.columna]      # Paso a letra
            except Exception as e:
                print(f'Error __init__ Celda :::: {e}')
                return None
        elif self.fila != None and self.columna != None:        # Si entra fila y columna, calculo la celda
            try:
                self.fila = abs(self.fila)                
                """ 
                Trabajamos con la  c o l u m n a ... pq puede venir como letra o como numero. """
                if isinstance(self.columna, str):           # E n t r a   u n a   l e t r a 
                    if isdigit(self.columna):               # E n t r a   u n a   n u m e r o  e n   s t r i n g
                        self.columna = abs(self.columna)
                        self.letra = SttS._may_nl[self.columna]      # Paso a letra...y mayusculas
                    else:
                        self.columna = self.columna.upper()         # Paso a mayusculas
                        self.letra = self.columna                   # Paso a letra
                        self.columna = SttS._may_ln[self.letra]      # Paso a numero
                
                elif isinstance(self.columna, int):         # E n t r a   u n   n u m e r o
                    self.columna = abs(self.columna)        # Paso a natural
                    self.letra = SttS._may_nl[self.columna]      # Paso a letra
                
            except Exception as e:
                print(f'Error __init__ Celda :::: {e}')
                return None
        else:
            print(f'Error __init__ Celda :::: Entrada de datos erronea :::: {e}')
            return None

        # ▄▄▄▄▄▄▄▄▄▄  v a l o r    
        if valor is None:
            valor = self.__class__.VALOR_INICIAL        
        self.valor = valor
        # ▄▄▄▄▄▄▄▄▄▄  Celda en formato 'A:0' 
        self.nombre_celda = f"{self.letra}:{self.fila}"

    def __str__(self):
        return f"{self.nombre_celda} = {self.valor}"
        
    def get_fila(self):
        return self.fila if self.fila else 0
    def get_columna(self):
        return self.columna if self.columna else 0
    def get_letra(self):
        return self.letra if self.letra else ''
    def get_nombre_celda(self):
        return self.nombre_celda if self.nombre_celda else ''
    def get_valor(self):
        return self.valor 
    def set_valor(self, valor, b_iter_to_str:bool=True):
        """ >>> Establece el valor de la celda y lo guarda en el diccionario celda:valor.
        [valor]: El valor a establecer en la celda.
        [b_iter_to_str]: Si es True, convierte el valor a string antes de guardarlo... int, list, dict, objetos, ....
        >>> Si quieres guardar un objeto(por ejemplo) debes poner False(guardarlo exactamente).
        ej: celda.set_valor(10, b_iter_to_str=False) => Guarda el 10 como int y no como str.
        ej: celda.set_valor(10, b_iter_to_str=True)  => Guarda el 10 como str.
        ej: celda.set_valor(10) => Guarda el 10 como str ( '10' ).
        """
        # if isinstance(valor, iterator):
        if isinstance(valor, str) or isinstance(valor, list) or isinstance(valor, tuple) or isinstance(valor, set) or isinstance(valor, dict):
            if isinstance(valor, str):
                self.valor = valor
            else:
                if b_iter_to_str == True:
                    self.valor = str(valor)
                else:
                    self.valor = valor
        else:
            self.valor = valor
        return self.valor

    # SUMA UNA FILA A UNA CELDA y DEVUELVE LA CELDA RESULTANTE
    def sumar_filas(self, filas:int = 1, b_copy_value = False):
        """ >>> Suma/O resta una cantidad de filas a una celda y devuelve la celda resultante 
        >>> No Transforma la celda en la que está, sino que crea una nueva celda con la suma de filas.
        >>> Hace validacion de que la fila no se pase de los limites de las filas posibles. 
            Si te pasas por abajo, lo deja en Zero(0)
            Por arriba no hay límite de filas....de momento.
        """
        try:
            new_fila = self.fila + filas
            if new_fila < 0: new_fila = 0   # las filas o tienen límite por arriba
            
            new_celda = f"{self.letra}:{new_fila}"
            if b_copy_value == True:
                return Celda(celda=new_celda , valor=self.valor)
            else:
                return Celda(celda=new_celda, valor=Celda.VALOR_INICIAL)            
        except Exception as e:
            print(f'Error suma_filas :::: {e}')
            return None
    
    def sumar_columnas(self, columnas:int = 1, b_copy_value = False):
        """ >>> Suma(o resta) una cantidad de columnas a una celda y devuelve la celda resultante 
        >>> No Transforma la celda en la que está, sino que crea una nueva celda con la suma de columnas.
        >>> Hace validacion de que la columna no se pase de los limites de las columnas posibles. 
            Si te pasas por abajo, lo deja en Zero(0)
            Si te pasas por arriba, lo deja en el máximo de columnas posibles=>(702)=>(len(SttS._may_ln))
        """
        try:
            new_columna = self.columna + columnas
            if new_columna < 0: new_columna = 0                                         # limite por abajo
            if new_columna >= len(SttS._may_ln): new_columna = len(SttS._may_ln) - 1    # limite por arriba
            new_celda = f"{SttS._may_nl[new_columna]}:{self.fila}"
            if b_copy_value == True:
                return Celda(celda=new_celda , valor=self.valor)
            else:
                return Celda(celda=new_celda, valor=Celda.VALOR_INICIAL)            
        except Exception as e:
            print(f'Error suma_columnas :::: {e}')
            return None
    
    def sumar_fc(self, filas:int, columnas:int, b_copy_value:bool = False):
        celda_suma_fila = self.sumar_filas(filas = filas, b_copy_value = b_copy_value)
        if not celda_suma_fila: return None
        celda_resultado = celda_suma_fila.sumar_columnas(columnas = columnas, b_copy_value = b_copy_value)
        return celda_resultado if celda_resultado else None


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
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# >>> Con la celda de inicio[C:2] y la dimension(3x4) ( o celda fin[H:8] ) tenemos todos los datos para crear un rango......
class Rango(Celda):
    """ Clase que crea un Rango. Que Qué es un rango? y tu lo pregutas...
    Un rango es una coleccion de datos. Equiparacion con celdas.... información. 
    Contiene como variables fundamentales la variable data, dicc, matriz, 
    b_ghost==True cambia el funcionamiento del rango y pasa de tener reflejo inmediato a ser un objeto virtual.    
    """
    def __init__(self, nombre_rango, celda_inicio:str = 'A:0', dimension:str = "1x1" ,  b_oculto = False, valor_inicial='', b_ghost=False):
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
        # VALIDACION INICIAL
        if not isinstance(dimension, str): return None
        fila, columna = SttS.fc_by_celda( celda = celda_inicio )        # valida que celda se introduce con el formato correcto.
        if fila == None or columna == None: return None

        super().__init__( celda = celda_inicio )
        """ >>> C e l d a   d e   i n i c i o  Rango se define como una celda de Inicio y a partir de ahora le sumamos cosas
        """ 

        # >>> DIMENSION  Puede venir como una celda de fin(AX:9) o como una dimension(3x4)  
        self.total_filas, self.total_columnas = self.__desempaqueta_dimension(dimension=dimension)  
        if self.total_filas == None or self.total_columnas == None: 
            print(f"Error en dimension: {dimension}")
            return None        
        
        """ >>> C e l d a   F I N  ... (a partir de celda_inicio y dimension) ...Esto define un rango. ahora hay que capturar las celdas implicadas y los valores de cada celda""" 
        celda_fin = self.__get_str_celda_fin(total_filas = self.total_filas , total_columnas = self.total_columnas)        
        if not celda_fin: 
            print("Error en la creacion de la Celda Fin")
            return None

        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ CREACION DE CELDA FIN DEL RANGO.
        self.celda_fin      = Celda(celda = celda_fin)
        
        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ LISTA DE LAS CELDAS IMPLICADAS
        self.lst_celdas = self.__get_list_celdas()                       
        """ >>> LISTA DE OBJETOS CELDA  """

        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ CREACION DE CELDA INICIO DEL RANGO A PARTIR DE LST_CELDAS (para no autoReferenciarme y crear una celda de inicio de la que soy heredera.)
        self.celda_inicio   = self.lst_celdas[0]      

        # A S I G N A C I O N   D E   P R O P I E D A D E S                
        self.nombre = nombre_rango                
        self.total_celdas   = self.total_filas * self.total_columnas        
        self.es_numerico = False
        self.flag = ''          
        self.family = ''  
        self.b_oculto = b_oculto    
        """ >>> Si no quieres que se vea en self.ver_rango con rango a None (ver Todos) 
            sirve para marcar el primer rango ('Tabero') como oculto... es todo el panel y son muchos valores que mostraar. así es mas agíl.
            con las filas pasa parecido.....en Monkey_Men
        """                                    
        self.b_ghost = b_ghost      
        """ >>> True, no se copia de tablero directamente al crear el rango (es virtual, para operar) 
                False, se crea y se copian los valores de tablero.         """
        pass       
        self.b_print_cabecera = True
        """ >>> True(byDef) Indica que se tienen que imprimir las cabeceras en __str__  y False que se imprimen por fuera.
        """        
        
        # V A L O R   I N I C I O ... puede ser una lista, una matriz, un str, int, bool...
        if valor_inicial:
            self.set_data_plana(data = valor_inicial, relleno = valor_inicial)
            
        self.matriz = self.__get_matriz()
        if not self.matriz: return None

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # Info del Rango
    def __str__(self):
        """Devuelve una representación legible del diccionario de datos.
        """
        # Validacion
        if self.b_print_cabecera == True:
            # Cabeceras de la tabla
            titulos = ["Rango", "Inicio", "Fin", "Total Celdas", "Filas", "Columnas", "Es Oculto", "Ghost"]
            tamanos_columnas = [25, 10, 10, 15, 8, 10, 10, 10]
            # Valores de los datos
            valores = [
                self.nombre ,
                self.get_nombre_celda() ,
                self.celda_fin.get_nombre_celda() ,
                self.total_celdas ,
                self.total_filas ,
                self.total_columnas ,
                self.b_oculto ,
                self.b_ghost                
            ]
            # Formateo de cabeceras y datos
            cabeceras = "".join([f"{titulo:<{ancho}}" for titulo, ancho in zip(titulos, tamanos_columnas)])
            datos = "".join([f"{str(valor):<{ancho}}" for valor, ancho in zip(valores, tamanos_columnas)])
            # Resultado final
            return f"{cabeceras}\n{'-' * sum(tamanos_columnas)}\n{datos}"
        else:
            return f"\nDatos del Rango( {self.nombre} ): [ {self.get_celda()} ]  To [ {self.celda_fin.get_celda()} ] Total Celdas: {self.data['total_celdas']} => {self.total_filas} Filas y {self.total_columnas} Columnas .......es Oculto?: {self.b_oculto} ..... Ghost?: {self.b_ghost}"  
    
    # DEVUELVE LA MATRIZ DE self.lst_celdas
    def __get_matriz(self):
        """ >>> Devuelve un rango en forma de lista de listas. """
        if not self.lst_celdas: return None
        lst_matriz = [] 
        for i in range(self.total_filas):
            lst_fila = []            
            for j in range(self.total_columnas):
                nombre_celda = SttS.celda_by_fc(fila = self.fila + i, columna = self.columna + j)
                celda = self.get_celda_by_nombre(nombre_celda=nombre_celda)
                if not celda: return None
                lst_fila.append(celda)
            pass
            lst_matriz.append(lst_fila)
        pass
        return lst_matriz if lst_matriz else None
    
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # DEVUELVE UNA LISTA DE LOS VALORES EN FORMATO MATRIZ O IMPRIME VALORES BASIC
    def get_values(self, b_print=True):
        """ >>>  """
        lst_matriz = []
        for fila in self.matriz:
            lst_fila   = []
            for celda in fila: 
                lst_fila.append(celda.valor)            
            lst_matriz.append(lst_fila)
        
        if b_print == False:
            return lst_matriz
        else:
            self.imprimir(sp_columna=3)            
            # for fila in lst_matriz:
            #     for i, valor in enumerate(fila):
            #         print(f'{valor}' , end= '\t| ') if i != len(fila) - 1 else print(f'{valor}', end='\n')
    
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def ver_matriz(self):
        """ >>> Muy basico, sirve para ver el nombre de las celdas en su posicion matricial. """
        if not self.matriz: return None
        for fila in self.matriz:
            for celda in fila:
                print(celda.nombre_celda, end=' '*4)
            print()
        pass

    # From nombre celda('C:3') To objeto_celda 
    def get_celda_by_nombre(self, nombre_celda:str):
        """ Entra el nobmre de una celda y comprueba que está en la lista de celdas del rengo.
        [nombre_celda](str): nombre de la celda a buscar. pej: 'C:3'
        Retorno: el objeto celda encontrado | None si no lo encuentra
        """
        if not self.lst_celdas: return None
        for celda in self.lst_celdas:
            if nombre_celda == celda.nombre_celda:
                return celda
        return None

    # ············································    
    # G E T T E R ' S   A N D   S E T T E R ' S    
    def get_oculto(self):                               # oculto,   para ver. no para buscar.
        if isinstance(self.b_oculto, bool):
            return self.b_oculto
        else:
            self.b_oculto = False
            return self.b_oculto
    def set_oculto(self, valor:bool=True):
        self.b_oculto = valor
    def get_ghost(self):                                # Ghost
        return self.b_ghost
    def set_ghost(self, valor:bool):
        self.b_ghost = valor
    def get_flag(self):                                 # Flag
        return self.flag
    def set_flag(self, valor:str):
        self.flag = valor
    def get_family(self):                               # Family
        return self.family
    def set_family(self, valor:str):
        self.family = valor

    # D e s e m p a q u e t a   D i m e n s i o n   y  devuelve fila y columna
    def __desempaqueta_dimension(self, dimension:str):
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
        total_columnas = None
        total_filas = None
        
        dimension = dimension.upper()                                               # Para poner la x minuscula.
        if ':' in dimension:
            bi_columna , bi_fila = SttS.desata_binomio(dimension, ':')
            """ dimension como CELDA_FINAL ( M:13 ) hay que transformar esto en una dimension
            """
            try:
                bi_fila:int = int(bi_fila)                                                  
                # Saca el numero de columna de la dimension, que es con lo que se va a calcular la dimension.
                columna:int = SttS.letra_to_numcol(letra = bi_columna)
                if columna == None: 
                    return None, None
                """ 
                Aplica la Formula  """    
                total_filas = int(bi_fila) - self.get_fila() + 1
                total_columnas = int(columna) - self.get_columna() + 1

                # Valida que la columna fin sea mayor que la columna inicio. y que la fila fin sea mayor que la fila inicio.
                if total_filas < 0 or total_columnas < 0:
                    return None, None
            except Exception:
                return None, None        
        else:
            if 'X' in dimension:
                try:
                    """ d i m e n s i o n   c o m o   d i me n s i o n ( 3x4 )"""
                    total_filas , total_columnas = SttS.desata_binomio(dimension, 'X')
                    if total_filas == None or total_columnas == None:
                        return None, None
                    total_filas     = int(total_filas)                                     # si no es bueno, casca
                    total_columnas  = int(total_columnas)                                  # si no es bueno, casca
                except Exception as e:
                    print(f'Error init Rango: {e}')
                    return None, None
            else:
                return None, None
        
        return total_filas, total_columnas

    def __get_str_celda_fin(self, total_filas:int, total_columnas:int):
        """ >>> Obtiene la cadena de la celda fin (pej. 'D:3' ), no el objeto Celdt 
        """
        try:            
            fila_fin    = self.fila     + total_filas    - 1         
            columna_fin = self.columna  + total_columnas - 1 

            letra_columna_fin = SttS._may_nl[columna_fin]
            celda_fin = f'{letra_columna_fin}:{fila_fin}'
        except Exception as e:
            print(f'Error __init__ Rango :::: {e}')
            return None

        return celda_fin
    
    def __get_list_celdas(self):
        """ >>> Genera una lista de celdas iterando a través del número total de filas y columnas.
        Retorno:
            list: Una lista de celdas obtenidas llamando al método `sumar_fc` con los índices actuales de fila y columna.
                  Si ocurre una excepción, imprime un mensaje de error y retorna None.
        >>> lst_celdas=[]
        >>> for i in range(self.total_filas)):            
        >>>     for j in range(self.total_columnas):
        >>>         sig_celda = self.sumar_fc(filas = i, columnas = j,  b_copy_value=True)            
        >>>         lst_celdas.append(sig_celda)
        """
        try:
            return [
                self.sumar_fc(filas=i, columnas=j, b_copy_value=True)
                for i in range(self.total_filas )
                for j in range(self.total_columnas )                  
            ]

        except Exception as e:
            print(f'Error en __get_list_celdas :::: {e}')
            return None

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def set_data_plana(self, data, relleno:str = Celda.VALOR_INICIAL):
        """ >>> establece un dato en el rango .
        Aplana la lista dada, ajusta su longitud para que coincida con la lista interna `self.lst_celdas` rellenando con un valor predeterminado,
        y establece los valores de las celdas en `self.lst_celdas` a los valores correspondientes en la lista ajustada o no dependiendo de b_relleno.
        [data] : el dato a procesar. Puede ser matriz, lista, int, bool, str, o cualquier objeto.
        Returns:
            None
        """
        try:
            # APLANO EL DATO: ...Si es matriz lo convierte en lista , si es lista lo deja como lista y si es str , int, bool, lo deja como está.
            lista_plana = SttS.aplanar_matriz(matriz = data)
            
            # EVALUO SI TENGO QUE RELLENAR EL RESTO DEL RANGO CON DATOS DE INICIO O LO DEJO COMO ESTÁ
            if relleno == '':
                lista_plana = SttS.igualar_listas(lista_keys=self.lst_celdas, lista_to_relong = lista_plana, valor_relleno=Celda.VALOR_INICIAL)        
                """ >>> lst len(self.lst_celdas) == len(lista_plana). lista_plana se rellena con Celda.VALOR_INICIAL ( '' ) 
                """
            else:
                lista_plana = SttS.igualar_listas(lista_keys = self.lst_celdas, lista_to_relong = lista_plana, valor_relleno = relleno)        
                """ >>> lst len(self.lst_celdas) == len(lista_plana). lista_plana se rellena con cualquier valor 
                """
            # En caso de que b_relleno = False, se emparejan hasta el mas corto :)
            # El Rango (las celdas del rango) cambien de valor
            for celda, valor in zip(self.lst_celdas, lista_plana):
                celda.set_valor(valor=valor)  
            return True    
        except Exception as e:
            print(f'Error ::: Rango ::: set_data_plana ::: {e}')
            return None

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def push(self, data_push, celda_inicio:str='A:0', b_lineal:bool=False):
        """ >>> FROM MATRIZ, ITERATOR U OTRO TO RANGO SELF. 
        ... o FROM RANGO TO RANGO. DIFERENCIA ENTRE MATRIZ Y EL RESTO. SI ES EL RESTO, CREO UN RANGO CON LOS DATOS SEGÚN VIENEN EN LA CELDA_INICIO. 
        LUEGO LOS CRUZO CELDA A CELDA CON EL RANGO CON CROSS
        SI ES MATRIZ, SI B_LINEAL = TRUE, TB LOS CARGO SEGÚN VIENEN COMO EN LA TÉCNICA ANTERIOR.
        SI B_LINEAL = FASE, ENCUADRO LA MATRIZ Y CREO EL RANGO. LUEGO LO CRUZO CON CROSS COMO TODAS LAS ANTERIORES.
        """
        rango = None        
        
        # PASAMOS A LA ACCION: VALIDACION DE TIPOS.
        es_matriz = SttS.es_lista_de_listas( matriz = data_push )
        
        # EVALUAMOS EL TIPO        
        if not es_matriz: 
            
            if isinstance(data_push, list) or isinstance(data_push, tuple) or isinstance(data_push, set):
                """ >>> Es un iterador. Creo que tiene que entrar plano si o si. """
                if b_lineal == False:
                    """ >>> (By Def) METE LA LISTA HORIZONTAL 
                    """
                    dimension = f'1x{len(data_push)}'
                else:
                    """ >>> METE LA LISTA VERTICAL 
                    """                    
                    dimension = f'{len(data_push)}X1'
                rango = Rango( nombre_rango = "aux_iter" , celda_inicio = celda_inicio , dimension = dimension , valor_inicial = data_push )                
                # 2- SE PASA EL RANGO AL RANGO CON SELF.SET_DATA_PLANA
                # return self.cross(rango)
            
            elif isinstance(data_push, str):                
                if b_lineal == False:
                    """ (By Def) METE LA CADENA ENTERA EN LA CELDA_INICIO 
                    """
                    rango = Rango( nombre_rango = "aux_str" , celda_inicio = celda_inicio , dimension = f'1X1' , valor_inicial = data_push )                
                    # return self.cross(rango)
                else:   
                    """ METE LA CADENA COMO SI FUERA UNA LISTA A PARTIR DE LA CELDA DE INICIO PALABRA A PALABRA. 
                    """
                    lst_palabras = ' '.join(data_push)
                    if not lst_palabras: return None
                    # AHORA ES TRATADA COMO LISTA HORIZONTAL
                    dimension = f'1x{len(lst_palabras)}'
                    rango = Rango( nombre_rango = "aux_iter" , celda_inicio = celda_inicio , dimension = dimension , valor_inicial = data_push )                
                    # return self.cross(rango)            
            else:
                if any(celda_inicio in celda.nombre_celda for celda in self.lst_celdas):
                    rango = Rango( nombre_rango = "aux_other" , celda_inicio = celda_inicio , dimension = '1x1' , valor_inicial = data_push )                                    
                    # return self.cross(rango)
        else:
            """ 
            >>> ES MATRIZ """
            # QUIERO METER LOS DATOS A CAPÓN UNO DETRAS DE OTRO SIN ESTRUCTURA.
            if b_lineal == True:    
                rango = Rango( nombre_rango = "aux_matriz_lineal" , celda_inicio = celda_inicio , dimension = dimension , valor_inicial = data_push )
            else:            
                """ QUIERO METER LOS DATOS  CON LA ESTRUCTURA DE MATRIZ CON LA QUE ESTÁ LA MATRIZ... A PARTIR DE LA CELDA DE INICIO. """
                # CREO UNA MATRIZ CUADRADA DEPENDIENDO DEL MAXIMO NUMERO DE COLUMNAS QUE TENGA LA MATRIZ ENTRANTE
                matriz_cuadrada = SttS.encuadrar_matriz(matriz = data_push)        
                # SACO LOS DATOS QUE NECESITO DE LA MATRIZ RE-CREADA PARA CREAR UN RANGO CUADRADO
                filas = len(matriz_cuadrada)
                columnas = len(matriz_cuadrada[0])
                dimension = f'{filas}X{columnas}'
                try:
                    # ▄▄▄▄▄ CREO EL RANGO CUADRADO
                    rango = Rango( nombre_rango = 'rango_aux' , celda_inicio = celda_inicio , dimension = dimension , valor_inicial = matriz_cuadrada )            
                    if not rango: return False
            
                    # VALIDO LIMITES DEL RANGO
                    retorno = self.es_rango_in(rango=rango)
                    if not retorno: 
                        print("Error Logico ::: Limites ")
                        return False
                except Exception as e:
                    print(f'Error ::: Tablero ::: push ::: {e}')
                    return False
            print()
            rango.ver_matriz()
            print()
            rango.get_values()
            print()
            self.ver_matriz()
            print()
            self.get_values()       
            print()
            print(f'\n\nLast Fila Used: {self.__last_fila_used()}')    

            # ▄▄▄▄▄▄▄▄ W.I.P ▄▄▄▄▄▄▄▄▄▄
            return self.cross(rango = rango)
        

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # CRUZO UN RANGO CON SELF. CELDA A CELDA COINCIDENTE
    def cross(self, rango):
        """ Cruza Celda a Celda un Rango con otro y asigna su valor ....pej C:1 de self con C:1 de rango 
        [rango](class Rango): entra un rango y cruzo Celda a Celda(Las que coincidan) en self.
        Retorno: None, si hay algún fallo.
        True en caso de que todo haya ido bien.
        """
        if not rango: return None
        if not isinstance(rango, Rango):
            return False
        
        if rango.celda_inicio in self.lst_celdas and rango.celda_fin in self.lst_celdas:
            print('Encontrado por Celdas')
        
        # ▄▄▄▄▄▄▄ VALIDACION DE TODO EL CONTENIDO.
        if not self.es_rango_in(rango = rango): return False
        
        # ▄▄▄▄▄▄▄ CRUZO CELDA A CELDA COMPARANDO SUS NOMBRES_CELDA.
        for celda in self.lst_celdas:
            for celda_rango in rango.lst_celdas:
                if celda.nombre_celda == celda_rango.nombre_celda:
                    celda.valor = celda_rango.valor
                    break
        return True
        
    # RANGO IN SELF?
    def es_rango_in(self, rango):
        """ VALIDA SI UN RANGO ESTÁ CONTENIDO EN EL RANGO SELF. 
        Compara el nombre de la celda de inicio y celda de fin en self.lst_celdas 

        [rango](Class Rango): representa un objeto Rango(esta misma Clase).
        Retorno: True, si el rango está contenido en el Rango self. 
        False, si el Rango no está contenido (está sobre-pasado).

        """
        # VALIDACION INICIAL
        if not self.lst_celdas or not self.matriz or not rango: 
            return False
        # COMPROBACION DE NOMBRES POR MEDIO DE ANY
        if not any (rango.celda_inicio.nombre_celda in celda.nombre_celda for celda in self.lst_celdas):
            return False

        if not any (rango.celda_fin.nombre_celda in celda.nombre_celda for celda in self.lst_celdas):
            return False
        
        return True

            

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def get_filas(self, fila_from:int, fila_to:int):
        """ >>> Obtiene las filas consecutivas de un rango en una lista. """
        if not self.matriz: return None
        # lst_retorno = []
        # for i, fila in enumerate(self.matriz):
        #     if fila_from <= i <= fila_to:
        #         lst_retorno.append(fila)
        # return lst_retorno if lst_retorno else None
        
        return [ fila  for i, fila in enumerate(self.matriz) if (fila_from <= i <= fila_to) ]

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def get_columnas(self, columna_from:int, columna_to:int):
        """ >>> Obtiene las columnas consecutivas de un rango en una lista. """
        if not self.matriz: return None
        # lst_ret = []
        # for fila in self.matriz:
        #     for j , celda in enumerate(fila):
        #         if columna_from <= j <= columna_to:
        #             lst_ret.append(celda)
        # pass
        # return lst_ret if lst_ret else None

        return [celda for fila in self.matriz 
                        for j , celda in enumerate(fila)
                        if columna_from <= j <= columna_to ]


    # ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    #  I m p r i m e   u n   R a n g o . 
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def imprimir(self, sp_columna:int = 0 , **kwargs ):    
        """ 
        Imprime el Rango con configuracion. Es la base de impresion sobre todo. 
        [sp_columna] (int): el espacio entre columnas
        [**kwargs] (dict):  "ancho"(int)  = ancho de columna fixed or 
                            "lista"(list) = lista de anchos para cada columna. 
        
        >>> ejemplo: imprimir( ) => ajusta al maximo de cada columna(mode tabla)
        >>> ejemplo: imprimir( sp_columna = 2 ) => maximo de cada columna (mode tabla)        
        >>> ejemplo: imprimir( ancho = 0 , sp_columna = 0 ) => L i t e r a l   P u r o ....XindeX
        >>> ejemplo: imprimir( ancho = 1 , sp_columna = 0 ) => L i t e r a l   con espacio entre columnaas
        >>> ejemplo: imprimir( ancho = 15 , sp_columna = 5 ) => columnas al 15 todas. no restrictivo. sp_columna = 5 . espacio entre columnas de 5 char
        >>> ejemplo: imprimir( lista = [0,1,5,4,3,2] , sp_columna = 5 ) => cada columna a su ajuste y 5 entre columnas
        >>> ejemplo: imprimir( ancho = 15 , lista = [0,1,5,4,3,2] , sp_columna = 3 ) => Prevalece la lista. y deja 3 entre columnas.
        """
        # C a c h o   LOS DATOS DE ENTRADA
        ancho_columna = kwargs.get('ancho', None)  # Si no existe, usa 0
        lista = kwargs.get('lista', None)  # Si no existe, usa 0

        # V a l i d a c i o n   y asignacion a numero natural (por si se introducen numeros negativos)
        try:
            if ancho_columna: 
                ancho_columna = abs(ancho_columna)
            if lista:
                if not isinstance(lista, list): 
                    if isinstance(lista, int) or isdigit(lista):    # Aunque tiene que meter una lista pone list pero mete un 3 o '3' pejem.
                        lista = abs(lista)
                    else:
                        return None
        except Exception as e:
            print(f'Error ::: imprimir ::: {e}')
            return None
        #  A N A L I S I S  DE LOS DATOS DE ENTRADA
        if ancho_columna == None and lista == None:     # No mete ningún dato sobre el ancho de la columna ni en numero ni en lista. 
            if sp_columna == 0:   
                """ >>> < M o d e   M a x L e n - C o l u m n a   P u r o >  
                """
                str_format = self.__formato_to_prango_maxcol( sp_columna = 0  )
            else:
                """ >>> < M o d e   M a x L e n - C o l u m n a >   ...con espacio entre columnas   
                """
                str_format = self.__formato_to_prango_maxcol(  sp_columna = sp_columna  )
        
        elif ancho_columna != None and lista == None:       # A n c h o   d e   C o l u m n a   F i x e d .
            ancho_columna = abs(ancho_columna)
            sp_columna = abs(sp_columna)

            if ancho_columna == 0 and sp_columna == 0:                   
                """ >>> < M o d o   L i t e r a l >                        | sin tamaño de columna | escribes literalmente 
                """
                str_format = self.__formato_to_prango_fixed(  len_columnas = 0, sp_columna = 0)
                pass

            elif ancho_columna == 0 and sp_columna > 0:                   
                """ >>> < M o d o   L i t e r a l >                        | con  Espacios Entre Columnas 
                """
                str_format = self.__formato_to_prango_fixed(  len_columnas = 0, sp_columna = sp_columna)
                lst_max_len = self.__get_lst_max_filas()
            
            elif ancho_columna > 0 and sp_columna == 0:                   
                """ >>> < M o d o  F i x e d   P u r o > 
                """
                str_format = self.__formato_to_prango_fixed( len_columnas = ancho_columna, sp_columna = 0)

            elif ancho_columna > 0 and sp_columna > 0:                   
                """ >>> < M o d o   F i x e d >                          | con Espacios 
                """
                str_format = self.__formato_to_prango_fixed( len_columnas = ancho_columna, sp_columna = sp_columna)
                lst_max_len = self.__get_lst_max_filas()
            pass
        
        elif ancho_columna != None and lista != None:
            """ >>> < Modo  personalizado >  ... PERO RELLENA CON ANCHO_COLUMNA EN CASO DE QUE LA LISTA SEA MAS CORTA. 
            Y SP_COLUMNA
            """            
            try:
                # Valida que son enteros lo que hay en la lista y si no, peta aquí.
                lst_len = [int(item) for item in lista]

                # Igualo la lista aquí y así ya entra formateada bien
                fila_zero = self.get_filas(fila_from=0, fila_to=0)
                new_list_len_fila = [celda.valor for fila in fila_zero for celda in fila ]
                new_lista = SttS.igualar_listas(lista_keys = new_list_len_fila, lista_to_relong = lst_len, valor_relleno = ancho_columna)

                # Crea el formato preparado con los datos de la lista
                str_format = self.__formato_to_prango_list(lista = new_lista , sp_columna = sp_columna)
            except Exception as e:
                return None
            pass

        elif ancho_columna == None and lista != None:       
            """ >>> < Modo  personalizado >  Y o   E l i j o              
            """            
            try:
                # Valida que son enteros lo que hay en la lista y si no, peta aquí.
                lst_lens = [int(item) for item in lista]
                # Crea el formato preparado con los datos de la lista
                str_format = self.__formato_to_prango_list(lista=lst_lens , sp_columna = sp_columna)
            except Exception as e:
                print(f'Error ::: imprimir ::: formato columnas ::: {e}')
                return None
            pass
        
        else:
            return None
        
        """ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        >>> I m p r i m e   v a l o r e s  
        """                
        # Recorro las filas
        for i in range( len(self.matriz) ):
            
            lst_fila = self.__get_fila_rango_prango(fila_a_buscar = i )
            
            lst_values_fila = [celda.valor for celda in lst_fila]

            lst_format_to_print = self.__between_listas(lista=lst_values_fila)
            
            print(str_format.format(*lst_format_to_print))  # Cuando b_num_filas == False, no imprime los numeros de las Filas
    
    #  Devuelve los  v a l u e s   de   u n a   f i l a   d e   u n   r a n g o .
    def __get_fila_rango_prango(self,  fila_a_buscar:int):
        if SttS.b_fila_valida( fila = fila_a_buscar , from_incl=0, to_incl = self.total_filas ) == False: 
            return None
        for f, fila in enumerate(self.matriz):
            if  f == fila_a_buscar:
                return fila

    # FORMATO IMPR _____________________________
    def __formato_to_prango_maxcol(self,  sp_columna:int = 0 ):        
        """ >>> Pone cada columna a su maximo 
        strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}" 
        [sp_columna](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y la siguiente.
        """  
        totalLen    = 0
        strformato  = ''
        try:
            sp_columna = abs(sp_columna)
        except Exception as e:
            print(f'Error __formato_to_prango_maxcol ::: {e}')

        for i in range (self.total_columnas): 
            maximo = self.__get_len_max_columna( columna = i )
            # maximo += sp_columna
            strformato += "{:<" + str(maximo) + "}" + "{:<" + str(sp_columna) + '}'
            # strformato += "{:<" + str(maximo + sp_columna) + "}"  
        # print(strformato)
        return strformato
    
    # FORMATO IMPR _____________________________
    def __formato_to_prango_fixed(self,  len_columnas = 0, sp_columna=0):        
        """ >>> Imprime un Rango sin ajuste de ventanas.
        [len_columnas](int) : Longitud de la columna fijo... cuando b_ajustado = False
        [sp_columna](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y el siguiente.
        """  
        totalLen = 0
        strformato = ''
        """ >>> strformato +=  pejem: {:<"+str(15)+"}" {:<"+str(2)+"}"  """                

        for i in range (self.total_columnas):
            # strformato += "{:<" + str(len_columnas + sp_columna) + "}" 
            strformato += "{:<" + str(len_columnas) + "}" + "{:<" + str(sp_columna) + '}'
        return strformato
    
    # FORMATO IMPR _____________________________
    def __formato_to_prango_list(self, lista , sp_columna:int=0):        
        """ >>> Establece el formto de una fila. 
        introduce una columna de mas between  item a imprimir(sp_columna). 

        [lista](list) : Lista con las Longitudes de la columna fijo... cuando b_ajustado = False
        [sp_columna](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y el siguiente.
        """  
        strformato = ''
        """ >>> strformato += "{:<" + str(len(item)) + "}"  pejem: {:<"+str(15)+"}"  """                
        if not self.matriz: return None
        lista_fila = self.matriz[0]       # Una opción mas directa pero que me gusta menos.
        # print(lista_fila)


        # obtengo la fila zero... sólo la quiero por el tamaño.
        fila_zero = self.get_filas(fila_from=0, fila_to=0)
        
        # Creo la fila de valores... insisto, solo la quiero por el tamaño para luego llamar a igualar_listas
        new_lista_fila = [celda.valor for fila in fila_zero  for celda in fila ]
        
        # iguala las listas
        lista = SttS.igualar_listas(lista_keys = lista_fila, lista_to_relong = lista, valor_relleno=sp_columna)

        # crea el formato
        for item in lista:
            # strformato += "{:<" + str(len_columnas + sp_columna) + "}" 
            strformato += "{:<" + str(item) + "}" + "{:<" + str(sp_columna) + "}"
        return strformato

    # LONGITUD MAXIMA DEL CONTENIDO DE UNA COLUMNA DEL RANGO.
    def __get_len_max_columna(self, columna):
        lst_columna = self.get_columnas(columna_from = columna , columna_to= columna)
        longitudes = [len(str(celda.valor)) for celda in lst_columna]
        return max(longitudes) if longitudes else 0                

    # LONGITUD MAXIMA DE TODAS LAS FILAS    
    def __get_max_filas(self):
        """ >>> Devuelve el valor maximo de todas las filas """
        lst_fila    = []
        for fila in self.matriz:
            long_fila=0
            for celda in fila:
                long_fila += len(str(celda.valor))
            pass
            lst_fila.append(long_fila)    
                
        return max(lst_fila) if lst_fila else 0
    
    # LISTA CON LA LONGITUD MAXIMA DE CADA FILA
    def __get_lst_max_filas(self):
        """ Para imprimir marco horizontal """
        lst_retorno    = []
        for fila in self.matriz:
            longitud_total_fila=0
            for celda in fila:
                longitud_total_fila += len(celda.valor)

            lst_retorno.append(longitud_total_fila)    
                
        return lst_retorno if lst_retorno else None

    # ULTIMA FILA CON USO DE UN TABLERO
    def __last_fila_used(self):
        """ Devuelve la última fila usada de la matriz.
        """        
        for i, fila in enumerate(self.matriz):
            b_match = 0
            for celda in fila:
                if celda.valor == Celda.VALOR_INICIAL:
                    b_match += 1
            if b_match == self.total_columnas:
                return i-1
        return None

    # ENTRA [1, 2, 3, 4] SALE => [1, '', 2, '', 3, '', 4, '']
    def __between_listas(self , lista , char:str=Celda.VALOR_INICIAL):
        """ >>> Intercala el valor inicial entre los elementos de una lista duplicando su len  
        """
        return [elem for item in lista for elem in (item, char)]

# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
""" 
                        T A B L E R O  : ... somos cuadrados (Berto y BuenaFuente) 
"""
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████

import copy             # Para realizar copia profunda de self.tablero

class Tablero(Rango):
    """ >>> Crea un MARCO para Imprimir """
    # ______________________________________________________________________
    # C O N S T A N T E S   D E   C L A S E ....(Tablero.SP  ó Tablero.TAB)
    SP  = ' '
    TAB = f'{SP*4}'
    pass
    def __init__(self, total_columnas_tablero:int, total_filas_tablero:int = 10 , valor_inicial = Celda.VALOR_INICIAL):       
        """ >>> Crea un Tablero(Rango), que empieza en A:0 y tiene la dimension establecida por total_filas_tablero y total_columnas_tablero 
        Se puede poner un valor inicial '-' distinto del que tiene Celda.VALOR_INICIAL = ''.
        Se tienen que crear y almacenar los rangos característicos del tablero como son: rango_filas y rango_columnas.
        Hay que incluir las características oculto, ghost, numerico, 
        crear_rango() |  rango_to_tablero() | tablero_to_rango() | buscar_rango() | ver_rangos() 

        >>> pej: tablero = Tablero(total_filas_tablero = 30 y total_columnas_tablero = 20 , valor_inicial='')
        """
        self.valor_inicial = valor_inicial
        try:
            total_columnas_tablero  = abs(int(total_columnas_tablero))
            total_filas_tablero     = abs(int(total_filas_tablero))
        except Exception as e:
            print(f'{e}')
            return None
        
        # Creamos la  d i m e n s i o n  para llamar al padre(Rango).
        self.dimension = f'{total_filas_tablero}X{total_columnas_tablero}'
        """ 
        >>> Después de esto, self es un Rango. CRUD. Mantiene una lista de rangos creados sobre el Rango Tablero. 
        """
        super().__init__(nombre_rango = 'main_tablero' , 
                        celda_inicio = 'A:0' , 
                        dimension = self.dimension ,
                        valor_inicial = self.valor_inicial , 
                        b_oculto = False , 
                        b_ghost = False)
        
        # ╚ ╔ ╩ ╦ ╠ ╬╚ ╔ ╩ ╦ ╠ ╬╚ ╔ ╩ ╦ ╠ ╬╚ ╔ ╩ ╦ ╠ ╬╚ ╔ ╩ ╦ ╠ ╬╚ ╔ ╩ ╦ ╠ ╬╚ ╔ ╩ ╦ ╠ ╬╚ ╔ ╩ ╦ ╠ ╬╚ ╔ ╩ ╦ ╠ ╬
        # M O N T O   L A   E S T R U C T U R A   D E   C O L U M N A S ..... (sobre la que voy a trabajar)       
        SttS._inicializa_diccs_letra_numero()

        # ╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔╔
        # V A L I D A C I O N   D E   D A T O S   D E   E N T R A D A               
        if total_columnas_tablero >= len( SttS._may_ln ):                   
            total_columnas_tablero = len( SttS._may_ln.keys() )-1
        pass        


        # # Diccionario creado para montar el tablero
        # dicc_numcol_value = { c:self.valor_inicial for c in range(self.total_columnas)}
        # """ >>> dicc (key):numero_columna (value): '-'   X   numero_columnas (...de 0 a numero_columnas) """
        
        # # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # self.tablero = [copy.deepcopy(dicc_numcol_value) for f in range(self.total_filas)]
        # """ >>> Por cada fila hace una copia profunda del diccionario (numero_columna:valor), que almacena en tablero.
        # El resultado final es una lista de diccionarios numero_columna:valor  y se puede acceder a tablero por 
        # acceso_1: self.tablero[numero fila][numero de columna]              ==> acceso por indice
        # acceso_2: self.tablero[numero fila][SttS._may_nl[numero columna]]   ==> 
        # """
        # # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # if not self.tablero: return
        # """ >>> tablero: Es una lista de diccionarios que conforman una fila. 
        # self.tablero[2][3] => fila 2, columna 3 |  self.tablero[2][self.dicc_may_letr_num['C']] => fila 2, columna 3
        # self.tablero[1]['3']='dato_1'
        # """
        self.init_tablero(value=self.valor_inicial)
        pass

        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # L I S T A   D E   R A N G O S   D E   T A B L E R O        
        self.lst_rangos=[]   
        """ Cada Tablero pueda tener su coleccion de rangos """
    # _________________________________str__
    def __str__(self):
        for dicc_fila in self.tablero:
            print(*dicc_fila)
        pass
        
    def get_tablero(self, es_X2=False):
        if not self.tablero: return None
        return self.tablero if esX2==False else copy.deepcopy(self.tablero)
      
    # ?????????????????????????????
    # INICIALIZA LOS VALORES DEL TABLERO CON UN VALOR DE ENTRADA O '-'  - over tablero - 
    def init_tablero(self, value=Celda.VALOR_INICIAL):
        try:
            for i, fila in enumerate(self.matriz):
                for celda in fila:
                    celda.valor = value
            
            # self.lst_celdas
            # pass
        except Exception as e:
            print(f'Error init_tablero :::: {e}')
            return 
        
    # ?????????????????????????????
    # G E T / S E T   U N   V A L O R   E N   T A B L E R O  - over tablero - 
    def xy(self, fila, columna, valor='<<<out>>>'):
        """ >>> xy(3, 5, valor='hola') : pone el valor 'hola' en la posicion fila=3, columna=5
                xy(3, 5) : obtiene el valor de la posicion fila=3, columna=5
        """
        if not self.tablero: return None
        # Valida  FILA
        # if not isinstance(fila, int): return None
        try:
            fila=abs(int(fila))
            if not (0 <= fila < len(self.tablero)):  
                return None
        except Exception as e:
            return None
        
        # VALIDACION COLUMNA
        try:
            columna=int(columna)
            """ Se convierte a entero y si falla es que viene en formato letra y se trata en la excepcion. """
        except Exception as e:
            columna = SttS.letra_to_numcol(letra=columna)
            if columna == None: 
                return None
            # if  not (0 <= columna < self.total_columnas) :
            if  not (0 <= columna < len(self.tablero[0].keys())) :
                return None
            
        """ 
        RECORREMEOS EL TABLERO """
        for i, dicc_fila in enumerate(self.tablero):
            if i == fila:
                if valor == '<<<out>>>':       # para get. le pongo uno imposible? para que solo cuando no tenga valor sea get. y en caso contrario, que coja el '' y el None
                    return dicc_fila[columna]      # Devuelve un valor
                else:
                    if valor == None: 
                        valor = self.valor_inicial

                    dicc_fila[columna] = valor     # Pone un valor
                    return True
        pass

    # ddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    # E L I M I N A   U N   V A L O R   E N  TA B L E R O  - over tablero - 
    def del_xy(self, fila, columna):
        retorno = self.xy(fila=fila, columna=columna, valor=self.valor_inicial)
        print('Borrar :( ') if retorno == None else ('Borrar ;)')

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
                if self.b_existe_nombre_rango(nombre_a_buscar = rango.nombre) == True:  return None

                # L o s   f a n t a s m a s   no   se   cargan  de   tablero .... luego self.tablero_to_rango()
                if rango.b_ghost == False:
                    # self.tablero_to_rango(nombre_rango=rango.nombre)
                    for celda in rango.dicc.keys():
                        valor_celda_en_tablero = self.nombre_celda(celda=celda)
                        """ >>> cruzo cada celda con el tablero 
                        """
                        if valor_celda_en_tablero != False and valor_celda_en_tablero != None:
                            rango.dicc[celda] = valor_celda_en_tablero
                        else:
                            rango.dicc[celda] = self.valor_inicial
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

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    #                  -  O V E R   F I L A S   Y   C O L U M N A S    - 

    #  ESTABLECE UN VALOR EN UNA FILA  
    def set_valor_over_fila(self , fila_to_set=0, valor=''):        
        fila = self.get_lst_filas(filaFrom=fila_to_set, filaTo=fila_to_set)
        if not fila: return
        # if fila_to_set not in self.dicc_may_num_letra: return
        if fila_to_set not in SttS._may_nl: return

        
        try:
            generic_cols = SttS._may_ln if SttS._may_ln else None
            if not generic_cols: return 
            for i,columna in enumerate(generic_cols):
                self.xy(fila=fila_to_set, columna=columna, valor=valor)

        except Exception as e:
            print(f'Error::: set_valor_over_fila {e}')
            return False
    
    # ESTABLECE UN VALOR EN UNA COLUMNA ENTERA DE TABLERO 
    def set_valor_over_columna(self, columna, valor):
        numero_columna = SttS.letra_to_numcol(letra=columna)           
        if numero_columna == None:
            """ No es una letra. será un Numero? """
            try:
                numero_columna = int(columna)
            except Exception as e:
                print(f'Error set_valor_over_columna: {e}')
                return None
        # print(len(self.tablero[1]))     #Longitud de las columnas

        # _____________________________________________
        # Llama a la funcion que cambia el valor y devuelve True en una lista....o None si hay error.
        lst_columna=[ self.xy(fila=i, columna=numero_columna, valor=valor) for i in range(self.get_numero_filas_tablero())]

        return lst_columna if lst_columna else False

    # DEVUELVE 1 FILA (DICC DE TABLERO)  
    def __get_dicc_fila(self, fila):
        """ >>> Devuelve el dicc que se corresponde con una fila en la list self.tablero """
        for f , dicc_cols in enumerate(self.tablero):
            if f == fila:
                return dicc_cols
    
    # DEVUELVE UN RANGO DE FILAS CONSECUTIVAS 
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

    # FROM FILA(int) TO LIST_STR  
    def get_fila(self, filaBusca):
        """ >>> Obtiene una lista de str de values de self.tablero 
        """
        # if not self.valid_ROW(fila=filaBusca): return None
        if SttS.b_fila_valida(fila=filaBusca, from_incl=0, to_incl=len(self.tablero)) == False: 
            return None
        for f, dicc_cols in enumerate(self.tablero):
            if  f == filaBusca:
                return dicc_cols.values()      
    
    # FROM COLUMNA(int) TO LIST VALORES . 
    def get_columna(self, columna):     

        numero_columna = SttS.letra_to_numcol(letra=columna)
        if numero_columna == None:
            """ No es una letra. será un Numero? """
            try:
                numero_columna = int(columna)
            except Exception as e:
                print(f'Error get_columna:::: {e}')
                return None
        pass
        lst_columna=[ self.xy(fila=i, columna=numero_columna) for i in range(self.get_numero_filas_tablero()) ]
        """>>> Formo la lista de retorno con los valores de la columna """    
        # rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr            
        return lst_columna if lst_columna else None    
    
    # LEN MAX DE UNA COLUMNA 
    def get_len_max_columna(self, columna):
        lst_columna = self.get_columna(columna=columna)
        longitudes = [len(str(item)) for item in lst_columna]
        return max(longitudes) if longitudes else 0                
    
    # LONGITUD MAXIMA DE TODAS LAS FILAS   
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
    
    # LISTA CON EL LEN MAXIMO DE CADA FILA 
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
        if SttS.b_fila_valida(fila=numfila, from_incl=0, to_incl=len(self.tablero)) == False: 
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
        lst_columnas_tablero = [i for i in range(self.total_columnas)]
        print(str_format.format(*lst_columnas_tablero)) if b_columnas_head==True else None
        
        """ >>>  I m p r i m e   L e t r a s   de cabecera de columna....si tal """
        dicc_letras = {char:num_col for char,num_col in SttS._may_ln.items() if num_col in lst_columnas_tablero}
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
            for i in range (self.total_columnas):
                strformato += "{:<" + str(len_columnas) + "}"
        else:
            if pad_x >= 0:
                """ Ajustado y con PadX -> calcula el maximo de la columna y le añade un margen de pad_x """
                for i in range (self.total_columnas):
                    maximo = self.get_len_max_columna(columna=i)
                    maximo += pad_x
                    strformato += "{:<" + str(maximo) + "}"
            else:
                for i in range (self.total_columnas):
                    maximo = self.get_len_max_columna(columna=i)
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
            for columna, valor in dicc_fila.items():
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
            set_v = self.xy(fila=f, columna=c)
            return set_v if set_v != None else False
        else:
            set_v = self.xy(fila=f, columna=c, valor=valor)
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
            if SttS.b_fila_valida(fila=fila, from_incl=0, to_incl=len(self.tablero)-1) == False:
                return None, None                
            """ 
            Valida que la columna está dentro del Tablero. """
            if SttS.b_columna_valida(columna=columna, from_incl=0, to_incl=len(self.tablero[0])-1) == False: 
                return None, None
        
            return fila, columna
        except Exception as e:
            print(f'Error __celda_to_fil_col:\n{e}')
            return None, None
        
    # ENTRA UNA fila y columna (3 , 2) y devuelvo una celda (C:2)
    def celda_by_fil_col(self, fila, columna):
        if not self.tablero: return None
        """ 
        >>> Valida que la fila está dentro del Tablero. """
        if SttS.b_fila_valida(fila=fila, from_incl=0, to_incl=len(self.tablero)-1) == False: 
            return None
        """ 
        >>> Valida que la columna está dentro del Tablero. """
        if SttS.b_columna_valida(columna=columna, from_incl=0, to_incl=len(self.tablero[0])-1) == False: 
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
                    self.elimina_rango(nombre_rango=rango.nombre)
                else: 
                    rango.flag = 'RNG_ROW'

        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # C r e a   u n   R a n g o   p o r   C o l u m n a        
        for j in range(len(self.rango_tablero.matriz[0])):
            dimension_columna = f'{len(self.rango_tablero.matriz)}x1'
            nombre_rango_columna = self.__new_nombre_secuencial(cadena=self.BASE_RANGO_COLUMNA)
            celda_inicio = f'{SttS.celda_by_fc(fila=0, columna=j)}'
            if nombre_rango_columna:
                rango = self.crear_rango(nombre = nombre_rango_columna, celda_inicio=celda_inicio, dimension=dimension_columna , b_ghost=False )
                rango.flag = 'RNG_COL'
            

    # sssssssssssssssssssssssssssssssssssssssssssssssssss
    # C r e a   u n   n o m b r e   s e c u e n c i a l 
    def __new_nombre_secuencial(self, cadena:str, separador:str='_'):
        """ Crea un nuevo nombre en lst.rangos a partir de una cadena de head. """
        lst_nombres = [rango.nombre for rango in self.lst_rangos]
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
                if self.b_existe_nombre_rango(nombre_a_buscar = rango.nombre) == True:  return None

                # L o s   f a n t a s m a s   no   se   cargan  de   tablero .... luego self.tablero_to_rango()
                if rango.b_ghost == False:
                    # self.tablero_to_rango(nombre_rango=rango.nombre)
                    for celda in rango.dicc.keys():
                        valor_celda_en_tablero = self.nombre_celda(celda=celda)
                        """ >>> cruzo cada celda con el tablero 
                        """
                        if valor_celda_en_tablero != False and valor_celda_en_tablero != None:
                            rango.dicc[celda] = valor_celda_en_tablero
                        else:
                            rango.dicc[celda] = self.valor_inicial
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
        if rango.total_filas == 1 and rango.total_columnas == 1:
            typo = Type_Rng(CELDA)        
        elif rango.total_filas == 1:
            typo = Type_Rng(COL)
        elif rango.total_columnas == 1:
            typo = Type_Rng(FIL)
        if rango.total_filas == rango.total_columnas :
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

    # VALIDA SI UN RANGO ESTÁ CONTENIDO EN OTRO RANGO.
    def valida_limites_rango(self, rango):
        # VALIDA SI UN RANGO ESTÁ CONTENIDO EN EL RANGO SELF.
        if not self.lst_celdas or not self.matriz: 
            return False

        if any (rango.celda_fin.nombre_celda in celda.nombre_celda for celda in self.lst_celdas):
            pass
        if any (rango.celda_inicio.nombre_celda in celda.nombre_celda for celda in self.lst_celdas):
            pass
        
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
                if rango.nombre == nombre_a_buscar:
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
                if rango.nombre == nombre_rango:
                    if  b_valores == False:
                        rango.b_print__str__ = True                        
                        print(rango)                                    
                        print(self.imprimir_info_rangos(lista_rangos = [rango.nombre], flag = flag), end='\n') 
                    else:                        
                        self.imprimir_valores_rangos(lista_rangos = [rango.nombre], celdas_por_linea = 4)
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
        if any(rango.nombre == nombre_a_buscar for rango in self.lst_rangos):
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
                            print(f'el Rango {rango.nombre} tiene las mismas propiedades que {rango_a_buscar.data.['nombre']}')        
        """        
        total_filas = rango_a_buscar.total_filas
        total_columans = rango_a_buscar.total_columnas
        lst_retorno = []
        for rango in self.lst_rangos:
            if (rango.get_celda() == rango_a_buscar.get_celda() and
                    rango.total_filas == total_filas and
                    rango.total_columnas == total_columnas):
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
            lst_rangos_fila = [rango for rango in self.lst_rangos if self.BASE_RANGO_FILA in rango.nombre and rango.b_ghost == False]
            if not lst_rangos_fila:
                return None
            for rango in lst_rangos_fila:
                self.tablero_to_rango(nombre_rango = rango.nombre)            
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
        for i in range( rango.total_filas ):
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
        lst_nombre_rango = [rango.nombre for rango in self.lst_rangos  if self.BASE_RANGO_FILA in rango.nombre ]

        if not lst_nombre_rango: 
            return None
        for i , nombre_rango in enumerate(lst_nombre_rango):
            if desde <= i <= hasta:
                self.Prango(nombre_rango = nombre_rango  , column_adjust = column_adjust , pad_x = pad_x)
    
    def Prango_cols(self, desde:int, hasta:int, column_adjust = None , pad_x:int = 0):
        """ >>> imprime desde la column hasta la columna con las mismas características que Prango 
        """
        # Cogemos sólo los nombres de los rangos que tienen 'rango_columna_' en su nombre
        lst_nombre_rango = [rango.nombre for rango in self.lst_rangos  if self.BASE_RANCO_COLUMNA in rango.nombre ]
        if not lst_nombre_rango: 
            return None
        for i , nombre_rango in enumerate(lst_nombre_rango):
            if desde <= i <= hasta:
                self.Prango(nombre_rango = nombre_rango  , column_adjust = column_adjust , pad_x = pad_x)

    #  Devuelve los  v a l u e s   de   u n a   f i l a   d e   u n   r a n g o .
    def __get_fila_rango_prango(self, rango,  fila_a_buscar:int):
        if not rango: 
            return None
        if SttS.b_fila_valida( fila = fila_a_buscar , from_incl=0, to_incl = rango.total_filas ) == False: 
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
            for i in range (rango.total_columnas): 
                maximo = self.get_len_max_columna(columna=i)
                maximo += pad_x
                strformato += "{:<" + str(maximo) + "}"
        else:
            for i in range (rango.total_columnas):
                maximo = self.get_len_max_columna(columna=i)
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

        for i in range (rango.total_columnas):
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
        lista = SttS.igualar_listas(lista_keys = rango.matriz[0], lista_to_relong = lista, valor_relleno=0)

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
            retorno = self.rango_to_tablero( nombre_rango = rango_aux.nombre )
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
        lst_max_columna = [i for i in range(columnas)]

        # hago la matriz de entrada uniforme y relleno los vacios con el valor Inicial.
        for i  in range(len(matriz)):
            matriz[i] = SttS.igualar_listas(lista_keys = lst_max_columna, lista_to_relong = matriz[i], valor_relleno = self.get_valor_inicial())

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
        # self.xy(fila=4, columna='B', valor = self.ESPACIO*self.x_pad)
        self.xy(fila=4, columna='E', valor='En un lugar de la mancha jAJAJAJAJAJAJAJAJA')
        matriz = [
            [1, 2, 3],
            [4, 5],
            [7, 8, 9, 8]
        ]        
        retorno = self.matriz_to_tablero(matriz = matriz, celda_inicio = 'M:8')

        
        # HEAD.xy(fila=1, columna='C', valor = 'F r a s e   d e   E n t r a d a')
        # PIE.xy(fila=0, columna='C', valor = 'F r a s e   d e   S a l i d a')
        

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
            HEAD.xy(fila=i, columna= HEAD.ultima_columna(), valor=f'{self.ESPACIO * ( faltan + self.pad_x )}█')
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
            self.xy(fila=i, columna= self.ultima_columna(), valor=f'{self.ESPACIO * (faltan + self.pad_x)}█')
        self.tablero_to_rango()

        # paso del tablero al rango principal..... de esta forma puedo imprimir con Prango
        PIE.tablero_to_rango()
        # colocando el pie
        lst_length_pie = PIE.get_lst_max_filas( rango = PIE.buscar_rango(PIE.BASE_RANGO_TABLERO) )
        print(lst_length_pie)
        lst_num_faltan_pie = [ self.total_len - int(length) for length in lst_length_pie ]
        for i, faltan in enumerate(lst_num_faltan_pie):
            PIE.xy(fila=i, columna= PIE.ultima_columna(), valor=f'{self.ESPACIO * (faltan + self.pad_x)}█')
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
        self.lst_celdas_reservadas_marco = [f'{self.rango_tablero.get_letra()}:{i}' for i in range(self.num_filas)]        
        self.lst_celdas_reservadas_marco +=[f'{self.rango_tablero.celda_fin.get_letra()}:{i}' for i in range(self.num_filas)]
        return True    
    
    def es_reservada(self, celda)->bool:
        """ >>> Valida si la celda es una celda reservada para el marco. """
        return True if celda in self.lst_celdas_reservadas_marco else False
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================