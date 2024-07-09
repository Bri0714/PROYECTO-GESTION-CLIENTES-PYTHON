## importamos las librerias
import os, sys
import yaml
## creamos variables globales
#clientes = {11: {'nombre': 'Juan', 'direccion': 'calle 45', 'email': 'juan@hotmail.com', 'preferente': True}, 22: {'nombre': 'Mario', 'direccion': 'dfgsf', 'email': 'mario@gmail.com', 'preferente': True}}
clientes = {}   
repetir = 'c'
## funcion para borrar el contenido de la consola 
def cleaning():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


def nuevoCliente():
    while True:
        cleaning() ## limpia la consola de python
        datos = {} ## creacion diccionario temporal
        
        ## Leemos el nit del cliente
        nit = int(input('Ingresa el NIT del cliente: '))
        ## validamos que exista el cliente
        while nit in clientes:
            print('el NIT {} ya se encuetra registrado'.format(nit))
            print('--------------------------------------------------')
            nit = int(input('Ingresa el NIT del cliente: '))      
        ## Leemos los datos de los cliente
        nombre = input('Ingresa el nombre del cliente: ')
        direccion = input('Ingresa la direccion del cliente: ')
        email = input('Ingresa el email del cliente: ')
        preferente = input('Ingresa alguna de las siguiente opciones: \n\t 1. Si es un cliente Preferente \n\t 2. Si NO es un cliente Preferente \n\t\t su opcion es:  ')
        aux3 = preferente[0]
        if ord(aux3) != 49 and ord(aux3) != 50:
            while ord(aux3) != 49 and ord(aux3) != 50:
                cleaning() ## limpia la consola de python
                print('--------------------------------------------------')
                print('Error, Opcion NO valida intente nuevamente')
                print('--------------------------------------------------\n')
                preferente = input('Ingresa alguna de las siguiente opciones: \n\t 1. Si es un cliente Preferente \n\t 2. Si NO es un cliente Preferente \n\t\t su opcion es:  ')
                if ord(preferente[0]) == 49 or ord(preferente[0]) == 50:
                    break
        preferenteAux = False
        if preferente == '1': 
            preferenteAux = True
        else:
            preferenteAux = False
            
        ## Creamos el diccionario con los datos del cliente
        datos['nombre']=nombre
        datos['direccion']=direccion
        datos['email']=email
        datos['preferente']= preferenteAux
        ## guardamos la informacion en el diccionario de los clientes
        clientes[nit] = datos
        print('Se ha agregado un nuevo cliente a la BD correctamente! ')
        print('--------------------------------------------------')
        repetir = input('Desea agregar otro cliente? \n\t 1. Si \n\t 2. No \n\t ')
        while ord(repetir[0]) != 49 and ord(repetir[0]) != 50:
            cleaning() ## LIMPIAMOS LA CONSOLA
            print('--------------------------------------------------')
            print('Error, Opcion NO valida intente nuevamente')
            print('--------------------------------------------------\n')
            repetir = input('Desea agregar otro cliente? \n\t 1. Si \n\t 2. No \n\t ')
            if ord(repetir[0]) == 49 or ord(repetir[0]) == 50:
                break
            
        if repetir == '1': 
            cleaning() ## LIMPIAMOS LA CONSOLA
            continue
        else:
            cleaning() ## LIMPIAMOS LA CONSOLA
            break
 
def deleteCliente(nit):
    ## VALIDAMOS QUE EXISTA UN CLIENTE CON ESE NIT 
    if nit in clientes:
        print('Datos del Cliente: \n ')
        print(yaml.dump(clientes[nit], sort_keys=False, default_flow_style=False))
        valida = input('Esta segur@ de elimiar este cliente? \n\t 1. Si \n\t 2. No \n\t ')
        if valida == '1': 
            clientes.pop(nit) ## ELIMINAMOS EL CLIENTE DE LA BD
            print('Se ha eliminado correctamente! ')
    else:
        print('El cliente NO se encuentra registrado')
    
def buscaClientes(nit2=0,opt=0):
    ## VALIDAMOS QUE NO EXISTA NINGUN PARAMETRO DE NIT Y QUE EXISTAN DATOS
    if nit2 == 0 and len(clientes) > 0:
        print('Clientes de la base de datos: \n ')
        if opt == 4:
            ## ======================================================
            ## ============ IMPRIMIMOS TODOS LOS CLIENTES ===========
            ## ======================================================    
            cleaning() ## LIMPIAMOS LA CONSOLA
            print('NIT \t| Nombre \t| Email \t| Preferente \t')
            
            ## IMPRIMIMOS TODOS LOS CLIENTES
            for clave,valor in clientes.items():
                print('{} \t| {}\t| {}\t| {}\t'.format(clave,valor['nombre'],valor['email'],valor['preferente']))
                
            ## HACEMOS UNA PAUSA EN LA EJECUCION  
            print('\n ------------------------------------------------')
            input('Preciona una tecla para continuar: ')
        elif opt == 5:
            ## ======================================================
            ## ========= IMPRIMIMOS LOS CLIENTE PREFERENTES =========
            ## ======================================================
            cleaning() ## LIMPIAMOS LA CONSOLA
            print('NIT \t| Nombre \t| Email \t')
            for clave,valor in clientes.items():
                ## FILTRAMOS LOS CLIENTES PREFERENTES
                if valor['preferente'] == True:
                    print('{} \t| {}\t| {}\t'.format(clave,valor['nombre'],valor['email']))
                    
            ## HACEMOS UNA PAUSA EN LA EJECUCION
            print('\n ------------------------------------------------')
            input('Preciona una tecla para continuar: ')
    else:
        ## VALIDAMOS QUE EL CLIENTE EXITA EN EL DICCIONARIO
        if nit2 in clientes:
            print('Datos del Cliente: \n ')
            ## RETORNAMOS LOS DATOS DE UN SOLO CLIENTE
            return clientes[nit2]
        else:
            print('El cliente NO se encuentra registrado')
     
     
