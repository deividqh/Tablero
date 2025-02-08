import re

class TiposValidReg():
    """ 
    Enumerador y padre de ValidReg......  lo primero fue la variable
    """
    VRG_ENTERO=0
    VRG_FLOTANTE=1
    VRG_FRASE=2
    VRG_CHAR=3
    VRG_IP=4
    VRG_MAIL=5
    VRG_TLF=6

class ValidReg(TiposValidReg):
    """ 
    Clase Estática que usa expresiones regulares para validar patrones:
    Tb es convertidor de tipo int, float, str, date(aun no).
    Tb tiene funciones utiles con listas y diccionarios.

    partirDNI()       => r"^(\d{8})[-.\s]?([a-zA-Z])$"
    esMail()          => r'^(\w+)@(\w+)$'
    esIPValida()      => r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
    partirIP()        => r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
    estaEnLista()     => Valida si un elemento está en una lista pasada como argumento.
    esInt()           => r'^-?\d+$'
    esFrase()         => r'^[da-zA-Z]+$'
    esFloat()         => r"^[+-]?(\d*\.\d+|\d+\.\d*|\d+)$"
    copyDict() copyList() => lo dejo pq ya está hecho, pero se sustituye por: 
        dicc2=dicc1.copy() 
        dicc2=dict(dicc1)
    copyList() => lo dejo pq ya está hecho, pero se sustituye por: 
        list2=list(list1)
    """
    def __init__(self):
        """ 
        Constructor: 
        """
        pass
    def __str__(self):
        pass

    @staticmethod
    def esType(self, valor, tipo=TiposValidReg.VRG_ENTERO):
        """ 
        Valida el tipo de datos entre los tipos validables
        Puedo ocultarlas todas y llamar sólo a esta funcion....pero no quiero.
        """
        if tipo == ValidReg.VRG_ENTERO:
            return self.esInt(valor)
        elif tipo == ValidReg.VRG_FLOTANTE:
            return self.esFloat
        elif tipo == ValidReg.VRG_FRASE:
            return self.esFrase
            
    @staticmethod
    def partirDNI(dni):
        """
        Def: Valida un dni con expresiones regulares (8numeros['.','-',' ']letra) 
        Retorno: El numero de dni , la letra del dni
        None si no es formato valido.
        """
        pattern = r"^(\d{8})[-.\s]?([a-zA-Z])$"
        
        match = re.match(pattern, dni)
        if match:
            number = match.group(1)
            letter = match.group(2)
            return number, letter
        else:
            return None, None

    @staticmethod
    def partirIP(ip):
        """ 
        Def: Entra una ip y la descompongo en los 4 grupos que tiene.
        Args: [ip]: Una ip
        Return: return grupo_1, grupo_2, grupo_3, grupo_4 
        """
        try:
            regIp = r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
            if infoSocket.esIPValida():
                match = re.match(regIp, ip)
                if match:
                    grupo_1 = match.group(1)
                    grupo_2 = match.group(2)
                    grupo_3 = match.group(3)
                    grupo_4 = match.group(4)            
                    return grupo_1,grupo_2, grupo_3, grupo_4
                else:
                    return None
        except Exception as e:
            return None

    @staticmethod
    def esIPValida(ip='127.0.0.1'):
        """  
        Def: Comprueba que la ip es desde 0.0.0.0 hasta 255.255.255.255
        Retorno: True si ip buena
        False si ip mala.
        """
        try:
            regIp = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
            if re.search(regIp, ip):
                return True
            else:
                return False
        except Exception as e:
            return None
    @staticmethod
    def esMail(cad):
        """  
        Valida mail. Puede haber otras expresiones regulares mas adecuadas pero esta vale.
        cadena de caracteres @ cadena de caracteres
        """
        try:
            cad=cad.strip()
            patron = r'^(\w+)@(\w+)$'    
            palabra=re.match(patron, cad)
        
            return palabra.group(1), palabra.group(2)
        except Exception as e:
            return None

    @staticmethod
    def esDate(cadena, formato_entrada="%d/%m/%Y", formato_salida="%d/%m/%Y"):
        """ Valida si una cadena se puede convertir a una fecha con cualquier formato dado y devuelve la fecha en el formato deseado.
        [cadena] (str): La cadena que contiene la fecha.
        [formato_entrada] (str): El formato en que se espera recibir la fecha (e.g., "%d%m%Y", "%Ymd").
        [formato_salida] (str): El formato en que se quiere retornar la fecha. Por defecto es "%d/%m/%Y".
        Returns:
            str | None: La fecha en el formato deseado si es válida, o None si no es válida. 
        """   
        from datetime import datetime
        try:
            fecha = datetime.strptime(cadena, formato_entrada)
            return fecha.strftime(formato_salida)
        except ValueError:
            return False

    @staticmethod
    def estaEnLista(valor, lista):
        """ 
        Valida un elemento entre unos dados en una lista. Tambien vale para los que no están en la lista.
        """
        if valor in lista:
            return True
        else:
            return False


    @staticmethod
    def esInt(strNum):
        """ 
        Def: Valida si el codeDigit pasado como argumento es un número entero.
                No incluye _ , . (decimal)
                si entra en el patron True / si no entra, False 
        """
        # .... Se lee: en toda la cadena [ From Ini(^); to Fin ($) ]
        #              Buscamos:  guion(-) opcional(?) y/o  0-9(\d)   ,  n veces(+)(solo el digito) 
        patronInt=r'^-?\d+$'
        num=re.match(patronInt, str(strNum))        
        if num:
            return int(strNum) 
        else:
            return False

        # return (int(num) if num else False)
    # _______________________________
    @staticmethod
    def esFrase(texto):        
        """     
        Def:    Valida la Entrada segun expresion la Regular: r'^[da-zA-Z]+$' 
                Si [texto] no se ajusta al patron => ha introducido un char no valido($ pej)

                ^          => Inicio de la cadena
                [da-zA-Z]  => [char] | d=>un digito | a-z => From a To z | A-Z => from A to Z
                + =>  cualquier numero de veces. Si no se pone sólo valdría para un sólo char
                $          => Fin de la cadena
        Args:   [texto] = str() no Validado.
        
        Return: (True/False)
                None, si texto==''
        """                
        if not isinstance(texto, str):  return False
        texto=texto.strip()
        if texto=='': return None
        # patron=r'^[\da-zA-Z_.\s]+$'
        patron=r'^[a-zA-Z0-9\s._-]+$'
        if re.search(patron, texto):
            return True
        else:
            return False
    
    @staticmethod
    def es_char(sting):
        """>>> Valida un solo caracter imprimible 
        [sting] (str): El caracter a validar.
        """
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]$'
        return True if re.search(patron, sting) else False

    @staticmethod
    def es_n_char(sting):
        """ >>> Valida si toda la cadena contiene solo caracteres alfanuméricos, caracteres especiales permitidos y espacios.
        [sting] (str): La cadena a validar.
        Retorno:
            bool: True si es válida, False en caso contrario.
        """
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]+$'
        return bool(re.fullmatch(patron, sting))

    @staticmethod
    def es_palabra(sting):
        """ 
        Letras may y min digitos _ 
        """
        patron= r'^\w$'
        return True if re.search(patron, sting) else False
    
    @staticmethod
    def esFloat(cadena):
        """ 
        Def: valida si se pasa un float
        ^[+-]?: Opcionalmente permite un signo + o - al inicio.
        \d*\.\d+: Opcionalmente dígitos antes del punto, pero al menos uno después del punto (ej. .5 o 0.123)
        \d+\.\d*: Al menos un dígito antes del punto y opcionalmente dígitos después (ej. 5.)
        \d+: Solo dígitos, por si deseas considerar números enteros como válidos (ej. 3)

        Ejemplo: 
            peso = ValidReg.esFloat(peso)
            if ValidReg.estaEnLista(sexo, ['H', 'M']): pass

                
        """
        patron = r"^[+-]?(\d*\.\d+|\d+\.\d*|\d+)$"
        num = re.match(patron, cadena)
        return float(cadena) if num else False
    
    # ____________________
    # Copia superficial de un diccionario. Usar list() de los diccionarios mejor. 
    # Me di cuenta tarde
    # ********************
    @staticmethod
    def copy_list(lista):
        """ 
        Def => Devuelve una copia de una lista por valor
        [lista] => lista a copiar
        Retorno => una nueva lista.
        Ejemplo => otraLista = ValidReg.copyList(lista_a_copiar)
        """
        if not isinstance(dicc, list): return None
        listCopy=[n for n in lista]
        return listCopy
    # ____________________
    # Copia superficial de un diccionario. Usar .copy() de los diccionarios mejor. 
    # Me di cuenta tarde
    # ********************
    @staticmethod
    def copy_dicc(dicc):
        """ 
        Def => Devuelve una copia por valor de un diccionario(superficial)
        dicc => diccionario a copiar
        Retorno => diccionario
        None si no es un diccionario
        Ejemplo => dict2=ValidReg.copyDict(dict_a_copiar)
        """
        if not isinstance(dicc, dict): return None
        diccCopy={k:v for k,v in dicc.items()}
        return diccCopy
    
    