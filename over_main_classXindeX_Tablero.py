import os           
from enum import Enum

from fromdvd.classMenuDvd.classXindeX_Tablero import XindeX
# from fromdvd.classMenuDvd.classXindeX_Tablero import Over_Main
# from fromdvd.classMenuDvd.classMotorMain import Over_Main

# Acceso a Tablero / Rangutan / MonkeyHead
from fromdvd.classMenuDvd.Tablero_X_Men import Rangutan as Rangutan 
""" 
=======================================================================================================================
=======================================================================================================================
DEF: intento sustituir la impresion de   X i n d e X  con  T a b l e r o ( G O R I L A )  y así poder ampliar las funciones de xindex: 
modo Directorio:>>  *b (asterisco)+(opcion del menu)  quiero que sea la forma en que se ejecuta ve sólo el menu b.(solo primeros niveles???)

=======================================================================================================================
=======================================================================================================================
"""

# ###########
def main():
    # 1- INSTANCIO EL OBJETO ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    # The_X_Men = Over_Main()
    The_X_Men = XindeX()
    # 2- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    list_Main = [ ("XindeX" , None), ("Hilos" , None),("Flask" , None), ("BBDD" , None) ]
    Menu1=The_X_Men.addX(titulo='Menu1', lst_items=list_Main, fraseHead="| - M A I N M E N U - ")
    The_X_Men.addX(titulo='subFlask', lst_items=[  ("Ejecutar Servidor",None), ("Ver Servidor",None), ("Parar Servidor", None) ])
    The_X_Men.addX(titulo='subXindex', lst_items=[  ("Estilos e Info", func1 ), ("Alfabeto A" ,None ),("Alfabeto 1",None),("Alfabeto A1", None ) ])
    The_X_Men.addX(titulo='subHilos', lst_items=[  ("Ver Hilos", None) , ("Detener Hilos", None), ("Ejecutar Funcion" , None) ])    
    The_X_Men.addX(titulo='subNivel', lst_items=[  ("Guardar Menu BBDD", None) , ("Lanzar Flask", None) ])    

    # 3- COFIGURO LA GENETICA DEL INDICE ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    The_X_Men.config(titulo='Menu1'     , suPadre=None     , indexInPadre = None )
    The_X_Men.config(titulo='subFlask', suPadre='Menu1'  , indexInPadre='Flask' )
    The_X_Men.config(titulo='subXindex', suPadre='Menu1'  , indexInPadre='XindeX' )    
    The_X_Men.config(titulo='subHilos', suPadre='Menu1', indexInPadre='Hilos' )
    The_X_Men.config(titulo='subNivel', suPadre='Menu1', indexInPadre='BBDD' )

    # 4- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦
    retorno = The_X_Men.Mystyca(titulo='Menu1', configurado=True, execFunc=True, tipo_marcador='a', execAll=False, Loop=True , padX=50)
    """ Def: Genera un Indice que se Imprime en Pantalla.
    [titulo]      = Id del Menu Añadido/Configurado/Mostrados sus Items.
    [execFunc]    = True  ::: Cuando sale de aquí ya se ha ejecutado la funcion del menu.....lleve donde lleve, pero tiene que estar  
                    False ::: Se retorna a main la respuesta.
    [configurado]  = True  ::: Con La configuracion previa | False ::: Muestra Menu Simple Numerico de primer Nivel.
    [tipo_marcador] = '1'   ::: Numerico(byDef) | 'a' ::: Alfabetico Min | 'A' ::: Alfabetico May  | 'A1', '1A', a1, 1a ::: Mixto
    [execAll]    = True  ::: Solo se ejecutan ( o solo es opcion valida) los subMenus Finales (no padres) 
                    False ::: Se ejecuta ( o  solo es opcion valida) todo lo que no sea None en func.
                    si execFunc == False ::: No iterfiere pq refleja las opciones validas indmnt de si se ejecuta o se retorna. 
    [Loop]        = True  ::: Se auto-e<<jecuta hasta que <<<. | False ::: Se ejecuta 1 vez y sale a main.    """
    

    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    

    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else '.... el camino del no retorno'} ")

# ==========================================================        
# ==========================================================        
# ==========================================================      
def func1():    print('soy func1')
def func2():    print('soy func2')
def func3():    print('soy func3')
def func4():    print('soy func4')
def func5():    print('soy func5')
def func6():    print('soy func6')
def func7():    print('soy func7')


""" 
>>> Las funciones tienen que estar definidas para poder ser pasadas al menu 
    Desde las funciones puedes importar y ejecutar cualquier programa o codigo.
    Ademas se tienen que ejecutar en hilos separados unos de otros y controlados desde Over_Main o hilo principal.
"""


# ==========================================================        
# ==========================================================        
# ==========================================================      
if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main() 
    