def menu():
    ##  CREAMOS EL MENU CON LAS OPCIONES
    while True:
        print('---------------  APLICACION EN PYTHON ----------------------')
        print(' 1. Agregar cliente \n 2. Eliminar Cliente \n 3. Mostrar Cliente \n 4. Lista de Clientes \n 5. Lista de clientes Preferentes \n 6. Salir')
        
        try:
            opt = int(input('Ingresa una opcion:  '))
            if opt == 1:
                ## ==============================================================
                ## ========== AGREGAMOS NUEVO CLIENTE ===========================
                ## ==============================================================
                ## EJECUTAMOS LA FUNCION PARA CREAR UN NUEVO CLIENTE
                nuevoCliente()
            elif opt == 2:
                ## ==============================================================
                ## ================= ELIMINAR CLIENTE ===========================
                ## ==============================================================
                cleaning() ## LIMPIAMOS LA CONSOLA
                ## VALIDAMOS QUE EXISTA DATA EN EL DICCIONARIO
                if len(clientes) > 0 : 
                    ## LEEMOS EL NIT DEL CLIENTE A BUSCAR
                    nit = int(input('Ingresa el NIT del cliente: '))
                    ## EJECUTAMOS LA FUNCION PARA ELIMINAR UN CLIENTE DEL DICCIONARIO
                    deleteCliente(nit)  
                else:
                    print('No se han registrado clientes en la BD')
                    
                ## HACEMOS UNA PAUSA EN LA EJECUCION        
                print('\n ------------------------------------------------')
                input('Preciona una tecla para continuar: ')     
            elif opt == 3:
                ## ==============================================================
                ## =================== BUSCAR CLIENTE ===========================
                ## ==============================================================
                cleaning() ## LIMPIAMOS LA CONSOLA
                ## VALIDAMOS QUE EXISTA DATA EN EL DICCIONARIO
                if len(clientes) > 0 :
                    ## LEEMOS EL NIT DEL CLIENTE A BUSCAR
                    nit = int(input('Ingresa el NIT del cliente: '))
                    ## IMPRIMIMOS EL RESULTADO DE LA BUSQUEDA
                    print(yaml.dump(buscaClientes(nit), sort_keys=False, default_flow_style=False)) 
                else:
                    print('No se han registrado clientes en la BD')
                    
                ## HACEMOS UNA PAUSA EN LA EJECUCION    
                print('\n ------------------------------------------------')
                input('Preciona una tecla para continuar: ')
            elif opt == 4:
                ## ==============================================================
                ## ================= MOSTRAR LISTA DE CLIENTES ==================   
                ## ==============================================================
                cleaning() ## LIMPIAMOS LA CONSOLA
                buscaClientes(nit2=0,opt=4)
                input('Preciona una tecla para continuar: ')
            elif opt == 5:
                ## ==============================================================
                ## =========== MOSTRAR LISTA DE CLIENTES PREFERENTES ============
                ## ==============================================================
                buscaClientes(nit2=0,opt=5)
                input('Preciona una tecla para continuar: ')
            else:
                print('\n Ejecucion Finalizada con EXITO !')
                break
            
        except ValueError:
            print('Error, NO es una opcion Valida!! :( ')
            ## HACEMOS UNA PAUSA EN LA EJECUCION
            print('\n ------------------------------------------------')
            input('Preciona una tecla para continuar: ')
            cleaning() ## LIMPIAMOS LA CONSOLA
        except KeyboardInterrupt:
            print('\n Ejecucion Finalizada con EXITO !')
            cleaning() ## LIMPIAMOS LA CONSOLA 
            ## FORZAMOS LA SALIDA DEL PROGRAMA
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        except Exception as e:
            ## IMPRIMIMOS EL ERROR CON SU NOMBRE
            print('Error, ',type().__name__)
        cleaning() ## LIMPIAMOS LA CONSOLA 


## ==============================================================
## ====================== EJECUCION MAIN ========================   
## ==============================================================
menu()
   
        
     
        
        
