## importamos las librerias
import os, sys
import yaml 
## creamos variables globales
""" clientes = {
            11: {'nombre': 'Juan', 'direccion': 'calle 45', 'email': 'juan@hotmail.com', 'preferente': True}, 
            22: {'nombre': 'Mario', 'direccion': 'dfgsf', 'email': 'mario@gmail.com', 'preferente': True},
            33: {'nombre': 'Mario', 'direccion': 'dfgsf', 'email': 'mario@gmail.com', 'preferente': True},
            } """
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

##  Creamos el MENU con las opciones 
while True:
    print('---------------  APLICACION EN PYTHON ----------------------')
    print(' 1. Agregar cliente \n 2. Eliminar Cliente \n 3. Mostrar Cliente \n 4. Lista de Clientes \n 5. Lista de clientes Preferentes \n 6. Salir')
    try:
        opt = int(input('Ingresa una opcion:  '))
        if opt == 1:
            ## ==============================================================
            ## ========== AGREGAMOS NUEVO CLIENTE ===========================
            ## ==============================================================
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
        elif opt == 2:
            ## ==============================================================
            ## ================= ELIMINAR CLIENTE ===========================
            ## ==============================================================
            cleaning() ## limpia la consola de python
            if len(clientes) > 0 :
                ## Leemos el nit del cliente a eliminar
                nit = int(input('Ingresa el NIT del cliente: '))
                ## validamos que exista el cliente
                if nit in clientes:
                    print('Datos del Cliente: \n ')
                    print(yaml.dump(clientes[nit], sort_keys=False, default_flow_style=False))
                    repetir = input('Esta segur@ de elimiar este cliente? \n\t 1. Si \n\t 2. No \n\t ')
                    ## Eliminamos el cliente se esta segur@
                    while ord(repetir[0]) != 49 and ord(repetir[0]) != 50:
                        cleaning() ## LIMPIAMOS LA CONSOLA
                        print('--------------------------------------------------')
                        print('Error, Opcion NO valida intente nuevamente')
                        print('--------------------------------------------------\n')
                        repetir = input('Esta segur@ de elimiar este cliente? \n\t 1. Si \n\t 2. No \n\t ')
                        if ord(repetir[0]) == 49 or ord(repetir[0]) == 50:
                            break
            
                    if ord(repetir[0]) == 49:
                        clientes.pop(nit) ## eliminamos el cliente de la BD
                        print('Se ha eliminado correctamente! ')
                else:
                    print('El cliente NO se encuentra registrado')
                    
                print('\n ------------------------------------------------')
                input('Preciona una tecla para continuar: ')
            else:
                print('No se han registrado clientes en la BD')
                print('\n ------------------------------------------------')
                input('Preciona una tecla para continuar: ')
                
        elif opt == 3:
            os.system('clear') ## limpia la consola de python
            if len(clientes) > 0 :
                ## Leemos el nit del cliente a buscar
                nit = int(input('Ingresa el NIT del cliente: '))
                ## validamos que exista el cliente 
                if nit in clientes:
                    print('Datos del Cliente: \n ')
                    print('\t',yaml.dump(clientes[nit], sort_keys=False, default_flow_style=False))
                else:
                    print('El cliente NO se encuentra registrado')
            else:
                print('No se han registrado clientes en la BD')
            print('\n ------------------------------------------------')
            input('Preciona una tecla para continuar: ')
        elif opt == 4:
            ## ==============================================================
            ## ================= MOSTRAR LISTA DE CLIENTES ==================   
            ## ==============================================================
            os.system('clear') ## limpia la consola de python
            print('NIT \t| Nombre \t| Email \t')
            for clave,valor in clientes.items():
                print('{} \t| {}\t| {}\t'.format(clave,valor['nombre'],valor['email']))
            print('\n ------------------------------------------------')
            input('Preciona una tecla para continuar: ')
        elif opt == 5:
            ## ==============================================================
            ## ======= MOSTRAR LISTA DE CLIENTES PREFERENTES ================   
            ## ==============================================================
            os.system('clear') ## limpia la consola de python
            print('NIT \t| Nombre \t| Email \t')
            for clave,valor in clientes.items():
                ## filtramos los clientes preferentes
                if valor['preferente'] == True:
                    print('{} \t| {}\t| {}\t'.format(clave,valor['nombre'],valor['email']))
            print('\n ------------------------------------------------')
            input('Preciona una tecla para continuar: ')
        else:
            print('\n Ejecucion Finalizada con EXITO !')
            break
    except ValueError:
        print('Error, NO es una opcion Valida!! :( ')
        input()
        cleaning()
    except KeyboardInterrupt:
        print('\n Ejecucion Finalizada con EXITO !')
        cleaning()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except Exception as e:
        print('Error, ',type().__name__)
    cleaning()