import os           
from enum import Enum

from fromdvd.classMenuDvd.classXindeX_Tablero import XindeX
# from fromdvd.classMenuDvd.classXindeX_Tablero import Over_Main
# from fromdvd.classMenuDvd.classMotorMain import Over_Main

# Acceso a Tablero / Rangutan / MonkeyHead
from fromdvd.classMenuDvd.Tablero_X_Men import Rangutan as Rangutan 
""" 
=======================================================================================================================
=======================================================================================================================
DEF: intento sustituir la impresion de   X i n d e X  con  T a b l e r o ( G O R I L A )  y así poder ampliar las funciones de xindex: 
modo Directorio:>>  *b (asterisco)+(opcion del menu)  quiero que sea la forma en que se ejecuta ve sólo el menu b.(solo primeros niveles???)

=======================================================================================================================
=======================================================================================================================
"""

# ###########
def main():
    # 1- INSTANCIO EL OBJETO ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    # The_X_Men = Over_Main()
    The_X_Men = XindeX()
    # 2- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    list_Main = [ ("XindeX" , None), ("Hilos" , None),("Flask" , None), ("BBDD" , None) ]
    Menu1=The_X_Men.addX(titulo='Menu1', lst_items=list_Main, fraseHead="| - M A I N M E N U - ")
    The_X_Men.addX(titulo='subFlask', lst_items=[  ("Ejecutar Servidor",None), ("Ver Servidor",None), ("Parar Servidor", None) ])
    The_X_Men.addX(titulo='subXindex', lst_items=[  ("Estilos e Info", func1 ), ("Alfabeto A" ,None ),("Alfabeto 1",None),("Alfabeto A1", None ) ])
    The_X_Men.addX(titulo='subHilos', lst_items=[  ("Ver Hilos", None) , ("Detener Hilos", None), ("Ejecutar Funcion" , None) ])    
    The_X_Men.addX(titulo='subNivel', lst_items=[  ("Guardar Menu BBDD", None) , ("Lanzar Flask", None) ])    

    # 3- COFIGURO LA GENETICA DEL INDICE ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    The_X_Men.config(titulo='Menu1'     , suPadre=None     , indexInPadre = None )
    The_X_Men.config(titulo='subFlask', suPadre='Menu1'  , indexInPadre='Flask' )
    The_X_Men.config(titulo='subXindex', suPadre='Menu1'  , indexInPadre='XindeX' )    
    The_X_Men.config(titulo='subHilos', suPadre='Menu1', indexInPadre='Hilos' )
    The_X_Men.config(titulo='subNivel', suPadre='Menu1', indexInPadre='BBDD' )

    # 4- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦╔╦╦
    retorno = The_X_Men.Mystyca(titulo='Menu1', configurado=True, execFunc=True, tipo_marcador='a', execAll=False, Loop=True , padX=50)
    """ Def: Genera un Indice que se Imprime en Pantalla.
    [titulo]      = Id del Menu Añadido/Configurado/Mostrados sus Items.
    [execFunc]    = True  ::: Cuando sale de aquí ya se ha ejecutado la funcion del menu.....lleve donde lleve, pero tiene que estar  
                    False ::: Se retorna a main la respuesta.
    [configurado]  = True  ::: Con La configuracion previa | False ::: Muestra Menu Simple Numerico de primer Nivel.
    [tipo_marcador] = '1'   ::: Numerico(byDef) | 'a' ::: Alfabetico Min | 'A' ::: Alfabetico May  | 'A1', '1A', a1, 1a ::: Mixto
    [execAll]    = True  ::: Solo se ejecutan ( o solo es opcion valida) los subMenus Finales (no padres) 
                    False ::: Se ejecuta ( o  solo es opcion valida) todo lo que no sea None en func.
                    si execFunc == False ::: No iterfiere pq refleja las opciones validas indmnt de si se ejecuta o se retorna. 
    [Loop]        = True  ::: Se auto-e<<jecuta hasta que <<<. | False ::: Se ejecuta 1 vez y sale a main.    """
    

    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    

    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else '.... el camino del no retorno'} ")

# ==========================================================        
# ==========================================================        
# ==========================================================      
def func1():    print('soy func1')
def func2():    print('soy func2')
def func3():    print('soy func3')
def func4():    print('soy func4')
def func5():    print('soy func5')
def func6():    print('soy func6')
def func7():    print('soy func7')


""" 
>>> Las funciones tienen que estar definidas para poder ser pasadas al menu 
    Desde las funciones puedes importar y ejecutar cualquier programa o codigo.
    Ademas se tienen que ejecutar en hilos separados unos de otros y controlados desde Over_Main o hilo principal.
"""


# ==========================================================        
# ==========================================================        
# ==========================================================      
if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main() 
    

