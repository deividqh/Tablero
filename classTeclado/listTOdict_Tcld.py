import re
from datetime import date as fecha
from datetime import time as hora

class listTOdict_byTcld():
    """ 
    Def => entra una list de str y devuelve esa list como keys de un diccionario y los values son 
    pedidos por Teclado. Se pueden pasar el [tipoDato, PERMITENULL] en una lista de lista o lista de tupla
    [Ejemplo de uso]:
    >>> from listTOdict_Tcld import listTOdict_byTcld as listToDict
    >>> oneDict=listToDict.byDef(
                                    listaStrKeys=['Cuanto','Quieres','Entrar?'],
                                    listaDef= [(int,True), (float,False), (str,False)],
                                    permiteNulo=True,
                                    esCapital=False)
    >>> print(oneDict)
        
        [Resultado] => {'Cuanto': 5, 'Quieres': 5.0, 'Entrar?': '5'}
    """
    def __init__(self):
        """ 
        Constructor: 
        """
        pass
        self.estilo={'capital':False, 'may':False}

    def __str__(self):
        pass
    
    # ********************
    # From lista1 de str To Dict(k)valorLista1 (v)Intro Teclado. No Permite Nulo
    # ********************
    @staticmethod
    def __introToString(strValor):
        # permiteNulo=True
        valorLista = str(strValor.group()).capitalize()
        while True:
            retorno = input(f'intro {valorLista}..... ')
            # No Permite espacio vacio
            if retorno == '': 
                continue
            else:   
                break
        
        return retorno
    @staticmethod
    def toString(listaStrKeys=True):
        """ 
        Def => Devuelve un diccionario Segun una lista pasada como argumento pidiendo datos al usuario y almacenandolos en una lista. 
        No permite Introducir Vacio ( '' )
        listaStrKeys => [str] que son las keys del diccionario de retorno.
        Retorno => diccionario (k) los valores de listaStrKeys (v)Los valores str de los datos pedidos x Teclado. 
                None si algo va mal.
        
        Ejemplo => dict2 = listTOdict_byTcld.listTOdict_byTcld( ['nombre','dni' ,'tlf'] )

        Mejora: Introducir tratamiento de errores y 
                Introducir validacio de datos
        """
        if not isinstance(listaStrKeys, list): return None
        # patron = r'^[\w#$%/()\s]+$'
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]+$'

        dictRetorno={ strKey:re.sub(patron, listTOdict_byTcld.__introToString, strKey) 
                      for strKey in listaStrKeys }
        # print(dictRetorno)    
        return dictRetorno
    
    # ********************
    # From lista1 de str To Dict(k)valorLista1 (v)Intro Teclado. Permite elegir Nulo/noNulo y crecer
    # ********************
    @staticmethod
    def __introByDef(strValor, options=None):
        """ 
        Llamada desde byDef. 
        Se ejecuta para pedir datos al usuario y devolver el valor.
        Se pueden crear distintas opciones 
        [options] => diccionrio con pares clave:valor que se generan en la funcion byDef y aqui se obtienen y tratan

        Ejemplo => dict2 = listTOdict_byTcld.byDef( ['nombre','dni' ,'tlf'] , permiteNulo=True )        
        """
        # _____________________
        options = options or {}
        # _____________________
        permiteNulo = options.get('permiteNulo', False)  # Obtén 'permiteNulo' con un valor predeterminado de False
        esCapital = options.get('capital', False)  # Obtén 'permiteNulo' con un valor predeterminado de False
        msgIntro = options.get('msgIntro', False)  # Obtén 'permiteNulo' con un valor predeterminado de False

        # _____________________
        if esCapital:
            valorLista = str(strValor.group()).capitalize()
        else:
            valorLista = str(strValor.group())
        # _____________________
        while True:
            retorno = input(f'{msgIntro}-{valorLista} ..... ')
            if retorno == '' and not permiteNulo:
                continue
            elif retorno == '' and permiteNulo:
                break
            else:
                # Validación o transformación adicional aquí
                break
        
        return retorno
    # ***************************************************
    # Funcion Que hace Tipado del diccionario una vez introducidos todos los datos.
        # En caso de que no se ajusten a los datos de tipo mete los valores por defecto. 
        # Lo mas importate es que el analisis se hace Después de introducir los datos.
    # Sobre re.sub: 
        # re.sub (pattern, repl, string, count=0, flags=0)
        #  repl    => Cadena de texto o función con el valor que reemplazará las coincidencias del patrón en la cadena.
        #  string  => La cadena en la que se realizará la búsqueda y el reemplazo
        #  count (opcional) => Número máximo de reemplazos a realizar. Si se establece en 0, reemplazará todas las coincidencias
        #  flags (opcional) => Modificadores de la expresión regular, como re.IGNORECASE para hacer la búsqueda sin diferenciar entre mayúsculas y minúsculas.
            # >>> Ejemplo => 
            # dictRetorno = {
            # strKey : re.sub(patron, 
            #             lambda match: listTOdict_byTcld.__introByDef(match, options), 
            #             strKey) 
            #             for strKey in listaStrKeys
    # ***************************************************
    @staticmethod
    def byDef(listaStrKeys, listaDef=None, permiteNulo=True, msgIntro='Intro', esCapital=False):
        """         
        Devuelve un diccionario solicitando datos al usuario según las claves de 'listaStrKeys' pero con los datos tipados
        
        Es una version de toString() pero añadiendo los datos a pasar a la funcion con lambda.
        ademas se permitenn mas datos en el dicicionario de entrada options y luego se reciben en la funcion dedicada
        
        >>> [listaStrKeys]  => lista de str que son las claves del diccionario de retorno.        
        [listaDef] => lista de listas/tuplas: 
                      (classType)[tipo] , (bool)[permiteNulo] => [(int, True), (float, False),...]         
        [permiteNulo] => bool. =True Permite Nulo en Entrada por teclado.

        [msgIntro] =>  str. Formato del menú de entrada. Es el mensaje antes de los valores de la lista.
        
        [esCapital] => bool. Formato del menú de entrada. Si quieres que las claves de la lista sean mostradas en may
        
        -Esto crea un diccionario de (key)'nombre','dni' ,'tlf' (values) str
        >>>    from validator import listTOdict_byTcld as VReg
        >>>    otherDict = VReg.byDef(listaStrKeys=['nombre','dni','tlf?'], permiteNulo=True, esCapital=False)
        >>>    print(otherDict)
        """
        if not isinstance(listaStrKeys, list): 
            return None
        # ______________________
        # Patron valido: todos los caracteres,  n caracteres 
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]+$'
        # ______________________
        # Opciones a pasar a la funcion __introByDef().
        # Crear mas pares clave:valor para introducir mas parametros.
        options = { 'msgIntro':msgIntro,                # msgIntro strKey.... + introTeclado 
                    'permiteNulo': permiteNulo,         # =True Permite Nulo,
                    'capital':esCapital                 #letra capital para el valor de la key en el menú.
                    }
        # ______________________
        # Creo un diccionario con los argumentos opcionales que le quiero pasar a la 
        # funcion __introByDef para que procese los datos introducidos.
        dictRetorno = {
            strKey:re.sub(patron, lambda match: listTOdict_byTcld.__introByDef(match, options), strKey) for strKey in listaStrKeys
        }
        # _____________________
        # Esto hace que cuando se pasa una lista de Definicion [[int, True], [int, True], [int, True]] por Ejemplo
        # te devuelva el diccionario tipado.
        if dictRetorno:
            if listaDef:
                return listTOdict_byTcld.__tiparDiccionario(diccionario=dictRetorno,listaDef=listaDef)
            else:
                return dictRetorno                
        else:
            return None
    
    # Valida las listas de entrada 
    def validaListasEntrada(listaKeys, listaDef):
        """  
        >>> listaKeys = ["key_1", "key_2" , "key_3" ]
        >>> listaDef = [(int,True),(float, False),(str, False)]
        >>> if not validaListaEntrada(listaKeys, listaDef):...
        """
        # Validamos listaKeys
        try:
            if isinstance(listaKeys, list) :
                for unaKey in listaKeys:
                    if isinstance(unaKey, str):
                        pass
                    else:
                        return False
        except:
            return False
        pass
        # Ahora validamos listaDef
        try:
            if isinstance(listaDef, list) :
                for unPar in listaDef:
                    for unaKey, unValor in listaDef:
                        if not isinstance(unaKey, type):
                            return False
                        if not isinstance(unValor, bool):
                            return False
            return True
        except:
            return False
        pass
    

    def __tiparDiccionario(diccionario, listaDef):
        """ 
        Quiero Tipar el diccionario creado en byDef proveniente de una lista de string
        donde todos los valores del diccionario son string.
        La idea que tengo es pasar una lista de listas [ [int, True] , [float, False] , [str, False] ]
                           
        >>> key_1:[intro_1, tipo_1  , True/False]
            key_2:[intro_2, listatipo_2  , True/False]
            key_n:[intro_n, listatipo_n  , True/False]

            Si el tipado da error, tengo que corregir a string
        """

        # _________________
        # IGUALA LA LONGITUD DE LAS LISTAS 
        # En funcion de listaKeys. (cambia la longitud de listaDef)
        listaKeys=dict(diccionario).keys()
        listaDef=listTOdict_byTcld.__igualarListas(listaKeys=listaKeys, listaDef=listaDef)
        # _________________
        # Ahora se recorre la lista de valores y se re-tipan: 
        listaVals=dict(diccionario).values()
        listaValoresTipados=[]
        TIPO=0
        PERMITENULL=1       
        for i, valor in enumerate(listaVals):            
            # if PERMITENULL==False:            
            # ________________
            if listaDef[i][TIPO]==int:
                try:
                    listaValoresTipados.append(int(valor))
                except Exception:
                    # listTOdict_byTcld.__excepcionTipado(valor=valor, lista=listaValoresTipados, permiteNulo=listaDef[i][PERMITENULL], tipo=listaDef[i][TIPO])
                    listTOdict_byTcld.__setValoresByDef(lista=listaValoresTipados, tipo=listaDef[i][TIPO])
            # ________________
            elif listaDef[i][TIPO]==float:
                try:
                    listaValoresTipados.append(float(valor))                        
                except Exception:
                    # listTOdict_byTcld.__excepcionTipado(valor=valor, lista=listaValoresTipados, permiteNulo=listaDef[i][PERMITENULL], tipo=listaDef[i][TIPO])
                    listTOdict_byTcld.__setValoresByDef(lista=listaValoresTipados, tipo=listaDef[i][TIPO])
            # ________________
            elif listaDef[i][TIPO]==str:                    
                listaValoresTipados.append(str(valor))
            # ________________
            elif listaDef[i][TIPO]==bool:
                try:
                    booleano=listTOdict_byTcld.__tratarBoolano(valor)
                    # listaValoresTipados.append(bool(valor))
                    listaValoresTipados.append(booleano)
                except Exception:
                    # listTOdict_byTcld.__excepcionTipado(valor=valor, lista=listaValoresTipados, permiteNulo=listaDef[i][PERMITENULL], tipo=listaDef[i][TIPO])
                    listTOdict_byTcld.__setValoresByDef(lista=listaValoresTipados, tipo=listaDef[i][TIPO])
            # ________________
            else:                    
                try:
                    listaValoresTipados.append(str(valor))
                except Exception:
                    listaValoresTipados.append(valor)
        # print(listaValoresTipados)
        pass
        # Ahora tengo una lista con los valores ya tipados.
        # y Compongo el diccionario con la listaKeys y listaValoresTipados.

        # =======================
        # 2 Formas de hacer el diccionario: 1-listas Comprension 2-zip()
        # _______________________
        # diccionarioRetorno={
        #     keyDicc:valorTipado for i, keyDicc in enumerate(diccionario)
        #                         for j, valorTipado in enumerate(listaValoresTipados) 
        #                             if i==j
        # }
        # print(diccionarioRetorno)        
        # _______________________
        diccionarioRetorno = dict(zip(listaKeys, listaValoresTipados))
        # print(diccionarioRetorno)
        pass
        return diccionarioRetorno

    def __igualarListas(listaKeys, listaDef):
        """             
        Trata las longitudes de las listas y las igualo según listaKeys como referencia.
        La que se Re-dimensiona creciendo o decreciendo para igualarse con listaKeys.
        
        [Ejemplo de uso]:
        >>> listTOdict_byTcld.__igualarListas(listaKeys=listaKeys, listaDef=listaDef)
        
        listaKeys y listaDef son mutables, se pasan por referencia y no hay que retornar valor.
        """
        if len(listaKeys)==len(listaDef):
            # print("misma longitud")
            pass
        elif len(listaKeys)>len(listaDef):
            # print("long dicc > longTipo.....tipos hasta longTipo y luego Tipo=str y PERMITENULL=False")
            listaNewTipos=[[str,False] for i, (k) in enumerate(listaKeys) if i >= len(listaDef)]
            listaDef=listaDef+listaNewTipos
            # print(listaDef)
        else:
            # print("long dicc < longTipo.....vale hasta la long del dicc- hay que reducir la dimension del la listaDef")
            longListaTipos = len(listaDef)
            longListaKeys  = len(listaKeys)
            for i in range(longListaKeys , longListaTipos ):
                listaDef.pop()

        return listaDef
        pass

    def __excepcionTipado(permiteNulo, valor, tipo, lista):
        """ 
        Def => Pone los valores por defecto en la lista pasada, según el tipo que se pase.
        Es llamada cuando se produce una excepcion.
        """
        # _________________
        # Valida que tipo es una variable type
        if not isinstance(tipo, type): return

        # ==========================
        # SI permiteNulo , NO Valor => Hay que asignar un valor por defecto.
        if permiteNulo==True and valor == '':
            listTOdict_byTcld.__setValoresByDef(tipo=tipo, lista=lista)

        # ==========================
        # SI permiteNulo, SI Valor  
        elif permiteNulo==True and valor != '':
            try:
                lista.append(tipo(valor))
            except Exception:
                listTOdict_byTcld.__setValoresByDef(tipo=tipo, lista=lista)

        # ==========================
        # NO permiteNulo, NO Valor. Acepta Nulo ('')
        elif permiteNulo==False and valor == '':
            lista.append(str(valor))

        # ==========================
        # NO permiteNulo, SI Valor
        elif permiteNulo==False and valor != '':
            if isinstance(valor, tipo):
                lista.append(tipo(valor))
            else:
                listTOdict_byTcld.__setValoresByDef(tipo=tipo, lista=lista)           

    def __validarTipo(valor, tipo_dato):
        if isinstance(valor, tipo_dato):
            print(f"{valor} es de tipo {tipo_dato.__name__}")
            return True
        else:
            print(f"{valor} no es de tipo {tipo_dato.__name__}")
            return False

    def __setValoresByDef(tipo, lista):
        """ 
        Def: Asigna los valores por defecto de los tipos de datos.
        Sig-Ver: se pueden añadir mas tipos de datos(date, time,...)
        llamada desde __excepcionTipado()
        """
        FECHA_POR_DEFECTO = fecha(year=1900, month=1, day=1)  # Una fecha convencional como valor predeterminado
        HORA_POR_DEFECTO = hora(hour=1, minute=1,second= 1)  # Una fecha convencional como valor predeterminado

        if tipo is int:
            lista.append(0)     #Valor por defecto
        elif tipo is float:
            lista.append(0.0)   #Valor por defecto
        elif tipo is str:
            lista.append('')    #Valor por defecto de str
        elif tipo is bool:
            lista.append(False) #Valor por defecto de bool(es engañoso)
        elif tipo is fecha:
            lista.append(FECHA_POR_DEFECTO) #Valor por defecto de bool(es engañoso)
        elif tipo is hora:
            lista.append(HORA_POR_DEFECTO) #Valor por defecto de bool(es engañoso)
        else:
            lista.append(None)  #Valor por defecto
        pass
    
    # *******************************************
    # Igual que byDef() pero obliga (permiteNulo=True) a introducir el dato buenoo DESDE EL TECLADO
    # Funcion Que hace Tipado del diccionario JUSTO DESPUÉS DE INTRODUCIR LOS DATOS.
        # OBLIGA A INTRODUCIR EL DATO CORRECTO.
        # En caso de que no se ajusten a los datos de tipo mete los valores por defecto. 
        # Lo mas importate es que el analisis se hace en el momento de Introducir los datos.
    # *******************************************
    @staticmethod
    def byTcld(listaStrKeys, listaDef=None, msgIntro='Intro', permiteNulo=False, esCapital=False):
        """          
        Convierte una lista de entrada en un diccionario (key): valor lista ; (values): introTeclado.
        Te hace tipado si se introduce una lista de tipo(tipo),permiteNull(boolean) despues de introducir
        el dato, por lo que te obliga a meter el dato correcto.
        """
        # Validacion
        if not isinstance(listaStrKeys, list): 
            return None
        pass
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]+$'
        pass
        # Diccionario de parametros         
        options = { 'msgIntro':msgIntro ,                
                    'permiteNulo': permiteNulo ,     
                    'capital':esCapital }        
        pass        
        if listaDef:       
            # _________________
            # IGUALA LA LONGITUD DE LAS LISTAS 
            # En funcion de listaKeys. (cambia la longitud de listaDef) 
            if listTOdict_byTcld.validaListasEntrada(listaKeys=listaStrKeys, listaDef=listaDef)==False:
                return None
            listaDef=listTOdict_byTcld.__igualarListas(listaKeys=listaStrKeys, listaDef=listaDef)
            # _________________
            # CREA EL DICCIONARIO de retorno Generando un patron(cualquier frase) Para 
            # Ejecutar una funcion(__introByTcld)
            dictRetorno = {
                strKey:re.sub(
                    pattern=patron, 
                    repl=lambda match: listTOdict_byTcld.__introByTcld(match, listaDef[index] , options),
                    string=str(strKey)
                    )
                    for index, strKey in enumerate(listaStrKeys) }
        pass
        # ______________
        # Retorno:
        if dictRetorno:
            if listaDef:
                # lo tipa y lo retorna, pero los datos aunque vienen en str 
                # Vienen con los valores buenos
                return listTOdict_byTcld.__tiparDiccionario( diccionario = dictRetorno, listaDef = listaDef )
            else:
                # Si no hay definicion de tipos/Nulos se queda con diccionario de (k)str (v)str
                return dictRetorno
        else:
            return None

    # ********************
    # From lista1 de str To Dict(k)valorLista1 (v)Intro Teclado. Permite elegir Nulo/noNulo y crecer
    # ********************
    @staticmethod
    def __introByTcld(strValor, listaDefinicion, options=None):
        """ 
        Llamada desde byTcld()
        
        """
        # __________________
        # Validacion
        options = options or {}
        # __________________
        # Recogida de datos de entrada (se crean en la llamada)
        # permiteNulo = options.get('permiteNulo', False)  
        msgIntro  = options.get('msgIntro', False)  
        esCapital = options.get('capital', False)  
        # __________________
        TIPO=0
        PERMITENULL=1
        pass
        # print(listaDefinicion)
        # print(listaDefinicion[TIPO])
        # print(listaDefinicion[PERMITENULL])
        pass
        # __________________
        # Formato del texto para preguntar por Teclado
        if esCapital:
            valorLista = str(strValor.group()).capitalize()
        else:
            valorLista = str(strValor.group())
        pass
        # _______________________
        # Informe del tipo esperado y si permite nulo(N) o No Nulo(NN)
        tipo=listaDefinicion[TIPO].__name__
        permitenulo=listaDefinicion[PERMITENULL]
        if permitenulo==True:
            strnulo='N'
        else:
            strnulo='NN'
        pass
        # __________________
        # Pedimos datos por Teclado
        while True:
            retorno = input(f'{msgIntro} {valorLista} - ( {listaDefinicion[TIPO].__name__} - {strnulo} )..... ').strip()
            try:
                if retorno == '' and listaDefinicion[PERMITENULL]:
                    break
                elif retorno == '' and not listaDefinicion[PERMITENULL]:
                    continue
                else:
                    # Se hace CASTING al tipo recogido. y se Re-CASTING a str para que no casque en re.sub al volover
                    try:
                        if listaDefinicion[TIPO] is bool:
                            retorno=listTOdict_byTcld.__tratarBoolano(retorno)
                            if retorno == None:
                                continue
                        else:
                            retorno=listaDefinicion[TIPO](retorno)
                        retorno=str(retorno)
                    except:
                        continue
                    else:
                        break
            except Exception as e:
                print(f'ERROR: {e}')
                return None
        return retorno
    
    def __tratarBoolano(strValor):
        strValor=str(strValor).strip().lower()
        if (strValor=='v' or 
            strValor=='verdad' or 
            strValor=='verdadero' or 
            strValor=='t' or 
            strValor=='true' or 
            strValor=='y' or 
            strValor=='yes' or 
            strValor=='si' or 
            strValor=='s' 
            ):
            return True
        elif (strValor=='f' or 
            strValor=='false' or 
            strValor=='no' or 
            strValor=='n' or 
            strValor=='falso' 
            ):
            return False
        else:
            return None