# ==============================================================================
# C L A S S    P R I N T E X 
# ==============================================================================
# [rowformat] Admite una cadena con formato '{:<num1}{:<num2}{:<num3}{:<numN}' 
#                                           ' {:<30}  {:<15}  {:<25}'
# >>> signnifica: 
#     (':') Inicio de opciones de formato
#     ('<') alineado a la izquierda
#     (30) numero de espacios reservados para esa columna

# >>> print('{:<30}{:<15}{:<25}'.format("Nombre", "Edad", "Ocupación"))
# ==============================================================================
class PrinteX():
    """ 
    Quiero con esta clase dar formato a la impresion en terminal.
    Quiero formar tablas 
    Recibir una listaTitulos. Lista de str: lista=['str1','str2', 'str3'...]

    Recibir una lista de lista de str de columnas-titulo:
    listaValues=list = [ { 'key1':[0, 1, [0,1,0],2,1] }

    Imprimir en funcion de la cantidad de titulos y formatear una salida standar.
    """
    def __init__(self, listaTitulo, listaDatos, esAjustado=True, nombrePrinteX=''):        
        """ 
        Espera ("Tit1", "Tit2", "Tit3") ,  ( (2, 3, 4) , (5, 6, 7) ,.... ) )
        """
        if self.validaEntrada(listaTitulo, listaDatos)==False: 
            print("Error de Entrada")
            return None
        
        
        self.listaTitulo = listaTitulo
        self.listaDatos  = self.convierteToString(listaDatos)

        # # self.strformato=self.getFormato(listaTitulo=self.listaTitulo, listaDatos=self.listaDatos, esAjustado=esAjustado)
        # self.Impr(listaTitulo=self.listaTitulo, 
        #         listaDatos=self.listaDatos, 
        #         esAjustado=esAjustado, nombrePrinteX=nombrePrinteX)

    # ___________________________________        
    def getFormato(self, listaTitulo=None, listaDatos=None, esAjustado=False):
        """ 
        Establece el formato según la listaTitulo pasada, que es una lista de str tipo:
        >>> listaTitulosPrint=["Item", "Level", "Contador", "Posicion", "FilaR", "ColumR"]        
        -Puede ser un formato ajustado = True al tamaño maximo de CADA COUMNA o ajustado = False, se ajuta al tamaño del maximo str de la lista
        
        -Se Basa en saber cuantas columnas quieres(listaTitulos) y formatear cada linea al formato generado dinamicamente.
        >>> strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}"  
        """
        if listaTitulo==None: 
            listaTitulo = self.listaTitulo if self.listaTitulo else None
        
        if listaDatos == None: 
            listaDatos = self.listaDatos if self.listaDatos else None
        
        if  not listaDatos: return None

        totalLen=0
        strformato=''
        if esAjustado == True:
            listaMaxCol = self.maximoXColumna(listaTitulo=listaTitulo, listaDatos=listaDatos)
            """ lista con el numero maximo de caracteres por columna. 
            Devuelve tantos numeros como columnas tiene tanto listaTitulo como listaDatos
            Con estos datos Genera el Formato ajustado a la columna. """
            listaMaxCol = [item + 2 for item in listaMaxCol]
            for i in range (len(listaTitulo)):
                strformato += "{:<" + str(listaMaxCol[i]) + "}"
            
            # totalLen = sum(listaMaxCol) + len(listaMaxCol)
            totalLen = sum(listaMaxCol)
            # totalLen+=2
        else:
            maximo = self.get_maximo(listaTitulo, listaDatos)        
            for i in range (len(listaTitulo)):
                strformato += "{:<" + str(maximo) + "}"

            totalLen = maximo

        # print(strformato)
        return strformato, totalLen
    # ___________________________________
    def validaEntrada(self, listaTitulo=None, listaDatos=None):
        """ 
        Valida que listaTitulo es una lista de str
        Valida que listaDatos es una lista de lista de str o diccionario de listas de str
        Devuelve True/False                                    
        """
        if listaTitulo==None: 
            listaTitulo=self.listaTitulo if self.listaTitulo else None
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaTitulo and not listaDatos: return None

        # primera Validacion
        if not isinstance(listaTitulo, list): return None
        if not isinstance(listaDatos, list): return None

        # segunda Validacion        
        for iterador in listaDatos:
            if isinstance(iterador, list) or isinstance(iterador, tuple):
                pass
            elif isinstance(iterador, dict): 
                return False
                pass
            else:
                return False

        return True
    # ___________________________________
    def convierteToString(self, listaDatos):
        t_fila_str=[]
        
        for iterador in listaDatos:
            if isinstance(iterador, list) or isinstance(iterador, tuple):                
                t_fila_str.append(str(iterador))
        
            elif isinstance(iterador, dict): 
                t_fila = [(key, *item) for key, item in iterador.items()][0]          
                """ >>> Convierte en una lista con el primer elemento la key del diccionario """
                fila_str = [str(item) for item in t_fila]
                """ >>> Convierte a string cada elemento del diccionario """
                t_fila_str.append(fila_str)
        
        return t_fila_str
    # ___________________________________
    def Impr(self, listaTitulo=None, listaDatos=None, esAjustado=False, nombrePrinteX=''):
        """ 
        Es la funcion que hay que llamar para imprimir 
        """

        # SE ESTABLECE LA CADENA STR DE FORMATO()
        self.strformato, sumaTotChar=self.getFormato(listaTitulo=listaTitulo, 
                                                     listaDatos=listaDatos, 
                                                     esAjustado=esAjustado)        
        # _________
        # Encabezado        
        print(f'{str(nombrePrinteX).upper()}')
        numChar=len(nombrePrinteX)+2
        print(f'{'='*numChar}')

        print(self.strformato.format(*listaTitulo))   
        if esAjustado==False:
            maximo = self.get_maximo(listaTitulo=listaTitulo, listaDatos=listaDatos)        
            print("-"*len(listaTitulo)*(maximo))     #Linea de corte
        else:
            print("-"*(sumaTotChar))     #Linea de corte
            
        # _________
        # Datos
        for iterador in listaDatos:           
            self.imprListaDatos(listaDatos=iterador)
        
        # _________
        # Fin
        if esAjustado==False:
            maximo = self.get_maximo(listaTitulo=listaTitulo, listaDatos=listaDatos)        
            print("-"*len(listaTitulo)*(maximo))     #Linea de corte
        else:
            print("-"*(sumaTotChar))     #Linea de corte
    
    def maximoXColumna(self, listaTitulo, listaDatos):
        """ 
        Retorna una lista con el máximo número de caracteres de cada columna.
        """
        # Inicia la lista `retorno` con las longitudes de cada título en `listaTitulo`
        retorno = [len(titulo) for titulo in listaTitulo]

        # Recorre las filas en `listaDatos` y compara con el máximo de cada columna
        for fila in listaDatos:
            for columna, item in enumerate(fila):
                retorno[columna] = max(retorno[columna], len(item))
        
        return retorno
    # ___________________________________
    # Imprime en consola con un formato alineado. 
    def imprListaDatos(self, listaDatos=None):
        """ 
        Def: Imprime en la Terminal CON FORMATO
        -Calculando la longitud maxima para alinear correctamente.
        listaDatos tiene que ser un list de str
        """        
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaDatos: return None
        # TIENE QUE SER RECURSIVA PARA QUE COJA LAS LISTAS DE LISTAS 
        # tupleDatos=tuple(listaDatos)
        try:               
            print(self.strformato.format(*listaDatos))
        except Exception as e:
            print(f'Error: {e}')
            return False
        else:
            return True
    # _________________________
    def imprTitulos(self, listaTitulo=None):
        print(self.strformato.format(*listaTitulo))   
        print("-"*len(listaTitulo)*(self.maximo))     #Linea de corte

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def get_maximo(self,listaTitulo:list = None, listaDatos:list = None):
        """ Se trata de conseguir saber cual es el maximo valor en una lista de datos 
        """
        if listaTitulo == None: 
            listaTitulo = self.listaTitulo if self.listaTitulo else None
        if listaDatos == None: 
            listaDatos = self.listaDatos if self.listaDatos else None

        if not listaTitulo and not listaDatos: return None
        # _____________________
        # Recojo datos de listaTitulo
        longTitulo=len(listaTitulo)
        max_len_titulo = self.get_max_len_lststr(listaTitulo)
        
        # ╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═
        max_len_datos = self.get_max_len(listaDatos)
        """ Recojo datos de listaDatos """

        # _____________________
        # CALCULO EL MAXIMO DE ESPACIO 
        maximo = max_len_titulo if max_len_titulo>=max_len_datos else max_len_datos 
        return maximo + 1
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def get_max_len(self, iterador):
        listaCadenas = self.listRcsv(iterador=iterador)
        if listaCadenas:
            listaLen=[len(string) for string in listaCadenas]
            return max(listaLen)

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    
    # F u n c i o n   R e c u r s i v a    para Recorrer listas y devolver el str mas largo
    def listRcsv(self, iterador, retorno=None):
        """ Devuelve los valores que se va encontrando en una estructura de izquierda a derecha."""
        if retorno==None: retorno=[]        

        if isinstance(iterador, list) or isinstance(iterador, tuple):
            for subList in iterador:
                self.listRcsv(iterador = subList, retorno = retorno)
        else:
            retorno.append(iterador)
        return retorno

        pass
    # ________________________
    # Calcula la maxima longitud de un titulo o un genero en la tupla de peliculas
    def get_max_len_lststr(self, iterador:list):
        listLargos=[len(item) for item in iterador]        
        # Como ya tengo una lista con solo números, puedo aplicar max()         
        max_longitud = max(listLargos)        
        return max_longitud
# ==============================================================================
# F I N    C L A S S    P R I N T E X 
# ==============================================================================
