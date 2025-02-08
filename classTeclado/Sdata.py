import re
from datetime import date 
from datetime import time 
from .validator import StringTo as STo


class Sdata():
    """ 
    Def => entra una list de str y devuelve esa list como keys de un diccionario y los values son 
    pedidos por Teclado. Se pueden pasar el [tipoDato, PERMITENULL] en una lista de lista o lista de tupla
    [Ejemplo de uso]:
    >>> from Sdata import Sdata as listToDict
    >>> oneDict=listToDict.byDef(
                                    key_dict=['Cuanto','Quieres','Entrar?'],
                                    tipo= [(int,True), (float,False), (str,False)],
                                    permite_nulo=True,
                                    esCapital=False)
    >>> print(oneDict)
        
        [Resultado] => {'Cuanto': 5, 'Quieres': 5.0, 'Entrar?': '5'}
    """
    
    TIPOS_VALIDOS = {
        int: lambda v: int(v) if STo.esInt(v) else None,
        float: lambda v: float(v) if STo.esFloat(v) else None,
        str: lambda v: v  ,
        bool: lambda v: v ,  # SOLO DEVUELVE VALOR, VALIDACION FUERA
        list: lambda v: v ,  # SOLO DEVUELVE VALOR, VALIDACION FUERA
        set: lambda v: v  ,  # SOLO DEVUELVE VALOR, VALIDACION FUERA
        tuple: lambda v: v ,  # SOLO DEVUELVE VALOR, VALIDACION FUERA
        date: lambda v: datetime.strptime(v, "%d/%m/%Y").date() if STo.esDate(v) else None,
        time: lambda v: datetime.strptime(v, "%H:%M").time() if re.match(r"^(2[0-3]|[01]?\d):([0-5]\d)$", v) else None,
        "DNI": lambda v: v if STo.partirDNI(v)[0] else None,
        "Email": lambda v: v if STo.esMail(v) else None,
        "IP": lambda v: v if STo.esIPValida(v) else None,
        "between": lambda v: v  # SOLO DEVUELVE VALOR, VALIDACION FUERA
    }

    TIPOS_VALIDACION_EXTERNA = [bool, list, set, tuple, 'between']


    VALORES_POR_DEFECTO = {
        int: 0,
        float: 0.0,
        str: "",
        bool: False,
        list: [],
        set: set(),
        tuple: (),
        date: date(1900, 1, 1),
        time: time(0, 0),
        "DNI": "00000000X",
        "Email": "unknown@mail.com",
        "IP": "0.0.0.0",
        "between": None , 
        "object": None
    }


    def __init__(self):
        self.lst_tipos = []

    def __str__(self):
        pass
   
    @staticmethod
    def get_valor_bydef(tipo):
        """ Devuelve el valor por defecto de un tipo."""
        return Sdata.VALORES_POR_DEFECTO.get(tipo, None)

    @staticmethod
    def set_valor_bydef(tipo, valor):
        """ Modifica o agrega un nuevo tipo a los valores por defecto."""
        Sdata.VALORES_POR_DEFECTO[tipo] = valor

    @staticmethod
    def reset_valores_bydef():
        """ Restaura los valores por defecto a sus valores iniciales."""
        Sdata.VALORES_POR_DEFECTO = {
            int: 0,
            float: 0.0,
            str: "",
            bool: False,
            list: [],
            set: set(),
            tuple: (),
            date: date(1900, 1, 1),
            time: time(0, 0),
            "DNI": "00000000X",
            "Email": "unknown@mail.com",
            "IP": "0.0.0.0",
            "between": None
        }

    
    # *******************************************
    # OBLIGA A INTRODUCIR EL DATO CORRECTO.
    # CON ( permite_nulo = True ) SI INTRODUCE ''(INTRO) SE BUSCA EL VALOR POR DEFECTO.
    # Funcion Que hace Tipado del diccionario JUSTO DESPUÉS DE INTRODUCIR LOS DATOS.

    # *******************************************
    @staticmethod
    def get_data(key_dict:str, dicc:dict = None, tipo = str, msg_entrada:str='Intro... ', permite_nulo:bool=False  ):
        """          
        Convierte una lista de entrada en un diccionario (key): valor lista ; (values): introTeclado.
        Te hace tipado si se introduce una lista de tipo(tipo),permiteNull(boolean) despues de introducir
        el dato, por lo que te obliga a meter el dato correcto.

        """        
        
        # CUALQUIER FRASE CON CUALQUIER CARACTER
        # patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]+$'
        # pass
        if not tipo in Sdata.TIPOS_VALIDOS: 
            tipo = str                   # Tipo por defecto.
        
        # Diccionario de parametros         
        options = { 'msg_entrada':msg_entrada , 'permite_nulo': permite_nulo  } 
        
        # Diccionario creado con la llamada a una funcion en base a un patron(cualquier cosa introducida) 
        # para ejecutar una funcion que pregunta el dato al usuario y 
        dictRetorno = {
            key_dict:Sdata.__introByTcld(key_dict = key_dict, tipo = tipo , options = options )
        }
        pass
        # ______________
        # Retorno:
        if dictRetorno:
            if dicc:
                dicc[key_dict] = Sdata.__tiparDiccionario( diccionario = dictRetorno, tipo = tipo )
                return dicc
            else:
                return Sdata.__tiparDiccionario( diccionario = dictRetorno, tipo = tipo )
        else:
            return None


    # ********************
    # From lista1 de str To Dict(k)valorLista1 (v)Intro Teclado. Permite elegir Nulo/noNulo y crecer
    # ********************
    @staticmethod
    def __introByTcld(key_dict, tipo, options=None):
        """ Llamada desde get_data(): 
        [tipo](list) pasa siempre tipo =>[(int, False), (int, False)] lista de tuplas tipo, b_Permite_Nulo
        [options](dict)= { 'msg_entrada':msg_entrada , 'permite_nulo': permite_nulo , 'capital':esCapital } las opciones que se pasan 
        Return: 
        ejemplo:        
        
        """
        ENTRADA_NULL = ''
        # EL DICT OPTIONS SE TIENE QUE DEFINIR ASÍ: Si tiene datos, se asignan , si no tiene datos se asigna diccionario vacio {}
        options = options or {}
        
        # RECOGE LOS DATOS DEL DICCIONARIO DE ENTRADA OPTIONS
        permite_nulo = options.get('permite_nulo', False)  
        msg_entrada  = options.get('msg_entrada', False)  
        
        # KEY DEL DICCIONARIO A CREAR ... INFO DEL MENSAJE INPUT
        
        pass
        
        # .... INFORMACION DEL TIPO EN STR
        if tipo.__name__: 
            str_tipo = tipo.__name__.upper()
        elif isinstance(tipo, str):
            str_tipo = tipo
        elif isinstance(tipo, date): 
            str_tipo = 'DATE'
        elif isinstance(tipo, time):
            str_tipo = 'TIME'

        # .... INFO PERMITE NULL EN STR
        if permite_nulo == True:
            msg_nulo = 'NULL'
        else:
            msg_nulo = 'NOT NULL'
        pass
        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # PIDO DATOS POR TECLADO
        while True:
            entrada = input(f'\nK{key_dict} - {msg_entrada}  - ( {str_tipo} - {msg_nulo} )..... ')
            entrada = entrada.strip()
            try:
                if entrada == ENTRADA_NULL and permite_nulo == True:
                    """ RETORNA ESTE VALOR PARA QUE SE TRATE EL VALOR POR DEFECTO """
                    break
                elif entrada == ENTRADA_NULL and not permite_nulo:
                    """ REPITE, NO ADMITE NULO """
                    continue
                elif entrada != ENTRADA_NULL:                
                    """ >>> ENTRA DATO ... Se hace CASTING al tipo recogido """
                    try:
                        if tipo is bool:
                            entrada=Sdata.__tratarBoolano(entrada)
                            if entrada == None:
                                continue
                        elif tipo is list:
                            entrada = Sdata.__tratarListas(entrada)
                            if not entrada: 
                                continue
                            else:
                                entrada = tipo(entrada)                            
                        else:
                            entrada = Sdata.TIPOS_VALIDOS[tipo](entrada) 
                        # entrada=str(entrada)
                    except:
                        continue
                    else:
                        break
            except Exception as e:
                print(f'ERROR: {e}')
                return None
        return entrada

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def __tiparDiccionario(diccionario, tipo):
        """ 
        Quiero Tipar el diccionario creado en byDef/get_data proveniente de una lista de string
        donde todos los valores del diccionario son string.
        La idea que tengo es pasar una lista de listas [ [int, True] , [float, False] , [str, False] ]
                           
        >>> key_1:[intro_1, tipo_1  , True/False]
            key_2:[intro_2, listatipo_2  , True/False]
            key_n:[intro_n, listatipo_n  , True/False]

            Si el tipado da error, tengo que corregir a string
        """

        # _________________
        # IGUALA LA LONGITUD DE LAS LISTAS (cambia la longitud de tipo)
        lst_key = diccionario.keys()
        # tipo = Sdata.__igualarListas(lst_key=lst_key, tipo=tipo)
        # _________________
        # Ahora se recorre la lista de valores y se re-tipan: 
        lst_valores = diccionario.values()
        lst_valores_tipados = []
        TIPO = 0
        PERMITENULL = 1     

        for i, valor in enumerate(lst_valores):            
            # if PERMITENULL==False:            
            # ________________
            if tipo==int:
                try:
                    lst_valores_tipados.append(int(valor))
                except Exception:
                    return Sdata.__get_valor_bydef(lista=lst_valores_tipados, tipo=tipo)
            # ________________
            elif tipo==float:
                try:
                    lst_valores_tipados.append(float(valor))                        
                except Exception:
                    return Sdata.__get_valor_bydef(lista=lst_valores_tipados, tipo=tipo)
            # ________________
            elif tipo==str:                    
                lst_valores_tipados.append(str(valor))
            # ________________
            elif tipo==bool:
                try:
                    booleano=Sdata.__tratarBoolano(valor)
                    lst_valores_tipados.append(booleano)
                except Exception:
                    return Sdata.__get_valor_bydef(lista=lst_valores_tipados, tipo=tipo)
            # ________________
            else:                    
                try:
                    lst_valores_tipados.append(str(valor))
                except Exception:
                    lst_valores_tipados.append(valor)
        pass
        diccionarioRetorno = dict(zip(lst_key, lst_valores_tipados))

        pass
        return diccionarioRetorno

    @staticmethod
    def __validar_tipo(valor, tipo, opciones=None):
        """ Valida y convierte el valor al tipo correcto """
        if tipo == date:
            return datetime.strptime(valor, "%d/%m/%Y").date() if STo.esDate(valor) else None
        elif tipo == time:
            return datetime.strptime(valor, "%H:%M").time() if re.match(r"^(2[0-3]|[01]?\d):([0-5]\d)$", valor) else None
        elif tipo == STo.partirDNI:
            return valor if STo.partirDNI(valor)[0] else None
        elif tipo == STo.esMail:
            return valor if STo.esMail(valor) else None
        elif tipo == STo.esIPValida:
            return valor if STo.esIPValida(valor) else None
        elif isinstance(tipo, tuple) or isinstance(tipo, list) and tipo == "between":
            return valor if valor in tipo[1] else (tipo[1][0] if opciones and None in opciones else None)
        else:
            return 
        return valor

    def __get_valor_bydef( tipo ):
        """ 
        >>> DEVUELVE EL VALOR POR DEFECTO DEL TIPO PASADO
        """
        FECHA_POR_DEFECTO = date(year=1900, month=1, day=1)  # Una fecha convencional como valor predeterminado
        HORA_POR_DEFECTO = time(hour=0, minute=0,second= 0)  # Una fecha convencional como valor predeterminado

        if tipo is int:
            return 0                 # Valor por defecto
        elif tipo is float:
            return 0.0               # Valor por defecto
        elif tipo is str:
            return ''                # Valor por defecto de str
        elif tipo is bool:
            return  False             # Valor por defecto de bool(es engañoso)
        elif tipo is date:
            return FECHA_POR_DEFECTO # Valor por defecto de bool(es engañoso)
        elif tipo is time:
            return HORA_POR_DEFECTO  # Valor por defecto de bool(es engañoso)
        elif tipo == 'mail':
            return ''                # Valor por defecto de bool(es engañoso)
        elif tipo == 'dni':
            return ''                # Valor por defecto de bool(es engañoso)            
        elif tipo == 'ipv4':
            return ''                # Valor por defecto de bool(es engañoso)
        elif tipo == 'ipv6':
            return ''                # Valor por defecto de bool(es engañoso)
        elif tipo == 'route':
            return ''                # Valor por defecto de bool(es engañoso)
        
        else:
            lista.append(None)  # Valor por defecto
        pass


    def __tratarBoolano(entrada_bool:str):
        """ 
        >>> ADMITE TODAS ESTAS FORMAS DE BOOLEANO
        """
        entrada_bool=str(entrada_bool).strip().lower()
        if (entrada_bool=='v' or 
            entrada_bool=='verdad' or 
            entrada_bool=='verdadero' or 
            entrada_bool=='t' or 
            entrada_bool=='true' or 
            entrada_bool=='y' or 
            entrada_bool=='yes' or 
            entrada_bool=='si' or 
            entrada_bool=='s' 
            ):
            return True
        elif (entrada_bool=='f' or 
            entrada_bool=='false' or 
            entrada_bool=='no' or 
            entrada_bool=='n' or 
            entrada_bool=='falso' 
            ):
            return False
        else:
            return None
    
    def __tratarListas(str_to_lista:str):
        """ 
        >>> CONVIERTE UN STRING SEPARADO POR , EN UNA LISTA Y LA RETORNA.
        """
        str_to_lista = str_to_lista.strip()
        lst_retorno = str_to_lista.split(sep=',')
        if not lst_retorno: return 
        lst_retorno = [str(item).strip() for item in lst_retorno if str(item) != '']
        return lst_retorno